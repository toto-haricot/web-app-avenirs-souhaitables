from flask import Flask, render_template, request, redirect, url_for
import datetime
app = Flask(__name__)
 
 # turn on debugging mode
app.debug = True

@app.route('/')
def homepage():
    return render_template("homepage-index.html")

@app.route('/test')
def testpage():
    return render_template("test.html")

@app.route('/qui_sommes_nous', methods=['GET', 'POST'])
def qui_sommes_nous():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('qui-sommes-nous-index.html')

@app.route('/tous_nos_articles', methods=['GET', 'POST'])
def tous_nos_articles():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('tous-nos-articles-index.html')

@app.route('/article_00001', methods=['GET', 'POST'])
def article_00001():
    return render_template('article-00001-index.html')

@app.route('/article_00002', methods=['GET', 'POST'])
def article_00002():
    return render_template('article-00002-index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
