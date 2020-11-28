from flask import Flask, render_template
from code_generator import *
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path, static_url_path='')

@app.route("/")
def my_index():
    train_python_model()
    train_sql_model()
    train_js_model()
    train_php_model()
    return render_template('index.html')

@app.route("/get_result/<platform>/<desc>/")
def get_result(platform, desc):
    s = ''
    if (platform == 'python'):
        s = gpt_python.get_top_reply(desc).partition(' ')[2]
        return render_template('result.html', s=s)
    elif (platform == 'sql'):
        s = gpt_sql.get_top_reply(desc)
        return render_template('result.html', s=s)
    elif (platform == 'js'):
        s = gpt_js.get_top_reply(desc)
        return render_template('result.html', s=s)
    elif (platform == 'php'):
        s = gpt_php.get_top_reply(desc)
        return render_template('result.html', s=s)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(port=8093)