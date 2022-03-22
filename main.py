from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    for i in [['Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org'],
              ['Klimov', 'Lenar', 16, 'officer', 'engineer', 'module_2', 'klimov_lenar@mars.org'],
              ['Agliuillin', 'Ilsaf', 15, 'lieutenant', 'researcher', 'module_3', 'ilsaf_agliullin@mars.org'],
              ['Valeev', 'Karim', 15, 'capral', 'programmer', 'module_4', 'karim_valeev@mars.org']]:
        user = User()
        user.surname = i[0]
        user.name = i[1]
        user.age = i[2]
        user.position = i[3]
        user.speciality = i[4]
        user.address = i[5]
        user.email = i[6]
        db_sess.add(user)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
