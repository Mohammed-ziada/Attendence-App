import tkinter as tk
from tkinter import messagebox
import pandas as pd

# دالة لحفظ البيانات إلى ملف Excel
def save_attendance(day, grade, time, supervisor, students):
    df = pd.DataFrame(students)
    df['Day'] = day
    df['Grade'] = grade
    df['Time'] = time
    df['Supervisor'] = supervisor
    output_file = 'attendance_record.xlsx'
    df.to_excel(output_file, index=False)
    messagebox.showinfo("Success", "Attendance saved successfully!")

# دالة لجمع المدخلات
def submit():
    day = day_var.get()
    grade = grade_var.get()
    time = time_var.get()
    supervisor = supervisor_var.get()
    students = [
        {"name": "Student 1", "amount": 100},
        {"name": "Student 2", "amount": 150},
        {"name": "Student 3", "amount": 200}
    ]
    
    save_attendance(day, grade, time, supervisor, students)

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Attendance Form")

# المتغيرات
day_var = tk.StringVar()
grade_var = tk.StringVar()
time_var = tk.StringVar()
supervisor_var = tk.StringVar()

# إعداد عناصر الواجهة
tk.Label(root, text="Select Day:").pack()
tk.OptionMenu(root, day_var, 'Sunday', 'Monday', 'Tuesday').pack()

tk.Label(root, text="Select Grade:").pack()
tk.OptionMenu(root, grade_var, 'Grade 1', 'Grade 2', 'Grade 3').pack()

tk.Label(root, text="Select Time:").pack()
tk.OptionMenu(root, time_var, '10:00 AM', '11:00 AM', '12:00 PM').pack()

tk.Label(root, text="Select Supervisor:").pack()
tk.OptionMenu(root, supervisor_var, 'Supervisor 1', 'Supervisor 2', 'Supervisor 3').pack()

tk.Button(root, text="Submit", command=submit).pack()

# بدء حلقة التطبيق
root.mainloop()
