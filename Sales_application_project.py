month=("January","February","March","April","May","June","July","August","September","October","November","December")
profits=(20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)
from tkinter import *
root=Tk()
root.geometry("700x500")
root.title("Sales Application")
all_months=Label(root,text="Months :"+str(month))
all_months.place(relx=0.5,rely=0.2,anchor=CENTER)
root.configure(bg="yellow")
all_profit=Label(root,text="Profits :"+str(profits))
all_profit.place(relx=0.5,rely=0.3,anchor=CENTER)
def max_month():
    max_profit_month=month[profits.index(max(profits))]
    label_max_month=Label(root,text="Maximum profit of "+str(max(profits))+" was recorded in the month of "+str(max_profit_month))
    label_max_month.place(relx=0.5,rely=0.5,anchor=CENTER)
def min_month():
    min_profit_month=month[profits.index(min(profits))]
    label_min_month=Label(root,text="Minimum profit of "+str(min(profits))+" was recorded in the month of "+str(min_profit_month))
    label_min_month.place(relx=0.5,rely=0.7,anchor=CENTER)
max_btn=Button(root,text="Show Max Profitable Month",bg="#4567e6",fg="white",command=max_month)
max_btn.place(relx=0.5,rely=0.4,anchor=CENTER)
min_btn=Button(root,text="Show Min Profitable Month",bg="#4567e6",fg="white",command=min_month)
min_btn.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()