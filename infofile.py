# -*- coding: UTF-8 -*-
UPLOAD_PATH = '/var/www/flask/static/uploads'

class InfoFile:
    filefullpath = '' 
    ext = ''
    filepurename = ''
    filename = ''

    def setfilepath(self, filename):
        self.filefullpath = UPLOAD_PATH + '/' + filename
        self.filename = filename

    def getfilefullpath(self):
        return self.filefullpath
    
    def getfilefullname(self):
        return self.filename
    
    def getfilepurename(self):
        if self.filename.rfind('.') != -1:
            self.filepurename = self.filename.rsplit('.',1)[0]
        else:
            print 'Error! Extension is not found'
        return self.filepurename

    def getfileext(self):
        if self.filename.rfind('.') != -1:
           self.ext = self.filename.rsplit('.',1)[1]
        else:
            print 'Error! Extension is not found'
        return self.ext

