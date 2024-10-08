
import matplotlib.pyplot as pyplot
from config import *
import draw

if __name__ == '__main__':
    # image 1
    figure, axis = draw.init()
    draw.title(axis, '1.1 从数据中学习规则')
    draw.subtitle(axis, '1. 传统编程')
    draw.text(axis, '传统编程三要素：规则 (Rule)、数据 (Data)、答案 (Answer)', index=0)
    draw.text(axis, '举例：确认一个人是否符合银行贷款需求？', index=2)
    draw.text(axis, '规则：年龄在 18 - 65 岁之间，年收入 3 万元，才能够进行贷款', index=3)
    draw.text(axis, '数据：年龄 30 岁，年收入 10 万元', index=4)
    draw.text(axis, '答案：可以贷款', index=5)
    draw.code(axis, 'def check_loan_eligibility(age, income):', index=7)
    draw.code(axis, "    if age < 18 or age > 65: return 'NO'", index=8)
    draw.code(axis, "    if income < 30000: return 'NO'", index=9)
    draw.code(axis, "    return 'YES'", index=10)
    draw.text(axis, "优点：简单、高效、明确", index=12)
    draw.text(axis, "缺点：处理复杂数据集困难，比如识别照片中的花", index=13)
    draw.image_v_center(axis, 'res/deep_learning/flower_tatarian_aster.jpg', left=LARGE_OFFSET * 23, scale=1.5)
    draw.save('01_01_classical_programming.png')

    # image 2
    figure, axis = draw.init()
    draw.title(axis, '1.1 从数据中学习规则')
    draw.subtitle(axis, '2. 机器学习')
    draw.text(axis, '机器学习将上述过程反过来，它通过观察输入数据和对应的回答，来理解规则是什么', index=0)
    draw.image_h_center(axis, 'res/deep_learning/machine_learning_paradigm.drawio.png', bottom=LARGE_OFFSET * 4)
    draw.save('01_02_machine_learning_paradigm.png')

    # image 3
    figure, axis = draw.init()
    draw.title(axis, '1.1 从数据中学习规则')
    draw.subtitle(axis, '3. 查看数据集')
    draw.text(axis, '包含几千张花卉的照片以及它们对应的名称（雏菊、玫瑰、向日葵、蒲公英、郁金香）', index=0)
    draw.text(axis, '传统编程很难通过编写规则的方式识别图片中的菊花（图1和图3）', index=1)
    draw.text(axis, '使用机器学习非常容易，通过学习非常多的示例，得到规则从而能对花卉照片进行精确分类', index=2)
    draw.image_h_center(axis, 'res/deep_learning/flower_dataset.jpg', bottom=LARGE_OFFSET * 2, scale=2)
    draw.save('01_03_flower_dataset.png')

    # image 4
    figure, axis = draw.init()
    draw.title(axis, '1.1 从数据中学习规则')
    draw.subtitle(axis, '4. 什么是机器学习')
    draw.text(axis, '机器学习是人工智能的子领域，通过观察数据对模型进行训练，从而能够做出决策', index=0)
    draw.text(axis, '这个领域已经爆发式增长，现在几乎是 AI 的代名词', index=1)
    draw.text(axis, '深度学习 (Deep Learning) 是机器学习的一个分支', index=2)
    draw.image_by_offset(axis, 'res/deep_learning/ai_ml_dp.drawio.png', left = LEFT_OFFSET * 12, bottom=LARGE_OFFSET * 2, scale=0.8)
    draw.save('01_04_what_is_machine_learning_1.png')

    # image 5
    figure, axis = draw.init()
    draw.title(axis, '1.1 从数据中学习规则')
    draw.subtitle(axis, '4. 什么是机器学习')
    draw.text(axis, '机器学习通过给定示例数据，在处理数据过程中发现规则，那么机器学习需要三点东西：', index=0)
    draw.text(axis, '(1) 输入数据 (Input Data)：比如语音识别任务，数据可以是人们说话的声音文件', index=1)
    draw.text(axis, '图像打标签任务，输入就是图片和对应的标签', index=2)
    draw.text(axis, '(2) 期望输出 (Expected Output)：在语音识别任务中，输出可以是识别的文本', index=3)
    draw.text(axis, '在图像识别任务中，输出可以是猫、狗、花等标签', index=4)
    draw.text(axis, '(3) 测量算法好坏的手段 (Measure)：计算系统当前的输出和期望输出的距离，测量手段是非常有必要的', index=5)
    draw.text(axis, '测量的结果将作为反馈信号去调整算法的工作，这个调整步骤通常称之为学习 (Learning)', index=6)
    draw.text(axis, '因此机器学习的核心问题就是有用的数据转换 (Data Transform)：', index=8)
    draw.text(axis, '学习输入数据有用的表示 (Representation) ，这种表示可以更接近得到期望输出。', index=9)
    draw.save('01_04_what_is_machine_learning_2.png')

    # image 6
    figure, axis = draw.init()
    draw.title(axis, '1.1 从数据中学习规则')
    draw.subtitle(axis, '4. 什么是机器学习')
    draw.save('01_04_what_is_machine_learning_3.png')
