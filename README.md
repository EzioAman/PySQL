# PySQL — MySQL Database Viewer (Python GUI)

PySQL is a **Python-based graphical interface for interacting with a MySQL database**.
It allows users to fetch and display data from database tables and execute custom SQL queries through an easy-to-use GUI.

The project demonstrates integration between **Python, MySQL, and a desktop GUI using Tkinter**.

---

# 📌 Project Overview

This project connects a Python application to a MySQL database and displays query results in a **dynamic table interface**.

Users can:

* Retrieve records from predefined tables
* Execute custom SQL queries
* View results in a structured table format
* Interact with a database without using the command line

---

# ✨ Features

✔ Connects to a **MySQL database**
✔ Fetch data from multiple tables
✔ Execute **custom SQL queries**
✔ Display results in a **dynamic table view**
✔ Scrollable results table
✔ Simple GUI built with Tkinter

---

# 🛠 Technologies Used

* **Python**
* **Tkinter (GUI framework)**
* **MySQL**
* **mysql-connector-python**

---

# 📂 Project Structure

```
PySQL
│
├── DBMS.py
└── README.md
```

---

# ⚙️ How the Application Works

The program connects to a MySQL database using:

```python
mysql.connector.connect()
```

The GUI provides buttons to fetch data from tables such as:

* Students
* Staff
* Salary

Users can also write and execute **custom SQL queries** directly from the interface.

---

# 🚀 Running the Project

### 1️⃣ Install dependency

```
pip install mysql-connector-python
```

### 2️⃣ Configure database connection

Update the connection credentials inside `DBMS.py`.

Example:

```
host="localhost"
user="root"
password="your_password"
database="your_database"
```

### 3️⃣ Run the application

```
python DBMS.py
```

The GUI will open and allow interaction with the database.

---

# 📊 Example Use Cases

* Viewing student records
* Checking staff information
* Managing salary data
* Running custom SQL queries for analysis

---

# ⚠️ Security Note

Avoid committing real database credentials to public repositories.
Use environment variables or configuration files for sensitive information.

---

# 👤 Author

**Aman Sinha**

GitHub:
https://github.com/EzioAman
