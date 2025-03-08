URL Shortener API (FastAPI)
A simple and efficient URL shortener built with FastAPI and a basic HTML frontend.

🚀 Features
Generate short URLs from long URLs
Redirect users to the original URL using the short URL
Simple frontend using HTML, CSS, and JavaScript
API built with FastAPI and database management using SQLAlchemy
CORS enabled for frontend communication
🛠 Tech Stack
Backend: FastAPI, SQLAlchemy, SQLite/PostgreSQL
Frontend: HTML, CSS, JavaScript (vanilla)
Database: SQLite (or any SQL database)
Validation: Pydantic
Security: UUID and secrets for URL generation
🖥 Installation & Setup
1️⃣ Clone the repository
sh
Copy
Edit
git clone https://github.com/akshar99/URL-Shortener.git
cd URL-Shortener
2️⃣ Set up the Backend
Create and activate a virtual environment:
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
Install dependencies:
sh
Copy
Edit
pip install -r requirements.txt
Run the FastAPI server:
sh
Copy
Edit
uvicorn testProject.main:app --reload
Open the API documentation:
Swagger UI: http://127.0.0.1:8000/docs
Redoc UI: http://127.0.0.1:8000/redoc
3️⃣ Set up the Frontend
Inside the project directory, locate index.html (your frontend).
Open index.html in a browser.
The frontend interacts with the FastAPI backend to create and retrieve short URLs.
🛠 API Endpoints
Method	Endpoint	Description
GET	/	Welcome message
POST	/url	Create a short URL
GET	/{url_key}	Redirect to the original URL
🛠 Example Usage
🔹 Create a Short URL
Request:

json
Copy
Edit
POST /url
{
  "target_url": "https://realpython.com/"
}
Response:

json
Copy
Edit
{
  "target_url": "https://realpython.com/",
  "url": "ABCDE",
  "admin_url": "XKRTU123"
}
🔹 Redirect to Original URL
Visit http://127.0.0.1:8000/ABCDE to be redirected.

✨ Future Enhancements
✅ Custom short URL generation
✅ Click tracking and analytics
✅ Expiry date for short URLs
✅ User authentication and dashboard
✅ Docker containerization
📌 Author
Akshar Rastogi
GitHub: akshar99
