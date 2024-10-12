from config import *
import draw

if __name__ == '__main__':
    # cover
    figure, axis = draw.init()
    draw.headline(axis, '深度学习基础', x_pos = WIDTH_4K / 4, y_pos=HEIGHT_4K * 2 / 3, font_properties=noto_sans_sc['ExtraBold'], fontsize=LARGE_SIZE + SMALL_SIZE)
    draw.headline(axis, '适合新手入门的人工智能课程', x_pos=WIDTH_4K / 2, y_pos=HEIGHT_4K / 3, font_properties=noto_sans_sc['Medium'], fontsize=LARGE_SIZE)
    draw.text_h_center(axis, '@machine_learning_series', bottom=ULTRA_OFFSET, font_size=MEDIUM_SIZE + TINY_SIZE)
    draw.image_center(axis, 'res/deep_learning/networkx_sample.png', pos_x=WIDTH_4K * 3 / 4, pos_y=HEIGHT_4K * 2 / 3)
    draw.save('00_00_cover.png')

    # image 1
    figure, axis = draw.init()
    draw.title(axis, '前言-课程介绍')
    draw.subtitle(axis, '1. 为什么要学？')
    draw.text(axis, '2024 年诺贝尔物理学奖授予约翰·J·霍普菲尔德和杰弗里·E·辛顿，', index=0)
    draw.text(axis, '以表彰他们“通过人工神经网络实现机器学习的基础性发现和发明”。', index=1)
    draw.text(axis, '霍普菲尔德创造了一种可以存储和重建信息的结构。', index=3)
    draw.text(axis, '辛顿发明了一种可以独立发现数据属性的方法，这种方法对于目前使用的大型神经网络至关重要。', index=4)
    draw.text(axis, '基于人工神经网络的机器学习目前正在彻底改变科学、工程和日常生活。', index=5)
    draw.image_2_h_center(axis, 'res/deep_learning/artificial_neural_network.webp', 'res/deep_learning/physics_nobel_prize_2024.webp', bottom=LARGE_OFFSET, scale=1.5)
    draw.save('00_01_why_learn_1.png')

    # image 2
    figure, axis = draw.init()
    draw.title(axis, '前言-课程介绍')
    draw.subtitle(axis, '1. 为什么要学？')
    draw.text(axis, '(1) AlphaGo 掌握了古老的围棋游戏，击败了围棋世界冠军，并开启了人工智能系统的新时代。', index=1)
    draw.text(axis, '(2) AlphaFold 揭示了数百万种复杂的 3D 蛋白质结构，并帮助科学家了解生命分子如何相互作用。', index=3)
    draw.text(axis, '(3) Telsa FSD 自动驾驶系统，旨在实现车辆从起点到目的地的全程自主驾驶。', index=5)
    draw.text(axis, '(4) Github Copilot 全球最广泛采用的人工智能开发工具。', index=7)
    draw.text(axis, '(5) ChatGPT 能够理解并生成自然语言，用于回答问题、提供建议和进行互动交流。', index=9)
    draw.text(axis, '(6) Apple Intelligence 帮助用户轻松书写、表达自我和完成工作。', index=11)
    draw.text(axis, '(7) Midjourney 根据用户的文本描述生成高度创意的艺术作品和视觉图像。', index=13)
    draw.save('00_01_why_learn_2.png')

    # image 3
    figure, axis = draw.init()
    draw.title(axis, '前言-课程介绍')
    draw.subtitle(axis, '1. 为什么要学？')
    draw.text(axis, 'AlphaFold', index=0)
    draw.save('00_01_why_learn_3.png')

    # image 4
    figure, axis = draw.init()
    draw.title(axis, '前言-课程介绍')
    draw.subtitle(axis, '1. 为什么要学？')
    draw.text(axis, 'Tesla FSD', index=0)
    draw.save('00_01_why_learn_4.png')

    # image 5
    figure, axis = draw.init()
    draw.title(axis, '前言-课程介绍')
    draw.subtitle(axis, '1. 为什么要学？')
    draw.text(axis, 'ChatGPT', index=0)
    draw.save('00_01_why_learn_5.png')

    # image 3
    figure, axis = draw.init()
    draw.title(axis, '前言-课程介绍')
    draw.subtitle(axis, '2. 机器学习系列')
    draw.text(axis, '(1) 计算机：包含 Python 教程，数据结构与算法， 以及编程基础知识。', index=0)
    draw.text(axis, '(2) 数学：基础数学、微积分、线性代数、概率论、统计学等。', index=1)
    draw.text(axis, '(3) 机器学习：从理论到实践，拆解每个过程，熟练使用主流的机器学习库。', index=2)
    draw.text(axis, '(4) 前沿：探索最新的人工智能技术，包括底层原理实现。', index=3)
    draw.text(axis, '(1) 计算机：Python 教程 、计算机科学导论、数据结构与算法、C语言程序设计', index=5)
    draw.text(axis, '(2) 数学：初等数学 、微积分 第 1 卷 、微积分 第 2 卷 、线性代数 、统计学入门', index=6)
    draw.text(axis, '(3) 机器学习：深度学习基础 、PyTorch 详解 、CUDA 编程、机器学习编译器', index=7)
    draw.text(axis, '(4) 前沿：待定', index=8)
    draw.save('00_02_machine_learning_series.png')

    # image 4
    figure, axis = draw.init()
    draw.title(axis, '前言-课程介绍')
    draw.subtitle(axis, '3.《深度学习基础》介绍')
    draw.text(axis, '《深度学习基础》(Fundamentals of Deep Learning) 是机器学习的入门课程，许多教程都是从', index=0)
    draw.text(axis, 'MNIST 数据集开始，对于初学者，特别是数学和编程基础不牢固的读者来说，难度仍然比较大。', index=1)
    draw.text(axis, '(1) 为了充分理解神经网络，比如为什么要引入梯度这些复杂的概念，网络从零维的数字开始讲起，', index=3)
    draw.text(axis, '然后将其拓展到二维的坐标系中，其中的每个过程都能可视化。', index=4)
    draw.text(axis, '(2) 通过介绍 TensorFlow 中张量、自动微分、模型等概念，讲述市场上机器学习主流库的基本要素，', index=6)
    draw.text(axis, '充分理解神经网络的基础概念，从而能够轻易地切换到其它机器学习库中。', index=7)
    draw.text(axis, '(3) 分别使用 TensorFlow, NumPy, PyTorch, JAX 实现 MNIST 数据集的训练，掌握这些机器学习库', index=9)
    draw.text(axis, '的入门知识。最后手写 micrograd 库结尾，为进阶学习做好充分的准备。', index=10)
    draw.save('00_03_deep_learning_introduction_1.png')

    # image 5
    figure, axis = draw.init()
    draw.title(axis, '前言-课程介绍')
    draw.subtitle(axis, '3.《深度学习基础》介绍')
    draw.text(axis, 'MNIST 手写数据集包含 60000 个训练样本，10000 个测试样本', index=0)
    draw.text(axis, '美国国家标准技术研究所 (National Institute of Standards and Technology)', index=1)
    draw.image_h_center(axis, 'res/deep_learning/mnist_dataset.png', bottom=MEDIUM_OFFSET, scale=1.5)
    draw.save('00_03_deep_learning_introduction_2.png')
