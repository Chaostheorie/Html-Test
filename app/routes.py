from app import app, db, db_session
from app.models import User, Role
from flask_user import UserManager
from flask import request, render_template
import time, datetime

#setup user manager
user_manager = UserManager(app, db, User)

# Check if admin and guest User already exists
if not User.query.filter(User.username == "Admin").all():
    # If it doesn't the admin user will be created
    user = User(
        username = "Admin",
        password = user_manager.hash_password("Password1")
    )
    user.roles.append(Role(name="Admin"))
    db_session.add(user)
    db_session.commit()

# Add the guest if enabled and not yet created
if app.config["GUEST_USER"] == True:
    if not User.query.filter(User.username == "guest").all():
        user = User(
            username = "guest",
            password = user_manager.hash_password("Passwort")
            )
        db_session.add(user)
        db_session.commit()

# if the config is set to Flase and guest exists it will be deleted
# otherwise nothing happens
elif app.config["GUEST_USER"] == False:
    if not User.query.filter(User.username == "guest").all():
        pass
    else:
        user = User.query.filter_by(username = "guest").first()
        db_session.delete(user)
        db_session.commit()

# If sth is in the config that doesn't match, nothing will happen
else:
    pass

# The test function is taking an Arg and look for the html file in
# the templates directory 
# if there is no .html ending in the template arg it will be added

@app.route("/<template>")
def view_template(template):
    if request.method == "GET":
        try:
            return render_template(template)
        except:
            test = template.split(".")
            template = test[0] + ".html"
            try:
                return render_template(template)
            except:
                return render_template("404.html")

# 404 errorhandler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
