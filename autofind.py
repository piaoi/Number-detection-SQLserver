'''
Author: 木白广木林
Date: 2024-05-18 09:02:09
LastEditTime: 2024-05-18 09:04:07
LastEditors: 木白广木林
Description: None
FilePath: \Desktop\db-SQLserver-autofind.py
检查自己的代码是非常愚蠢的行为，这是对本身实力的不信任。
'''
import tkinter as tk

def on_key_release(event):
    # 获取文本框中的输入内容
    input_text = entry.get()
    # 检查输入长度是否达到10个字符
    if len(input_text) >= 10:
        print("输入长度达到或超过10个字符，清空输入框。")
        # 清空输入框
        entry.delete(0, tk.END)

# 创建主窗口
root = tk.Tk()
root.title("清空输入框示例")

# 创建一个文本框，允许用户输入文本
entry = tk.Entry(root, width=50)
entry.pack(pady=20)

# 绑定键盘释放事件到on_key_release函数
entry.bind('<KeyRelease>', on_key_release)

# 启动事件循环
root.mainloop()