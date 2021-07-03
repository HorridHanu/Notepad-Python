

########################################################################################
########################################################################################
## # CODE LANGUAGE IS PYHTON!          ##      ##                                     ##
## # DATE: 1-JULY-2021                 ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                     ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!     ##########    #######   ##     ##   ##     ##  ##
## # MENU AND SUBMENU!                 ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                    ##      ##    #######   ##     ##   ########   ##
########################################################################################
########################################################################################


from tkinter import *
root = Tk()
root.geometry("733x566")
root.title("Menu and submenu!")
root.bell()                 #used to bell on openin

def file():
    print("yes menu work!")

    # create for non drop command
# mymenu= Menu(root)
# mymenu.add_command(label="file",command=file)
# mymenu.add_command(label="exit",command=quit)
# root.config(menu=mymenu)


 # its menu!
filemenu = Menu(root, tearoff = 00)

# these are submenu!
m1=Menu(filemenu)
m1.add_command(label="new project",command=file)
m1.add_separator()
m1.add_command(label="new",command=file)
m1.add_command(label="open",command=file)
m1.add_command(label="rename",command=file)
m1.add_command(label="close",command=file)
m1.add_command(label="save project",command=file)
m1.add_command(label="setting",command=file)
m1.add_command(label="save all",command=file)
m1.add_command(label="print",command=file)
m1.add_command(label="exit",command=exit)
filemenu.add_cascade(label="file",menu=m1)


m2=Menu(filemenu)
m2.add_command(label="new project",command=file)
m2.add_separator()
m2.add_command(label="new",command=file)
m2.add_command(label="open",command=file)
m2.add_command(label="rename",command=file)
m2.add_command(label="close",command=file)
m2.add_command(label="save project",command=file)
m2.add_command(label="setting",command=file)
m2.add_command(label="save all",command=file)
m2.add_command(label="print",command=file)
m2.add_command(label="exit",command=exit)           #exit has pre-function to exit!
filemenu.add_cascade(label="edit",menu=m1)
root.config(menu=filemenu)
root.mainloop()