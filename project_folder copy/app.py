from flask import Flask, render_template
import pandas as pd
import qrcode
import os
#welcome
# يا اهلا بمن فتح بوابه الجحيم
app = Flask(__name__)

# Excel تحميل بيانات الطلاب من ملف 
def load_data():
    #you have here to get the path of the file from folders and put it in the ('')
    #>>>>df = pd.read_excel('/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/college/uni/Web-application/Web-application/project_folder/students_data 3.xlsx')
    df['national_id'] = df['national_id'].astype(str)
    return df.set_index('national_id')

students_data = load_data()

# QR Codes لجميع الطلاب
def generate_all_qr_codes():
    for national_id in students_data.index:
        #ipشيل الكومنت الي تحتي لما تجيب ال 
        #>>>student_url = f'http://<put your raoter ip addres here use (ipconfig) in terminal for windos>:5000/student/{national_id}'
        #مثلا كدا
        #student_url = f'http://127.0.0.1:5000/student/{national_id}'
        img = qrcode.make(student_url)
        qr_path = f'qr_codes/{national_id}.png'
        img.save(qr_path)
        print(f'QR Code generated for {national_id} at {qr_path}')

# إنشاء صفحة لعرض بيانات الطالب
@app.route('/student/<national_id>')
def student(national_id):
    try:
        student_info = students_data.loc[national_id]
        return render_template('student.html', 
                               name=student_info['name'], 
                               national_id=national_id, 
                               paid=student_info['paid'])
    except KeyError:
        return "Student not found", 404

if __name__ == '__main__':
    # QR Codes التأكد من وجود مجلد لحفظ 
    if not os.path.exists('qr_codes'):
        os.makedirs('qr_codes')

    #QR Codes توليد  لجميع الطلاب
    generate_all_qr_codes()
    
 #دا عشان يشغل السيرفر 
    app.run(host='0.0.0.0', port=5000, debug=True)

