# 📧 Email OTP Authentication API

A Django REST API that enables secure user registration and login using email-based One-Time Password (OTP) verification. This service features OTP generation, validation, rate limiting, and Docker support.

---

## 🚀 Features

- ✅ User registration via email
- 🔐 OTP-based authentication (printed in logs)
- 🔁 OTP verification
- ⏳ Rate limiting for OTP requests
- 🐳 Docker support for containerized deployment

---

## 🔧 API Endpoints

| Method | Endpoint              | Description                 |
|--------|-----------------------|-----------------------------|
| POST   | `/api/register`       | Register a new user         |
| POST   | `/api/request-otp`    | Request an OTP via email    |
| POST   | `/api/verify-otp`     | Verify the received OTP     |

---

## 🛠️ Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/PranjalAyare/Email_Otp_Auth.git
cd Email_Otp_Auth
2. Create Virtual Environment & Install Dependencies
pip install -r requirements.txt
3. Apply Migrations and Run Server
python manage.py migrate
python manage.py runserver
🧪 Testing the API
You can test the following endpoints using tools like Postman, cURL, or Thunder Client:

POST /api/register – with {"email": "user@example.com"}

POST /api/request-otp – with {"email": "user@example.com"}

POST /api/verify-otp – with {"email": "user@example.com", "otp": "123456"}

⚠️ OTPs will be printed in the terminal logs (as a placeholder for email sending).

🐳 Docker Setup (Optional)
1. Build and Start the Container

docker-compose up --build
2. Access the API
Visit: http://localhost:8000

📌 Notes
Rate limiting is enabled on OTP requests to prevent abuse.

Email sending is mocked by printing OTPs to the console.

Secure and extensible for real-world authentication.

📄 License
This project is licensed under the MIT License. Feel free to use and modify it.

🙋‍♂️ Author
Created by Pranjal Ayare
GitHub: github.com/PranjalAyare

