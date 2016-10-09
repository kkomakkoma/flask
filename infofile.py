# -*- coding: UTF-8 -*-

class InfoFile(object):
    def __init__(self, upload_path, filename):
        self.filefullpath = upload_path + '/' + filename
        self.filename = filename
        self.ext = ''
        self.filepurename = ''


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

