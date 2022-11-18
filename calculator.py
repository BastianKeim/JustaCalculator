from tkinter import*

root = Tk()

root.configure(background='#000000')
root.title("Calculator")
root.geometry('224x190')

equation = StringVar()
def onPress(num):

    equation.set(equation.get() + str(num))

def onEqual():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except: 
        equation.set('Err0r')
def onClear():
    equation.set("")

expression_entry = Entry(root, textvariable=equation,background='#333333', fg='#fff', font=('Consolas',15))
expression_entry.grid(row=0,columnspan=4,sticky='nswe')

btn7 = Button(root, text=' 7 ', fg='#fff', background='#666', command=lambda: onPress(7))
btn7.grid(row=1,column=0,sticky='nswe')

btn8 = Button(root, text=' 8 ', fg='#fff', background='#666', command=lambda: onPress(8))
btn8.grid(row=1,column=1,sticky='nswe')

btn9 = Button(root, text=' 9 ', fg='#fff', background='#666', command=lambda: onPress(9))
btn9.grid(row=1,column=2,sticky='nswe')

btn4 = Button(root, text=' 4 ', fg='#fff', background='#666', command=lambda: onPress(4))
btn4.grid(row=2,column=0,sticky='nswe')

btn5 = Button(root, text=' 5 ', fg='#fff', background='#666', command=lambda: onPress(5))
btn5.grid(row=2,column=1,sticky='nswe')

btn6 = Button(root, text=' 6 ', fg='#fff', background='#666', command=lambda: onPress(6))
btn6.grid(row=2,column=2,sticky='nswe')

btn3 = Button(root, text=' 3 ', fg='#fff', background='#666', command=lambda: onPress(3))
btn3.grid(row=3,column=2,sticky='nswe')

btn2 = Button(root, text=' 2 ', fg='#fff', background='#666', command=lambda: onPress(2))
btn2.grid(row=3,column=1,sticky='nswe')

btn1 = Button(root, text=' 1 ', fg='#fff', background='#666', command=lambda: onPress(1))
btn1.grid(row=3,column=0,sticky='nswe')

btn0 = Button(root, text=' 0 ', fg='#fff', background='#666', command=lambda: onPress(0))
btn0.grid(row=4,column=0,sticky='nswe', columnspan=2)

btndot = Button(root, text=' . ', fg='#fff', background='#666', command=lambda: onPress('.'))
btndot.grid(row=4,column=2,sticky='nswe')

btnplus = Button(root, text=' + ', fg='#fff', background='#e0981b', font='bold', command=lambda: onPress('+'))
btnplus.grid(row=1, column=3, sticky='nswe' )

btnsub = Button(root,text=' - ', fg='#fff', background='#e0981b', font='bold' , command=lambda: onPress('-'))
btnsub.grid(row=2, column=3, sticky='nswe')

btnmult = Button(root, text=' * ', fg='#fff', background='#e0981b', font='bold', command=lambda: onPress('*'))
btnmult.grid(row=3, column=3, sticky='nswe')

btndiv = Button(root, text= ' / ', fg='#fff', background='#e0981b', font='bold' , command=lambda: onPress('/'))
btndiv.grid(row=4, column=3, sticky='nswe')

btnclear = Button(root,text=' C ', fg='#fff', background='#666', font='bold', command=onClear)
btnclear.grid(row=5, column=2, sticky='nswe')

btnequal = Button(root, text=' = ', fg='#fff', background='#333333', font='bold', command=onEqual)
btnequal.grid(row=5, column=3, sticky='nswe')



root.mainloop()

