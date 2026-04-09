import pyautogui
import time
import os
from colorama import Fore, init

init(autoreset=True)
os.system('chcp 65001 > nul')

def spam_messenger():
    print(Fore.CYAN + "=== TOOL SPAM MESSENGER (PHÍM GIẢ LẬP) ===")
    msg = input("nội dung cần spam: ")
    count = int(input("số lượng cần spam: "))
    delay = float(input("Giãn cách (giây) - Nên để > 0.5: "))

    print(Fore.YELLOW + "\n[!] Bạn có 5 giây để quay lại cửa sổ Messenger và click vào ô nhập tin nhắn...")
    time.sleep(5)

    for i in range(count):
        # Gõ nội dung
        pyautogui.write(msg)
        # Nhấn Enter để gửi
        pyautogui.press("enter")
        
        print(Fore.GREEN + f"[{i+1}] Đã gửi: {msg}")
        time.sleep(delay)

    print(Fore.CYAN + "\n=== XONG! ===")

if __name__ == "__main__":
    spam_messenger()
