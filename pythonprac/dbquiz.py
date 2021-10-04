from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

matrix = db.movies.find_one({'title':'매트릭스'})
matrix_star = matrix['star']
print(matrix_star)

same_star = list(db.movies.find({'star':matrix_star},{'_id':False}))
for same_star_list in same_star:
    print(same_star_list['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})
# 문자열 통일을 위해 0 이 아닌 '0' 으로 값 입력
