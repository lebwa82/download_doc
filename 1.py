from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#for file in file_list:
#    print('title: %s, id: %s' % (file['title'], file['id']))

print(type(file_list[0]))
print(len(file_list[0]))
#print(file_list[0])



file1 = drive.ListFile({'q': "'{1z8NsAr1mqSmKe8jxNfPb0oJwnDWLlsrL}' in parents and trashed=false"}).GetList()

# to download all files in a folder . Here file1 is the folder that we want to download
for file in file1:
   print('title: %s, id: %s' % (file['title'], file['id']))
   file1.GetContentFile(file1['title'])

'''
#print(file_list[0])

fileID = '1z8NsAr1mqSmKe8jxNfPb0oJwnDWLlsrL'
filetodownload = drive.CreateFile({'id':fileID})
filetodownload.GetContentFile('1st')
print("done")
'''