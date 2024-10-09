from config import *
import draw

if __name__ == '__main__':
    # image 1
    figure, axis = draw.init()
    draw.headline(axis, '深度学习基础', y_pos=HEIGHT_4K * 2 / 3, font_properties=noto_sans_sc['ExtraBold'], fontsize=LARGE_SIZE + SMALL_SIZE)
    draw.save('00_00_headline.png')

    # image 2
    figure, axis = draw.init()
    draw.title(axis, '课程介绍')
    draw.subtitle(axis, '2. 为什么要学？')
    draw.text(axis, '2024 年诺贝尔物理学奖授予约翰·J·霍普菲尔德和杰弗里·E·辛顿，', index=0)
    draw.text(axis, '以表彰他们“通过人工神经网络实现机器学习的基础性发现和发明”。', index=1)
    draw.text(axis, '霍普菲尔德创造了一种可以存储和重建信息的结构。', index=3)
    draw.text(axis, '辛顿发明了一种可以独立发现数据属性的方法，这种方法对于目前使用的大型神经网络至关重要。', index=4)
    draw.text(axis, '基于人工神经网络的机器学习目前正在彻底改变科学、工程和日常生活。', index=5)
    draw.image_2_h_center(axis, 'res/deep_learning/artificial_neural_network.webp', 'res/deep_learning/physics_nobel_prize_2024.webp', bottom=LARGE_OFFSET, scale=1.5)
    draw.save('00_01_why_learn.png')

    # image 2
    figure, axis = draw.init()
    draw.title(axis, '课程介绍')
    draw.subtitle(axis, '1. 机器学习系列')
    draw.text(axis, '(1) 计算机：包含 Python 教程，数据结构与算法， 以及编程基础知识。', index=0)
    draw.text(axis, '(2) 数学：基础数学、微积分、线性代数、概率论、统计学等。', index=1)
    draw.text(axis, '(3) 机器学习：从理论到实践，拆解每个过程，熟练使用主流的机器学习库。', index=2)
    draw.text(axis, '(4) 前沿：探索最新的人工智能技术，包括底层原理实现。', index=3)
    draw.text(axis, '(1) 计算机：Python 教程 、计算机科学导论、数据结构与算法、C语言程序设计', index=5)
    draw.text(axis, '(2) 数学：初等数学 、微积分 第 1 卷 、微积分 第 2 卷 、线性代数 、统计学入门', index=6)
    draw.text(axis, '(3) 机器学习：深度学习基础 、PyTorch 详解 、CUDA 编程、机器学习编译器', index=7)
    draw.text(axis, '(4) 前沿：待定', index=8)
    draw.save('00_02_machine_learning_series.png')

    


    # image 3
    figure, axis = draw.init()
    draw.title(axis, '课程介绍')
    draw.subtitle(axis, '2.《深度学习基础》介绍')
    draw.save('00_02_deep_learning_series.png')
