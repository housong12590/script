from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_HOST'] = '123.207.152.86'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'kx_ops'
app.config['DEBUG'] = True

mongo = PyMongo(app)


@app.route('/')
def index():
    user = mongo.db.build.find({'name': 'coasts'}).sort('tag', -1)
    print(user)
    return ''


@app.route('/images', methods=['POST'])
def images():
    json = request.json
    json.update({'created_at': '123'})
    name = json.get('name')
    print(name)
    print(json)
    mongo.db.build.insert(json)

    return 'images'


app.run()
