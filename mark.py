from flask import Flask,render_template
app=Flask("deepu")
@app.route('/<int:score>')
def hello(score):
    return render_template('hello.html',marks=score)
app.run(debug=True)