from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        event = request.form["event"]

        return render_template(
            "register.html",
            name=name,
            email=email,
            phone=phone,
            event=event
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
