from app import app

# Run
app.run("0.0.0.0", debug=app.config["DEBUG"], port=app.config["PORT"])
