
'''
Author: 木白广木林
Date: 2024-05-18 08:19:40
LastEditTime: 2024-05-18 09:32:30
LastEditors: 木白广木林
Description: None
FilePath: \Desktop\db-SQLserver copy.py
检查自己的代码是非常愚蠢的行为，这是对本身实力的不信任。
'''
import sys
import pyodbc
import tkinter as tk
from tkinter import messagebox

# 连接SQL Server数据库
# conn = pyodbc.connect('DRIVER={SQL Server};SERVER=Your_Server_Name;DATABASE=Your_Database_Name;UID=Your_Username;PWD=Your_Password')
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-FCCVVU8;DATABASE=db;UID=sa;PWD=root')
cursor = conn.cursor()

# def showMessage(message, type='info', timeout=2500):
#     import tkinter as tk
#     from tkinter import messagebox
 
#     root = tk.Tk()
#     root.withdraw()
#     try:
#         root.after(timeout, root.destroy)
#         if type == 'info':
#             messagebox.showinfo('Info', message, master=root)
#         elif type == 'warning':
#             messagebox.showwarning('Warning', message, master=root)
#         elif type == 'error':
#             messagebox.showerror('Error', message, master=root)
#     except:
#         pass
 
# showMessage("Hello, world", timeout=1000)

# 查询数据库中是否已存在序列号
def check_duplicate(serial):
    cursor.execute("SELECT * FROM number WHERE numbers = ?", (serial,))
    if cursor.fetchall():
        return True
    else:
        return False

# 写入数据到数据库
def insert_serial(entry):
    serial = entry.get()
    if len(serial) != 6:
        messagebox.showerror("错误", "序列号长度必须为6位")
    elif check_duplicate(serial):
        messagebox.showinfo("提示", f"序列号 {serial} 已存在，不重复写入数据库")
    else:
        cursor.execute("INSERT INTO number (numbers) VALUES (?)", (serial,))
        conn.commit()
        messagebox.showinfo("提示", f"序列号 {serial} 已成功写入数据库")
        

# 创建UI界面
def create_ui():

    def on_key_release(event):
        # 获取文本框中的输入内容
        input_text = entry.get()
        # 检查输入长度是否达到6个字符
        if len(input_text) >= 6:
            insert_serial(entry)
            print("输入长度达到6个字符，写入数据。")
            # 清空输入框
            entry.delete(0, tk.END)
            

    root = tk.Tk()
    root.title("序列号查询软件")

    label = tk.Label(root, text="手动输入序列号并查重写入数据库")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    # 绑定键盘释放事件到on_key_release函数
    entry.bind('<KeyRelease>', on_key_release)

    button = tk.Button(root, text="写入序列号", command=lambda: insert_serial(entry))
    button.pack()

    root.mainloop()

# 主程序
if __name__ == "__main__":
    create_ui()

# 关闭数据库连接
cursor.close()
conn.close()