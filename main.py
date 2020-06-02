#-*- coding:utf-8 -*-
import itertools
import zipfile
import time
import os

nowtime = time.time()

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
		return "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+`~"
	elif answer == '5':
		return "012345789"
	else:
		print ("\n1: 소문자\n2: 소문자, 대문자\n3: 소문자, 대문자, 숫자\n4: 소문자, 대문자, 숫자, 특수문자\n5: 숫자")
		setting_string()

def check_password(string, zFile, nowtime, time):
	for len in range(1, 17):
		attempt = itertools.product(string, repeat = len)
		for attemptst in attempt:
			passwd = ''.join(attemptst)
			print(":" + passwd)
			print(time.time() - nowtime)
			try:
				zFile.extractall(pwd = passwd.encode())
				print ("\n\n비밀번호: "+passwd)
				print(time.time() - nowtime)
				return True
			except:
				pass

def main():
	zipfilename = input("압축해제할 파일명: ")
	if zipfile.is_zipfile(zipfilename):
		zFile = zipfile.ZipFile(zipfilename)
	
		string = setting_string()
		result = check_password(string, zFile, nowtime, time)
	
		if result != True: 
			print ("\n압축파일의 비밀번호를 찾지 못했습니다. 대입할 문자를 재설정해주세요")
		exit()
	else:
		print ("없는 파일이거나 손상된 압축 파일입니다.")
		main()
	
if __name__ == "__main__":
	main()