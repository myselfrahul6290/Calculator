from tkinter import *

root=Tk()
root.title("Calculator")

e=Entry(root,width=50, borderwidth=5)
e.grid(row=0, column=0,pady=30, columnspan=4)

#Arrange Number in screen
def click_number(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

#clear screen
def clear_button():
    e.delete(0,END)  

#for addtion button
def Add():
    first_num=e.get()
    global num1,math
    num1=int(first_num)
    math="Add"
    e.delete(0,END)      

#for Subtraction button
def subtract():
    first_num=e.get()
    global num1,math
    num1=int(first_num)
    math="subtract"
    e.delete(0,END)

#for Multiplication button
def Multiplication():
    first_num=e.get()
    global num1,math
    num1=int(first_num)
    math="Multiply"
    e.delete(0,END) 

#for division button
def division():
    first_num=e.get()
    global num1,math
    num1=int(first_num)
    math="divide"
    e.delete(0,END) 



def equal():
    num2=e.get()
    e.delete(0,END)
    if(math=="Add"):
        ans=num1+int(num2)

    if(math=="subtract"):
        ans=num1-int(num2)

    if(math=="Multiply"):
        ans=num1*int(num2)

    if(math=="divide"):
        ans=num1/int(num2)                
    
    e.insert(0,ans)    
   

#create buttons

Button_1=Button(root, text="1", padx=35, pady=30,bg="#004d99", fg="#ffffff", command=lambda: click_number(1))
Button_2=Button(root, text="2", padx=35, pady=30,bg="#004d99",fg="#ffffff", command=lambda: click_number(2))
Button_3=Button(root, text="3", padx=35, pady=30,bg="#004d99",fg="#ffffff", command=lambda: click_number(3))
Button_4=Button(root, text="4", padx=35, pady=30,bg="#004d99",fg="#ffffff", command=lambda: click_number(4))
Button_5=Button(root, text="5", padx=35, pady=30,bg="#004d99",fg="#ffffff", command=lambda: click_number(5))
Button_6=Button(root, text="6", padx=35, pady=30,bg="#004d99",fg="#ffffff", command=lambda: click_number(6))
Button_7=Button(root, text="7", padx=35, pady=30,bg="#004d99",fg="#ffffff", command=lambda: click_number(7))
Button_8=Button(root, text="8", padx=35, pady=30,bg="#004d99",fg="#ffffff", command=lambda: click_number(8))
Button_9=Button(root, text="9", padx=35, pady=30,bg="#004d99",fg="#ffffff", command=lambda: click_number(9))
Button_0=Button(root, text="0", padx=35, pady=30,bg="#004d99",fg="#ffffff", command=lambda: click_number(0))
Button_clear=Button(root, text="clear", padx=26, pady=30,bg="#ff471a", command=clear_button)
Button_equal=Button(root, text="equal", padx=23, pady=30, bg="#ffa64d", command=equal)
Button_add=Button(root, text="+", padx=25, pady=30,bg="#80aaff", command=Add)
Button_sub=Button(root, text="-", padx=25, pady=30,bg="#80aaff", command=subtract)
Button_Mul=Button(root, text="*", padx=25, pady=30,bg="#80aaff", command=Multiplication)
Button_div=Button(root, text="/", padx=25, pady=30, bg="#80aaff",command=division)



#position set the buttons
Button_9.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_7.grid(row=1,column=2)
Button_div.grid(row=1,column=3)

Button_6.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_4.grid(row=2,column=2)
Button_Mul.grid(row=2,column=3)


Button_3.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_1.grid(row=3,column=2)
Button_sub.grid(row=3,column=3)


Button_0.grid(row=4,column=0)
Button_clear.grid(row=4,column=1)
Button_equal.grid(row=4, column=2)
Button_add.grid(row=4,column=3)








root.mainloop()
