id = "kopo15"
pw = "kkkk15"

def account(userid,userpw) :
    if id == userid:
        if pw == userpw:
            print("로그인 완료!")

        else:
            print("다시 시도하세요 - 비밀번호 오류")

    else:
        print("다시 시도하세요 - 아이디 오류")


input_id = input("id:")
input_pw = input("pw:")
account(input_id,input_pw)
