from scraper import scrape_data
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/api/get/<searchTerm>')
def api(searchTerm):
    return render_template("home.html",query=searchTerm, jobs = scrape_data(searchTerm))

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

