import collections


def load_data(filepath):
    with open(filepath, encoding="utf8") as myfile:
        data = myfile.read().replace('\n', '')
    return data


def get_most_frequent_words(text):
    length = len(text)
    i = 0
    word = ""
    all_words = []
    while i < length:
        if str(text[i]).isalpha():
            word += text[i]
        else:
            all_words.append(word)
            word = ""
        i += 1
    all_words.append(word)
    c = collections.Counter()
    for word in all_words:
        c[word] += 1
    return c.most_common(10)


if __name__ == '__main__':
    print(get_most_frequent_words("load_data("file.txt")"))
