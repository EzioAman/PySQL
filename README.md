# 🗄️ MySQL Database Viewer (Python GUI)

A Python desktop application that connects to a **MySQL database** and allows users to **fetch, view, and execute SQL queries through a graphical interface**.

The application provides a simple interface to interact with database tables such as **Students, Staff, and Salary**, and supports executing **custom SQL queries dynamically**.

---

# 📌 Project Overview

This project demonstrates how to connect a **Python application to a MySQL database** and interact with database tables using a **graphical user interface built with Tkinter**.

The tool enables users to:

* Retrieve records from specific tables
* Execute custom SQL queries
* Display results dynamically in a table format
* Manage database data through a GUI instead of a terminal

---

# ✨ Features

✔ Connect to a **MySQL database**
✔ Fetch records from multiple tables
✔ Execute **custom SQL queries**
✔ Display results dynamically in a **table view**
✔ Scrollable and adjustable data table
✔ User-friendly **GUI interface**

---

# 🛠 Technologies Used

* **Python**
* **Tkinter (GUI framework)**
* **MySQL**
* **mysql-connector-python**

---

# 📂 Project Structure

```
MySQL-Database-Viewer
│
├── DBMS.py
└── README.md
```

---

# ⚙️ How It Works

The application connects to a MySQL database using:

```
mysql.connector
```

Users can:

1. Fetch data from predefined tables such as:

   * Students
   * Staff
   * Salary

2. Enter and execute **custom SQL queries**.

3. View results displayed in a **dynamic table interface** built with Tkinter.

---

# 🚀 How to Run

### 1️⃣ Install required library

```
pip install mysql-connector-python
```

### 2️⃣ Configure database connection

Edit the database connection section inside `DBMS.py`:

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

The GUI will launch and allow interaction with the database.

---

# 📊 Example Use Cases

* Viewing student records
* Checking staff details
* Monitoring salary data
* Running custom SQL queries for analysis

---

# ⚠️ Security Note

Avoid committing real database credentials to public repositories.
Use **environment variables or configuration files** for sensitive information.

---

# 👤 Author

**Aman Sinha**

GitHub:
https://github.com/EzioAman
