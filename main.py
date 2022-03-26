import datetime

from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def works():
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs, User).filter(Jobs.team_leader == User.id)
    return render_template("works.html", jobs=jobs)


def main():
    app.run()


if __name__ == '__main__':
    main()
