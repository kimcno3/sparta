from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

# 클라이언트가 서버에게 'localhost:5000/' 라는 이름의 문을 통해 파일을 요청
# 서버에서는 flask 에서 만든 함수 활용하여 요청받은 루트의 함수를 돌려 나온 return 값을 다시 클라이언트에게 전송
   # 그 함수란? render_template: 자동으로 'templates' 폴더의 ('ㅇㅇㅇ.ㅇㅇ')이름의 파일을 서버로 가져오는 역할

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
#
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)