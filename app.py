from flask import Flask, escape, request

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == 'main':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)