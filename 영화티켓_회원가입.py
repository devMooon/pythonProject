member = [0, 0, 0]
member[0] = {"NAME": "", "ID": "", "PASSWORD": "", "securePW": ""}

def signUp():
    print("                    [회원가입]                      ")
    print("==================================================")  # 50
    name = input("이름              :")
    ID = input("ID               :")
    while True:
        PASSWORD = input("PASSWORD<8자 이상>:")
        if len(PASSWORD) < 8:
            print("8자 이상 비밀번호를 입력 하세요.")
            print()
        else:
            break

    member[0]["NAME"] = name
    member[0]["ID"] = ID
    member[0]["PASSWORD"] = PASSWORD
    PASSWORD = list(PASSWORD)
    for i in range(-1, -6, -1):
        PASSWORD[i] = "*"
    securePW = "".join(PASSWORD)
    member[0]["securePW"] = securePW


while True:
    print("==================================================") #50
    print("              WELCOME TO CCV[SOHUI]               ")
    print("==================================================")
    print()
    print("CGV에 오신 것을 환영합니다.")
    print("영화예매를 하시겠습니까?[yes/no]")
    YorN = input(">>")

    if YorN.lower() != "yes":
        print("==================================================")  # 50
        print("                프로그램을 종료합니다.                ")
        break

    print("영화예매는 로그인 후 이용 가능합니다.")
    print("회원가입 창으로 넘어갑니다.")

    signUp()
    print(member[0]["NAME"], "님 CGV[SOHUI]에 회원가입이 완료되었습니다.")

    print("id : ", member[0]["ID"])
    print("password : ", member[0]["securePW"])
    print("==================================================")
    print("회원가입 환영 영화 할인 쿠폰이 지급되었습니다!")
    print("[3000원 할인 쿠폰]")
    print("==================================================")
    print("영화 예매창으로 넘어갑니다.")
    print()
    break

