
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
    draw.save('01_01_classical_programming.png')

    # image 2
    figure, axis = draw.init()
    draw.title(axis, '1.1 从数据中学习规则')
    draw.subtitle(axis, '2. 机器学习')
    draw.text(axis, '机器学习将上述过程反过来，它通过观察输入数据和对应的回答，来理解规则是什么', index=0)
    draw.image(axis, 'res/deep_learning/machine_learning_paradigm.drawio.png', bottom=LARGE_OFFSET * 4)
    draw.save('01_02_machine_learning_paradigm.png')

    # image 3
    figure, axis = draw.init()
    draw.title(axis, '1.1 从数据中学习规则')
    draw.subtitle(axis, '3. 查看数据集')
    draw.save('01_03_flower_dataset.png')

    # image 4
    figure, axis = draw.init()
    draw.title(axis, '1.1 从数据中学习规则')
    draw.subtitle(axis, '4. 什么是机器学习')
    draw.save('01_04_what_is_machine_learning.png')
