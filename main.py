from database import init_db
from auth import register_user, login

if __name__ == '__main__':
    init_db()

    ok, message = register_user("maria", "maria2323")
    print(ok, message)

    print(login("maria", "maria2323"))