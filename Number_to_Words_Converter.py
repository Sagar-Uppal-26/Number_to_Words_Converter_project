word=""
def ten_lakhs(x):
    global word
    z=x%1000000
    y=int(x/100000)
    if y!=0:
        tens(y)
        if y==1:
            word=word+" lakh"
        else:
            word=word+" lakhs"
    lakhs(z)
def lakhs(x):
    global word
    z=x%100000
    y=int(x/100000)
    if word=="":
        unit(y)
        if y==1:
            word=word+" lakh"
        else:
            word=word+" lakhs"
    ten_thousands(z)
def ten_thousands(x):
    global word
    z=x%10000
    y=int(x/1000)
    if y!=0:
        tens(y)
        word=word+" thousand"
    thousands(z)
def thousands(x):
    global word
    z=x%1000
    y=int(x/1000)
    if word=="":
        unit(y)
        word=word+" thousand"
    hundreds(z)
def hundreds(x):
    global word
    z=x%100
    y=int(x/100)
    if y!=0:
        unit(y)
        word=word+" hundred"
    tens(z)
def tens(x):
    global word
    z=x%10
    if(x==11):
        word=word+" eleven"
    elif(x==12):
        word=word+" twelve"
    elif(x==13):
        word=word+" thirteen"
    elif(x==14):
        word=word+" forteen"
    elif(x==15):
        word=word+" fifteen"
    elif(x==16):
        word=word+" sixteen"
    elif(x==17):
        word=word+" seventeen"
    elif(x==18):
        word=word+" eighteen"
    elif(x==19):
        word=word+" nineteen"
    else:
        y=int(x/10)
        x=y*10
        if(x==10):
            word=word+" ten"
        elif(x==20):
            word=word+" twenty"
        elif(x==30):
            word=word+" thirty"
        elif(x==40):
            word=word+" forty"
        elif(x==50):
            word=word+" fifty"
        elif(x==60):
            word=word+" sixty"
        elif(x==70):
            word=word+" seventy"
        elif(x==80):
            word=word+" eighty"
        elif(x==90):
            word=word+" ninety"
        if z!=0:
            unit(z)
def unit(x):
    global word
    if(x==0):
        word=word+" zero"
    elif(x==1):
        word=word+" one"
    elif(x==2):
        word=word+" two"
    elif(x==3):
        word=word+" three"
    elif(x==4):
        word=word+" four"
    elif(x==5):
        word=word+" five"
    elif(x==6):
        word=word+" six"
    elif(x==7):
        word=word+" seven"
    elif(x==8):
        word=word+" eight"
    elif(x==9):
        word=word+" nine"
def convert(num):
    global word
    word=""
    length=len(str(num))
    if length==1:
        unit(num)
    elif length==2:
        tens(num)
    elif length==3:
        hundreds(num)
    elif length==4:
        thousands(num)
    elif length==5:
        ten_thousands(num)
    elif length==6:
        lakhs(num)
    elif length==7:
        ten_lakhs(num)
    return word