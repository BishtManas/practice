from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pymysql

# Create FastAPI app
app = FastAPI()

# MySQL connection
conn = pymysql.connect(
    host="your_localhost",
    user="your_root",
    password="your_password",
    database="your_database",
    cursorclass=pymysql.cursors.DictCursor
)

# Pydantic model for request body
class User(BaseModel):
    name: str
    email: str
    age: int

# 🟢 Create a new user
@app.post("/users")
def create_user(user: User):
    with conn.cursor() as cursor:
        sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user.name, user.email, user.age))
        conn.commit()
    return {"message": "User created successfully"}

# 🔵 Get all users
@app.get("/users")
def get_users():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
    return result

# 🟡 Update a user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    with conn.cursor() as cursor:
        sql = "UPDATE users SET name=%s, email=%s, age=%s WHERE id=%s"
        cursor.execute(sql, (user.name, user.email, user.age, user_id))
        conn.commit()
    return {"message": "User updated successfully"}

# 🔴 Delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with conn.cursor() as cursor:
        sql = "DELETE FROM users WHERE id=%s"
        cursor.execute(sql, (user_id,))
        conn.commit()
    return {"message": "User deleted successfully"}