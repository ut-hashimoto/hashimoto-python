import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        #self.master.geometry("300x650")
        #self.master.title("自動化システム")
        self.create_widgets()

    def create_widgets(self):
        #URL_sheet
        url = tk.LabelFrame(self,text="スプレットシートURL")
        self.ad_url=tk.Entry(url,width=20)
        self.ad_url.pack(side=tk.LEFT)
        self.readbut=tk.Button(url,text="読込")
        self.readbut.pack(side=tk.LEFT,)
        url.pack(anchor=tk.W, fill=tk.X,ipadx=27)

        #掲載番号
        number = tk.LabelFrame(self,text="掲載番号")
        OptionList =[" ","1","2","3"]
        self.variable = tk.StringVar(number)
        self.variable.set(OptionList[0])
        self.opt = tk.OptionMenu(number, self.variable, *OptionList)
        self.opt.config(width = 28)
        self.opt.pack()
        number.pack(anchor=tk.W, fill=tk.X)

       #クライアント名
        cliantname = tk.LabelFrame(self,text="クライアント名")
        cliantname.pack( fill=tk.X)
        self.cliantname=tk.Entry(cliantname)
        self.cliantname.pack(fill=tk.X)
def main():
    root = tk.Tk()
    root.geometry("300x650")
    root.title("自動化システム")
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()