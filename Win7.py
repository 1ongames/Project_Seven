import os
import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
import subprocess

class Windows7Mockup:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows 7")
        self.root.geometry("800x600")
        
        # 시작메뉴 열렸나요? - 기본값: 아니요
        self.start_menu = None
        
        # 배경 이미지 불러오기
        image_path = os.path.join(os.path.dirname(__file__), 'image', 'Win7_bg.jpg')
        self.set_background_image(image_path)
        
        # 작업 표시줄 만들고~
        self.create_taskbar()
        
        # 시작 버튼도 만들기
        self.create_start_button()
        
    def set_background_image(self, image_path):
        if not os.path.exists(image_path):
            print(f"파일을 찾지 못했습니다! 반드시 재설치하시길 바랍니다.: {image_path}")
            return
        
        self.canvas = tk.Canvas(self.root, width=800, height=560)  # Adjust height for taskbar
        self.canvas.pack(fill="both", expand=True)
        
        # image_path 불러오고
        self.bg_image = Image.open(image_path)
        
        # 이 사이즈에 맞게 수정하면
        self.bg_image = self.bg_image.resize((800, 560), Image.Resampling.LANCZOS)
        
        # Tkinter가 읽으라고 바꿔준 뒤에
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        
        # 배경 이미지 불러오기
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
  
    def create_taskbar(self):
        # Win7 Aero 작업표시줄은 구현 불가로 반투명 제거.
        taskbar_color = "#A7C1DC"
        self.taskbar = tk.Frame(self.root, bg=taskbar_color, height=40)
        self.taskbar.pack(side="bottom", fill="x")

    def create_start_button(self):
        start_button_image_path = os.path.join(os.path.dirname(__file__), 'image', '구현중이라 당분간 안떠요.png')
        if os.path.exists(start_button_image_path):
            try:
                start_button_image = Image.open(start_button_image_path)
                start_button_image = start_button_image.resize((40, 40), Image.Resampling.LANCZOS)
                self.start_button_image = ImageTk.PhotoImage(start_button_image)
                
                self.start_button = tk.Button(self.taskbar_frame, image=self.start_button_image, command=self.toggle_start_menu, borderwidth=0)
                self.start_button.pack(side="left", padx=5, pady=2)
            except Exception as e:
                print(f"시작 버튼을 정상적으로 구현하지 못했습니다! 0xc00000f02: {e}")
        else:
            print(f"파일을 찾을 수 없습니다!: {start_button_image_path}")
            self.start_button = tk.Button(self.taskbar_frame, text="시작", command=self.toggle_start_menu)
            self.start_button.pack(side="left", padx=5, pady=2)
        
    def toggle_start_menu(self):
        if self.start_menu is None or not tk.Toplevel.winfo_exists(self.start_menu):
            self.open_start_menu()
        else:
            self.close_start_menu()
    
    def open_start_menu(self):
        self.start_menu = tk.Toplevel(self.root)
        self.start_menu.title("시작 메뉴")
        self.start_menu.geometry("200x300")
        self.start_menu.protocol("WM_DELETE_WINDOW", self.close_start_menu)
        
        menu = Menu(self.start_menu)
        self.start_menu.config(menu=menu)
        
        file_menu = Menu(menu)
        menu.add_cascade(label="설정", menu=file_menu)
        file_menu.add_command(label="windows7")
        file_menu.add_command(label="windows7")
        
        shutdown_menu = Menu(menu)
        menu.add_cascade(label="전원", menu=shutdown_menu)
        shutdown_menu.add_command(label="로그아웃")
        shutdown_menu.add_command(label="다시 시작")
        shutdown_menu.add_command(label="시스템 종료", command=self.shutdown_system)
    
    def close_start_menu(self):
        if self.start_menu is not None:
            self.start_menu.destroy()
            self.start_menu = None
    
    def shutdown_system(self):
        # 시스템 종료 클릭하면 shut_down.py 실행
        script_path = os.path.join(os.path.dirname(__file__), 'shut_down.py')
        subprocess.Popen(["python", script_path], shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = Windows7Mockup(root)
    root.mainloop()
