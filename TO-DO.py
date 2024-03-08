import tkinter
def GONDER():
    a=var.get()
    
    if a=="options[0]":
        metin = metin_kutusu.get("1.0", "end")
        b=open("dosya.txt","a")
        b.write(metin)
    if a=="options[1]":
        b=open("dosya.txt","r")
        print(b.read())
    if a=="options[2]":
        metin = metin_kutusu.get("1.0", "end")
        b=open("dosya.txt","w")
        b.write(metin)
        


root=tkinter.Tk()
sol_seç=tkinter.Canvas(root,height="500",width="400",bg="lightblue")
sol_seç.pack(side="left")
sağ_fonk=tkinter.Canvas(root,height="500",width="400",bg="lightblue")
sağ_fonk.pack(side="right")
frame1=tkinter.Frame(sol_seç)
frame1.pack()
options=["TO-DO LİST EKLEME","TO-DO OKUMA","TO-DO RESET AND ADD"]
var=tkinter.StringVar()
var.set(options[0])
radio_button1=tkinter.Radiobutton(frame1,bg="lightgray",text="TO-DO LİST EKLEME YAPMA",variable=var,value="options[0]")
radio_button1.pack()
radio_button2=tkinter.Radiobutton(frame1,bg="lightgray",text="TO-DO LİST GÖRÜNTÜLEME",variable=var,value="options[1]")
radio_button2.pack()
radio_button3=tkinter.Radiobutton(frame1,bg="lightgray",text="TO-DO RESET AND ADD",variable=var,value="options[2]")
radio_button3.pack()

metin_kutusu=tkinter.Text(sağ_fonk,height="10",width="100")
metin_kutusu.pack(side="right")
button=tkinter.Button(sağ_fonk,text="GÖNDER",bg="lightblue",command=GONDER)
button.place(relx=0.8,rely=0.8)
root.mainloop()