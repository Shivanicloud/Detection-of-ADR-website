from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return render_template("index.html")
    # return "<p>Hello, World!</p>"


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)
