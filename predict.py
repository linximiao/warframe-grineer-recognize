import cv2
from ultralytics import YOLO
import dxcam
import torch
from pynput.mouse import Controller

model = YOLO('best.pt')
# model.export(format='onnx', dynamic=True, simplify=True)
# model = onnx.load('yolo11s.onnx')
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)
camera = dxcam.create(region=(960, 400, 1600, 1040))
mouse = Controller()

while True:
    screen = camera.grab()
    if screen is None:
        continue
    results = model.predict(screen, conf = 0.5)

    center = []
    for result in results:
        for box in result.boxes:
            x,y,w,h = box.xywh.tolist()[0]
            center.append((x,y))
            #print(f'中心：({x:.2f}，{y:.2f}), 类别：{model.names[int(box.cls)]}, 置信度：{box.conf[0]:.3f}')

    frame = results[0].plot()
    cv2.imshow('Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # if len(aims):
    #     min_dis = 100000
    #     target_x = 960
    #     target_y = 540
    #     for a, b in aims:
    #         dis = a + b - mid_screen
    #         if dis < min_dis:
    #             target_x = a
    #             target_y = b
    #             min_dis = dis
                
    #     aims = []
    #     # 移动鼠标
    #     mouse.position = (target_x, target_y)

camera.stop()  # 停止捕获
cv2.destroyAllWindows() 
# cv2.waitKey(0)
# cv2.destroyAllWindows()