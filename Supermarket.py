from flask import Flask, render_template, request, redirect
import os.path
from os import path

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("Login.html")

@app.route("/info",methods=["GET", "POST"])
def GetInfo():
    global username,userpasswd
    global fileDir
    fileDir = os.path.dirname(os.path.realpath("__file__"));

    username = request.form.get('txtusername');
    userpasswd = request.form.get('txtpassword');
    usermsg = request.form.get('usermsg');

    print(usermsg)
    if(usermsg == "Admin"):
        return render_template("DepartmentsAdmin.html",username = username);
    else:
        return User();

def User():
    userfilename = username + ".doc";
    IfExist(userfilename);
    
    if(TorF == "false"):
        adminfile = open(userfilename,"x");
        adminfile.close();
        Append(userfilename,userpasswd);
        print("Created")
    else:
        print("existed")
        adminfile = open(userfilename,"r+");
        fileitems = adminfile.read().split(";");
        if(fileitems[0] != userpasswd):
            errormsg = "Incorrect password!"
            return render_template("Login.html", errormsg = errormsg);

    return render_template("DepartmentsUser.html",username = username);
        
def IfExist(thefile):
    global TorF;
    fileexist = bool(path.exists(thefile));
    if(fileexist == False):
        TorF = "false";
    else:
        TorF = "true";

def Append(name,info):
    adminfile = open(name,"a");
    adminfile.write(info + ";");
    adminfile.close();

@app.route("/fruit")
def fruit():
    global dptmFileName
    dptmFileName = "Fruit.doc"
    print("Welcome to fruit section")
    IfExist(dptmFileName);
    if(TorF == "false"):
        return render_template("Fruit.html");
    else:
        adminfile = open(dptmFileName,"r+")
        allInfo = adminfile.read();
        thelength = len(allInfo);
        if(thelength == 0):
            return render_template("Fruit.html");
        else:
            Retrieve();
            headings = ("Image","Product","Price","Unit")
            return render_template("Fruit.html",headings = headings,data = data)
        

@app.route("/fruitinfo",methods=["POST"])
def GetfruitInfo():
    print("info is added")
    GetProductInfo();
    dptmFileName = "Fruit.doc"
    AddProductInfo();
    Retrieve();
    headings = ("Image","Product","Price","Unit")
    return render_template("Fruit.html",headings = headings,data = data)

def GetProductInfo():
    global pimage,pname,pprice,punit;
    pimage = request.form.get('Selectimg');
    pname = request.form.get('txtproductname');
    pprice = request.form.get('txtproductprice');
    punit = request.form.get('txtunit');

def AddProductInfo():
    IfExist(dptmFileName);
    if(TorF == "false"):
        adminfile = open(dptmFileName,"x");
        adminfile.close();
    WriteInfo();

def WriteInfo():
    adminfile = open(dptmFileName,"r+")
    allInfo = adminfile.read();
    thelength = len(allInfo);
    if(thelength == 0):
        adminfile = open(dptmFileName,"w")
        adminfile.write(str(pimage) + ";" + str(pname) + ";" + str(pprice) + ";" + str(punit));
    else:
        adminfile = open(dptmFileName,"a")
        adminfile.write(";" + str(pimage) + ";" + str(pname) + ";" + str(pprice) + ";" + str(punit));
    adminfile.close()

def Retrieve():
    global data
    data = [];
    adminfile = open(dptmFileName,"r+")
    allInfo = adminfile.read().split(";");
    length = (len(allInfo)/4);
    num = 0
    
    for i in range(int(length)):
        theimage = allInfo[num]
        thename = allInfo[num+1]
        theprice = allInfo[num+2]
        theunit = allInfo[num+3]
        subdata = [];

        subdata.append(theimage)
        subdata.append(thename)
        subdata.append(theprice)
        subdata.append(theunit)

        num = num+4
        data.append(subdata)

@app.route("/adminhome")
def AdminHome():
    return render_template('DepartmentsAdmin.html')

@app.route("/poultry")
def poultry():
    global dptmFileName
    dptmFileName = "Poultry.doc"
    print("Welcome to poultry section")
    IfExist(dptmFileName);
    if(TorF == "false"):
        return render_template("poultry.html");
    else:
        adminfile = open(dptmFileName,"r+")
        allInfo = adminfile.read();
        thelength = len(allInfo);
        if(thelength == 0):
            return render_template("poultry.html");
        else:
            Retrieve();
            headings = ("Image","Product","Price","Unit")
            return render_template("poultry.html",headings = headings,data = data)
        
@app.route("/poultryinfo",methods=["POST"])
def GetpoultryInfo():
    print("info is added")
    GetProductInfo();
    dptmFileName = "Poultry.doc"
    AddProductInfo();
    Retrieve();
    headings = ("Image","Product","Price","Unit")
    return render_template("poultry.html",headings = headings,data = data)

@app.route("/meat")
def meat():
    global dptmFileName
    dptmFileName = "Meat.doc"
    print("Welcome to meat section")
    IfExist(dptmFileName);
    if(TorF == "false"):
        return render_template("Meat.html");
    else:
        adminfile = open(dptmFileName,"r+")
        allInfo = adminfile.read();
        thelength = len(allInfo);
        if(thelength == 0):
            return render_template("Meat.html");
        else:
            Retrieve();
            #Displayinfo();
            headings = ("Image","Product","Price","Unit")
            return render_template("Meat.html",headings = headings,data = data)
        
@app.route("/meatinfo",methods=["POST"])
def GetMeatInfo():
    print("info is added")
    GetProductInfo();
    dptmFileName = "Meat.doc"
    AddProductInfo();
    Retrieve();
    headings = ("Image","Product","Price","Unit")
    return render_template("Meat.html",headings = headings,data = data)

#####CONTROL USER DPTM HTMLS#####

@app.route("/Ufruit")
def userfruit():
    global dptmFileName
    dptmFileName = "Fruit.doc"
    print("Welcome to fruit section USER")
    IfExist(dptmFileName);
    if(TorF == "false"):
        return render_template("EmptyDepartment.html");
    else:
        adminfile = open(dptmFileName,"r+")
        allInfo = adminfile.read();
        thelength = len(allInfo);
        if(thelength == 0):
            return render_template("UserFruit.html");
        else:
            Retrieve();
            headings = ("Image","Product","Price","Unit")
            return render_template("UserFruit.html",headings = headings,data = data)

@app.route("/userhome")
def UserHome():
    return render_template('DepartmentsUser.html')

    
if __name__ == "__main__":
    app.run();
