from scraper import scrape_data
from flask import Flask, render_template,request, redirect

app = Flask(__name__)

@app.route('/', methods= ["GET","POST"])
def home():
    if request.method == 'POST':
        query = request.form['query']
        return redirect(f'/api/get/{query}')
    return render_template("home.html")

@app.route('/api/get/<searchTerm>')
def api(searchTerm):
    return render_template("jobs.html",query=searchTerm, jobs = scrape_data(searchTerm))

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

