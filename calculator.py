from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("400x300")

input = Entry(window,width=60,borderwidth=3)
input.place(x=10,y=10)

def click(number):
    result = input.get()
    input.delete(0,END)
    input.insert(0,str(result)+str(number))

key_1=Button(window,text="1",bg="black",fg="white",width=10,command=lambda:click(1))
key_1.place(x=10,y=70)

key_2=Button(window,text="2",bg="black",fg="white",width=10,command=lambda:click(2))
key_2.place(x=100,y=70)

key_3=Button(window,text="3",bg="black",fg="white",width=10,command=lambda:click(3))
key_3.place(x=190,y=70)

key_4=Button(window,text="4",bg="black",fg="white",width=10,command=lambda:click(4))
key_4.place(x=10,y=100)

key_5=Button(window,text="5",bg="black",fg="white",width=10,command=lambda:click(5))
key_5.place(x=100,y=100)

key_6=Button(window,text="6",bg="black",fg="white",width=10,command=lambda:click(6))
key_6.place(x=190,y=100)

key_7=Button(window,text="7",bg="black",fg="white",width=10,command=lambda:click(7))
key_7.place(x=10,y=130)

key_8=Button(window,text="8",bg="black",fg="white",width=10,command=lambda:click(8))
key_8.place(x=100,y=130)

key_9=Button(window,text="9",bg="black",fg="white",width=10,command=lambda:click(9))
key_9.place(x=190,y=130)

key_0=Button(window,text="0",bg="black",fg="white",width=10,command=lambda:click(0))
key_0.place(x=100,y=160)

def add():
    n1 = input.get()
    global i
    global math
    math="addition"
    i=int(n1)
    input.delete(0,END)

key_o1=Button(window,text="+",bg="black",fg="white",width=10,command=add)
key_o1.place(x=280,y=100)

def sub():
    n1 = input.get()
    global i
    global math
    math="subtraction"
    i=int(n1)
    input.delete(0,END)

key_o2=Button(window,text="-",bg="black",fg="white",width=10,command=sub)
key_o2.place(x=280,y=130)

def mul():
    n1 = input.get()
    global i
    global math
    math="multiplication"
    i=int(n1)
    input.delete(0,END)

key_o3=Button(window,text="*",bg="black",fg="white",width=10,command=mul)
key_o3.place(x=280,y=160)

def div():
    n1 = input.get()
    global i
    global math
    math="division"
    i=int(n1)
    input.delete(0,END)


key_o4=Button(window,text="/",bg="black",fg="white",width=10,command=div)
key_o4.place(x=10,y=160)

def mod():
    n1 = input.get()
    global i
    global math
    math="modulo"
    i=int(n1)
    input.delete(0,END)

key_o5=Button(window,text="%",bg="black",fg="white",width=10,command=mod)
key_o5.place(x=190,y=160)

def equal():
    n2=input.get()
    input.delete(0,END)
    if math=="addition":
        input.insert(0,i+int(n2))
    elif math=="subtraction":
        input.insert(0,i-int(n2))
    elif math=="multiplication":
        input.insert(0,i*int(n2))
    elif math=="division":
        input.insert(0,i/int(n2))
    elif math=="modulo":
        input.insert(0,i%int(n2))

key_o6=Button(window,text="=",bg="black",fg="white",width=49,command=equal)
key_o6.place(x=10,y=190)

def clear():
    input.delete(0,END)

key_o7=Button(window,text="clear",bg="black",fg="white",width=10,command=clear)
key_o7.place(x=280,y=70)


window.mainloop()