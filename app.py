from dis import Instruction
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    generated_email = None
    if request.method == "POST":
        Instructions=request.form.get("instructions")
        generated_email=f"you wrote: {Instructions}"
    return render_template("index.html", generated_email=generated_email)



if __name__ == "__main__":
    app.run(debug=True)


