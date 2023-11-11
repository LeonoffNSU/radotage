with open('Generation-П.txt', encoding='utf-8') as text_lit:
    text_str = text_lit.read()

text_str = text_str.replace('', '')
list_of_words = list(set(text_str.split()))
list_of_words.remove('–')
print(list_of_words)
