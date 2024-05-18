'''
Author: 木白广木林
Date: 2024-05-18 08:19:40
LastEditTime: 2024-05-18 08:59:00
LastEditors: 木白广木林
Description: None
FilePath: \Desktop\db-SQLserver.py
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
    root = tk.Tk()
    root.title("序列号查询软件")

    label = tk.Label(root, text="手动输入序列号并查重写入数据库")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="写入序列号", command=lambda: insert_serial(entry))
    button.pack()

    root.mainloop()

# 主程序
if __name__ == "__main__":
    create_ui()

# 关闭数据库连接
cursor.close()
conn.close()