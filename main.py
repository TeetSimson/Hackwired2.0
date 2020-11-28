import flask
from backend.code_generator import *

app = flask.Flask("__main__")

@app.route("/")
def my_index():
    return flask.render_template("index.html")

@app.route("/get_result/<platform>/<desc>")
def get_result(platform, desc):
    s = ''
    if (platform == 'python'):
        train_python_model()
        s = gpt_python.get_top_reply(desc)
        return s.split(' ', 1)[1]
    elif (platform == 'sql'):
        train_sql_model()
        s = gpt_sql.get_top_reply(desc)
        return s.split(' ', 1)[1]
    elif (platform == 'js'):
        train_js_model()
        s = gpt_js.get_top_reply(desc)
        return s.split(' ', 1)[1]
    elif (platform == 'php'):
        train_php_model()
        s = gpt_php.get_top_reply(desc)
        return s.split(' ', 1)[1]

app.run(debug=True)