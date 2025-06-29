# Flask + MongoDB CRUD API (Dockerized)

Hi! This is a simple REST API I built using **Flask** and **MongoDB**. The goal was to perform full CRUD (Create, Read, Update, Delete) operations on a User resource using a clean and modular project structure. The whole app runs inside Docker using `docker-compose`.

---

## 💻 What It Does

- Adds new users
- Gets all users or a specific user
- Updates user info
- Deletes a user
- All using REST API endpoints with MongoDB as the backend

---

## 🧰 Tools & Tech Used

- **Flask** – Python web framework
- **MongoDB** – For storing user data
- **PyMongo** – MongoDB driver for Python
- **Docker & Docker Compose** – To containerize and run everything
- **Postman** – For testing API requests
- **.env** – For managing configs like DB URI

---

## 📁 Folder Structure

flask-mongodb-crud/
├── app/
│ ├── models/
│ ├── routes/
│ └── config.py
├── tests/
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── main.py
## ⚙️ How to Run (Using Docker)

Make sure Docker is installed, then:

```bash
git clone https://github.com/Meghna1904/flask-mongodb-crud.git
cd flask-mongodb-crud
docker-compose up --build

The API will be running at:

http://localhost:5000