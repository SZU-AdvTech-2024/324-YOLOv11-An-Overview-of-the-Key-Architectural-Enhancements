# YOLOv11 加入注意力机制的复现与结果

本项目基于 YOLOv11 模型进行复现，并通过引入注意力机制对其性能进行了改进。模型在复杂场景和小目标检测中表现出色，实验表明注意力机制显著提升了检测性能。

## 特性与改进点

1. **YOLOv11 基线模型**：使用 YOLOv11 原始架构作为对比基线。

2. **注意力机制的引入**：加入了创新的 **C2PSA**（并行空间注意力模块），增强了模型的特征提取和目标定位能力，特别是在复杂场景和密集环境中表现突出。

3. 结果改进

   ：

   - 精度从 **0.782** 提升至 **0.868**，如精度-置信度曲线所示。
   - 提高了模型在低光环境、小目标检测和复杂背景中的鲁棒性。
   - 降低了训练和验证损失，并加速了模型的收敛速度。

4. **数据集支持**：模型在 COCO 数据集上进行了训练和验证，支持自定义的训练和验证集。

## 数据集结构

数据集支持以下两种文件结构：

- 方式一

  ：

  ```
  kotlin复制代码dataset/
  ├── images/
  │   ├── train/
  │   └── val/
  └── labels/
      ├── train/
      └── val/
  ```

- 方式二

  ：

  ```
  kotlin复制代码dataset/
  ├── train/
  │   ├── images/
  │   └── labels/
  └── val/
      ├── images/
      └── labels/
  ```

请根据实际情况选择合适的结构，并确保路径配置正确。

## 环境要求

代码使用 Python 实现，依赖以下环境：

- Python >= 3.8

- PyTorch >= 1.10

- CUDA >= 11.8

- 所需的 Python 库：

  ```
  bash
  
  
  复制代码
  pip install torch torchvision torchaudio opencv-python pillow matplotlib tqdm
  ```

## 本地文件准备与安装

1. 将本地的代码文件解压到指定文件夹，例如：

   ```
   kotlin复制代码yolov11-attention/
   ├── train.py
   ├── val.py
   ├── data.yaml
   ├── yolov11.yaml
   ├── utils/
   └── runs/
   ```

   确保代码文件夹中包含训练和验证所需的 `train.py` 和 `val.py` 文件，以及模型配置文件 `yolov11.yaml` 和数据配置文件 `data.yaml`。

2. 创建虚拟环境并安装依赖：

   ```
   bash复制代码conda create -n yolov11 python=3.8 -y
   conda activate yolov11
   pip install -r requirements.txt
   ```

3. 准备数据集并按照上述结构组织文件。

## 模型训练

在您的数据集上训练模型：

1. 修改 `data.yaml` 配置文件，添加数据集路径和类别信息。

2. 运行训练脚本：

   ```
   bash
   
   
   复制代码
   python train.py --img 640 --batch 16 --epochs 50 --data data.yaml --cfg yolov11.yaml --weights '' --device 0
   ```

   - `--weights ''` 表示从头开始训练。如需使用预训练权重进行微调，请指定权重路径。
   - 根据您的 GPU 配置调整 `--img` 和 `--batch` 参数。

## 模型验证

在验证集上评估模型性能：

```
bash


复制代码
python val.py --data data.yaml --weights runs/train/exp15_coco/weights/best.pt --img 640 --device 0
```

## 结果可视化

### 精度-置信度曲线

以下曲线展示了引入注意力机制后，模型精度与置信度的关系：



![P_curve](C:\Users\谢\Desktop\ultralytics\ultralytics\runs\train\exp15_coco\P_curve.png)

## 关键改进点

1. 损失下降

   ：

   - 训练和验证损失（如 box loss 和 classification loss）下降更加平稳，且收敛速度更快。

2. 小目标检测

   ：

   - 小目标的边界框更准确，漏检和误检现象显著减少。

3. 精度提升

   ：

   - 精度从 **0.782** 提升到 **0.868**，性能表现显著优化。

4. 复杂场景适应能力

   ：

   - 在密集目标和复杂背景的场景中表现更优，检测结果更为稳定。

## 未来改进方向

- 优化注意力机制的计算效率，进一步降低计算开销。
- 测试更多数据集，以验证模型的通用性。
- 探索更先进的损失函数以提升极端场景下的性能。