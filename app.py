from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        infomation = request.form
        subject = infomation['subject']
        grade = infomation['grade']
        score = infomation['score']
        conn = pymysql.connect(host='database-1.csdokwgktrmi.ap-northeast-2.rds.amazonaws.com',
        user='admin', password='tls342005.', db='info', charset='utf8', port=3306)

        curs = conn.cursor()
        sql = """insert info(subject, grade, score values (%s, %s, %s)"""
        curs.execute(sql, (subject, grade, score))

        conn.commit()

        conn.close()

        return redirect('/users')
    return render_template('grade_calc.html')

@app.route('/users')
def users() :
    conn = pymysql.connect(host='database-1.csdokwgktrmi.ap-northeast-2.rds.amazonaws.com',
        user='admin', password='tls342005.', db='info', charset='utf8', port=3306)
    curs = conn.cursor()
    resultValue = curs.execute('select * form users')
    if resultValue > 0 :
        userDetails = curs.fetchall()
        return render_template('grade_calc.html', userDetails = userDetails)

if __name__ == '__main__' :
    app.run(debug = True)