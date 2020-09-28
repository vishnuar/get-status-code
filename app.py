from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if(request.method == 'POST'):
            userDetails = request.form
            url = userDetails['url']
            if(len(url) > 8):
                url_request = requests.head(url)
                return render_template('status.html', result=url_request.status_code)
            else:
                return render_template('status.html', result="Please enter a valid url")
        return render_template('status.html')
    except:
        return render_template('status.html', result="Oops, something went wrong")

if __name__ == '__main__':
    app.run(debug=False)