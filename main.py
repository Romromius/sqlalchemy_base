from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")

    ridley = User()
    ridley.surname = 'Scott'
    ridley.name = 'Ridley'
    ridley.age = 21
    ridley.position = 'captain'
    ridley.speciality = 'research engineer'
    ridley.address = 'module_1'
    ridley.email = 'scott_chief@mars.org'

    arthur = User()
    arthur.surname = 'Ripley'
    arthur.name = 'Ellen'
    arthur.age = 34
    arthur.position = 'executive officer'
    arthur.speciality = 'gun user'
    arthur.address = 'module_2'
    arthur.email = 'xeno_lover@mars.org'

    dennis = User()
    dennis.surname = 'Parker'
    dennis.name = 'Dennis'
    dennis.age = 42
    dennis.position = 'adeptus inquisitoris'
    dennis.speciality = 'exterminatus'
    dennis.address = 'Terra'
    dennis.email = 'xeno_exgumatus@terra.org'

    gruss = User()
    gruss.surname = 'Delfan'
    gruss.name = 'Gruss'
    gruss.age = 289
    gruss.position = 'magos'
    gruss.speciality = 'explorator'
    gruss.address = 'Caestus Metallican'
    gruss.email = 'gruss_magos@mechan.net'

    db_sess = db_session.create_session()
    db_sess.add(ridley)
    db_sess.add(arthur)
    db_sess.add(dennis)
    db_sess.add(gruss)
    db_sess.commit()

    # app.run()


if __name__ == '__main__':
    main()
