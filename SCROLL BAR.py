

########################################################################################
########################################################################################
## # CODE LANGUAGE IS PYHTON!          ##      ##                                     ##
## # DATE: 1-JULY-2021                 ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                     ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!     ##########    #######   ##     ##   ##     ##  ##
## # SCROLLBAR WITH TEXT!              ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                    ##      ##    #######   ##     ##   ########   ##
########################################################################################
########################################################################################




from tkinter import *

root = Tk()
root.geometry("400x250")
root.title("Scroll Bar")
root.bell()     #used to bell on openin



# for list

# sb =Scrollbar(root)
# sb.pack(side=LEFT, fill=Y)
#
# list =Listbox(root, yscrollcommand=scrollbar.set)
# for i in range(101):
#     list.insert(END, i)
# list.pack()
# sb.config(command=list.yview)



# for text

sb = Scrollbar(root)
sb.pack(fill=Y, side=RIGHT)
#enter the text and doing fun with them!
text = Text(root, yscrollcommand=sb.set)
text.pack(fill=BOTH)
sb.config(command=text.yview)

root.mainloop()
