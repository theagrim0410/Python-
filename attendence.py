import tkinter as tk
from tkinter import PhotoImage

from tkinter import messagebox, ttk
import mysql.connector as emp

# Connect to the MySQL database
myd = emp.connect(host="localhost", user="your user name",
                  password="your password", charset="utf8")
mycursor = myd.cursor()

# Create database and tables if they do not exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS employprofile")
mycursor.execute("USE employprofile")
mycursor.execute("""CREATE TABLE IF NOT EXISTS empregis (
        id_no_ VARCHAR(20) PRIMARY KEY,
        name_of_employ VARCHAR(30),
        phone_no CHAR(10),
        address VARCHAR(30),
        date_of_birth DATE
    )""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS empsalary (
        employ_name VARCHAR(20),
        id_no_ VARCHAR(20),
        designation VARCHAR(10),
        salary_given VARCHAR(25),
        salary_remained VARCHAR(10)
    )""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS attendance (
        employ_name VARCHAR(20),
        id_no VARCHAR(10),
        attendance VARCHAR(10)
    )""")
myd.commit()


def show_table_data(table_name):
    mycursor.execute(f"SELECT * FROM {table_name}")
    records = mycursor.fetchall()
    if records:
        messagebox.showinfo(f"{table_name} Data", "\n".join(
            str(record) for record in records))
    else:
        messagebox.showwarning("No Data", f"No records found in {table_name}.")


def update_table_entry(table_name, columns):
    def submit():
        id_no = entry_id.get()
        values = [entry.get() for entry in entries]
        set_clause = ", ".join(f"{col} = %s" for col in columns)
        query = f"UPDATE {table_name} SET {set_clause} WHERE id_no_ = %s"
        try:
            mycursor.execute(query, values + [id_no])
            myd.commit()
            messagebox.showinfo(
                "Success", f"{table_name} updated successfully!")
            window.destroy()
        except emp.Error as err:
            messagebox.showerror("Error", str(err))

    window = tk.Toplevel()
    window.title(f"Update {table_name}")
    window.geometry("400x400")
    window.config(bg="#d5f4e6")
    ttk.Label(window, text="ID:").pack(pady=5)
    entry_id = ttk.Entry(window)
    entry_id.pack(pady=5)
    entries = []
    for col in columns:
        ttk.Label(window, text=f"{col}:").pack(pady=5)
        entry = ttk.Entry(window)
        entry.pack(pady=5)
        entries.append(entry)
    ttk.Button(window, text="Update", command=submit).pack(pady=20)


def delete_table_entry(table_name):
    def submit():
        id_no = entry_id.get()
        try:
            mycursor.execute(
                f"DELETE FROM {table_name} WHERE id_no_ = %s", (id_no,))
            myd.commit()
            messagebox.showinfo(
                "Success", f"Record deleted from {table_name}!")
            window.destroy()
        except emp.Error as err:
            messagebox.showerror("Error", str(err))

    window = tk.Toplevel()
    window.title(f"Delete from {table_name}")
    window.geometry("300x400")
    window.config(bg="#ffef96")
    ttk.Label(window, text="Enter ID:").pack(pady=5)
    entry_id = ttk.Entry(window)
    entry_id.pack(pady=5)
    ttk.Button(window, text="Delete", command=submit).pack(pady=20)


# GUI functions
def create_employee():
    def submit():
        no = entry_id.get()
        name = entry_name.get()
        phone = entry_phone.get()
        address = entry_address.get()
        dob = entry_dob.get()

        try:
            mycursor.execute("INSERT INTO empregis VALUES (%s, %s, %s, %s, %s)",
                             (no, name, phone, address, dob))
            myd.commit()
            messagebox.showinfo("Success", "Account created successfully!")
            window.destroy()
        except emp.Error as err:
            messagebox.showerror("Error", str(err))

    window = tk.Toplevel()
    window.title("Create Employee")
    window.geometry("400x400")
    window.config(bg="#d5f4e6")

    ttk.Label(window, text="ID:").pack(pady=5)
    entry_id = ttk.Entry(window)
    entry_id.pack(pady=5)

    ttk.Label(window, text="Name:").pack(pady=5)
    entry_name = ttk.Entry(window)
    entry_name.pack(pady=5)

    ttk.Label(window, text="Phone:").pack(pady=5)
    entry_phone = ttk.Entry(window)
    entry_phone.pack(pady=5)

    ttk.Label(window, text="Address:").pack(pady=5)
    entry_address = ttk.Entry(window)
    entry_address.pack(pady=5)

    ttk.Label(window, text="Date of Birth (yyyy-mm-dd):").pack(pady=5)
    entry_dob = ttk.Entry(window)
    entry_dob.pack(pady=5)

    ttk.Button(window, text="Submit", command=submit).pack(pady=20)


def enter_salary():
    def submit():
        name = entry_name.get()
        id_no = entry_id.get()
        designation = entry_designation.get()
        salary_given = entry_salary_given.get()
        salary_remained = entry_salary_remained.get()

        try:
            mycursor.execute("INSERT INTO empsalary VALUES (%s, %s, %s, %s, %s)",
                             (name, id_no, designation, salary_given, salary_remained))
            myd.commit()
            messagebox.showinfo(
                "Success", "Salary details added successfully!")
            window.destroy()
        except emp.Error as err:
            messagebox.showerror("Error", str(err))

    window = tk.Toplevel()
    window.title("Enter Salary")
    window.geometry("400x400")
    window.config(bg="#f7cac9")

    ttk.Label(window, text="Name:").pack(pady=5)
    entry_name = ttk.Entry(window)
    entry_name.pack(pady=5)

    ttk.Label(window, text="ID:").pack(pady=5)
    entry_id = ttk.Entry(window)
    entry_id.pack(pady=5)

    ttk.Label(window, text="Designation:").pack(pady=5)
    entry_designation = ttk.Entry(window)
    entry_designation.pack(pady=5)

    ttk.Label(window, text="Salary Given:").pack(pady=5)
    entry_salary_given = ttk.Entry(window)
    entry_salary_given.pack(pady=5)

    ttk.Label(window, text="Salary Remained:").pack(pady=5)
    entry_salary_remained = ttk.Entry(window)
    entry_salary_remained.pack(pady=5)

    ttk.Button(window, text="Submit", command=submit).pack(pady=20)


def mark_attendance():
    def submit():
        name = entry_name.get()
        id_no = entry_id.get()
        attendance = entry_attendance.get()

        try:
            mycursor.execute("INSERT INTO attendance VALUES (%s, %s, %s)",
                             (name, id_no, attendance))
            myd.commit()
            messagebox.showinfo("Success", "Attendance recorded successfully!")
            window.destroy()
        except emp.Error as err:
            messagebox.showerror("Error", str(err))

    window = tk.Toplevel()
    window.title("Mark Attendance")
    window.geometry("400x400")
    window.config(bg="#ffef96")

    ttk.Label(window, text="Name:").pack(pady=5)
    entry_name = ttk.Entry(window)
    entry_name.pack(pady=5)

    ttk.Label(window, text="ID:").pack(pady=5)
    entry_id = ttk.Entry(window)
    entry_id.pack(pady=5)

    ttk.Label(window, text="Attendance (Present/Absent):").pack(pady=5)
    entry_attendance = ttk.Entry(window)
    entry_attendance.pack(pady=5)

    ttk.Button(window, text="Submit", command=submit).pack(pady=20)


def main():
    root = tk.Tk()
    root.title("Employee Management System")
    root.geometry("500x700")
    root.config(bg="#2c3e50")
    icon = PhotoImage(file="path/to/your/icon.png")
    root.iconphoto(False, icon)

    ttk.Label(root, text="Employee Management System", font=(
        "Arial", 16), background="#2c3e50", foreground="white").pack(pady=20)

    ttk.Button(root, text="Create Employee", command=create_employee).pack(
        pady=10, fill='x', padx=20)
    ttk.Button(root, text="Enter Salary", command=enter_salary).pack(
        pady=10, fill='x', padx=20)
    ttk.Button(root, text="Mark Attendance", command=mark_attendance).pack(
        pady=10, fill='x', padx=20)

    tables = {
        "Employee Records": "empregis",
        "Employee Salary": "empsalary",
        "Attendance Records": "attendance"
    }

    for name, table in tables.items():
        ttk.Button(root, text=f"Show {name}", command=lambda t=table: show_table_data(
            t)).pack(pady=10, fill='x', padx=20)
        ttk.Button(root, text=f"Update {name}", command=lambda t=table: update_table_entry(t, ["name_of_employ", "phone_no", "address", "date_of_birth"] if t == "empregis" else [
                   "employ_name", "designation", "salary_given", "salary_remained"] if t == "empsalary" else ["employ_name", "attendance"])).pack(pady=10, fill='x', padx=20)
        ttk.Button(root, text=f"Delete {name}", command=lambda t=table: delete_table_entry(
            t)).pack(pady=10, fill='x', padx=20)

    root.mainloop()
    myd.close()


if __name__ == "__main__":
    main()
