import os

# إنشاء هيكل المجلدات
project_name = "flask_project"
os.makedirs(f"{project_name}/templates", exist_ok=True)

# كود app.py
app_code = """
from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

# قراءة البيانات من ملف Excel
data = pd.read_csv('sample.csv')

# جلب القيم الفريدة لكل قائمة منسدلة
days = data['Day'].unique().tolist()
grades = data['Grade'].unique().tolist()
times = data['Time'].unique().tolist()
supervisors = ["Supervisor 1", "Supervisor 2", "Supervisor 3"]

@app.route('/', methods=['GET', 'POST'])
def index():
    students = []
    if request.method == 'POST':
        selected_day = request.form['day']
        selected_grade = request.form['grade']
        selected_time = request.form['time']
        selected_supervisor = request.form['supervisor']

        # نموذج بيانات الطلبة
        students = [
            {"name": "Student 1", "amount": 100},
            {"name": "Student 2", "amount": 150},
            {"name": "Student 3", "amount": 200}
        ]

        if 'submit' in request.form:
            df = pd.DataFrame(students)
            df['Day'] = selected_day
            df['Grade'] = selected_grade
            df['Time'] = selected_time
            df['Supervisor'] = selected_supervisor

            output_file = 'attendance_record.xlsx'
            df.to_excel(output_file, index=False)

            return send_file(output_file, as_attachment=True)

    return render_template('index.html', days=days, grades=grades, times=times, students=students, supervisors=supervisors)

if __name__ == '__main__':
    app.run(port=4050, debug=True)
"""

# كود HTML للصفحة الرئيسية
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attendance Form</title>
</head>
<body>
    <h1>Attendance Form</h1>
    <form method="POST">
        <label for="day">Day:</label>
        <select name="day" id="day" required>
            {% for day in days %}
            <option value="{{ day }}">{{ day }}</option>
            {% endfor %}
        </select>
        <br><br>

        <label for="grade">Grade:</label>
        <select name="grade" id="grade" required>
            {% for grade in grades %}
            <option value="{{ grade }}">{{ grade }}</option>
            {% endfor %}
        </select>
        <br><br>

        <label for="time">Time:</label>
        <select name="time" id="time" required>
            {% for time in times %}
            <option value="{{ time }}">{{ time }}</option>
            {% endfor %}
        </select>
        <br><br>

        <button type="submit" name="load_students">Load Students</button>
        <br><br>

        {% if students %}
        <table border="1">
            <tr>
                <th>Student Name</th>
                <th>Amount</th>
            </tr>
            {% for student in students %}
            <tr>
                <td>{{ student.name }}</td>
                <td>{{ student.amount }}</td>
            </tr>
            {% endfor %}
        </table>
        <br><br>
        {% endif %}

        <label for="supervisor">Supervisor:</label>
        <select name="supervisor" id="supervisor" required>
            {% for supervisor in supervisors %}
            <option value="{{ supervisor }}">{{ supervisor }}</option>
            {% endfor %}
        </select>
        <br><br>

        <button type="submit" name="submit">Submit</button>
    </form>
</body>
</html>
"""

# إنشاء ملف app.py
with open(f"{project_name}/app.py", "w", encoding='utf-8') as f:
    f.write(app_code)

# إنشاء ملف index.html داخل templates
with open(f"{project_name}/templates/index.html", "w", encoding='utf-8') as f:
    f.write(html_code)

print(f"تم إنشاء مشروع Flask بنجاح داخل المجلد: {project_name}")
