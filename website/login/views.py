from django.shortcuts import render
import mysql.connector as sql
em = ""
pwd = ""

def login_action(request):
    global em,pwd

    if request.method == "POST":
        m = sql.connect(host ="localhost", user='root',password="123456@asdf",database="website")
        cursor = m.cursor()
        d = request.POST

        for key,value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        c = " select * from users where email = '{}' and password = '{}' ".format(em,pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            c = " select * from users "
            cursor.execute(c)
            t = tuple(cursor.fetchall())
            print(t)
            if t == ():
               return render(request, 'welcome.html')
            else:
                return render(request, 'home.html', {'response':t})




    return render(request,'login_page.html')
