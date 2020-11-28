import flask
from code_generator import *

app = flask.Flask("__main__", static_url_path='')

@app.route("/")
def my_index():
    return app.send_static_file('index.html')

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

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(port=9092)