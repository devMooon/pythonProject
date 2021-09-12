##변수 선언
member = [0, 0, 0]
member[0] = {"NAME": "", "ID": "", "PASSWORD": "", "securePW": ""}
dayList = ['Mon', 'Tue', 'Wed', 'Tur', 'Fri', 'Sat', 'Sun']
movieList = ['Harry Potter', 'Gravity Fall', 'Iron Man', 'The Avengers']
ScreenTimeList = ['13:00', '15:00', '17:00', '19:00']
theaterNum = 1
sDay = ""
sMovie = ""
sTime = ""

##함수
#part1 opening
def drawLineBold():
    print("==================================================")
    
def signUp():
    print("                    [회원가입]                      ")
    drawLineBold()
    name = input("이름              :")
    ID = input("ID                :")
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

def Qeixt(user):
    if user.lower() != "yes":
        drawLineBold()
        print("                프로그램을 종료합니다.                ")
        quit()

def welcome():
    drawLineBold()
    print("              WELCOME TO CCV[SOHUI]               ")
    drawLineBold()
    print()
    print("CGV에 오신 것을 환영합니다.")
    print("영화예매를 하시겠습니까?[yes/no]")
    YorN = input(">>")

    Qeixt(YorN)
    
    print("영화예매는 로그인 후 이용 가능합니다.")
    print("회원가입 창으로 넘어갑니다.")

    signUp()
    
    print()
    print(member[0]["NAME"], "님 CGV[SOHUI]에 회원가입이 완료되었습니다.")

    print("ID                :", member[0]["ID"])
    print("PASSWORD          :", member[0]["securePW"])
    print()
    drawLineBold()
    print("회원가입 환영 영화 할인 쿠폰이 지급되었습니다!")
    print("[3000원 할인 쿠폰]")
    drawLineBold()
    print("영화 예매창으로 넘어갑니다.")
    print()

#part2 Ticketing

def ticketing():
    selectDay()
    selectMovie()
    selectTime()
    
def selectDay():
    print("\n예매 날짜를 선택해주세요.")

    for d in dayList:
        print(d, end=' ')
    print()

    while True:
        global sDay
        sDay = input(">>")

        if sDay in dayList:
            return
        else:
            print("요일을 다시 선택해주십시오.")
            
def selectMovie():
    print("\n" + sDay + "에 상영되는 영화입니다.")
    print("영화를 선택해주십시오.\n")
    for m in movieList:
        print(m)

    while True:
        global sMovie
        sMovie = input(">>")

        if sMovie in movieList:
            return
        else:
            print("영화를 다시 선택해주십시오.")


def selectTime():
    global theaterNum
    print("\n" + sDay + " " + sMovie +" 상영시간표 입니다. 상영시간을 선택해주십시오.\n")
    for t in ScreenTimeList:
        print( t +"___제" + str(theaterNum) + "상영관_[?/80]") # 남은 자리 수 연결?
        theaterNum+=1
        
    while True:
        global sTime
        sTime = input(">>")

        if sTime in ScreenTimeList:
            return
        else:
            print("상영시간을 다시 선택해주십시오.")



#main코드
while True:
    welcome()
    ticketing()
