---
title: CV算法学习路径
date: 2026-01-06 01:00:27
tags: [算法, CV ,机器学习，深度学习，图像识别，目录]
categories: 学习路径
---
# 学习路径
## 1. 🔢 图像处理基础 (Image Processing)
在碰深度学习之前，你必须知道计算机是如何“看”信号的。

核心概念： 像素、通道（RGB/HSV）、灰度化、直方图。

空间域处理： 卷积核 (Kernel) 的数学定义、平滑（高斯滤波）、锐化、边缘检测（Sobel/Canny）。

几何变换： 仿射变换、缩放、旋转（理解矩阵运算）。

学习建议： 结合 Python 的 OpenCV 库，把上述每一个操作都动手实现一遍。

## 2. ⚡ 特征工程与传统算法 (Classical CV)
虽然现在是深度学习时代，但面试常考传统方法来检测你的基本功。

核心概念： 特征点检测（SIFT, SURF, ORB）、HOG 特征。

经典任务： 图像拼接、全景图生成（理解 RANSAC 算法）。

## 3. 🧠 深度学习基础与 CNN (Deep Learning & CNN)
这是面试的重灾区。

数学功底： 反向传播 (Backpropagation) 的链式法则、损失函数 (Loss Functions)。

CNN 组件： 卷积层（步长 Stride、填充 Padding）、池化 (Pooling)、批归一化 (Batch Normalization)、激活函数 (ReLU, Sigmoid)。

经典架构： 理解从 AlexNet 到 VGG，再到 ResNet（残差网络） 的演变逻辑。


Shutterstock
## 4. 🛠️ 三大实战领域 (Practical Applications)
根据你想投递的岗位，深入学习以下一到两个方向：

目标检测： 理解 Anchor-based (Faster R-CNN) vs Anchor-free (YOLO系列) 的区别。

语义分割： 理解 FCN 和 U-Net 的跳跃连接 (Skip Connection) 结构。

Transformer in CV： 学习 ViT (Vision Transformer) 如何将图像切块处理。

