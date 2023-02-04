from flask import Flask,request
from datetime import datetime 
import csv
import pandas as p

app=Flask(__name__)

#function to validate date
def checkDate(d,m,y):
    s=y+'-'+m+'-'+d
    try:
        dt=datetime.strptime(s,'%Y-%m-%d').date()
    except:
        return False
    else:
        return dt >= datetime.now().date()

#function to create a id for the new task
def getId():
    i=1
    try:
        f=open("List.csv","r")
    except:
        head=['id','task','status','due date']
        f=open("List.csv","a",newline='')
        write=csv.writer(f)
        write.writerow(head)
        return i
    else:
        read=csv.reader(f)
        f.readline()
        for t in read:
            if int(t[0]) != i:
                return i
            i+=1
        return i

#add a new to the list
@app.route("/add")
def addTodo():
    try:
        t=request.args.get("task")
        d=request.args.get("date")
        m=request.args.get("month")
        y=request.args.get("year")
    except:
        return "Please enter parameterized data"
    else:
        if len(t) == 0:
            return "task should not be empty"
        if checkDate(d,m,y):
            task=[getId(),t,"incomplete",d+"-"+m+"-"+y]
            f=open("List.csv","a",newline='')
            write=csv.writer(f)
            write.writerow(task)
            return "added"
        return "Please enter correct date!!"

#mark the task as completed/incomplete
@app.route("/update/status")
def updateStatus():
    try:
        id=int(request.args.get("id"))
    except:
        return "enter id correctly"
    temp=0
    try:
        f=p.read_csv("List.csv",index_col='id')
        if f.iloc[id-1,1] != 'completed':
            f.iloc[id-1,1]='completed'
            temp=1
        else:
            f.iloc[id-1,1]='incomplete'
    except:
        return "task does not exists"
    else:
        f.to_csv("List.csv")
        if temp==1:
            return "task marked as completed"
        else:
            return "task marked as incomplete"

#extend the due date
@app.route("/update/date")
def updateDate():
    try:
        id=int(request.args.get("id"))
    except:
        return "enter id correctly"
    try:
        d=request.args.get("date")
        m=request.args.get("month")
        y=request.args.get("year")
    except:
        return "enter date properly"
    try:
        f=p.read_csv("List.csv",index_col="id")
        s=f.iloc[id-1,2]
    except:
        return "task not present"
    try:
        d1=datetime.strptime(y+'-'+m+'-'+d,'%Y-%m-%d').date()
        d2=datetime.strptime(s,'%d-%m-%Y').date()
        if d2<d1:
            s=f.iloc[id-1,2]=d+'-'+m+'-'+y
            f.to_csv("List.csv")
        else:
            return "date should be greater than the previos due date"
    except:
        return "not a valid date"
    return "date updated"

#remove a task
@app.route("/remove/")
def removeTask():
    try:
        id=int(request.args.get("id"))
    except:
        return "enter id correctly"
    try:
        f=p.read_csv("List.csv",index_col="id")
        f.drop(id,axis=0,inplace=True)
    except:
        return "task not present"
    else:
        f.to_csv("List.csv")
        return "task removed"

#display the list of tasks
@app.route("/todo")
def getTodo():
    try:
        f=open("List.csv","r")
        read=csv.reader(f)
    except:
        return "No tasks"
    else:
        lt=dict()
        f.readline()
        for task in read:
            x=[]
            x.append("task - "+task[1])
            x.append("status - "+task[2])
            x.append("due date - "+task[3])
            lt["id - "+task[0]]=x
        return lt

if __name__=="__main__":
    app.run()