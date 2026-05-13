from app.database import get_db_connection
from passlib.hash import bcrypt


def get_all_users():
    db = get_db_connection()
    rows = db.execute("SELECT id, username, email FROM users;").fetchall()
    return [dict(r) for r in rows]


def get_user(user_id):
    db = get_db_connection()
    row = db.execute("SELECT id, username, email FROM users WHERE id = ?", (user_id,)).fetchone()
    return dict(row) if row else None


def create_user(username, email, password):
    hashed = bcrypt.hash(password)
    db = get_db_connection()
    cur = db.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, hashed),
    )
    db.commit()
    user_id = cur.lastrowid
    return get_user(user_id)


def update_user(user_id, username=None, email=None, password=None):
    db = get_db_connection()
    # Get existing
    existing = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    if not existing:
        return None
    new_username = username if username is not None else existing["username"]
    new_email = email if email is not None else existing["email"]
    new_password = existing["password"]
    if password is not None:
        new_password = bcrypt.hash(password)
    db.execute(
        "UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?",
        (new_username, new_email, new_password, user_id),
    )
    db.commit()
    return get_user(user_id)


def delete_user(user_id):
    db = get_db_connection()
    row = db.execute("SELECT id FROM users WHERE id = ?", (user_id,)).fetchone()
    if not row:
        return False
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
    return True
