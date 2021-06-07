from flask import Flask, render_template


app = Flask(__name__)


@app.route('/feedback', methods=['POST', 'GET'])
def feedback():
    return render_template('feedback.html')


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    return render_template('submit.html')


if __name__ == "__main__":
    app.run(debug=True)
