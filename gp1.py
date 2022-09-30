from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
root=Tk()
root.title('S.M.S')
root.geometry('500x400+300+300')
root.configure(background='yellow')
class user(Exception):
	def __init__(self,msg,val):
		self.msg=msg
		self.val=val
def check(r):
	if r=='':
		raise user("Roll No can not be empty",1)
	if r.isspace():
		raise user("Roll no can not be space",1)
	if r.isdigit():
		r=int(r)	
		if r<1:	
			raise user("Roll No. should be greater than zero",1)
	else:
		raise user("Invalid Roll No.",1)	
def checkmark(m):
	if m=='':
		raise user("Enter marks",3)
	if m.isspace():
		raise user("Marks no can not be space",3)
	if m.isdigit():
		m=int(m)
		if m<0 or m>100:
			raise user("Enter marks between 0-100",3)
	else:
		raise user("Invalid Marks",3)
def checkname(n):
	if n=='':
		raise user("Name can not be empty",2)
	if n.isspace():
		raise user("Name can not be space",2)
	for char in n:
		if (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
			if len(n)<2:
				raise user("Minimum length should be of 2 character",2)
			else:
				return n
	else:
		raise user("Only Characters are allowed",2)
def f1():	
	root.withdraw()
	addst.deiconify()
	entRno.focus()
def f2():
	addst.withdraw()
	root.deiconify()
def f3():
	stData.delete(1.0,END)
	root.withdraw(),
	viewst.deiconify()
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect('system/abc123')
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=''
		for d in data:
			msg=msg+'rno:'+str(d[0])+'   '+'name:'+d[1] +'        '+'marks:'+str(d[2])+'\n'
		stData.insert(INSERT,msg)
	except cx_Oracle.DatabaseError as e:
		print('some issue ',e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print('disconnected')

def f4():
	viewst.withdraw()
	root.deiconify()
def f5():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect('system/abc123')
		rno=entRno.get()
		check(rno)
		name=entName.get()
		checkname(name)
		name=name.strip()
		name=name.title()
		mark=entmark.get()
		checkmark(mark)
		cursor=con.cursor()
		sql="insert into student values('%s','%s','%s')"
		args=(rno,name,mark)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+'records inserted'
		messagebox.showinfo('Added ',msg)
		entRno.delete(0,END)
		entName.delete(0,END)
		entmark.delete(0,END)
		entRno.focus()
	except user as u:
		messagebox.showerror('Sorry',u.msg)
		if u.val==1:
			entRno.delete(0,END)
			entRno.focus()
		if u.val==2:
			entName.delete(0,END)
			entName.focus()
		if u.val==3:
			entmark.delete(0,END)
			entmark.focus()
	except Exception:
		messagebox.showerror("Something's wrong ","Roll no already exist")	
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror('Galat kiya re',e)
		con.rollback()
		entRno.delete(0,END)
		entName.delete(0,END)
		entmark.delete(0,END)
		entRno.focus()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		entRno.delete(0,END)
		entName.delete(0,END)
		entmark.delete(0,END)
		entRno.focus()
def f6():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect('system/abc123')
		rno=entRno1.get()
		check(rno)
		name=entName1.get()
		checkname(name)
		name=name.strip()
		name=name.title()
		marks=entmark1.get()
		checkmark(marks)
		cursor=con.cursor()
		sql="update student set name='%s',marks='%s' where rno='%s'"
		args=(name,marks,rno)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+'records updated'
		messagebox.showinfo('Updated ',msg)
		entRno1.delete(0,END)
		entName1.delete(0,END)
		entmark1.delete(0,END)
		entRno1.focus()
	except user as u:
		messagebox.showerror('Sorry',u.msg)
		if u.val==1:
			entRno1.delete(0,END)
			entRno1.focus()
		if u.val==2:
			entName1.delete(0,END)
			entName1.focus()
		if u.val==3:
			entmark1.delete(0,END)
			entmark1.focus()
	except ValueError:
		messagebox.showerror('Sorry',"Numbers only")
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror('Galat kiya re',e)
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f7():
	updatest.withdraw()
	root.deiconify()
def f8():
	root.withdraw()
	updatest.deiconify()
	entRno1.focus()
def f9():
	root.withdraw()
	deletest.deiconify()
	entRno2.focus()
def f10():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect('system/abc123')
		rno=entRno2.get()
		check(rno)
		cursor=con.cursor()
		sql="delete from student where rno='%s'"
		args=(rno)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+'record deleted'
		messagebox.showinfo('Deleted ',msg)
		entRno2.delete(0,END)
		entRno2.focus()
	except user as u:
		messagebox.showerror('Sorry',u.msg)
		if u.val==1:
			entRno2.delete(0,END)
			entRno2.focus()
	except ValueError:
		messagebox.showerror('Roll No',"Numbers only")
		entRno2.delete(0,END)
		entRno2.focus()
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror('Galat kiya re',e)
		entRno2.delete(0,END)
		entRno2.focus()
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f11():
	deletest.withdraw()
	root.deiconify()
def f12():
	import matplotlib.pyplot as plt
	import numpy as np
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect('system/abc123')
		cursor=con.cursor()
		sql="select name,marks from student"	
		cursor.execute(sql)	
		data=cursor.fetchall()
		#print(data)
		n,m=[],[]
		for d in data:
			n.append(d[0])
			m.append(d[1])
		plt.bar(n[0:5],m[0:5],width=0.25)
		x=np.arange(len(n))
		plt.xticks(x,n[0:5],fontsize=10)
		plt.xlabel('Student')
		plt.ylabel('Score')
		plt.title('Top 5 Entry')
		plt.grid()
		plt.show()
		#print(n)
		#print(m)
	except cx_Oracle.DatabaseError as e:
		print('some issue ',e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print('disconnected')
def f13():	
	import bs4
	import requests
	try:
		res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
		soup=bs4.BeautifulSoup(res.text,'lxml')
		quote=soup.find('img',{"class":"p-qotd"})['alt']
	
		text=quote['alt']
		return text
	except OSError:	
		text="NA"
		return text
q=f13()
def f14():
	import socket	
	import requests
	temp=None
	city='mumbai'
	try:
		socket.create_connection(("www.google.com",80))
		a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2="&q="+city
		a3="&appid=c6e315d09197cec231495138183954bd"
		api_address=a1+a2+a3
		res=requests.get(api_address)
		data=res.json()
		main=data['main']
		tempe=main['temp']
		return tempe
	except OSError:
		#print('check network')
		lbltemp=Label(root,text="NA",bg='yellow',font=("arial",18,"bold"))
t='Temp: '+str(f14())+'\u00B0'+'C'
btnadd=Button(root,text="Add",fg='white',bg='black',font=('arial',18,'bold'),width=10,command=f1)
btnview=Button(root,text='View',fg='white',bg='black',font=('arial',18,'bold'),width=10,command=f3)
btnupdate=Button(root,text='Update',fg='white',bg='black',font=('arial',18,'bold'),width=10,command=f8)
btndelete=Button(root,text="Delete",fg='white',bg='black',font=('arial',18,'bold'),width=10,command=f9)
btngraph=Button(root,text="Graph",fg='white',bg='black',font=('arial',18,'bold'),width=10,command=f12)
lblquote=Label(root,text=q,bg='yellow')
lbltemp=Label(root,text=t,bg='yellow')
btnadd.pack(pady=10)
btnview.pack(pady=10)
btnupdate.pack(pady=10)
btndelete.pack(pady=10)
btngraph.pack(pady=10)
lblquote.pack(pady=10)
lbltemp.place(x=5,y=5)

addst=Toplevel(root)
def doSomething():
    # check if saving
    # if not:
    root.destroy()

addst.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
addst.title("ADD S")
addst.geometry('400x500+300+300')
addst.configure(background='sky blue')
addst.withdraw()
lblrno=Label(addst,text="Enter Rollno.",font=('arial',18,'bold'))
entRno=Entry(addst,bd=5,font=('arial',18,'bold'))
lblname=Label(addst,text="Enter Name",font=('arial',18,'bold'))
entName=Entry(addst,bd=5,font=('arial',18,'bold'))
lblmark=Label(addst,text="Enter Marks",font=('arial',18,'bold'))
entmark=Entry(addst,bd=5,font=('arial',18,'bold'))
btnaddsave=Button(addst,text="Save",font=('arial',18,'bold'),command=f5)
btnaddback=Button(addst,text="Back",font=('arial',18,'bold'),command=f2)
lblrno.pack(pady=10)
entRno.pack(pady=10)
lblname.pack(pady=10)
entName.pack(pady=10)
lblmark.pack(pady=10)
entmark.pack(pady=10)
btnaddsave.pack(pady=10)
btnaddback.pack(pady=10)

viewst=Toplevel(root)
def doSomething():
    # check if saving
    # if not:
    root.destroy()

viewst.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
viewst.title("View S")
viewst.geometry('400x300+300+300')
viewst.withdraw()
stData=scrolledtext.ScrolledText(viewst,width=40,height=15)
btnviewback=Button(viewst,text='Back',font=('arial',18,'bold'),command=f4)
stData.pack()
btnviewback.pack()

updatest=Toplevel(root)
def doSomething():
    # check if saving
    # if not:
    root.destroy()

updatest.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
updatest.title("Update S")
updatest.geometry('400x550+300+300')
updatest.configure(background='cyan')
updatest.withdraw()
lblrno1=Label(updatest,text="Enter Rollno.",font=('arial',18,'bold'))
entRno1=Entry(updatest,bd=5,font=('arial',18,'bold'))
lblname1=Label(updatest,text="Enter Name",font=('arial',18,'bold'))
entName1=Entry(updatest,bd=5,font=('arial',18,'bold'))
lblmark1=Label(updatest,text='Enter Marks',font=('arial',18,'bold'))
entmark1=Entry(updatest,bd=5,font=('arial',18,'bold'))
btnaddsave1=Button(updatest,text="Save",font=('arial',18,'bold'),command=f6)
btnaddback1=Button(updatest,text="Back",font=('arial',18,'bold'),command=f7)
lblrno1.pack(pady=10)
entRno1.pack(pady=10)
lblname1.pack(pady=10)
entName1.pack(pady=10)
lblmark1.pack(pady=10)
entmark1.pack(pady=10)
btnaddsave1.pack(pady=10)
btnaddback1.pack(pady=10)

deletest=Toplevel(root)
def doSomething():
    # check if saving
    # if not:
    root.destroy()

deletest.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
deletest.title("DELETE S")
deletest.geometry('400x400+300+300')
deletest.configure(background='red')
deletest.withdraw()
lblrno2=Label(deletest,text="Enter Rollno.",font=('arial',18,'bold'))
entRno2=Entry(deletest,bd=5,font=('arial',18,'bold'))
btndelete=Button(deletest,text='Delete',font=('arial',18,'bold'),command=f10)
btnback2=Button(deletest,text="Back",font=('arial',18,'bold'),command=f11)
lblrno2.pack(pady=10)
entRno2.pack(pady=10)
btndelete.pack(pady=10)
btnback2.pack(pady=10)


root.mainloop()