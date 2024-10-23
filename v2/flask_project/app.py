from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

# بيانات عينة بدلاً من قراءة ملف Excel
data = {
    'Day': ['Sunday', 'Monday', 'Tuesday'],
    'Grade': ['Grade 1', 'Grade 2', 'Grade 3'],
    'Time': ['10:00 AM', '11:00 AM', '12:00 PM']
}

# جلب القيم الفريدة لكل قائمة منسدلة
days = data['Day']
grades = data['Grade']
times = data['Time']
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
