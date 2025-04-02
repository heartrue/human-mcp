import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Human MCP")

@mcp.tool()
def ask_human(ask) -> str:
    """
    询问人类以获取问题的答案，以下情况需要调用这个工具：
    当问题条件不足时
    有疑虑时
    有需要人类提供信息时
    """
    answer = None
    
    def submit():
        nonlocal answer
        answer = text.get("1.0", "end-1c")
        root.quit()
        root.destroy()
    
    root = tk.Tk()
    root.title("人类回答")
    root.geometry("400x300")
    
    # 显示问题
    label = ttk.Label(root, text=ask, wraplength=380)
    label.pack(pady=10)
    
    # 文本输入框
    text = tk.Text(root, height=10, width=40)
    text.pack(pady=10)
    
    # 提交按钮
    submit_btn = ttk.Button(root, text="回答", command=submit)
    submit_btn.pack(pady=10)
    
    root.mainloop()
    return answer if answer else ""

if __name__ == "__main__":
    mcp.run(transport='stdio')