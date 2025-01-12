
# MySQL User Deletion Script

This project provides a Python script to securely delete user IDs (UIDs) from a MySQL database. It is designed for simplicity, security, and efficiency, ensuring a smooth experience for database administrators and developers.

---

## 🔑 Key Features
- **Secure Connection:** Connects to the MySQL database using credentials stored in environment variables.
- **UID Validation:** Ensures only valid UIDs are processed.
- **Detailed Reporting:** Displays deleted and not-found UIDs after the operation.
- **Error Handling:** Handles database connection and query errors gracefully.

---

## 🛠️ Prerequisites
- **Python:** Version 3.7 or higher
- **Libraries:**
  - `mysql-connector-python` (`pip install mysql-connector-python`)
  - `python-dotenv` (`pip install python-dotenv`)
- **MySQL Database:** Ensure you have a `Users` table with a `uID` column.
- **Environment Variables:** Use a `.env` file to store database credentials securely.

---

## 🚀 Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/mysql-user-deletion-script.git
cd mysql-user-deletion-script
```

### Step 2: Set Up Environment Variables
Create a `.env` file in the project directory and add your database credentials:
```env
DB_HOST=your-database-host
DB_PORT=3306
DB_USER=your-database-username
DB_PASSWORD=your-database-password
DB_NAME=your-database-name
```

### Step 3: Install Required Libraries
```bash
pip install mysql-connector-python python-dotenv
```

### Step 4: Run the Script
```bash
python delete_users.py
```

### Step 5: Enter UIDs to Delete
When prompted, enter the UIDs to delete, separated by commas:
```text
Enter UIDs to delete, separated by commas: 1, 2, 3
```

---

## 📝 Example Output
```text
Enter UIDs to delete, separated by commas: 1, 2, 3
UID 1 successfully deleted.
UID 2 not found in the database.
UID 3 successfully deleted.

Operation Completed.
Deleted UIDs: 1, 3
Not Found UIDs: 2
```

---

## 🛡️ Security Note
- **Sensitive Information:** The `.env` file containing credentials is excluded from version control using `.gitignore`.
- **Best Practices:** Never hardcode credentials in the script.

---

## 🔧 Project Structure
```
mysql-user-deletion-script/
├── delete_users.py   # Main Python script
├── .env              # Environment variables (not included in GitHub)
├── .gitignore        # Ignores .env file
├── README.md         # Project description
```

---

## 📚 Technologies Used
- **Python:** Programming language for the script.
- **MySQL:** Database for user management.
- **mysql-connector-python:** Library for connecting Python to MySQL.
- **dotenv:** Library for managing environment variables.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to improve the project.

---

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 📧 Contact
If you have any questions or suggestions, feel free to reach out:
- **Email:** berksenturk00@gmail.com
