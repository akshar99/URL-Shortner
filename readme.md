# URL Shortener API (FastAPI)

A simple and efficient **URL Shortener** built with **FastAPI** and a minimal **HTML frontend**.

---

## 🚀 Features

- **Shorten Long URLs**: Convert long URLs into short, easy-to-share links.
- **Redirect Mechanism**: Use short URLs to redirect users to the original website.
- **FastAPI Backend**: Built with Python's FastAPI framework for high performance.
- **Simple Frontend**: Basic HTML, CSS, and JavaScript frontend to interact with the API.
- **CORS Enabled**: Ensures seamless frontend-backend communication.

---

## 🛠 Tech Stack

- **Backend**: FastAPI, SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (or PostgreSQL)
- **Validation**: Pydantic
- **Security**: Secrets-based URL generation

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository


## 2️⃣ Set up the Backend

### Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### Install dependencies:

```sh
pip install -r requirements.txt
```

### Run the FastAPI server:

```sh
uvicorn testProject.main:app --reload
```

### Open the API documentation:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 3️⃣ Set up the Frontend

1. Inside the project directory, locate `index.html` (your frontend).
2. Open `index.html` in a browser.
3. The frontend interacts with the FastAPI backend to create and retrieve short URLs.

---

## 🛠 API Endpoints

| Method | Endpoint      | Description                      |
|--------|--------------|----------------------------------|
| `GET`  | `/`          | Welcome message                 |
| `POST` | `/url`       | Create a short URL              |
| `GET`  | `/{url_key}` | Redirect to the original URL    |

---

## 🛠 Example Usage

### 🔹 Create a Short URL

**Request:**
```json
POST /url
{
  "target_url": "https://github.com/akshar99"
}
```

**Response:**
```json
{
  "target_url": "https://github.com/akshar99/",
  "url": "ABCDE",
  "admin_url": "XKRTU123"
}
```

---

### 🔹 Redirect to Original URL

Visit:  
```
http://127.0.0.1:8000/ABCDE
```
This redirects to **https://github.com/akshar99/**.

---

## ✨ Future Enhancements

✅ Custom short URL generation  
✅ Click tracking and analytics  
✅ Expiry date for short URLs  
✅ User authentication and dashboard  
✅ Docker containerization  

---

## 📌 Author

**Akshar Rastogi**  
GitHub: [akshar99](https://github.com/akshar99)
