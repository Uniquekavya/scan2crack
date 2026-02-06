ADMIN_EMAIL = "admin@scan2crack.com"
ADMIN_PASSWORD = "admin123"




import streamlit as st
from database import load_users, save_users
import hashlib
def admin_login(email, password):
    return email == ADMIN_EMAIL and password == ADMIN_PASSWORD

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, email, password):
    users = load_users()

    if email in users:
        return False, "User already exists"

    users[email] = {
        "name": name,
        "password": hash_password(password),
        "resume": False,
        "interview": False,
        "ai": False
    }

    save_users(users)
    return True, "Registration successful"

def login_user(email, password):
    users = load_users()
    hashed = hash_password(password)

    if email in users and users[email]["password"] == hashed:
        return True, users[email]

    return False, None
