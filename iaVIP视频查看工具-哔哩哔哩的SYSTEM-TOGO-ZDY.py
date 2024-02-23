import  re
import tkinter as  tk
from urllib import parse
import  tkinter.messagebox as msgbox
import  webbrowser
root=tk.Tk()
root.title('iaVIP视频查看工具-哔哩哔哩的SYSTEM-TOGO-ZDY')
root.geometry('580x415+500+280')
#img=tk.PhotoImage(file='img\\1.png')
#tk.Label(root,image=img).pack()
def show():
    word=input_va.get()
    num=num_int_va.get()
    if num==1:
        link='https://jx.qqwtt.com/?url='+word
        webbrowser.open(link)
    elif num == 2:
        link='http://okjx.cc/?url='+word
        webbrowser.open(link)
    elif num==3:
        link='https://svip.bljiex.cc/?url='+word
        webbrowser.open(link)
choose=tk.LabelFrame(root)
choose.pack(fill='both',pady=5)
#设置文本标签
tk.Label(choose,text='请选择你的线路',font=('华文琥珀',13)).pack(side=tk.LEFT)
#设置可变变量--》确定你点击哪一个
num_int_va=tk.IntVar()
num_int_va.set(1)
tk.Radiobutton(choose,text='1号线路   ',font=('仿宋',13),variable=num_int_va,value=1).pack(side=tk.LEFT)
tk.Radiobutton(choose,text='2号线路   ',font=('仿宋',13),variable=num_int_va,value=2).pack(side=tk.LEFT)
tk.Radiobutton(choose,text='3号线路',font=('仿宋',13),variable=num_int_va,value=3).pack(side=tk.LEFT)
#创建第二个标签框
input_frame=tk.LabelFrame(root)
input_frame.pack(fill='both',pady=5)
tk.Label(input_frame,text='视频播放地址',font=('黑体',14)).pack(side=tk.LEFT)
#设置可变变量
input_va=tk.StringVar()
#设置输入框width 设置宽度relief 输入框样式输入
 
tk.Entry(input_frame,width=100,relief='flat',textvariable=input_va).pack(side=tk.LEFT,fill='both')
#设置按钮
tk.Button(root,text='点击进行跳转地址',font=('宋体',20),bg='skyblue',fg='black',command=show).pack(fill='both')
root.mainloop()