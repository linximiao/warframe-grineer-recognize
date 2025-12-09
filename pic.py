import time
import os
from PIL import ImageGrab
import numpy as np

# 创建保存截图的文件夹
save_folder = "picture"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
t=0
time.sleep(5)
try:
    while True:
        # 获取屏幕分辨率
        screen = ImageGrab.grab()
        screen_width, screen_height = screen.size
        
        # 计算截取区域的坐标（屏幕中心）
        left = (screen_width - 640) // 2
        top = (screen_height - 640) // 2
        right = left + 640
        bottom = top + 640
        
        # 截取指定区域
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
        
        # 生成文件名（使用时间戳）
        filename = f"{t}.png"
        filepath = os.path.join(save_folder, filename)
        t+=1
        # 保存图片
        screenshot.save(filepath, "PNG")
        print(f"截图已保存: {filepath}")
        
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\n程序已停止")