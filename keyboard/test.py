from button import *
import json

class Key:
    def __init__(self) -> None:
        self.step = 1
        self.button = [False]*8
        self.code = ""

        try :
            json_open = open('keymap.json', 'r')
            self.key_map = json.load(json_open)
        except Exception as e:
            print(e)

    def keyInput(self,touch_l,release_l):
        #変化がなければ処理しない
        if(len(touch_l)==0 and len(release_l)==0):
            return

        if((touch_l.count(8) + touch_l.count(9) + touch_l.count(10) + touch_l.count(11)) > 0):
            print("存在しないよ～")
            self.code=""
            self.step=1
            return
        if((release_l.count(8) + release_l.count(9) + release_l.count(10) + release_l.count(11)) > 0):
            print("存在しないよ～")
            self.code=""
            self.step=1
            return

        #ボタンが押された場合とリリースされた場合の処理
        if( self.step == 1 ):
            self.consonantTouch(touch_l)
        elif( self.step == 2 ):
            self.consonantFlick(release_l)

        #ボタンの状況
        for i in touch_l:
            self.button[i] = True
        for i in release_l:
            self.button[i] = False

        #触れられて無ければコードを保存する
        if(sum(self.button)==0):
            self.save()
            self.step = 1
            self.code = ""
            return


    def consonantTouch(self,touch_l):
        a_cnt,b_cnt,c_cnt,e_cnt,f_cnt = touch_l.count(A),touch_l.count(B),touch_l.count(C),touch_l.count(E),touch_l.count(F)

        if((a_cnt + b_cnt + c_cnt ) == 1 ):
            if(a_cnt == 1):
                self.code = "11"
            elif(b_cnt == 1):
                self.code = "22"
            elif(c_cnt == 1):
                self.code = "33"
        elif((e_cnt + f_cnt) == 1):
            if(e_cnt == 1):
                self.code = "5"
            elif(f_cnt == 1):
                self.code = "6"
        else:
            return

        self.step = 2

    def consonantFlick(self,release_l):

        if(self.code == ""):
            return

        #Button A (A ←D↑E→CF↓B)
        if(self.code[0]=="1"):
            button_l,code_l = [A,D,E,C,F,B,G],["1","4","5","6","6","7","7"]

        #Button B (B )
        if(self.code[0]=="2"):
            button_l,code_l = [B,D,A,E,C,F,G],["2","4","5","5","6","6","7"]

        #Button C (C ←ABD↑E→F↓G)
        if(self.code[0]=="3"):
            button_l,code_l = [C,A,B,D,E,F,G],["3","4","4","4","5","6","7"]

        if(self.code[0]=="5" or self.code[0]=="6"):
            return

        self.changeCode(release_l,button_l,code_l)


    def changeCode(self,release_l,button_l,code_l):

        for num,c in zip(button_l,code_l):
            if(num in release_l):
                self.code = self.code[0]+c

    def save(self):

        try:
            if(self.code not in self.key_map.keys()):
                raise Exception
            print('keycode:',self.code,"word:",self.key_map[self.code])
        except Exception:
            print("code:",self.code,",","おら間違ってんぞ")
