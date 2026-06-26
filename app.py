import os
from flask import Flask, request, jsonify
import psycopg
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_connection():
    return psycopg.connect(
    host = os.getenv("DB_HOST"),
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    port = os.getenv("DB_PORT")
)

@app.route("/webhook", methods=["POST"])

def receive_webhook():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "error": "data is required"
        }), 400
    
    name = data.get("name")
    email = data.get("email")
    company = data.get("company")
    message = data.get("message", "")

    if not name or not email or not company or not message:
        return jsonify({
            "error": "name, email, company and message are required"
        }), 400
    
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO leads (name, email, company, message)
                    VALUES (%s, %s, %s, %s)
                    """, (name, email, company, message)
                )

                return jsonify({
                    "success": True,
                    "message": "Submission saved",
                    "data": "yes"
                }), 201
    except Exception as error:
        print(error)
        return jsonify("Could not save submission")
    
if __name__ == "__main__":
    app.run(debug=True)