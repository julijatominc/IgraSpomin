
from tkinter import *
import random
import time

class Memory():
    def __init__(self, master):
        gumb1=Button(master,text="Pritisni1", command=self.beseda1)
        gumb1.grid(row=1,column=1)
        gumb2=Button(master,text="Pritisni2", command=self.beseda2)
        gumb2.grid(row=1,column=2)
        gumb3=Button(master,text="Pritisni3", command=self.beseda3)
        gumb3.grid(row=1,column=3)
        gumb4=Button(master,text="Pritisni4", command=self.beseda4)
        gumb4.grid(row=1,column=4)
        gumb11=Button(master,text="Pritisni5", command=self.beseda11)
        gumb11.grid(row=1,column=5)
        gumb22=Button(master,text="Pritisni6", command=self.beseda22)
        gumb22.grid(row=1,column=6)
        gumb33=Button(master,text="Pritisni7", command=self.beseda33)
        gumb33.grid(row=1,column=7)
        gumb44=Button(master,text="Pritisni8", command=self.beseda44)
        gumb44.grid(row=1,column=8)

        gumb5=Button(master,text="Pritisni9", command=self.beseda5)
        gumb5.grid(row=3,column=1)
        gumb6=Button(master,text="Pritisni10", command=self.beseda6)
        gumb6.grid(row=3,column=2)
        gumb7=Button(master,text="Pritisni11", command=self.beseda7)
        gumb7.grid(row=3,column=3)
        gumb8=Button(master,text="Pritisni12", command=self.beseda8)
        gumb8.grid(row=3,column=4)
        gumb55=Button(master,text="Pritisni13", command=self.beseda55)
        gumb55.grid(row=3,column=5)
        gumb66=Button(master,text="Pritisni14", command=self.beseda66)
        gumb66.grid(row=3,column=6)
        gumb77=Button(master,text="Pritisni15", command=self.beseda77)
        gumb77.grid(row=3,column=7)
        gumb88=Button(master,text="Pritisni16", command=self.beseda88)
        gumb88.grid(row=3,column=8)


        gumb9=Button(master,text="Premešaj",command=self.premesaj)
        gumb9.grid(row=5,column=1)


        
        self.a=0

        self.b="Nobena barva ni izbrana"

        self.c="neuspešno"

        self.rez=0

        self.resitve=[]

        self.koncna=[]

        self.poteze=0
        
        self.napis_spodaj= StringVar(value=str(self.b))
        napis = Label(master, textvariable=self.napis_spodaj)
        napis.grid(row=7, column=0, columnspan=2)
        
        self.napis_spodaj2= StringVar(value=str(self.c))
        napis2 = Label(master, textvariable=self.napis_spodaj2)
        napis2.grid(row=7, column=2, columnspan=1)
        
        self.rezultat= StringVar(value="rezultat:"+str(self.rez))
        rezultat = Label(master, textvariable=self.rezultat)
        rezultat.grid(row=7, column=5, columnspan=5)
        
        self.poteze2=StringVar(value="poteze:")
        poteze2= Label(master, textvariable=self.poteze2)
        poteze2.grid(row=8, column=4)
        
        self.poteze2=StringVar(value=str(self.poteze))
        poteze2= Label(master, textvariable=self.poteze2)
        poteze2.grid(row=8, column=5)

        self.w = Canvas(root, width=800, height=200)
        self.w.grid(row=2, column=1, columnspan=8)

        menu = Menu(master)
        master.config(menu=menu)
        
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_separator() 
        file_menu.add_command(label="Quit", command=master.destroy)


    def odpri(self):
        global s1
        global s2
        ime = filedialog.askopenfilename()
        self.w.delete(ALL)
        if ime == "":
            return
        s = open(ime, encoding="utf8")
        t = s.readlines()
        s.close

        s1=t[0].strip()[1:-1].split(',')
        s2=t[1].strip()[1:-1].split(',')
        s1 = [int(s) for s in s1]
        s2 = [int(s) for s in s2]                
        self.rez=int(t[2])
        self.poteze=int(t[3])

        self.koncna=t[4].strip()[1:-1].split(',')
        self.koncna=[s.strip()[1:-1] for s in self.koncna]
        
        print(self.koncna)
        self.rezultat.set("rezultat:" + str(self.rez))
        self.poteze2.set(str(self.poteze))
        
    def shrani(self):
        ime = filedialog.asksaveasfilename()
        if ime == "":
            return
        with open(ime, "wt", encoding="utf8") as f:
            f.write(str(s1) + "\n")
            f.write(str(s2) + "\n")
            f.write(str(self.rez) + "\n")
            f.write(str(self.poteze) + "\n")
            f.write(str(self.koncna))
            self.rezultat.set("rezultat:"+str(self.rez))
            self.poteze2.set(str(self.poteze))
        
    def premesaj(self):
        random.shuffle(s1)
        random.shuffle(s2)
        self.w.delete(ALL)
        self.resitve=[]
        self.koncna=[]
        self.napis_spodaj2.set(str("premesano"))
        self.poteze=0
        self.rez=0
        self.rezultat.set("rezultat:"+str(self.rez))
        self.poteze2.set(str(self.poteze))
        
    def skupna(self, barva, x1, y1, x2, y2):       
        if self.a ==2:
            self.w.delete(ALL)
            self.a=0
        self.w.create_rectangle(x1,y1,x2,y2,fill=barve[barva])
        self.a+=1
        self.napis_spodaj.set(str(barve[barva]))
        self.resitve+=[barve[barva]]
        self.poteze= self.poteze+1
        self.poteze2.set(str(self.poteze))
        print(s1)
        print(s2)
            
        if barve[barva] in self.koncna:
            self.napis_spodaj2.set(str("ojoj! to barvo ze imas"))
            self.resitve=[]
            
        elif len(self.resitve)==2 and self.resitve[0]==self.resitve[1]:
            self.napis_spodaj2.set(str("bravo"))
            self.resitve=[]
            self.rez+=1
            self.rezultat.set("rezultat:"+str(self.rez))
            self.koncna+=[barve[barva]]
            print(self.koncna)
                
        elif len(self.resitve)==2:
            self.resitve=[]
            self.napis_spodaj2.set(str("neuspesno"))
        if len(self.koncna)==8:
            self.napis_spodaj2.set(str("KONEC IGRE"))
        
    def beseda1(self):
        self.skupna(s1[3], 0,0,100,100)
        
    def beseda2(self):
        self.skupna(s1[2], 100,0,200,100)
    def beseda3(self):
        self.skupna(s1[1], 200,0,300,100)
    def beseda4(self):
        self.skupna(s1[0], 300,0,400,100)
    def beseda11(self):
        self.skupna(s1[4], 400,0,500,100)     
    def beseda22(self):
        self.skupna(s1[5], 500,0,600,100)
    def beseda33(self):
        self.skupna(s1[6], 600,0,700,100)    
    def beseda44(self):
        self.skupna(s1[7], 700,0,800,100)
    def beseda5(self):
        self.skupna(s2[3], 0,100,100,200)  
    def beseda6(self):
        self.skupna(s2[2], 100,100,200,200)   
    def beseda7(self):
        self.skupna(s2[1], 200,100,300,200)
    def beseda8(self):
        self.skupna(s2[0], 300,100,400,200)
    def beseda55(self):
        self.skupna(s2[4], 400,100,500,200)
    def beseda66(self):
        self.skupna(s2[5], 500,100,600,200)
    def beseda77(self):
        self.skupna(s2[6], 600,100,700,200)
    def beseda88(self):
        self.skupna(s2[7], 700,100,800,200)
        
s1=[0,1,2,3,4,5,6,7]
random.shuffle(s1)
barve=["green","blue","red","magenta","yellow","cyan","violet","brown"]
s2=[0,1,2,3,4,5,6,7]
random.shuffle(s2)

            
root = Tk()

aplikacija= Memory(root)
root.mainloop()
            
            
