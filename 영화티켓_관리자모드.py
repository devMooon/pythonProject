movieName = "Harry Potter"
theaterNum = 2
seatNum = ["F8", "F9"]
adultNum = 1
studentNum = 0
childNum = 1
peopleNum = 2
existingPeopleNum = 174
price = 12000

print("=================================")
print()
print("해당 영화 관리자 모드로 들어가시겠습니까?")
print("<no입력 시 프로그램이 종료됩니다.?[yes/no]")
YorN = input(">>")

if YorN.lower() == "yes":
    print("     =================================")
    print("       [%s] 관리자 창" % (movieName))
    print("      -------------------------------")
    print("       [%s] 추가 인원 및 수입" % (movieName))
    print()
    #가격 수정
    print("       제 %d 상영관 %s" % (theaterNum, " ".join(seatNum)))
    print()
    print("       어른[%d]   : %d" % (adultNum, adultNum * 10000))
    print("       청소년[%d] : %d" % (studentNum, studentNum * 8000))
    print("       어린이[%d] : %d" % (childNum, childNum * 5000))
    print()
    print("       추가 인원   : %d" % (peopleNum))
    print("       총인원      : %d" % (existingPeopleNum + peopleNum))
    print("       최근 수입   : %d" % (price))
    print("      -------------------------------")
    print("     =================================")

else:
    print("==================================================")  # 50
    print("                프로그램을 종료합니다.                ")


