import tkinter as tk

root = tk.Tk()

#窓枠
root.title("ｽｶｳﾄ自動化UI（橋本）")
root.geometry("290x650")

#spreadsheet url
l1 = tk.LabelFrame(root,text="spread sheet url",width = 217 , height = 45 )
l1.pack()


txt1 = tk.Entry(width=20)
txt1.place(x = 38, y = 20)

#読込ボタン
btn = tk.Button(root, text= "読込")
btn.place(x=162, y=17)

#掲載番号
l2 = tk.LabelFrame(root,text="掲載番号",width = 216 , height = 49 )
l2.pack()

OptionList = ["案件１","案件2","案件3","案件4"] 

variable = tk.StringVar(root)
variable.set(OptionList[0])

opt = tk.OptionMenu(l2, variable,*OptionList)
opt.config(width = 28)
opt.pack()


#クライアント名
l3 = tk.LabelFrame(root,text="クライアント名",width = 217 ,height = 39 )
l3.pack()

txt2 = tk.Entry(l3,width=35)
txt2.pack()

#enログインid
l4 = tk.LabelFrame(root,text="enログインid",width = 217 , height = 39 )
l4.pack()

txt3 = tk.Entry(l4,width=35)
txt3.pack()

#enログインpassword
l5 = tk.LabelFrame(root, text="enログインpassword", width = 217, height = 39 ,relief="groove")
l5.pack()

txt4 = tk.Entry(l5,width=35)
txt4.pack()

#通数
l6 = tk.LabelFrame(root, text="通数", width = 217 ,height = 39,relief="groove")
l6.pack()

txt5 = tk.Entry(l6,width=35)
txt5.pack()

#掲載原稿の職種
l7 = tk.LabelFrame(root, text="掲載原稿の職種",width = 217, height = 39 ,relief="groove")
l7.pack()

txt6 = tk.Entry(l7,width=35)
txt6.pack()

#検索条件
l8 = tk.LabelFrame(root, text="検索条件", width = 217 , height = 63 , relief="groove")
l8.pack()

txt7 = tk.Entry(l8,width=35)
txt7.pack()

OptionList1 = ["検索条件１","検索条件2","検索条件3","検索条件4"] 

variable1 = tk.StringVar(root)
variable1.set(OptionList1[0])

opt1 = tk.OptionMenu(l8, variable1,*OptionList1)
opt1.config(width=28)
opt1.pack()


#年齢下限
l9 = tk.LabelFrame(root, text="年齢下限",width = 217, height = 39 ,relief="groove")
l9.pack()

txt8 = tk.Entry(l9,width=35)
txt8.pack()

#年齢上限
l10 = tk.LabelFrame(root, text="年齢上限",width = 217, height = 39 ,relief="groove")
l10.pack()

txt9 = tk.Entry(l10,width=35)
txt9.pack()

#性別
l11 = tk.LabelFrame(root,text="性別",width = 217 , height = 49 )
l11.pack()

OptionList2 = ["なし","男性","女性"] 

variable2 = tk.StringVar(root)
variable2.set(OptionList2[0])

opt2 = tk.OptionMenu(l11, variable2,*OptionList2)
opt2.config(width=28)
opt2.pack()


#市区町村(「,」区切りで複数入力可能
l12 = tk.LabelFrame(root, text="市区町村(「,」区切りで複数入力可能）",width = 217, height = 39 ,relief="groove")
l12.pack()

txt10 = tk.Entry(l12,width=35)
txt10.pack()

#その他言語が「---」の人以外も対象にする
l13 = tk.LabelFrame(root,text="その他言語が「---」の人以外も対象にする",width = 216 , height = 49 )
l13.pack()

intvar1 = tk.IntVar()
chk1 = tk.Checkbutton(l13,variable=intvar1, onvalue=1, offvalue=0, height=0, width=27)
chk1.pack()

#実際に追加しない（テスト実行）
l14 = tk.LabelFrame(root,text="実際に追加しない（テスト実行）",width = 216 , height = 49 )
l14.pack()

intvar2 = tk.IntVar()
intvar2.set(True)
chk2 = tk.Checkbutton(l14,variable=intvar2, onvalue=1, offvalue=0, height=0, width=27)
chk2.pack()

#実行
btn = tk.Button(root, text= "実行",width = 50,)
btn.pack(pady = 10)

root.mainloop()