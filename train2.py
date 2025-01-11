import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    # model.load('yolo11n.pt') # 加载预训练权重,改进或者做对比实验时候不建议打开，因为用预训练模型整体精度没有很明显的提升
    model = YOLO(model=r'/root/ultralytics/ultralytics/cfg/models/11/yolo11.yaml')
    model.train(data=r'/root/ultralytics/ultralytics/cfg/datasets/coco128.yaml',
                imgsz=640,
                epochs=50,
                batch=4,
                workers=0,
                device='',
                close_mosaic=10,
                resume=False,
                project='runs/train',
                name='exp',
                single_cls=False,
                cache=False,
                )
