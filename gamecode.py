# RUSSIAREVOLUTIONGAME.py
try:
    import Tkinter as tk
except:
    import tkinter as tk
    
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<RUSSIA REVOLUTION>>>>>>>>>>", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self,text="made by 30618 유경선",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="PLAY GAME",
                  command=lambda: master.switch_frame(PageOne)).place(x=480,y=600)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()       
        tk.Label(self,text="1917년 4월 16일 밤",font=('Helvectica',16,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="끼이익 철컹",font=('Helvectica',20,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="기관사: 승객여러분은 오른쪽으로 내려 주시길 바랍니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack() 
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="열차에서 내린다.",
                  command=lambda: master.switch_frame(PageTwo01)).place(x=0,y=700)
        tk.Button(self, text="열차에서 내리지 않는다.",
                  command=lambda: master.switch_frame(PageTwo02)).place(x=1030,y=700)

class PageTwo01(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvectica', 18)).pack(side="top",fill="x", pady=5)
        tk.Label(self,text="붉은 깃발이 나부끼는 광장에 군악대가 연주하는 프랑스 대혁명의 노래가",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="울리고 노동자와 군인들은 환호성을 지른다.",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="군중: 와아아!! 레닌 동지께서 오셨다!",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="연설을 시작한다.",
                  command=lambda: master.switch_frame(PageSpeech)).place(x=600,y=700)

class PageTwo02(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="나데즈다 크룹스카야: 어서 안내리고 뭐해요 레닌.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="열차에서 내린다.",
                  command=lambda: master.switch_frame(PageTwo01)).place(x=600,y=700)

class PageSpeech(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="여러분이 임시정부의 약속을 다 믿지는 모르겠지만,",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="저들이 달콤한 말로 많은 것을 약속하면서",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="민중을 속이고 있다는 것만은 확신합니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="민중은 평화를 원합니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="민중은 빵을 원합니다. 민중은 또한 땅을 원합니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="그런데 저들은 전쟁과 굶주림만 줄 뿐 빵을 주지 않습니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="지주계급은 여전히 건재합니다. 우리는 사회주의 혁명을 위해 싸워야 합니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="프롤레타리아가 완전한 승리를 거둘때까지 싸워야 합니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="세계 사회주의혁명 만세!!",font=('Helvectica',20,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="연설을 마친다.",
                  command=lambda: master.switch_frame(PageThree)).place(x=600,y=700)

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="뻥! 뻥!",font=('Helvectica',20,"bold")).pack()
        tk.Label(self,text="흥분한 군중이 연단으로 몰려들었고 군인들이 총을 들고 들이닥쳤다.",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델레니예: 우두머리 레닌을 잡아라!!",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="백성들을 체포해라!! ",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="모두 반역자들이다!! ",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="경관 아프레델레니예와 대화를 한다.",
                  command=lambda: master.switch_frame(PageThree01)).place(x=0,y=700)
        tk.Button(self, text="도망친다.",
                  command=lambda: master.switch_frame(PageThree02)).place(x=650,y=700)
        tk.Button(self, text="경관 아프레델레니예와 싸운다.",
                  command=lambda: master.switch_frame(PageThree03)).place(x=1000,y=700)
  
class PageThree01(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌: 내가 레닌이오. 이야기를 하고 싶소 경관.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델레니예: 반역자 주제에 말이 많다. 전원 사격 개시!",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="뻥!  뻥! ",font=('Helvectica',20,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="골목으로 도망친다.",
                  command=lambda: master.switch_frame(PageThree02)).place(x=0,y=700)
        tk.Button(self, text="설득한다.",
                  command=lambda: master.switch_frame(PagePersuade)).place(x=630,y=700)
        tk.Button(self, text="맞서 싸운다.",
                  command=lambda: master.switch_frame(PageThree03)).place(x=1200,y=700)

class PageThree03(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌: 도망치지 마라!! 모두 맞서 싸워라! 소비에트를 위하여!!",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="군중들과 공산당원들은 일제히 총을 들고 경찰들과 싸우기 시작했다.",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델리예: 으흑!",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델리예가 쓰러지자 경찰들이 뿔뿔히 흟어졌다.",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="군중: 레닌 동지 만세!! 소비에트 만세!!",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="나데즈다 크룹스카야: 오늘은 이만 쉬는게 좋겠어요. 조만간 큰일이 있을테니..",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="잠을 잔다.",
                  command=lambda: master.switch_frame(PageACT2START)).place(x=30,y=700)
        tk.Button(self, text="연설을 한다.",
                  command=lambda: master.switch_frame(PageSpeech02)).place(x=1030,y=700)
 

class PageThree02(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌: 헉헉 괜찮소 부인.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="나데즈다 크룹스카야: 괜찮아요, 놈들이 오고 있어요.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="빨리 가요 레닌.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델레니예 : 거기서라 주동자 레닌!!",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="앞에 모여있는 군중들과 건물이 있다.",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="군중속에 숨는다.",
                  command=lambda: master.switch_frame(PageACT1END01)).place(x=30,y=700)
        tk.Button(self, text="건물에 들어간다.",
                  command=lambda: master.switch_frame(PageACT1END01)).place(x=1030,y=700)

class PageACT1END01(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델레니예 : 어디갔지? 주변을 싹싹히 뒤져봐!",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌과 그의 동지들은 경관 아프레델니예를 따돌렸다.",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌: 한숨 돌리겠군",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="나데즈다 크룹스카야: 오늘은 이만 쉬는게 좋겠어요. ",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="조만간 큰일이 있을테니..",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="잠을 잔다.",
                  command=lambda: master.switch_frame(PageACT2START)).place(x=600,y=700)

class PagePersuade(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌: 경관 자네는 무엇을 위해 그러는가?",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델레니예: 정의를 위해",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌:자네가 하는 것은 부자들과 자본가들이 독점하는 국가 경영을",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="위해 국민들을 억압하는 것 뿐일세",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="결코 정의가 아니야!",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="경관 아프레델레니예를 공산당원에 들어오라고 말한다.",
                  command=lambda: master.switch_frame(PageTeam)).place(x=30,y=700)
        tk.Button(self, text="그냥 보내달라고 말한다.",
                  command=lambda: master.switch_frame(PageEnd)).place(x=1030,y=700)

class PageSpeech02(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="군중여러분들 자본주의의 타도없이 이 전쟁은 끝나지 않을 것입니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="여러분 모두 임시정부를 더 이상 지원하지 말고",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="소비에트의 권력을 확장하고",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="볼셰비키의 권력을 확장해야 합니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="군대와 경찰은 폐지되지 않으면 안됩니다.",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="계속해서 새로운 혁명적 국제 조직을 창설합시다. ",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="임정을 타도하자! 모든 권력을 소비에트에게!!",font=('Helvectica',18,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="연설을 마치고 잠을 잔다.",
                  command=lambda: master.switch_frame(PageACT2START)).place(x=600,y=700)

class PageTeam(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌: 우리와 함께 가세 경관.",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델니예: ….",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌: 나는 이 부패한 사회를 바꾸고 노동자들 소비에트를 위한 연방을 세울걸세. 나와 함께 가세",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델레니에: 한번 믿어보겠네..",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델레니에가 공산당에 합류하였습니다.",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="나데즈다 크룹스카야: 오늘은 이만 쉬는게 좋겠어요. 조만간 큰일이 있을테니..",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="잠을 잔다.",
                  command=lambda: master.switch_frame(PageACT2START)).place(x=600,y=700)

class PageEnd(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="<<<<<<<<<<<<<<<ACT 1: 핀란드 역에서>>>>>>>>>>>>>>>", font=('Helvetica', 18)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="레닌: 경관 우리를 보내주게. 내가 이상적인 미래를 보여주겠네, 한번만 믿어주게",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델레니에: 한번 믿어보겠네..",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="경관 아프레델레니에가 철수했다.",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="나데즈다 크룹스카야: 오늘은 이만 쉬는게 좋겠어요. 조만간 큰일이 있을테니..",font=('Helvectica',13,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="잠을 잔다.",
                  command=lambda: master.switch_frame(PageACT2START)).place(x=600,y=700)

class PageACT2START(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self, text="", font=('Helvetica', 10)).pack(side="top", pady=5)
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="시간관계상 엑트1까지만 개발하였습니다.",font=('Helvectica',30,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Label(self,text="",font=('Helvectica',10,"bold")).pack()
        tk.Button(self, text="돌아가기",
                  command=lambda: master.switch_frame(StartPage)).place()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    app.resizable(width=False, height=False)
