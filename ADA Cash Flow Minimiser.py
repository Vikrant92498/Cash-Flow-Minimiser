
import cv2
import math
from glob import glob
from tkinter import *
from numpy import place
from PIL import ImageTk, Image
import random


final_graph=[]
inde=[]             
person_final=[]
count=0
def minCashFlow_1(amount ,person,d,count):
    mxCredit = getMax(amount)
    mxDebit = getMin(amount)
    if(amount[mxCredit]==0 and amount[mxDebit]==0):
        qwer =Label(end_root,text="Number of Transaction reduced from "+str(n)+" to " +str(count),font=("Times New Roman",14) ,padx=5,pady=5)
        qwer.place(x = 600, y = 200+40*d)
        return 0

    min = minOf2(-amount[mxDebit],amount[mxCredit])
    amount[mxCredit]-=min
    amount[mxDebit]+=min
    final_graph[mxDebit][mxCredit] = min
    resul = str(person[mxDebit])+" should pay "+str(min)+" INR Rupees to "+str(person[mxCredit])
    count+=1
    if person_final.count(person[mxDebit])==0:
        person_final.append(person[mxDebit])
    if person_final.count(person[mxCredit])==0:
        person_final.append(person[mxCredit])

    person_final.append(person[mxCredit])
    qwer1 =Label(end_root,text=resul,font=("Times New Roman",14) ,padx=5,pady=5)
    qwer1.place(x = 500, y = 200+40*d ,width=500,height=30)

    minCashFlow_1(amount,person,d+1,count)
    

def minCashFlow(graph,person):
    circle_plot(N,700,graph,person)
    global end_root
    end_root =Tk()
    end_root.title("Cash Flow Minimizer")
    end_root.geometry("%dx%d" % (width, height))
    img =Image.open(r'images\\1.jpg')
    resized = img.resize((width,height))
    bg = ImageTk.PhotoImage(resized)
    label = Label(end_root, image=bg)
    label.place(x=0,y=0)
    Button(
        end_root,
        text="New Problem ?", 
        padx=10, 
        pady=5,
        command=start_again
        ).place(x=800,y=550)
    Button(
        end_root,
        text="Exit ", 
        padx=10, 
        pady=5,
        command=exit
        ).place(x=400,y=550)
    heading(end_root)
    
    for d in range(N):
        for g in range(N):
            inde.append(-1)
        final_graph.append(inde)
    amount = [0 for i in range(N)]
    for p in range(N):
        for i in range(N):
            amount[p] += (graph[i][p] - graph[p][i])
    minCashFlow_1(amount,person,0,count)
    end_root.mainloop()


def B():
    
    for i in range(len(AMT)):
        person.append(AMT[i].get())
        p1_index.append(person.index(Left_person[i].get()))
        p2_index.append(person.index(Right_person[i].get()))
        amt_to.append(int(AMT[i].get()))
    root_to_detail.destroy()
    ins =[]
    for z in range (N):
        for m in range(N):
            ins.append(0)
        graph.append(ins)
        ins=[]
    for z in range (N):
        for m in range(N):
            for s in range(n):
                if(z==p1_index[s] and m==p2_index[s]):
                    graph[z][m]=amt_to[s]
    minCashFlow(graph,person)
def getMin(arr):
	minInd = 0
	for i in range(1, N):
		if (arr[i] < arr[minInd]):
			minInd = i
	return minInd

def getMax(arr):

	maxInd = 0
	for i in range(1, N):
		if (arr[i] > arr[maxInd]):
			maxInd = i
	return maxInd

def minOf2(x, y):

	return x if x < y else y 
def A():
    global n,Left_person,Right_person,AMT ,root_to_detail
    n=int(No_of_transaction.get())
    root_to_getinfo.destroy()
    root_to_detail = Tk()
    root_to_detail.title("Cash Flow Minimizer")
    root_to_detail.geometry("%dx%d" % (width, height))
    img =Image.open(r'images\\1.jpg')
    resized = img.resize((width,height))
    bg = ImageTk.PhotoImage(resized)
    img.close()
    label = Label(root_to_detail, image=bg)
    label.place(x=0,y=0)
    resized.close()
    Left_person=[]
    Right_person=[]
    AMT =[]
    heading(root_to_detail)
    for d in range(n):
        clicked1 = StringVar()
        clicked1.set( person[0] )
        drop1 = OptionMenu( root_to_detail , clicked1 , *person )
        drop1.config(width=15,height=1,font=("Times New Roman",14),pady=3)
        drop1.place(x = 295, y = 200+40*d)
        lblfrstrow = Label(root_to_detail, text =" have to pay Rs. ",font=("Times New Roman",14),pady=5 )
        lblfrstrow.place(x = 475, y = 200+40*d)
        Amount = Entry(root_to_detail,font=("Times New Roman",14),justify='center',width=22,)
        Amount.pack()
        Amount.place(x = 606, y = 200+40*d ,height=35)
        lblfrstrow = Label(root_to_detail, text =" to ",font=("Times New Roman",14),pady=5 )
        lblfrstrow.place(x = 800, y = 200+40*d)
        clicked2 = StringVar()
        clicked2.set( person[0] )
        drop2 = OptionMenu( root_to_detail , clicked2 , *person )
        drop2.config(width=15,height=1,font=("Times New Roman",14),pady=3)
        drop2.place(x = 830, y = 200+40*d)
        Left_person.append(clicked1)
        Right_person.append(clicked2)
        AMT.append(Amount)
        Button(
        root_to_detail,
        text=" Minimise Transactions ", 
        padx=10, 
        pady=5,
        command=B
        ).place(x=830,y=200+40*d +40)
    root_to_detail.mainloop()
def transaction_info():
    for i in range(len(objperson)):
        person.append(objperson[i].get())
    
    root_to_name.destroy()
    global root_to_getinfo ,n,d
    root_to_getinfo = Tk()
    root_to_getinfo.title("Cash Flow Minimizer")
    root_to_getinfo.geometry("%dx%d" % (width, height))
    img =Image.open(r'images\\1.jpg')
    resized = img.resize((width,height))
    bg = ImageTk.PhotoImage(resized)
    img.close()
    label = Label(root_to_getinfo, image=bg)
    label.place(x=0,y=0)
    resized.close()
    heading(root_to_getinfo)
    lblfrstrow = Label(root_to_getinfo, text ="Number of transactions : ",font=("Times New Roman",14) )
    lblfrstrow.pack(pady=30)
    global No_of_transaction
    No_of_transaction = Entry(root_to_getinfo,justify='center',font=("Times New Roman",14))
    No_of_transaction.pack(pady=40)
    Button(
        root_to_getinfo,
        text="Proceed", 
        padx=10, 
        pady=5,
        command=A
        ).place(x=650,y=350)
    root_to_getinfo.mainloop()

def getName():
    global root_to_name
    global N,person,graph,p1_index,p2_index,amt_to,objperson
    N = int(No_of_person.get())
    root.destroy()
    root_to_name = Tk()
    root_to_name.title("Cash Flow Minimizer")
    root_to_name.geometry("%dx%d" % (width, height))
    img =Image.open(r'images\\1.jpg')
    resized = img.resize((width,height))
    bg = ImageTk.PhotoImage(resized)
    img.close()
    label = Label(root_to_name, image=bg)
    label.place(x=0,y=0)
    resized.close()
    heading(root_to_name)
    person=[]
    objperson=[]
    graph =[]
    p1_index=[]
    p2_index=[]
    amt_to=[]
    global k,d
    instruction_1="Please Provide Name of all "+str(N)+" People " 
    lblfrstrow = Label(root_to_name, text =instruction_1,font=("Times New Roman",14) )
    lblfrstrow.pack()
    for k in range(N):
        instruction_i="Person "+str(k+1)
        Label(root_to_name,font=("Times New Roman",14), text =instruction_i ).place(x = 540, y = 220+50*k)
        name = Entry(root_to_name,justify='center',font=("Times New Roman",14))
        name.pack(pady=10)
        name.place(x = 640, y = 220+50*k)
        objperson.append(name)
    Button(
    root_to_name,
    text="Submit !", 
    padx=10, 
    pady=5,
    background='#60f568',
    command=transaction_info
    ).place(x=750,y=280+50*k)
    root_to_name.mainloop()

def heading(win_name):
    label2 = Label(win_name, text = "    Cash Flow Minimiser    ",
    font=("Impact", 34,),)
    label2.pack(pady = 38)

def start_again():
    end_root.destroy()
    global root ,No_of_person,width,height
    root = Tk()
    root.title("Cash Flow Minimizer")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    img =Image.open(r'images\\1.jpg')
    resized = img.resize((width,height))
    bg = ImageTk.PhotoImage(resized)
    img.close()
    label = Label(root, image=bg)
    label.place(x=0,y=0)
    resized.close()
    heading(root)
    
    label2 = Label(root, text ="Number of persons : ",font=("Times New Roman",14) ,padx=5,pady=5)
    label2.place(x = 505, y = 230)
    No_of_person = Entry(root,font=("Times New Roman",14),justify='center')
    No_of_person.pack(padx=100,pady=100)
    No_of_person.place(x = 695, y = 230,height=35)
    Button(
        root,
        text="Proceed", 
        padx=10, 
        pady=5,
        bg="brown",fg="white",
        command=getName
        ).place(x=775,y=350)
    root.mainloop()


def start():
    
    global root ,No_of_person,width,height
    root = Tk()
    root.title("Cash Flow Minimizer")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    img =Image.open(r'images\\2.jpg')
    resized = img.resize((width,height))
    bg = ImageTk.PhotoImage(resized)
    img.close()
    label = Label(root, image=bg)
    label.place(x=0,y=0)
    resized.close()
    
    heading(root)
    
    label1 = Label(root, text ="Number of persons : ",font=("Times New Roman",14) ,padx=5,pady=5)
    label1.place(x = 505, y = 230)
    No_of_person = Entry(root,font=("Times New Roman",14),justify='center')
    No_of_person.pack(padx=100,pady=100)
    No_of_person.place(x = 695, y = 230,height=35)
    Button(
        root,
        text="Proceed", 
        padx=10, 
        pady=5,
        bg="brown",fg="white",
        command=getName
        ).place(x=775,y=350)
        
    root.mainloop()

def circle_plot(n,shift,graph,person):
    path = r'images\\3.png'
    image = cv2.imread(path)
    window_name = 'Image'
    theta = 6.28/n
    X=shift
    Y = 350
    x_cor = []
    y_cor = []
    R = 210
    radius=40
    color = (0, 0, 255)
    thickness = -1
    for i in range(0,n):
        if(i==0):
            m = math.tan(i*theta)
            x = X + R/math.sqrt(1+m*m)
            y = m*(x-X)+Y
            x_cor.append(int(x))
            y_cor.append(int(y))
            center_coordinates = (int(x),int(y))
            cv2.circle(image, center_coordinates, radius, color, thickness)
            cv2.putText(image, person[i],(int(x),int(y)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                
        else:
            m = math.tan(i*theta)
            x1 = X + R/math.sqrt(1+m*m)
            y1 = Y+(m*R)/math.sqrt(1+m*m)
            d1 = (x_cor[-1] - x1)**2 + (y_cor[-1] - y1)**2
            x2 = X - R/math.sqrt(1+m*m)
            y2 = Y-(m*R)/math.sqrt(1+m*m)
            d2 = (x_cor[-1] - x2)**2 + (y_cor[-1] - y2)**2
            if(d1<d2):
                x_cor.append(int(x1))
                y_cor.append(int(y1))
                center_coordinates = (int(x1),int(y1))
                cv2.circle(image, center_coordinates, radius, color, thickness)
                cv2.putText(image, person[i], (int(x1),int(y1)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                
            elif(d2<d1):
                x_cor.append(int(x2))
                y_cor.append(int(y2))
                center_coordinates = (int(x2),int(y2))
                cv2.circle(image, center_coordinates, radius, color, thickness)
                cv2.putText(image, person[i], (int(x2),int(y2)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                
    window_name = 'Image'
    for s in range(N):
        for u in range(N):
            if(graph[s][u]!=0 and s!=u):
                d=math.sqrt((x_cor[s]-x_cor[u])**2 +(y_cor[s]-y_cor[u])**2)
                start_point = (int(((d-radius)*x_cor[s] + radius*x_cor[u])/d),int(((d-radius)*y_cor[s] + radius*y_cor[u])/d))
                end_point = (int(((d-radius)*x_cor[u] + radius*x_cor[s])/d),int(((d-radius)*y_cor[u] + radius*y_cor[s])/d))
                color = (0, 255, 0)
                thickness = 4
                cv2.arrowedLine(image, start_point, end_point,color, thickness)
                x_avg=(x_cor[s]+x_cor[u])/2
                y_avg=(y_cor[s]+y_cor[u])/2
                cv2.putText(image, str(graph[s][u]), (int(x_avg),int(y_avg)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    cv2.imshow(window_name, image)


start()
