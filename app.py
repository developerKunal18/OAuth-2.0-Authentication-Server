from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

# Demo users
users = {
    "admin": "admin123",
    "user": "user123"
}

# ---------- Login ----------
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if users.get(username) != password:

        return jsonify({
            "message": "Invalid credentials"
        }), 401

    token = create_access_token(
        identity=username
    )

    return jsonify({
        "access_token": token
    })


# ---------- Protected Resource ----------
@app.route("/profile")
@jwt_required()
def profile():

    current_user = get_jwt_identity()

    return jsonify({
        "user": current_user,
        "message": "Protected profile data"
    })


# ---------- Public ----------
@app.route("/")
def home():

    return jsonify({
        "message": "OAuth2 Authentication Server"
    })


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":

    app.run(debug=True)
