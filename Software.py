# --- --- ---
# imported modules/ libraries
import mysql.connector as sql
import csv
import os
import datetime as dt
import shutil as sht
import pathlib as pth

# --- --- ---
db=sql.connect(host="localhost",user="root",password="password",database="elib",autocommit="True")
c=db.cursor()

# --- --- ---
def directory(x):  # directory of undb folder.
    if x=="book":
        return(os.listdir(r"C:\Users\SATYA NADELA\Desktop\eBooks\undbBooks"))
    elif x=="mag":
        return(os.listdir(r"C:\Users\SATYA NADELA\Desktop\eBooks\skippedBooks"))

def curdate():
    return(dt.datetime.now().strftime("%d")+"/"+dt.datetime.now().strftime("%m")+"/"+dt.datetime.now().strftime("%Y"))

def pname_it(x):
    return(x+r"\{}")

def renamove(v11,v12,v13):  # rename and move the file from input path.
    os.rename(v11,v12)
    sht.move(v12,v13)

def book_ext(x):  # extract file extension of file name argument.
    return(pth.Path(x).suffix)

def add_to_db(x,y):  # add the input book information to the sql db.
    if y=="book":
        bk_id=int(unique_id("book"))
        bk_name=input("name: ").lower()
        bk_author=input("author: ").lower()
        bk_pub=input("pub: ").lower()
        bk_ed=input("ed: ")
        bk_series=input("series: ").lower()
        bk_ext=book_ext(x)
        bk_line=input("line: ").lower()
        c.execute("insert into books values({},'{}','{}','{}','{}','{}','{}','{}')".format(bk_id,bk_name,bk_author,bk_pub,bk_ed,bk_series,bk_ext,bk_line))
    elif y=="mag":
        mag_id=int(unique_id("mag"))
        mag_name=input("name: ").lower()
        mag_basis=input("enter d|w|m|y: ")
        mag_issue=int(input("issue: "))
        mag_pub=input("publisher: ")
        
        
    

def unique_id(x):  # to generate unique book/magazine id for db primary key.
    if x=="book":
        c.execute("select id from books;")
    elif x=="mag":
        c.execute("select id from magazines;")
    data=c.fetchall()
    if data!=[]:
        l=[int(i[0]) for i in data]
        v=max(l)+1
        for i in range(1,v):
            if i not in l:
                return(str(i))
        else:
            return(str(v))
    elif data==[]:
        return("1")
    
def db_data(x):
    if x=="book":
        c.execute("select * from books;")
    elif x=="mag":
        c.execute("select * from magazines;")
    return(c.fetchall())

def books_table():
    data=db_data()
    for i in data: print(i)

def notepad_backup():
    print(" "*20,"backing up data...")
    f=open("notepad backup.txt","a+")
    data=db_data()
    var2=csv.writer(f)
    v78=curdate()+"\n"
    f.write(v78)
    var2.writerows(data)
    f.close()
    print("notepad backup sucess")

def seperate():
    print("----- "*3)
    

def search():
    search_str=input("Enter: ")
    for i in ["id","name","author","pub","ed","series","type","line"]:
        c.execute("select * from books where {} like '%{}%'".format(i,search_str))
        for j in c.fetchall():
            for k in j:
                print(k,end=" ")
            print()

# --- --- ---
### main program
##old_path=r"C:\Users\SATYA NADELA\Desktop\eBooks\undbBooks"
##new_path=r"C:\Users\SATYA NADELA\Desktop\eBooks\dbBooks"
##copy_path=r"C:\Users\SATYA NADELA\Desktop\eBooks\bookCopy"
##def add_books():
##    bks_dir=directory("book")
##    book_no=0;more=1
##    while more==1:
##        old_name=bks_dir[book_no];print(old_name)
##        new_name=unique_id("book")+book_ext(old_name)
##        print(" "*20,"opening file...")
##        sht.copyfile(pname_it(old_path).format(old_name),pname_it(copy_path).format(old_name))
##        os.startfile(pname_it(copy_path).format(old_name))
##        print("--- 0:end|1:add to db|2:skip ---")
##        _=int(input("Enter:"))
##        if _==0:
##            break
##        elif _==1:
##            print(" "*20,"renaming and moving...")
##            renamove(pname_it(old_path).format(old_name),pname_it(old_path).format(new_name),new_path)
##            print(" "*20,"renamed({} to {}) and moved.".format(old_name,new_name))
##            add_to_db(old_name)
##            print(" "*20,"adding to database...")
##            print("added to database with id:",new_name)
##            more=int(input("add more(0|1): "))
##            book_no+=1
##            continue
##        elif _==2:
##            sht.move(pname_it(r"C:\Users\SATYA NADELA\Desktop\eBooks\undbBooks").format(old_name),r"C:\Users\SATYA NADELA\Desktop\eBooks\skippedBooks")
##            book_no+=1

    
# --- --- ---
def functions():
    print("1 | add books.\n2 | search books.\n3 | add magazines")
    v43=int(input("Enter: "))
    if v43==1:
        try:
            add_books()
        except IndexError:
            print("No Books Found.")
    elif v43==2:
        search()
    elif v43==3:
        try:
            add_magazines()
        except():
            print("No Magazines Found.")
    functions()

functions()
