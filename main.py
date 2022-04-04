import os
import urllib.parse
from datetime import datetime

from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)

app.config['UPLOAD_PATH'] = '/uploads'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SAVE_PATH'] = 'saved'

app.config["MAX_CONTENT_LENGTH"] = 3 * 1024 * 1024 * 1024 # 3 GB


@app.route('/upload_video', methods=['POST'])
# @cross_origin()
def upload_audio():
    f = request.files['file']
    print(request.form)
    print(request.files)
    uid = request.form['uid']
    safe_uid = urllib.parse.quote(uid)
    print(safe_uid)
    path = os.path.join(app.config['UPLOAD_PATH'], uid)
    os.makedirs(app.config['UPLOAD_PATH'], exist_ok=True)
    f.save(os.path.join(path, f'file_{safe_uid}_{datetime.now().strftime("%Y-%m-%dT-%H-%M-%S-%f%z")}.mp4'))
    return "done"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    app.config['SERVER_NAME'] = os.environ['URL']
