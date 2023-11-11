from random import randint
c = 0

with open('Generation-П.txt', encoding='utf-8') as text_lit:
    number_of_sentence = int(text_lit.readline())
    dict_of_words = {}

    for line in text_lit:
        text_str = line 
        text_str = text_str.replace('', '')
        sentence_list = text_str.split()

        if c > 0:
            if sentence_list != [] and prev_sentence != []:
                if prev_sentence[-1] in dict_of_words.keys():
                    dict_of_words[prev_sentence[-1]].append(sentence_list[0])
                else:
                    dict_of_words[prev_sentence[-1]] = [sentence_list[0]]

        for index in range(len(sentence_list) - 1):
            if sentence_list[index] != '-':
                if sentence_list[index] in dict_of_words.keys():
                    dict_of_words[sentence_list[index]].append(sentence_list[index + 1])
                else:
                    dict_of_words[sentence_list[index]] = [sentence_list[index + 1]]
        c += 1
        prev_sentence = sentence_list

for sent in range(number_of_sentence):
    word = list(dict_of_words.keys())[randint(0, len(dict_of_words.keys()))]
    print(word[0].upper() + word[1:], end= ' ')

    while word[-1] not in ['.', '!', '?']:
        word = dict_of_words[word][randint(0, len(dict_of_words[word])) - 1]
        print(word, end=' ')
    