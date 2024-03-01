from flask import Flask, render_template
from data.db_session import *

app = Flask(__name__)

@app.route('/index')
def index():
    global_init('blogs.db')
    db_sess = create_session()
    return render_template('index.html', data=db_sess.query(Jobs).all())

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
