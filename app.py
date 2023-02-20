from flask import Flask, request
from db import add_image, like, dislike, get_data

app = Flask(__name__)

@app.route('/api/add-img', methods=['POST'])
def home():
    if request.method == 'POST':
        data = request.get_json(force=True)
        photo_id = data['photo_id']

        if add_image(photo_id):
            return 'OK: Rasm qo`shildi'
        else:
            return 'ERROR: XATOLIK'       

@app.route('/api/like', methods=['POST'])
def like_photo():
    if request.method == 'POST':
        data = request.get_json(force=True)
        photo_id = data['photo_id']
        chat_id = data['chat_id']

        if like(photo_id, chat_id):
            return 'OK: Rasm yoqdi'
        else:
            return 'ERROR: XATOLIK'

@app.route('/api/dislike', methods=['POST'])
def dislike_photo():
    if request.method == 'POST':
        data = request.get_json(force=True)
        photo_id = data['photo_id']
        chat_id = data['chat_id']

        if dislike(photo_id, chat_id):
            return 'OK: Rasm yoqmadi'
        else:
            return 'ERROR: XATOLIK'

@app.route('/api/get-data/<photo_id>')
def get_photo_data(photo_id: str):
    data = get_data(photo_id)
    if data:
        return data
    else:
        return 'ERROR: XATOLIK'

if __name__ == '__main__':
    app.run(debug=True)
