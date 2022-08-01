import tkinter
from tkinter import *
import paramiko
from tkinter import messagebox
import re

class Application():
    def __init__(self,master):
        self.var_1 = StringVar()  # DgroupId
        self.var_2 = StringVar()  # DartifactId
        self.var_3 = StringVar()  # Dversion
        self.var_4 = StringVar()  # pom | jar
        self.var_4.set("jar")
        self.var_5 = StringVar()  # Dfile
        self.var_6 = StringVar()  # Durl
        self.var_7 = StringVar()  # DrepositoryId
        self.var_7.set("repo.murongtech.com")
        self.var_8 = StringVar() # XML文件路径
        self.master = master
        self.create_module()
        self.master.mainloop()
    def create_module(self):

        Label(master=self.master,text="MAVEN一键上传",font=("微软雅黑",15)).place(x="150",y="0")
        Label(master=self.master,text="日志输出",font=("微软雅黑",15)).place(x="650",y="0")
        Label(master=self.master,text="DgroupId:").place(x="0",y="30")
        Entry(master=self.master,width="50",textvariable=self.var_1).place(x="80",y="30")
        Label(master=self.master,text="DartifactId:").place(y="60",x="0")
        Entry(master=self.master,width="50",textvariable=self.var_2).place(y="60",x="80")
        Label(master=self.master,text="Dversion:").place(x="0",y="90")
        Entry(master=self.master,textvariable=self.var_3,width="50").place(y="90",x="80")
        Radiobutton(master=self.master,text="jar",value="jar",variable=self.var_4).place(y="120",x="90")
        Radiobutton(master=self.master, text="pom",value="pom",variable=self.var_4).place(y="120", x="200")
        Label(master=self.master,text="上传类型:").place(x="0",y="120")
        Label(master=self.master,text="Dfile:").place(x="0",y="150")
        Entry(master=self.master,width="50",textvariable=self.var_5).place(y="150",x="80")
        Label(master=self.master,text="Durl:").place(x="0",y="180")
        Entry(master=self.master,width="50",textvariable=self.var_6).place(y="180",x="80")
        Label(master=self.master,text="DrepositoryId:").place(x="0",y="210")
        Entry(master=self.master,width="50",textvariable=self.var_7).place(x="90",y="210")
        Label(master=self.master,text="XML文件路径:").place(x="0",y="240")
        Entry(master=self.master,width="50",textvariable=self.var_8).place(x="90",y="240")
        Button(master=self.master,activebackground="green",
               width="30",text="开始上传",command=self.start).place(x="130",y="270")
        Button(master=self.master,text="清空",command=self.clean_button).place(x="80",y="270")
        self.text1 = Text(master=self.master,width="70",height="35")
        self.text1.place(x="450",y="30")
    def clean_button(self):
        self.var_1.set("")
        self.var_2.set("")
        self.var_3.set("")
        self.var_5.set("")
        self.var_6.set("")
        self.var_8.set("")
    def start(self):
        self.text1.delete(1.0, END)
        Client = paramiko.SSHClient()
        Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        Client.connect(hostname="182.188.4.50",username="root",password="1234qwer",timeout=5)
        exec_cmd = '''
        /bin/bash --login -c "mvn deploy:deploy-file -DgroupId={0} -DartifactId={1} -Dversion={2} -Dpackaging={3} -Dfile={4} -Durl={5} -DrepositoryId={6} -s {7}"
        '''.format(self.var_1.get(), self.var_2.get(), self.var_3.get(),
                   self.var_4.get(), self.var_5.get(), self.var_6.get(),
                   self.var_7.get(), self.var_8.get())
        stdin,stdout,stderr = Client.exec_command(exec_cmd)
        out = stdout.read().decode()
        result = re.search("BUILD SUCCESS", out)
        if result == None:
            messagebox.showinfo(title="执行错误",message="执行错误,请查看日志")
            self.text1.insert("insert", out )
        else:
            messagebox.showinfo(title="上传成功", message="上传成功!!")
            self.text1.insert("insert", out)
if __name__ == "__main__":
    root = Tk()
    root.title("maven小工具")
    root.geometry("1000x500+300+150")
    a = Application(master=root)