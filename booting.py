import os
import time
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import subprocess

class BootScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Booting...")
        self.root.geometry("800x600")
        
        # GIF 로딩하기
        primary_image_path = os.path.join(os.path.dirname(__file__), 'image', 'Win7_booting.gif')
        fallback_image_path = os.path.join(os.path.dirname(__file__), 'image', 'Win7_boot_vista.gif')
        
        if os.path.exists(primary_image_path):
            self.load_gif(primary_image_path)
        elif os.path.exists(fallback_image_path):
            self.load_gif(fallback_image_path)
        else:
            self.show_error_message()
        
        # 10초 기다리고 부팅, 오류뜨면 블루스크린 -> 5초 후 종료
    
        self.root.after(10000, self.shutdown) if hasattr(self, 'frames') else self.root.after(5000, self.shutdown_with_error)

    def load_gif(self, gif_path):
        try:
            # GIF 로딩해주세요~
            gif = Image.open(gif_path)
            
            # 프레임 한장한장 로딩하게요~
            self.frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
            
            # 그리고 이 사이즈로 재생해줘요~
            self.canvas = tk.Canvas(self.root, width=800, height=600)
            self.canvas.pack(fill="both", expand=True)
            
            # GIF 로딩이 안되네요~
            self.show_frame(0)
        except Exception as e:
            print(f"Error loading GIF: {e}")
            self.show_error_message()

    def show_frame(self, frame_index):
        self.canvas.create_image(0, 0, anchor="nw", image=self.frames[frame_index])
        self.root.after(100, lambda: self.show_frame((frame_index + 1) % len(self.frames)))
        
        # 블1루스크린을 띄워서 큰2돈을 벌거야!
    def show_error_message(self):
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="#0000AA")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_text(400, 300, text="Windows 7을 부팅하지 못했습니다.\n오류 코드: 0xc00000f03", fill="#FFFFFF", font=("Helvetica", 16), justify="center")

    def shutdown(self):
        # 부팅했으니 난 죽어요 ㅇㅇ
        self.root.destroy()
        
        # 부팅 끗
        script_path = os.path.join(os.path.dirname(__file__), 'Win7.py')
        subprocess.Popen(["python", script_path], shell=True)

    def shutdown_with_error(self):
        # Windows 7 창 찾아서 종료
        try:
            subprocess.Popen(["taskkill", "/F", "/FI", 'WINDOWTITLE eq Windows 7'])
        except Exception as e:
            print(f"Windows7 시스템을 종료하는 도중에 오류 발생: 0xc00000f01 {e}")
        
        # 자1살
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BootScreen(root)
    root.mainloop()
