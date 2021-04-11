from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__, static_url_path='/static')


app.config["DEBUG"] = True

@app.route('/')
def index():
    #url_for('static', filename='/static/logo.png')
    return render_template('Index.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
