from flask import Flask

app =Flask(__name__)

@app.route("/")
def name():
    return "Jotheeswaran M"


@app.route("/registerNumber")
def register_number():
    return "22ITL02"

@app.route("/department")
def department():
    return "IT(Information Technology)"

if __name__ == "__main__":
    app.run(debug=True)
