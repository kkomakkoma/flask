# -*- coding: UTF-8 -*-
import os
from flask import Flask, url_for, render_template, request, redirect, Response
from werkzeug import secure_filename

import infofile
info = infofile.InfoFile()

import detection

ALLOWED_EXTENSIONS=set(['txt','pdf','png','jpg','jpeg','gif','mp4'])
app = Flask(__name__)
app.config['UPLOAD_PATH'] = infofile.UPLOAD_PATH
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploaded', methods=['GET','POST'])
def uploaded():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
                        # file name into class
                        info.setfilepath(file.filename)
			file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
			return redirect(url_for('uploaded', filename=filename))
        
        #info.setfilepath(request.args.get('filename'))
	filefullpath = info.getfilefullpath()
        filefullname = info.getfilefullname()
        ext = info.getfileext()


	if ext in ('png','jpg','jpeg','gif'):
                detection.detectionImage(infofile.UPLOAD_PATH, filefullname)
		return render_template('image.html')
	elif ext in ('mp4'):
                detection.detectionVideo(infofile.UPLOAD_PATH, filefullname)
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

