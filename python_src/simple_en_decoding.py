Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#kopo15

password = int(input("비밀번호를 입력하세요 =>"))
비밀번호를 입력하세요 =>1234
print('password : ',password)
password :  1234
encoding = password << 15
print('password 암호화 완료! =>',encoding)
password 암호화 완료! => 40435712
decoding = encoding >> 15
print('password 복호화 완료! =>',decoding)
password 복호화 완료! => 1234
