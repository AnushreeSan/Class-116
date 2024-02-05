from flask import Flask, render_templete
app = Flask(__name__)

@app.route("/index")
def first_webpage():
    name = 'Flask'
    return render_templete('index.html', index_variable = name)
app.run(debug=True)