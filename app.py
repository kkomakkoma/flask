# -*- coding: UTF-8 -*-
import os
from flask import Flask, url_for, render_template, request, redirect, Response
from werkzeug import secure_filename

UPLOAD_PATH='/var/www/flask/static/uploads'
ALLOWED_EXTENSIONS=set(['txt','pdf','png','jpg','jpeg','gif','mp4'])
app = Flask(__name__)
app.config['UPLOAD_PATH'] = UPLOAD_PATH
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploaded', methods=['GET','POST'])
def uploaded():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
			return redirect(url_for('uploaded', filename=filename))
	
	
	ext = request.args.get('filename').rsplit('.',1)[1]
	if ext in ('png','jpg','jpeg','gif'):
		return render_template('image.html')
	elif ext in ('mp4','avi','mpeg'):
		return render_template('video.html')
	else:
		return render_template('error.html')

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

