TaskVault 🔐  
A secure and modular Flask-based backend API for managing personal tasks featuring user authentication, CRUD functionality, and PostgreSQL integration. Ideal for showcasing backend development skills in RESTful design, JWT Auth, and API deployment.

---

## 🚀 Features

- 🔐 User Registration & Login with JWT authentication
- ✅ Task CRUD: Create, Read, Update, Delete operations
- 🧱 RESTful API structure
- 🗃️ PostgreSQL database integration (or SQLite fallback)
- 🐳 Container-ready with minimal setup
- 🌐 Ready for deployment on Render or Railway

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Auth:** JWT (via Flask-JWT-Extended)
- **Database:** PostgreSQL / SQLite
- **Tools:** Git, Postman, GitHub, Render
- **Deployment:** Render (Planned)

---

## 📁 Folder Structure

taskvault/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── auth.py (Coming Soon)
│ └── models.py (Coming Soon)
├── run.py
├── requirements.txt
├── README.md

yaml
Copy
Edit

---

## 🧪 Setup & Run Locally

```bash
# Clone the repo
git clone https://github.com/sarthak2443/TaskVault.git
cd TaskVault

# Create virtual env (optional but recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python run.py
Server: http://localhost:5000

Test route: GET / → { "msg": "TaskVault API working!" }

🔮 Coming Soon
✅ Complete JWT-based login/register

✅ Task schema & DB models

✅ Full CRUD for Tasks

🌍 Render deployment with live demo link

📄 Swagger/OpenAPI docs

📬 Contact
Made with 💻 by Sarthak Atlasia
📧 sarthak.atlasia@gmail.com


