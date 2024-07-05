import pickle
import random

class Word():
    
    def __init__(self,e,j,h=["",""],m="",t="",i="1"):
        self.E = e
        self.J = j
        self.hint = h
        self.memo = m
        self.tag = t.split(",")
        self.imp = int(i)
        self.qCount = 0
        self.aCount = 0
        self.xCount = 1
        self.rate = 0
        self.delFrag = False

    def question(self,r=2):
        self.qCount += 1
        if r == 2:
            r = random.randint(0,1)
        if "??" in self.E:
            r = 1
        elif "??" in self.J:
            r = 0
        print("---------------")
        if r:
            print(" Q: ",self.E)
            print("  hint: ",self.hint[0])
            answer = self.J
        else:
            print(" Q: ",self.J)
            print("  hint: ",self.hint[1])
            answer = self.E

        ans = input(" >>> ")
        if ans == answer:
            print("")
            print(" WIN!!!")
            self.aCount += 1
            self.xCount = 0
        else:
            print("")
            print(" Lose...")
            self.xCount += 1
            
        self.rate = (self.aCount / self.qCount) *100 //1

        print("  ans:  ",answer)
        print("  memo: ",self.memo)
        print(" show more?(y/else)")

        if input(" >>> ") == "y":
            self.showMore()
            

    def showData(self,i):
        i = str(i)
        e = self.E
        x = str(self.xCount)
        while len(i) < 4:
            i += " "
        while len(e) < 15:
            e += " "
        while len(x) < 2:
            x += " "
        print("    ",i,"  ", e,"  ", x,"  ", self.rate,"%" )


    def showMore(self):
        print("---------------")
        print("  English:   ",self.E)
        print("  Japanese:  ",self.J)
        print("  imp:       ",self.imp)
        print("  E->J hint: ",self.hint[0])
        print("  J->E hint: ",self.hint[1])
        print("  mamo:      ",self.memo)
        print("  tag:       ",self.tag)
        print("  rate:      ",self.rate)
        print("  x:         ",self.xCount)
        print("---------------")

        print(" edit?(y/else)")
        if input(" >>> ") == "y":
            self.edit()
        

    def edit(self):
        print(" which?(1:English 2:Japanese 3:hint 4:memo 5:tag 6:imp 9:reset 0:delete)")
        m = input(" >>> ")
        if not (m == "0" or m == "9" or m == "3"):
            print(" what?")
            d = input(" >>> ")
        if m == "1":
            self.E = d
        elif m == "2":
            self.J = d
        elif m == "3":
            print(" E->J hint?")
            ehint = input(" >>> ")
            print(" J->E hint?")
            jhint = input(" >>> ")
            self.hint = [ehint,jhint]
        elif m == "4":
            self.memo = d
        elif m == "5":
            d_ = d.split(",")
            print(" append or update?(a/else)")
            if input(" >>> ") == "a":
                self.tag.extend(d_)
            else:
                self.tag = d_
        elif m == "6":
            try:
                D = int(d)
                self.imp = D
            except:
                print(" failure...")
        elif m == "9":
            self.qCount = 0
            self.aCount = 0
            self.xCount = 1
            self.rate = 0
        elif m == "0":
            self.delFrag = True
            print(" deleting after")
        else:
            print(" stop...")

        if m != "0":
            self.showMore()

    def copyWord(self):
        T = self.tag[0]
        for i in range(len(self.tag)-1):
            T += ","
            T += self.tag[i+1]
            
        return Word(self.E,self.J,self.hint,self.memo,T,"1")

def manyEdit(Words,is_):
    print("--------------------------------")
    for i in is_:
        Words[i].showData(i)
    print("--------------------------------")
    print(" which?(5:tag 6:imp 9:reset 0:delete)")
    m = input(" >>> ")
    if m == "4" or m == "5":
        print(" what?")
        d = input(" >>> ")
    if m == "5":
        print(" append or update?(a/else)")
        if input(" >>> ") == "a":
            d_ = True
        else:
            d_ = False

    for i in is_:
        if m == "5":
            if d_:
                Words[i].tag.extend(d.split(","))
            else:
                Words[i].tag = d.split(",")
            print(" success!")
        elif m == "6":
            try:
                D = int(d)
            except:
                print(" failure...")
            else:
                Words[i].imp = D
                print(" success!")
        elif m == "9":
            Words[i].qCount = 0
            Words[i].aCount = 0
            Words[i].xCount = 0
            Words[i].rate = 0
            print(" success!")
        elif m == "0":
            Words[i].delFrag = True
            print(" deleting after")
        else:
            print(" stop...")
                

class Test():

    def __init__(self,name,Qnum,keys,r):
        self.name = name
        self.Qnum = Qnum
        self.tag = keys[0]
        self.imp = keys[1]
        self.rate = keys[2]
        self.wp = keys[3]
        self.x = keys[4]
        self.rn = keys[5]
        self.r = r
        self.keys = keys
        self.use = 0
        self.delFrag = False
        
    def showData(self,i):
        print("    ",i,"  ", self.name)


    def showMore(self):
        print("--------------")
        print("  name:       ",self.name)
        print("  Qnum:       ",self.Qnum)
        print("  tag:        ",self.tag)
        if self.rn[0] == 1:
            p = " or more"
        else:
            p = " or less"
        print("  imp:        ",self.imp,p)
        if self.rn[1] == 1:
            p = " or more"
        else:
            p = " or less"
        print("  rate:       ",self.rate,p)
        if self.rn[2] == 1:
            p = " or more"
        else:
            p = " or less"
        print("  x:          ",self.x,p)
        print("  word parts: ",self.wp)
        
        if self.r == 1:
            v = "E->J"
        elif self.r == 0:
            v = "J->E"
        else:
            v = "mix"
        print("  vector:     ",v)
        print("  use:       ",self.use)
        print("--------------")

        print(" edit?(y/else)")
        if input(" >>> ") == "y":
            self.edit()
        

    def edit(self):
        print(" which?(1:name 2:Qnum 3:tag 4:imp 5:rate 6:x 7:wordparts 8:vector 9:reset 0:delete)")
        m = input(" >>> ")
        if not (m == "0" or m == "9" or m=="8"):
            print(" what?")
            d = input(" >>> ")
        if m == "1":
            self.name = d
        elif m == "2":
            try:
                self.Qnum = int(d)
            except:
                print(" failure...")
        elif m == "3":
            self.tag = d
        elif m == "4":
            try:
                self.imp = int(d)
                print(" imp more or less?(l/else)")
                if input(" >>> ") == "l":
                    self.rn[0] = -1
                else:
                    self.rn[0] = 1
            except:
                print(" failure...")
        elif m == "5":
            try:
                self.rate = int(d)
                print(" rate more or less?(m/else)")
                if input(" >>> ") == "m":
                    self.rn[1] = 1
                else:
                    self.rn[1] = -1
            except:
                print(" failure...")
        elif m == "6":
            try:
                self.x = int(d)
                print(" rate more or less?(l/else)")
                if input(" >>> ") == "l":
                    self.rn[2] = -1
                else:
                    self.rn[2] = 1
            except:
                print(" failure...")
            
        elif m == "7":
            self.wp = d
        elif m == "8":
            print(" what?(1:E->J 2:J->E else:mix)")
            r = input(" >>> ")
            if r == "1":
                self.r = 1
            elif r == "2":
                self.r = 0
            else:
                self.r = 2
        elif m == "9":
            self.use = 0
        elif m == "0":
            self.delFrag = True
            print(" deleting after")
        else:
            print(" stop...")
            
        self.keys = [self.tag, self.imp, self.rate, self.wp, self.x, self.rn]
        
        if m != "0":
            self.showMore()
    

            
def makingMode(NAME):
    print("")
    print("========= Making Mode =========")
    newWords = []
    while True:
        newWords.extend(makeQ())
        print("")
        print(" continue?(n/else)")
        if input(" >>> ") == "n":
            break

    print(" export?(y/else)")
    if input(" >>> ") == "y":
        print(" memo?")
        memo = input(" >>> ")
        print(" file name?")
        name = input(" >>> ")
        try:
            with open(name+'.pickle',mode='wb') as f:
                exWords = []
                for w in newWords:
                    exWords.append(w.copyWord())
                    
                pickle.dump([memo,exWords,NAME],f)
        except:
            print("")
            print(" failure...")
        else:
            print("")
            print(" success!")
    return newWords
        
    
def makeQ():
    print("-------------------------------")
    print(" English?(nec)")
    e = input(" >>> ")
    print(" Japanese?(nec)")
    j = input(" >>> ")
    print(" E->J hint?")
    ehint = input(" >>> ")
    print(" J->E hint?")
    jhint = input(" >>> ")
    print(" memo? ")
    memo = input(" >>> ")
    print(" tag?")
    tag = input(" >>> ")
    print(" imp?(none:1)")
    imp = input(" >>> ")
    if imp == "":
        imp = "1"

    if e == "" or j == "":
        print("")
        print(" failure...")
    else:
        try:
            w = Word(e,j,[ehint,jhint],memo,tag,imp)
        except:
            print("")
            print(" failure...")
        else:
            print("")
            print(" success!")
            print("")
            print(" edit?(y/else)")
            if input(" >>> ") == "y":
                w.edit()
            if not w.delFrag:
                return [w]
    return []



        
def testMode(Words,Tests):
    print("")
    print("========== Test Mode ==========")
    for i in range(len(Tests)):
        Tests[i].showData(i)
    print(" which?")
    n = input(" >>> ")
    try:
        t = Tests[int(n)]
    except:
        print(" no find...")
    else:
        t.use += 1
        ran = choiceWord(Words,t.keys)
        lenran = len(ran)
        if lenran > t.Qnum:
            lenran = t.Qnum
        qs = random.sample(ran,lenran)
        for q in qs:
            Words[q].question(t.r)


    print(" now loading...")

    return [w for w in Words if w.delFrag==False]




def viewMode(Words):
    print("")
    print("========== View Mode ===========")
    Is = choiceWord(Words,makeKeys())
    print("--------------------------------")
    for i in Is:
        Words[i].showData(i)
    print("--------------------------------")

    while True:
        print("")
        print(" number?(none:quit)")
        n = input(" >>> ")
        if "to" in n:
            ns = n.split("to")
            try:
                N1 = int(ns[0])
            except:
                N1 = 0
            try:
                N2 = int(ns[1])
            except:
                N2 = Is[-1]
            if N1 < 0:
                N1 = 0
            if N2 > Is[-1]:
                N2 = Is[-1]

            is_ = []
            for i in Is:
                if i >= N1 and i <= N2:
                    is_.append(i)
            manyEdit(Words,is_)
            
        elif "," in n:
            ns = n.split(",")
            is_ = []
            for i in ns:
                try:
                    is_.append(int(i))
                except:
                    pass
            manyEdit(Words,is_)
            
        else:
            try:
                N = int(n)
                Words[N].showMore()
            except:
                break

    print(" now loading...")
    return [w for w in Words if w.delFrag==False]



def optionMode(Words,Tests,NAME):
    while True:
        print("")
        print("================= Option Mode ================")
        print(" mode?(1:setTest 2:import 3:export else:quit)" )
        m = input(" >>> ")
        
        if m == "1":
            while True:
                print("--------------------------------")
                for i in range(len(Tests)):
                    Tests[i].showData(i)
                print("--------------------------------")

                print(" edit or new or quit?(e/n/else)")
                m_ = input(" >>> ")
                if m_ == "e":
                    print(" number?")
                    n = input(" >>> ")
                    try:
                        N = int(n)
                        t = Tests[N].showMore()
                    except:
                        print(" no find...")
                elif m_ == "n":
                    print(" name?")
                    name = input(" >>> ")
                    print(" Qnum?(none:10)")
                    qnum = input(" >>> ")
                    try:
                        Qnum = int(qnum)
                    except:
                        Qnum = 10
                    keys = makeKeys()
                    print(" vector?(1:E->J 2:J->E else:mix)")
                    R = input(" >>> ")
                    if R == "1":
                        r = 1
                    elif R == "2":
                        r = 0
                    else:
                        r = 2
                    Tests.append(Test(name,Qnum,keys,r))
                else:
                    break

        elif m == "2":
            while True:
                print(" file name?")
                name = input(" >>> ")
                try:
                    with open(name + '.pickle',mode='rb') as f:
                        newWords = pickle.load(f)
                except:
                    print(" no find...")
                else:
                    print(newWords[0],"  by ",newWords[2])
                    for i in range(len(newWords[1])):
                        newWords[1][i].showData(i)
                    print(" import?(n/else)")
                    if input(" >>> ") != "n":
                        Words.extend(newWords[1])
                        print("")
                        print(" success!")
                print("")
                print(" continue?(n/else)")
                if input(" >>> ") == "n":
                    break

        elif m == "3":
            while True:
                exWords = []
                en = []
                Is = choiceWord(Words,makeKeys())
                print("--------------------------------")
                for i in Is:
                    Words[i].showData(i)
                print("--------------------------------")
                print(" delete number?")
                ns = input(" >>> ")
                if "to" in ns:
                    n = ns.split("to")
                    try:
                        N1 = int(n[0])
                    except:
                        N1 = 0
                    try:
                        N2 = int(n[1])
                    except:
                        N2 = Is[-1]
                    if N1 < 0:
                        N1 = 0
                    if N2 > Is[-1]:
                        N2 = Is[-1]
                    for i in Is:
                        if i >= N1 and i <= N2:
                            en.append(i)
                else:
                    for n in ns.split(","):
                        try:
                            N = int(n)
                        except:
                            pass
                        else:
                            en.append(N)
                
                print(" memo?")
                memo = input(" >>> ")
                print(" file name?")
                name = input(" >>> ")
                print("--------------------------------")
                for i in Is:
                    if not i in en:
                        ew = Words[i].copyWord()
                        ew.showData(i)
                        exWords.append(ew)
                print("--------------------------------")
                print("  memo: ",memo)
                print("  file: ",name+".pickle")
                print(" export?(y/else)")
                if input(" >>> ") == "y":
                    try:
                        with open(name + '.pickle',mode='wb') as f:
                            pickle.dump([memo,exWords,NAME],f)
                    except:
                        print("")
                        print(" failure...")
                    else:
                        print("")
                        print(" success!")
                print("")
                print(" continue?(n/else)")
                if input(" >>> ") == "n":
                    break
        else:
            break

    return [Words,[t for t in Tests if t.delFrag != True]]
            
    



def choiceWord(Words,keys):
    print(" now loading...")
    choice = []
    for i in range(len(Words)):
        if keys[5][0] == 1:
            If = keys[1] <= Words[i].imp
        else:
            If = keys[1] >= Words[i].imp
        if If:
            if keys[5][2] == 1:
                Xf = keys[4] <= Words[i].xCount
            else:
                Xf = keys[4] >= Words[i].xCount
            if Xf:
                if keys[5][1] == 1:
                    Rf = keys[2] <= Words[i].rate
                else:
                    Rf = keys[2] >= Words[i].rate
                if Rf:
                    if keys[0] in Words[i].tag or keys[0] == "":
                        if keys[3] in Words[i].E:
                            choice.append(i)

    print(" finish")
    return(choice)
            
            

def makeKeys():
    rn = []
    print(" tag?")
    tag = input( " >>> ")
    
    print(" imp?")
    imp = input(" >>> ")
    try:
        Imp = int(imp)
    except:
        Imp = 1
        rn.append(1)
    else:
        print(" imp more or less?(l/else)")
        if input(" >>> ") == "l":
            rn.append(-1)
        else:
            rn.append(1)
            
    print(" rate? ")
    rate = input(" >>> ")
    try:
        Rate = int(rate)
    except:
        Rate = 100
        rn.append(-1)
    else:
        print(" rate more or less?(m/else)")
        if input(" >>> ") == "m":
            rn.append(1)
        else:
            rn.append(-1)
    
    print(" x?")
    x = input(" >>> ")
    try:
        X = int(x)
    except:
        X = 0
        rn.append(1)
    else:
        print(" x more or less?(l/else)")
        if input(" >>> ") == "l":
            rn.append(-1)
        else:
            rn.append(1)
            
    print(" word parts?")
    wp = input(" >>> ")

    return([tag,Imp,Rate,wp,X,rn])

 

def main():
    print(" now loading...")
    try:
        with open('mydata.pickle',mode='rb') as f:
            d = pickle.load(f)
            NAME = d[0]
            Words = d[1]
            Tests = d[2]
            print(" HELLO ",NAME)
    except:
        print(" What's your name?")
        while True:
            NAME = input(" >>> ")
            print(" OK?(y/else)")
            if input(" >>> ") == "y":
                break
        Words = [Word("absorb","吸収する")]
        Tests = [Test("ALL",10,["",1,100,"",0,[1,-1,1]],2)]
    
    while True:
        print("")
        print("")
        print("========================= Main ==========================")
        print(" mode?(2:making 3:view 4:option 9:save 0:quit else:test)")
        m = input(" >>> ")
        if m == "2":
            Words.extend(makingMode(NAME))
        elif m == "3":
            Words = viewMode(Words)
        elif m == "4":
            o = optionMode(Words,Tests,NAME)
            Words = o[0]
            Tests = o[1]
        elif m == "9":
            print(" now saving...")
            with open('mydata.pickle',mode='wb') as f:
                pickle.dump([NAME,Words,Tests],f)
        elif m == "0":
            print(" now saving...")
            with open('mydata.pickle',mode='wb') as f:
                pickle.dump([NAME,Words,Tests],f)
            break
        else:
            Words = testMode(Words,Tests)
            Tests.sort(key=lambda x:x.use,reverse=True)
        

if __name__ == "__main__":
    main()
        
