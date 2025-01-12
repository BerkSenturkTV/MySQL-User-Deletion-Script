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
