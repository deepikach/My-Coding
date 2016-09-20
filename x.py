from flask import Flask,render_template
app=Flask("deepu")
@app.route('/<link>')
def index(link):
    return render_template('index.html',page=link) 
app.run(debug=True)