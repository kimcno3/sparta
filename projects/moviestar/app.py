from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_stars():
    stars = list(db.mystar.find({}, {'_id': False}).sort("like", -1)) # like 값을 역순으로 정렬하라는 sort 함수
    return jsonify({'stars': stars})


@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']

    target_star = db.mystar.find_one({'name': name_receive})
    current_like = target_star['like']
    new_like = current_like + 1
    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give'] # 브라우저에서 보내준 데이터(post방식은 data 딕셔너리에 입력)를 받아와 변수에 담는다
    db.mystar.delete_one({'name': name_receive}) # DB에 저장
    return jsonify({'msg': '삭제되었습니다!!'}) # 위 과정이 완료되면 return값 전송


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)