# -*- coding: utf-8 -*-
# @File : tokenization.py
# @Time : 3/13/23 14:34
class MaximumMatchTokenizer:
    def __init__(self, dict_path):
        self.word_dict = set()
        self.maximum = 0  # 最大匹配长度
        with open(dict_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line:
                    continue
                self.word_dict.add(line.strip().split('\t')[0])
                if len(line.strip().split('\t')[0]) > self.maximum:
                    self.maximum = len(line.strip().split('\t')[0])

    def cut(self, text):
        words = []
        text_len = len(text)
        start_idx = 0
        while start_idx < text_len:
            end_idx = min(start_idx + self.maximum, text_len)
            while end_idx > start_idx:
                word = text[start_idx:end_idx]
                if word in self.word_dict:
                    break
                end_idx -= 1
            words.append(word)
            if end_idx == start_idx:
                start_idx = end_idx + 1
            else:
                start_idx = end_idx
        return words


class ReversedMaximumMatchTokenizer:
    def __init__(self, dict_path):
        self.word_dict = set()
        self.maximum = 0  # 最大匹配长度
        with open(dict_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line:
                    continue
                self.word_dict.add(line.strip().split('\t')[0])
                if len(line.strip().split('\t')[0]) > self.maximum:
                    self.maximum = len(line.strip().split('\t')[0])

    def cut(self, text):
        words = []
        text_len = len(text)
        start_idx = text_len - self.maximum
        end_index = text_len
        while start_idx > 0:
            start_idx = max(end_index - self.maximum, 0)
            while end_index > start_idx:
                word = text[start_idx:end_index]
                if word in self.word_dict:
                    break
                start_idx += 1
            words.append(word)
            if start_idx == end_index:
                end_index = start_idx - 1
            else:
                end_index = start_idx
        return words


def word_correct(reference, modul_output):
    """
    :param reference: 人工标注的序列
    :param modul_output: 模型输出的分词结果
    :return: num_correct: 正确分词的数量
    """
    ref_words = reference.split("/")  # 人工分词的结果

    # 计算机器正确分词数
    num_correct = 0
    for word in ref_words:
        if word in modul_output:
            num_correct += 1

    return num_correct


def word_recall(reference, num_correct):
    """
    :param num_correct: 成功分词数量
    :param reference: 人工标注的序列
    :return: 召回率R
    """
    ref_words = reference.split("/")  # 人工分词的结果

    # 计算人工正确分词的总词数
    num_total = len(ref_words)

    # 计算分词召回率
    recall = num_correct / num_total

    return recall


def word_precise(modul_output, num_correct):
    """
    :param modul_output: 模型输出序列
    :param num_correct: 机器正确分词数
    :return: 准确率
    """
    # 模型输出数量
    model_output_number = len(modul_output)

    precise = num_correct / model_output_number

    return precise


def max_match(text):
    """
    :param text: 要进行分词的文本
    :return 分词结果
    """
    tokenizer = MaximumMatchTokenizer('30wdict_utf8.txt')
    tokenized_list = tokenizer.cut(text)

    print(tokenized_list)

    return tokenized_list


def reversed_max_match(text):
    """
    :param text: 要进行分词的文本
    :return 分词结果
    """
    tokenizer = ReversedMaximumMatchTokenizer('30wdict_utf8.txt')
    tokenized_list = tokenizer.cut(text)

    print(tokenized_list[::-1])

    return tokenized_list[::-1]


def evaluate(text_manually_tokenized, text_output):
    num_correct = word_correct(text_manually_tokenized, text_output)

    r = word_recall(text_manually_tokenized, num_correct)
    p = word_precise(text_output, num_correct)

    print("R=", r)
    print("P=", p)
    print("F1=", (2 * p * r) / (p + r))


def main():
    text = "申奥成功，深得民意。办好奥运会，不仅是北京市民的一件大事，也是全中国人民的一件大事。申奥成功，我们已经付出很多辛劳和汗水；承办，还需要做更多扎扎实实的工作。比照举办奥运会的要求，我们还有许多差距，但我们有信心有能力博采众长，弥补不足。我们将信守承诺，认真细致地做好各项筹备工作，建设一流场馆，营造一流环境，提供一流服务；我们要在全社会继续加强社会主义精神文明建设，特别是要在北京市民中深入开展文明礼貌教育，树立良好道德风尚，强化法制意识，提高市民综合素质，展现时代精神风貌，在国际社会面前展示“新北京、新奥运”的魅力"

    text_manually_tokenized_sample = "申奥/成功/，/深得/民意/。/办好/奥运会/，/不仅/是/北京/市民/的/一/件/大事/，/也是/全/中国/人民/的/一件/大事/。/\
    申奥/成功/，/我们/已经/付出/很多/辛劳/和/汗水/；/承办/，/还/需要/做/更多/扎扎实实/的/工作/。/比照/举办/奥运会/的/要求/，/\
    我们/还有/许多/差距/，/但/我们/有/信心/有/能力/博采众长/，/弥补/不足/。/我们/将/信守承诺/，/认真/细致/地/做好/各项/筹备/工作/，/\
    建设/一流/场馆/，/营造/一流环境/，/提供/一流服务/；/我们/要/在/全/社会/继续/加强/社会主义/精神文明/建设/，/\
    特别/是/要/在/北京/市民/中/深入/开展/文明礼貌/教育/，/树立/良好/道德/风尚/，/强化/法制/意识/，/提高/市民/综合/素质/，/\
    展现/时代精神/风貌/，/在/国际社会/面前/展示/“/新/北京/、/新/奥运/”/的/魅力"

    print("正向最大匹配：")
    evaluate(text_manually_tokenized_sample, max_match(text))
    print("逆向最大匹配：")
    evaluate(text_manually_tokenized_sample, reversed_max_match(text))


if __name__ == "__main__":
    main()
