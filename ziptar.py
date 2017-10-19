import shutil
import os
file_path=input("Enter the path of the File :")
res=os.path.exists(file_path)
if(res==True):
	opt=input("MAKE ZIP OR TAR :")
	shutil.make_archive(file_path,format=opt,root_dir=file_path)
	print("FILE IS BEEN CONVERTED TO %s"%(opt))
else:
	print("The path is INVALID!")
