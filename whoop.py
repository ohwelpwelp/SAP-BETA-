#GUI
import tkinter as tk
root = tk.Tk()
def getTextInput():
    result=textExample.get("1.0",tk.END+"-1c")
    cells=[0]
    loc=[]
    p=0
    for i in range(0,len(result)):
        loc.append(result[i])
    for i in loc:
        try:
            if i == "!":
                cells[p] = cells[p] + 1
            if i == "@":
                cells[p] = cells[p] - 1
            if i == "$":
                p = p - 1
            if i == "_":
                p = p + 1
            if i == "&":
                a = input("input (only take 1 character): ")
                cells[p] = ord(a[0])
            if i == "=":
                print(chr(cells[p]))
            if i == "?":
                cells.append(0)
            if i == ";":
                cells.pop(p)
            if i == "/":
                p = 0
            if i == "'":
                p = len(cells) - 1
        except:
            print("ERROR")
textExample=tk.Text()
textExample.pack()
btnRead=tk.Button(text="Run", command=getTextInput)
btnRead.pack()
root.mainloop()
#Process
