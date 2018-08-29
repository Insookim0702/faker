# -*- coding: utf-8 -*-
#파이썬 파일에 한글쓰기
from flask import Flask, render_template,request
import random
import csv
from faker import Faker
#names 딕셔너리

app = Flask(__name__)
fake = Faker('ko_kR')

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/result")
def result():
    #1. "/" 날아온 이름 두개를 가져온다.
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    #2. 궁합을 구라친다(50~100사이의 숫자를 랜덤하게 뽑는다.
    goonghap = random.randrange(50,101)
    #names.csv 파일을 만들어서 저장한다.
    f = open('names.csv','a', encoding='utf-8')
    a = csv.writer(f)
    a.writerow([name1, name2])
    f.close
    return render_template('result.html', name1=name1, name2=name2, match =goonghap)
    

@app.route("/admin")
def admin():
    # names에 들어가 있는 모든 이름을 출력한다.
    f = open('names.csv', 'r')
    rr = csv.reader(f)
    names =rr
    print(rr)
    return render_template('admin.html', names=names)
    
@app.route("/ffaker")
def ffaker():
    name = fake.name()
    address = fake.address()
    job =fake.job()
    return render_template('ffaker.html', name = name, address=address, job=job)
    
#flask run --host =0.0.0.0 --port=8080
app.run(host='0.0.0.0', port='8080', debug=True)

#debug=True의 힘
# 서버리로드 할 필요 없다.
