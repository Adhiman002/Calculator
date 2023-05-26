from tkinter import*
screen=Tk()
screen.geometry("350x355")
screen.title("Calculator")
screen.minsize(350,355)
screen.maxsize(350,355)

T_input=StringVar()
operator=''
def btn(num):
    global operator
    operator+=str(num)
    
    T_input.set(operator)
    print(T_input.get())
    
def equal():
    global operator
    n=str(eval(operator))
    T_input.set(n)
    operator=n
    print(T_input.get())

def clear():
    global operator
    operator=''
    T_input.set(operator)
    

displayEntry=Entry(screen,textvariable=T_input,font=('Arial',20,'bold'),bg='powder blue',bd=22)
displayEntry.grid(columnspan=4)

btn7=Button(screen,text='7',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(7))
btn7.grid(row=1,column=0)
btn8=Button(screen,text='8',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(8))
btn8.grid(row=1,column=1)
btn9=Button(screen,text='9',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(9))
btn9.grid(row=1,column=2)
btnplus=Button(screen,text='+',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn('+'))
btnplus.grid(row=1,column=3)


btn4=Button(screen,text='4',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(4))
btn4.grid(row=2,column=0)
btn5=Button(screen,text='5',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(5))
btn5.grid(row=2,column=1)
btn6=Button(screen,text='6',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(6))
btn6.grid(row=2,column=2)
btnminus=Button(screen,text='-',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn('-'))
btnminus.grid(row=2,column=3)


btn1=Button(screen,text='1',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(1))
btn1.grid(row=3,column=0)
btn2=Button(screen,text='2',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(2))
btn2.grid(row=3,column=1)
btn3=Button(screen,text='3',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(3))
btn3.grid(row=3,column=2)
btnmulti=Button(screen,text='*',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn('*'))
btnmulti.grid(row=3,column=3)


btnclear=Button(screen,text='C',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:clear())
btnclear.grid(row=4,column=0)
btn0=Button(screen,text='0',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn(0))
btn0.grid(row=4,column=1)
btnequal=Button(screen,text='=',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:equal())
btnequal.grid(row=4,column=2)
btndivide=Button(screen,text='/',font=('Arial',20,'bold'),bd=8,padx=15,command=lambda:btn('*'))
btndivide.grid(row=4,column=3)


screen.mainloop()