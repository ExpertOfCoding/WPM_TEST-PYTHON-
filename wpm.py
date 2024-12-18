import time
import tkinter as tk
import random
window=tk.Tk()
window.title("DBK Testi")
window.config(background="black",pady=100)
window.minsize(300,400)
sv=tk.StringVar()
CORRECT=0
with open("sentences.txt" ,"r",encoding="UTF-8") as file:
    readedlines=file.readlines()
    randomsayi=random.randint(0,len(readedlines)-1)
    text=readedlines[randomsayi]
    if not randomsayi==len(readedlines)-1:
        text=text[:-1]



origin_text=text
text_words=[]
sv_stack=""
currentl=0
FALSE=0
prevl=0
WPM=0
vurus=0
time_t=0
OKAY=True
for i in text.split():
    text_words.append(i+" ")
def goon():
    WPM = (((CORRECT)/5)/(time.time()-time_t))*60
    Label2.config(text=f"WPM: {WPM:0.1f}")
    if OKAY:
        window.after(100,goon)
    else:
        with open("sonuc.txt","a",encoding="UTF-8") as file:
            file.write(f"WPM: {WPM:0.1f} , Doğru Basılan Tuş: {CORRECT} , Yanlış Basılan Tuş: {FALSE} , TOPLAM: {CORRECT+FALSE} , SÜRE: {(time.time()-time_t):0.1f} saniye\n")
def start():
    global  time_t
    time_t=time.time()
    window.after(100,goon)
def callback(a,b,c):
    print(len([]))
    global CORRECT,text,text_words,origin_text,prevl,currentl,sv_stack,FALSE,vurus,time_t,OKAY
    if vurus==0:
        vurus += 1
        start()
    currentl=len(sv.get())
    currentsv=sv.get()[-1]
    if len(text_words)<=0:
        sv.set("")
        OKAY=False
        return True
    if sv.get()==text[:len(sv.get())] :
        CORRECT+=1
        sv_stack+=currentsv
        text=text[1:]
        Label.config(text=text)
        Label1.config(text=f"Correct: {CORRECT}")
        sv.set("")
        print("cor")
        if len(text)==0:
            sv.set("")
            OKAY=False
            return True
    else:
        FALSE+=1
        Label3.config(text=f"Typos: {FALSE}")

    if " " in sv.get():
        FALSE -= 1
        Label3.config(text=f"Typos: {FALSE}")
        text=text[len(text.split()[0]+" "):]
        text_words.pop(0)
        sv_stack=""
        sv.set("")
        print(text_words)
        print("POP WRONG")
        Label.config(text=text)
        Label1.config(text=f"Correct: {CORRECT}")
        if len(text)==0:
            sv.set("")
            OKAY=False
            return True
        return True

    if sv_stack==text_words[0]:
        text_words.pop(0)
        sv_stack=""
        print(text_words)
        print("POP")
    prevl=len(sv.get())
    return True
sv.trace_add("write", callback)

Label=tk.Label(text=text,pady=20,bg="black",fg="white")
Label.grid(column=0,row=0)

Entry=tk.Entry(width=50,textvariable=sv)
Entry.grid(column=0,row=1)
frame=tk.Frame()
frame.grid(column=0,row=2)
Label1=tk.Label(frame,text=f"Correct: {CORRECT}",pady=20,bg="black",fg="green")
Label1.pack(side=tk.LEFT)
Label3=tk.Label(frame,text=f"Typos: {FALSE}",pady=20,bg="black",fg="red")
Label3.pack(side=tk.RIGHT)
Label2=tk.Label(text=f"WPM: {WPM}",bg="black",fg="white")
Label2.grid(column=0,row=3)


window.mainloop()
