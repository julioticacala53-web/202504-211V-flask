from app import create_app
from app.database import init_db


def main():
    app = create_app()
    with app.app_context():
        init_db()
        print("Database initialized (users table)")


if __name__ == '__main__':
    main()
