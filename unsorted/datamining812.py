# -*- coding: utf-8 -*-
# @File : datamining8.py
# @Time : 6/14/23 20:34
import matplotlib.pyplot as plt


def computeTandF(data_tuples):
    # 用于绘制曲线的数组
    fpr_list = []
    tpr_list = []
    # 定义正例和负例的数量
    num_pos = sum([1 for tpl in data_tuples if tpl[1] == 'p'])
    num_neg = len(data_tuples) - num_pos

    # 定义TP、FP、TN和FN的初始值
    tp, fp, tn, fn = 0, 0, num_pos, num_neg
    t, f = 0, len(data_tuples)

    # 遍历每个数据元组
    for tpl in sorted(data_tuples, key=lambda x: x[2], reverse=True):
        t += 1
        f -= 1
        if tpl[1] == 'p':  # 如果当前元组是正例
            tp += 1
            fn -= 1
        else:  # 如果当前元组是负例
            fp += 1
            tn -= 1

        # 计算TPR和FPR
        tpr = tp / num_pos
        fpr = fp / num_neg
        tpr_list.append(tpr)
        fpr_list.append(fpr)
        # 输出当前元组的结果
        print(f"Tuple# {tpl[0]}: TP={tp}, FP={fp}, TN={tn}, FN={fn}, TPR={tpr:.2f}, FPR={fpr:.2f}")
    return tpr_list, fpr_list


def drawROC(tpr, fpr):
    plt.plot(fpr, tpr)
    plt.title('ROC Curve')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.show()


def main():
    fpr_list = []
    tpr_list = []
    # 定义数据元组
    data_tuples = [
        (1, 'p', 0.95),
        (2, 'n', 0.85),
        (3, 'p', 0.78),
        (4, 'p', 0.66),
        (5, 'n', 0.60),
        (6, 'p', 0.55),
        (7, 'n', 0.53),
        (8, 'n', 0.52),
        (9, 'n', 0.51),
        (10, 'p', 0.4)
    ]
    tpr_list, fpr_list = computeTandF(data_tuples)
    drawROC(tpr_list, fpr_list)


if __name__ == "__main__":
    main()
