import tkinter as tk

     
root=tk.Tk()
root.title('REGISTRATION FORM')
root.geometry("1920x1080")
name=tk.StringVar()
print(name)

d=tk.Label(root,text="REGISTRATION FORM",fg="blue",font=("Arial",20,"bold","underline"))
d.place(x=500,y=400)
d.pack()
a=tk.Label(root,text="NAME \n \nFATHERS NAME\n\nMOTHERS NAME\n\nBRANCH\n\nCOLLEGE NAME\n\nSTATE",font=("Arial",16,"bold","italic","underline"))
a.place(x=100,y=200)
e=tk.Entry(root,width=20,bg="yellow",font=("Arial",16),textvar=name)
e.place(x=400,y=200)
e=tk.Entry(root,width=20,bg="yellow",font=("Arial",16))
e.place(x=400,y=250)
e=tk.Entry(root,width=20,bg="yellow",font=("Arial",16))
e.place(x=400,y=300)
e=tk.Entry(root,width=20,bg="yellow",font=("Arial",16))
e.place(x=400,y=350)
e=tk.Entry(root,width=20,bg="yellow",font=("Arial",16))
e.place(x=400,y=400)
states=('Andhra Pradesh','ArunachalPrades','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh')


var=tk.StringVar()
var.set("Select State")
combobox=tk.OptionMenu(root,var,*states)
combobox.place(x=400,y=450)


    
b=tk.Button(root,text="SUBMIT",bg="purple",fg="black",activebackground="green",height=2,width=20,font=("bold"),command=name)
b.place(x=900,y=600)


root.mainloop()
