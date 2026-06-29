🧠 Why This Is Important

Instead of sharing usernames and passwords with every application:
User
   ↓
Application
   ↓
Username & Password ❌

OAuth 2.0 works like this:
User
   ↓
Authorization Server
   ↓
Access Token
   ↓
Client Application
   ↓
Protected API

Benefits:
✅ Secure authentication
✅ Token-based authorization
✅ Third-party login support
✅ Standardized API security

Used By :
Google Login
GitHub Login
Microsoft Login
Facebook Login
Spotify API

🛠 Tech Stack
Python
Flask
Flask-JWT-Extended
UUID

📂 Project Structure
oauth2-auth-server/
│
├── app.py
├── requirements.txt
└── README.md
