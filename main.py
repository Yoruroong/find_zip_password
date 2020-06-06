#-*- coding:utf-8 -*-
import itertools
import zipfile as zf
import time
import os
from platform import platform

nowtime = 0

def setting_string():
	print ("\n1: 소문자\n2: 소문자, 대문자\n3: 소문자, 대문자, 숫자\n4: 소문자, 대문자, 숫자, 특수문자\n5: 숫자")
	answer = input("대입할 문자를 선택해주세요: ")
	if answer == '1':
		return "abcdefghijklmnopqrstuvwxyz"
	elif answer == '2':
		return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	elif answer == '3':
		return "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	elif answer == '4':
		return "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+`~\"\\'"
	elif answer == '5':
		return "012345789"
	else:
		print ("\n1: 소문자\n2: 소문자, 대문자\n3: 소문자, 대문자, 숫자\n4: 소문자, 대문자, 숫자, 특수문자\n5: 숫자")
		setting_string()

def check_password(string, zipfile, nowtime, time):
	for len in range(1, 17):
		attempt = itertools.product(string, repeat = len)
		for attemptst in attempt:
			passwd = ''.join(attemptst)
			print("대입한 비밀번호: " + passwd)
			print(str(int(time.time()) - nowtime) + "초")
			try:
				zipfile.extractall(pwd = passwd.encode())
				print ("\n\n비밀번호: "+passwd)
				print(str(int(time.time()) - nowtime) + "초")
				return True
			except:
				if platform().startswith("Linux"): cc = "clear" 
				else: cc = "cls"

				os.system(cc)
				pass

def check_password_by_list(string, zipfile, nowtime, time):
	f = open("list.txt", 'r', encoding='UTF8')
	while True:
		line = f.readline()
		print(line)
		try:
			zipfile.extractall(pwd = line.encode())
			print ("\n\n비밀번호: "+ line)
			print(str(int(time.time()) - nowtime) + "초")
			return True
		except:
			pass
	f.close()

def main():
	zipfilename = input("압축해제할 파일명: ")
	if zf.is_zipfile(zipfilename):
		zipfile = zf.ZipFile(zipfilename)
	
		string = setting_string()
		nowtime = int(time.time())
		#result = check_password_by_list(string, zFile, nowtime, time)

		result = check_password(string, zipfile, nowtime, time)
	
		if result != True: 
			print ("\n압축파일의 비밀번호를 찾지 못했습니다. 대입할 문자를 재설정해주세요")
		exit()
	else:
		print ("없는 파일이거나 손상된 압축 파일입니다.")
		main()
	
if __name__ == "__main__":
	main()
