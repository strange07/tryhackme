import os
import zipfile
import sys

param_1 = sys.argv[1]
currentpath = os.getcwd()
os.makedirs(param_1 + "_extracted")
with zipfile.ZipFile(param_1,'r')  as main_zip:
	main_zip.extractall(currentpath +"/"+ param_1 + "_extracted")

os.makedirs(currentpath + "/extracted")
pathtoextract = currentpath+ "/extracted"
def question1():
	Files = os.listdir(currentpath + param_1 + "_extracted")
	mainpath = currentpath + param_1 + "_extracted"
	for file in Files:
		filepath = (mainpath + '/' + file)
		if filepath.endswith('.zip'):
			with zipfile.ZipFile(filepath, 'r') as zip_ref:
				zip_ref.extractall(pathtoextract)

	files_question1 = os.listdir(pathtoextract)
	counter = 0
	for files in files_question1:
		counter += 1
	#print("Files extracted: ",counter)
	return counter


def question2():
	Files = os.listdir(pathtoextract)
	mainpath = pathtoextract
	for files in Files:
		filepath = (mainpath + '/' + files)
		cmd = 'exiftool ' + filepath + ' >> exiftool.txt' 
		os.system(cmd)
		with open(currentpath + '/exiftool.txt','r') as f:
			metadata = f.readlines()
		counter = 0
		for line in metadata:
		    if "Version" in line and "1.1" in line:
		        counter += 1
	return counter

def question3():
	Files = os.listdir(pathtoextract)
	mainpath = pathtoextract
	for files in Files:
		filepath = (mainpath + '/' + files)
		try:
			with open(filepath,'r') as f:
				data = f.read()
				if "password" in data:
					password_found = filepath
					return password_found
		except:
			continue

print("Files Extracted: ",question1())
print("Files containing Version: 1.1 in their metadata: ",question2())
print("Password Found in :",question3())
