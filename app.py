from flask import Flask
app = Flask(__name__)


@app.route('/')
def random_reddit():
	return 'test'

if __name__ == "__main__":
    app.run()