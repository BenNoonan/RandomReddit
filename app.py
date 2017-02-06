from flask import Flask, render_template
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TEMPLATE_AUTO_RELOAD'] = True


@app.route("/")
def random_reddit():
	return render_template('index.html')

if __name__ == "__main__":
    app.run()