import os
import time
import tkinter as tk
from PIL import Image, ImageTk
import pygame
import subprocess
import signal
import pygetwindow as gw

def shutdown():
    # 배경 이미지를 설정할 Tkinter 창 생성
    root = tk.Tk()
    root.title("Shutdown")
    root.geometry("800x600")
    
    # 이미지 경로 설정
    image_path = os.path.join(os.path.dirname(__file__), 'image', 'Win7_shutdown.jpg')
    
    try:
        # 배경 이미지 로드 및 설정
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"파일을 찾지 못했습니다! 반드시 재설치하시길 바랍니다.: {image_path}")
        
        canvas = tk.Canvas(root, width=800, height=600)
        canvas.pack(fill="both", expand=True)
        
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)
        
        canvas.create_image(0, 0, anchor="nw", image=bg_image)
    
    except FileNotFoundError as e:
        print(e)
        root.destroy()
        return

    # 창을 즉시 표시
    root.update()
    
    # 소리 재생
    sound_path = os.path.join(os.path.dirname(__file__), 'sound', 'Win7_shutdown.mp3')
    try:
        if not os.path.exists(sound_path):
            raise FileNotFoundError(f"파일을 찾지 못했습니다! 반드시 재설치하시길 바랍니다.: {sound_path}")
        
        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
    
    except FileNotFoundError as e:
        print(e)
        pygame.quit()
        root.destroy()
        return

    # 3초 대기
    time.sleep(3)
    
    # Tkinter 창 닫기
    root.destroy()
    
    # "Windows 7" 창 닫기
    close_windows_7_window()

def close_windows_7_window():
    try:
        windows = gw.getWindowsWithTitle("Windows 7")
        for window in windows:
            window.close()
    except Exception as e:
        print(f"Windows7 시스템을 종료하는 도중에 오류 발생: 0xc00000f01 {e}")

if __name__ == "__main__":
    shutdown()
