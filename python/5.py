import tkinter
import tkinter.messagebox
def but_info():
    tkinter.messagebox.showinfo('提示','人生苦短')
root=tkinter.Tk()
root.title('消息对话框')
root.geometry('400x400')
root.resizable(False,False)
tkinter.Button(root,text='消息提示框',command=but_info).pack()
root.mainloop()