import os
import sqlite3
from datetime import date

from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "expense_tracker.db"
)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    try:
        with conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id            INTEGER PRIMARY KEY AUTOINCREMENT,
                    name          TEXT NOT NULL,
                    email         TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    created_at    TEXT DEFAULT (datetime('now'))
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id     INTEGER NOT NULL REFERENCES users(id),
                    amount      REAL NOT NULL,
                    category    TEXT NOT NULL,
                    date        TEXT NOT NULL,
                    description TEXT,
                    created_at  TEXT DEFAULT (datetime('now'))
                )
                """
            )
    finally:
        conn.close()


def seed_db():
    conn = get_db()
    try:
        if conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] > 0:
            return

        today = date.today()
        expenses = [
            (42.50, "Food", 2, "Groceries"),
            (15.00, "Transport", 4, "Metro card top-up"),
            (120.00, "Bills", 5, "Electricity bill"),
            (60.00, "Health", 8, "Pharmacy"),
            (25.00, "Entertainment", 11, "Movie night"),
            (89.99, "Shopping", 14, "New shoes"),
            (10.00, "Other", 18, "Miscellaneous"),
            (18.75, "Food", 22, "Lunch with friends"),
        ]

        with conn:
            cur = conn.execute(
                "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
                ("Demo User", "demo@spendly.com", generate_password_hash("demo123")),
            )
            user_id = cur.lastrowid
            conn.executemany(
                "INSERT INTO expenses (user_id, amount, category, date, description)"
                " VALUES (?, ?, ?, ?, ?)",
                [
                    (user_id, amount, category, today.replace(day=day).isoformat(), desc)
                    for amount, category, day, desc in expenses
                ],
            )
    finally:
        conn.close()
