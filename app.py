from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def number():
    if request.method == "POST":
        number = int(request.form["number"])

        if number % 2 == 0:
            msg = "Juft son"
        else:
            msg = "Toq son"

        return render_template("result45.html", msg=msg)

    return render_template("index45.html")

if __name__ == "__main__":
    app.run(debug=True)
