import flask

home = flask.Flask(__name__)
home.route('/')(lambda: flask.render_template('welcome.html'))

if __name__ == "__main__":
    home.run(debug = True, port = 1000)
