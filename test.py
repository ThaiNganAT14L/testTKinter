from tkinter import *
from tkinter import messagebox
import modul
#class shape
class inGame (Frame):
    def __init__ (self):
        Frame.__init__(self)
        self.master.title ("Trương Thái Ngân")
        self.master.geometry("400x600+100+100")
        self.grid()   
        
        frame1 = Frame(self)
        frame1.grid()    
        
        self.game = Canvas(frame1,width = 400, height = 600 )
        self.game.create_rectangle(10,10,100,100,outline = "red", fill = "yellow")
        self.game.grid()

        self.game.bind_all("<Key>", self.diChuyen)
    
    def diChuyen (self, event):
        key = event.keysym
        if(key == "Up"): #quay khối sang phải
            pass
        elif(key == "Down"): #quay khối sang trái 
            pass 
        elif(key == "Left"):
            self.game.move(1,-3,0) 
        else:
            self.game.move(1,3,0)

class mainGame(Frame):
    def __init__ (self, user):
        Frame.__init__(self)
        self.user = user
        self.master.title ("Sign")
        self.master.geometry("100x100+100+100")
        self.grid()

        frame = Frame(self)
        frame.grid()

        self.newBut = Button (frame, text = "New Game", command = lambda: self.playGame())   
        self.newBut.grid(padx =25, pady =5)

        self.hisBut = Button (frame, text = "History", command = lambda: self.history())
        self.hisBut.grid(padx = 27, pady = 0)

        self.exitBut = Button(frame, text = "Exit", command = lambda: self.exit())
        self.exitBut.grid(padx = 30, pady = 5)
    def exit(self):
        self.quit()
        self.master.destroy()
    def history(self):
        self.quit()
        self.master.destroy()
        historyMain(self.user).mainloop()
    def playGame (self):
        self.quit()
        self.master.destroy()
        inGame().mainloop()
class signGame (Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Đăng Nhập")
        self.master.geometry("200x200+100+100")
        self.grid()

        frame = Frame(self)
        frame.pack()
        # label User
        self.text = StringVar()
        self.label1 = Label (frame, text = "User: ", width = 6)
        self.label1.pack(side=TOP, padx=0, pady=0)
        self.user = Entry(frame, textvariable =  self.text)
        self.user.pack(fill=X, padx=5, expand=True)
        # label Pass
        self.label2 = Label (frame, text = "Pass: ", width = 6)
        self.label2.pack(side = TOP,padx=0,pady=0)
        self.password = Entry(frame,show = "*")
        self.password.pack(fill=X, padx=5, expand=True)
        # Button "Sign in"
        self.button =Button(frame, text = "Sign in", command = lambda :self.signBut())
        self.button.pack(pady= 5)
        # Button "Creat"
        self.buttonSign = Button (frame, text = "Creat Account", command = lambda : self.callCreatAcc())
        self.buttonSign.pack(side = BOTTOM)
    def callCreatAcc(self):
        self.quit()
        self.master.destroy()
        creatAcc().mainloop()
    def signBut(self):
        #get() bắt đoạn text nhập ở label
        strUser = self.user.get() 
        strPass = self.password.get()
        if (modul.checkPass(strUser, strPass) ==1 ):            
            self.quit() # Thoát khỏi self
            self.master.destroy() # destroy: xóa dữ liệu master
            mainGame(strUser).mainloop() #gọi Main Game
class creatAcc (Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("New Account")
        self.pack()

        frame = Frame(self)
        frame.pack()

        self.label1 = Label (frame, text = 'New User: ')
        self.label1.pack(side = TOP)
        self.text = Entry(frame, width = 15)
        self.text.pack()
        
        self.label2 = Label (frame, text = 'Password: ')
        self.label2.pack()
        self.text1 = Entry(frame, width = 15)
        self.text1.pack()

        self.button = Button (frame, text = "Create ", command = lambda: self.creat())
        self.button.pack(side = BOTTOM)

    def creat(self):
        strUser = self.text.get()
        strPass = self.text1.get()
        if (modul.checkUser(strUser) == 0):
            modul.creatUser(strUser, strPass)

class historyMain (Frame):
    def __init__ (self, user):
        Frame.__init__(self)
        self.user = user
        self.master.title ("History")
        self.pack()

        frame = Frame(self)
        frame.pack()

        self.id = modul.checkID(self.user)
        history1,history2,history3 = modul.checkHistory(self.id)

        self.label1 = Label (frame, text = "History")
        self.label1.pack(side = TOP)
    
        self.label2 = Label (frame, text = str(history1))
        self.label2.pack()

        self.label3 = Label (frame, text = str(history2))
        self.label3.pack()

        self.label4 = Label (frame, text = str(history3))
        self.label4.pack()
        
        self.exitBut = Button(frame, text = "Exit", command = lambda: self.exit())
        self.exitBut.pack(side = BOTTOM)

    def exit(self):
        self.quit()
        self.master.destroy()
        mainGame(self.user).mainloop()
signGame().mainloop()        
