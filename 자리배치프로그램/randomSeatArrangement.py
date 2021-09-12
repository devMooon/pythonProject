from tkinter import *
from tkinter.messagebox import *
from random import *

#전역변수
nameStr = ""
nameList = []
seatLabel1 = []
seatLabel2 = []
num = []
randomNumList = []

#함수
def randomNum():
    global num
    global randomNumList
    global seatLabel1
    global seatLabel2
    global nameList

    num = []
    randomNumList = []
    seatLabel1 = []
    seatLabel2 = []

    for i in range(4):
        for k in range(4):
            seatLabel2.append(Label(window, text = "", font=("Arial", 10), bg='lemon chiffon', width=7, height=2))

        seatLabel2[0].place(x=10, y=100 + (50*i))
        seatLabel2[1].place(x=10*8, y=100 + (50*i))
        seatLabel2[2].place(x=10*16-8, y=100 + (50*i))
        seatLabel2[3].place(x=10*22+4, y=100 + (50*i))
        seatLabel1.append(seatLabel2)
        seatLabel2 = []

    if len(nameList) <= 4:
        max = 0
    elif len(nameList) <= 8:
        max = 1
    elif len(nameList) <= 12:
        max = 2
    else:
        max = 3

    for i in range(len(nameList)):

        while True:
            num.append(randint(0,max))
            num.append(randint(0,3))
            if num not in randomNumList:
                randomNumList.append(num)
                num = []
                break
            else:
                num = []
    
    for i in range(len(nameList)):
        seatLabel = seatLabel1[randomNumList[i][0]][randomNumList[i][1]]
        seatLabel.configure(text = nameList[i])
    
def seatPlace():
    fileFoundLabel.place_forget()
    rePlayButton.place(x=230, y=10)
    endButton2.place(x=230, y=40)

    teachingDeskLabel = Label(window, text = "교탁",font=("Arial", 10), bg='saddle brown', width=10, height=2)
    teachingDeskLabel.place(x=100, y=10)
    randomNum()
    

def writeFileName():
    startLabel.place_forget()
    startButton.place_forget()
    endButton.place_forget()

    writeFileNameLabel.place(x=45, y=40)
    writeFileNameEntry.place(x=40, y=120)
    writeFileNameButton.place(x=75, y=160) 

def uploadFile():
    nameFile = writeFileNameEntry.get()
    try:
        nameFile = open(nameFile, 'r', encoding='UTF8')
    except FileNotFoundError:
        showerror("파일 이름 오류", "입력한 파일이 존재하지 않습니다.\n올바른 파일명을 작성 해주세요.")
        writeFileNameEntry.delete(0, "end")
        return
    else:
        writeFileNameLabel.place_forget()
        writeFileNameEntry.place_forget()
        writeFileNameButton.place_forget()

        global nameStr
        global nameList
        nameStr = nameFile.readline()
        nameList.extend(nameStr.split(","))
        nameFile.close()

        fileFoundLabel.place(x=20, y=12)
        window.after(2000, seatPlace)


#메인 함수
window = Tk()
window.geometry("300x300")
window.resizable(False, False)
window.configure(bg='LightPink1')
window.title("자리 배치 프로그램")
startLabel = Label(window, text = "랜덤으로 자리를 배치하는\n 프로그램입니다 ✿˘◡˘✿", font=("Arial", 16, "italic"), bg='LightPink2')
startButton = Button(window, text = "Start", command=writeFileName, font=("Arial", 14), bg='khaki1', width=15)
endButton = Button(window, text = "End", command=window.destroy, font=("Arial", 14), bg='khaki1', width=15)

startLabel.place(x=25, y=60)
startButton.place(x=65, y=150)
endButton.place(x=65, y=200)

writeFileNameLabel = Label(window, text = "이름을 콤마로 구분해 작성한 \n파일 이름을 입력하세요.\n<이름은 1~16개만 입력>", font=("Arial", 12, "italic"), bg='LightPink2')
writeFileNameEntry = Entry(window, width=20, font=("Arial", 15))
writeFileNameButton = Button(window, text = "랜덤 자리배치", command=uploadFile, font=("Arial", 15), bg='khaki1')

fileFoundLabel = Label(window, text = "배치중...\n(✌’ω’)✌", font=("Arial", 30, "italic"), bg='tan1', width=11, height=6)

rePlayButton = Button(window, text = "Replay", command=randomNum, font=("Arial", 9), bg='thistle1', width=7)
endButton2 = Button(window, text = "End", command=window.destroy, font=("Arial", 9), bg='thistle1', width=7)

window.mainloop()