from tkinter import *
 
MainWindow = Tk()
 
 
def Hamma(s, key):
    arr = []
    for i in range(0, len(s)):
        arr.append(s[i])
    for i in range(0, len(arr)):
        j = i % len(key)
        if (arr[i] != ' '):
            arr[i] = chr( 1072 + (1 + ord(arr[i]) + ord(key[j]))%1072 )
    s = ""
    s = "".join(arr)
    txt['text'] = s
 
def B1_window(event):
    root1 = Toplevel()
    Label(root1, text = "Введите шифруемое сообщение: ").pack()
    e = Entry(root1,width=20,bd=3)
    e.pack()
    e.focus_set()
    root1.transient(MainWindow)
    root1.grab_set()
    Label(root1, text = "Введите ключ:").pack()
    key = Entry(root1,width=20,bd=3)
    key.pack()
    go = Button(root1, text = "Зашифровать")
    go.pack()
    go.bind("<Button>",  lambda x: Hamma( e.get(), key.get()))

 
    MainWindow.wait_window(root1)
 
B1 = Button(MainWindow, text = "Зашифровать")
B1.pack()
B1.bind("<Button>", B1_window)
 
txt = Label(MainWindow, text="Результат", height=10, width=60)
txt.pack()
 
MainWindow.mainloop()
