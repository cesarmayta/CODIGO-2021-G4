import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_563=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_563["font"] = ft
        GLabel_563["fg"] = "#333333"
        GLabel_563["justify"] = "center"
        GLabel_563["text"] = "Nombre"
        GLabel_563.place(x=30,y=20,width=70,height=25)

        GLineEdit_169=tk.Entry(root)
        GLineEdit_169["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_169["font"] = ft
        GLineEdit_169["fg"] = "#333333"
        GLineEdit_169["justify"] = "center"
        GLineEdit_169["text"] = "Entry"
        GLineEdit_169.place(x=110,y=20,width=70,height=25)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
