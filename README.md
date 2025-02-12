# Employee Management System

## Overview
The Employee Management System is a GUI-based application built using Tkinter and MySQL. It allows users to manage employee records, salaries, and attendance efficiently.

## Features
- **Employee Records Management**
  - Add new employees
  - View employee details
  - Update employee information
  - Delete employee records

- **Employee Salary Management**
  - Add salary details
  - View salary details
  - Update salary records
  - Delete salary records

- **Employee Attendance Management**
  - Add attendance records
  - View attendance records
  - Update attendance records
  - Delete attendance records

## Requirements
- Python 3.x
- Tkinter (built-in with Python)
- MySQL Connector for Python (`pip install mysql-connector-python`)
- MySQL Server

## Database Configuration
The application connects to MySQL and creates a database named `employprofile` with three tables:
- `empregis`: Stores employee details
- `empsalary`: Stores salary records
- `attendance`: Stores attendance records

Ensure you update the MySQL credentials in the script before running the application:
```python
myd = emp.connect(host="localhost", user="username", password="YourPassword", charset="utf8")
```

## How to Run
1. Install MySQL and ensure it is running.
2. Install required dependencies:
   ```
   pip install mysql-connector-python
   ```
3. The GUI will launch, allowing you to manage employee records.

## UI Components
- **Show Records**: Displays all records from the selected table.
- **Update Records**: Opens a window to modify existing records.
- **Delete Records**: Removes an entry from the selected table.

## Customization
- To change the GUI colors, modify the `root.config(bg="<color>")` and label styles.
- To add icons, use:
  ```
  icon = PhotoImage(file="icon.png")
  window.iconphoto(False, icon)
  ```
