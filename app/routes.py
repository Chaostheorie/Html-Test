from app import app
from flask import request, render_template
from flask_misaka import markdown

# The test function is taking an Arg and look for the html file in
# the templates directory
# if there is no .html ending in the template arg it will be added

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("info.html")

@app.route("/post", methods=["GET", "POST"])
def post():
    if request.method == "POST":
        try:
            jinja_var = markdown(request.form["jinja_var"])
            return render_template(request.template_name["template_name"],
             jinja_var=jinja_var)
        except:
            try:
                jinja_var = markdown(request.form["jinja_var"])
                print(jinja_var)
                return render_template("post_info.html",
                jinja_var=jinja_var)
            except:
                try:
                    return render_template("post_info.html", jinja_var=request.form["jinja_var"])
                except:
                    return render_template("post_info.html")

@app.route("/template")
def info():
    return render_template("info.html")

@app.route("/template/<template>")
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
