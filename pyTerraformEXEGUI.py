from tkinter import *
from python_terraform import *

tk = Tk()
tk.title('Terraform EXE GUI made by ymcajudo@gmail.com')
tk.geometry('610x70')
#tk.resizable(True,True)
tk.resizable(False,False)
    
TFfolderlabel = Label(tk,text='Working Directory')
TFfolderlabel.grid(row=0, column=0)

outputlabel_row = 4
outputlabel_column = 0
outputlabel_columnspan = 4
outputlabel = Label(tk, text="", justify='center')
outputlabel.grid(row=outputlabel_row, column=outputlabel_column, columnspan=outputlabel_columnspan)

# Terraform 코드가 있는 Working Directory 값을 입력. 주의> 디렉토리 주소에 '\' => '/' 로 변경해야함
TFWorkingDir = Entry(tk, width=50)
TFWorkingDir.grid(row=0,column=1)

def printOutputOnGUI(return_code, output, err, tfCmd):
    if return_code == 0:
        print(output)
        return tfCmd + " is succeed with empty diff (no changes)"
    elif return_code == 2:
        print(output)
        return tfCmd + " is succeed with non-empty diff (changes present)"
    else:
        print(err)
        return tfCmd + " is failed with errors"
        
def TFinit():
    global outputlabel
    labelreset()
    
    try:
        tf = Terraform(working_dir=TFWorkingDir.get())
        return_code, output, err = tf.init(capture_output=True)
    except:
        outputlabel = Label(tk,text="Working Directory is wrong, check it again.", justify='center')
        outputlabel.grid(row=outputlabel_row, column=outputlabel_column, columnspan=outputlabel_columnspan)
    
    outputlabel = Label(tk,text=printOutputOnGUI(return_code, output, err,"Terraform code initializing"), justify='center')
    outputlabel.grid(row=outputlabel_row, column=outputlabel_column, columnspan=outputlabel_columnspan)
    
def TFplan():
    global outputlabel
    labelreset()
    
    try:
        tf = Terraform(working_dir=TFWorkingDir.get())
        return_code, output, err = tf.plan(capture_output=True)
    except:
        outputlabel = Label(tk,text="Working Directory is wrong, check it again.", justify='center')
        outputlabel.grid(row=outputlabel_row, column=outputlabel_column, columnspan=outputlabel_columnspan)

    outputlabel = Label(tk,text=printOutputOnGUI(return_code,output, err,"Terraform code planning"), justify='center')
    outputlabel.grid(row=outputlabel_row, column=outputlabel_column, columnspan=outputlabel_columnspan)
    
def TFapply():
    global outputlabel
    labelreset()
    
    try:
        tf = Terraform(working_dir=TFWorkingDir.get())
        return_code, output, err = tf.apply(capture_output=True,skip_plan=True)
    except:
        outputlabel = Label(tk,text="Working Directory is wrong, check it again.", justify='center')
        outputlabel.grid(row=outputlabel_row, column=outputlabel_column, columnspan=outputlabel_columnspan)

    outputlabel = Label(tk,text=printOutputOnGUI(return_code,output, err,"Terraform code applying"), justify='center')
    outputlabel.grid(row=outputlabel_row, column=outputlabel_column, columnspan=outputlabel_columnspan)
    
def TFdestroy():
    global outputlabel
    labelreset()
    
    try:
        tf = Terraform(working_dir=TFWorkingDir.get())
        return_code, output, err = tf.destroy(capture_output=True,auto_approve=True, force=None)
    except:
        outputlabel = Label(tk,text="Working Directory is wrong, check it again.", justify='center')
        outputlabel.grid(row=outputlabel_row, column=outputlabel_column, columnspan=outputlabel_columnspan)
    
    outputlabel = Label(tk,text=printOutputOnGUI(return_code, output, err,"Terraform code destroying"), justify='center')
    outputlabel.grid(row=outputlabel_row, column=outputlabel_column, columnspan=outputlabel_columnspan)
    
def labelreset():
    global outputlabel
    outputlabel.grid_forget()       #label을 위치를 grid 방식으로 정의한 경우, grid_forget()으로 삭제(실제는 안 보이게 만듦)

btnInit = Button(tk,text='init',bg='black',fg='white',command=TFinit).grid(row=0,column=2)
btnPlan = Button(tk,text='plan',bg='black',fg='white',command=TFplan).grid(row=0,column=3)
btnApply = Button(tk,text='apply',bg='black',fg='white',command=TFapply).grid(row=0,column=4)
btnDestroy = Button(tk,text='destroy',bg='black',fg='white',command=TFdestroy).grid(row=0,column=5)

tk.mainloop()