

########################################################################################
########################################################################################
## # CODE LANGUAGE IS PYHTON!          ##      ##                                     ##
## # DATE: 1-JULY-2021                 ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                     ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!     ##########    #######   ##     ##   ##     ##  ##
## # STATUS BAR!                       ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                    ##      ##    #######   ##     ##   ########   ##
########################################################################################
########################################################################################


from tkinter import *

def upload():
    statusvar.set("Busy...")




root = Tk()
root.geometry("477x335")
root.title("Status bar")
root.bell()

statusvar = StringVar() #String variable!
statusvar.set("ready")  #set the value os ready!
sbar = Label(root,textvariable=statusvar,relief=SUNKEN, anchor="w").pack(side=BOTTOM, fill=X)
Button(root,text="upload",command=upload).pack()


root.mainloop()

