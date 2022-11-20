##Eklentiler
import os

os.system("apt-get install figlet")
os.system("apt-get install Crunch")
os.system("clear")
os.system("figlet Password Security Tool")

print("""



=================================================

1)Password Sorgu
2)Password List Creater
3)Exit
	
=================================================
	
	
	
""")

Module = int(input("Lütfen Module Numarasını Giriniz: "))

if Module == 1:
	Type = int(input("Lütfen Bir Tür Numarası Seçiniz: "))

	if Type == 1:
		print("""
			
			
		""")
		Pass = input("Lütfen Şifrenizi Giriniz:")
		
		if "Ş"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ş"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "İ"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ı"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ğ"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ğ"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ç"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ç"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ö"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ö"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ü"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ü"  in Pass:
			print("Özel Karakter Olmamalı")
		else:
			with open(r"/root/Masaüstü/MyTools/MakeMoneyTools/PasswordTools/WordList/Gmail.txt", 'r') as f:
				bul = 0
				for index,line in enumerate(f):
					if Pass in line:
						bul = 1
					if bul == 1:
						print("Gmail'da Güvenlik Açığı Var Lütfen Şifrenizi Değiştirin")
					else:
						print("Gmail'da Güvenlik Açığı Yok İyi Günler Dilerim")
			print("İşlem Bitti")	
	if Type == 2:
		print("""
			
			
		""")
		Pass = input("Lütfen Şifrenizi Giriniz:")
		
		if "Ş"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ş"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "İ"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ı"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ğ"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ğ"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ç"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ç"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ö"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ö"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ü"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ü"  in Pass:
			print("Özel Karakter Olmamalı")
		else:
			with open(r"/root/Masaüstü/MyTools/MakeMoneyTools/PasswordTools/WordList/İnstagram.txt", 'r') as f:
				bul = 0
				for index,line in enumerate(f):
					if Pass in line:
					bul = 1
					if bul == 1:
					print("İnstagram'da Güvenlik Açığı Var Lütfen şifrenizi Değiştirin")
				else:
					print("İnstagram'da Güvenlik Açığı Yok İyi Günler Dilerim")
			print("İşlem Bitti")
	if Type == 3:
		print("""
			
			
		""")
		Pass = input("Lütfen Şifrenizi Giriniz:")
		
		if "Ş"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ş"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "İ"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ı"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ğ"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ğ"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ç"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ç"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ö"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ö"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "Ü"  in Pass:
			print("Özel Karakter Olmamalı")
		elif "ü"  in Pass:
			print("Özel Karakter Olmamalı")
		else:
			with open(r"/root/Masaüstü/MyTools/MakeMoneyTools/PasswordTools/WordList/Facebook.txt", 'r') as f:
				bul = 0
				for index,line in enumerate(f):
					if Pass in line:
						bul = 1
				if bul == 1:
					print("FaceBook'da Güvenlik Açığı Var Lütfen Şifrenizi Değiştirin")
				else:
					print("FaceBook'da Güvenlik Açığı Yok İyi Günler Dilerim")
			print("İşlem Bitti")
if Module == 2:
	os.system("apt-get install Crunch")
