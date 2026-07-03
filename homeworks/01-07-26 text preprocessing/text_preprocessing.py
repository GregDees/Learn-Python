#Открытие файла текста
import re
from collections import defaultdict
with open('C:/Users/GregDees/Documents/Python/Learn-Python/homeworks/01-07-26 text preprocessing/input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    textwords = text.split(sep=' ')
    textwords = re.findall(r'\w+|[!.?]', text) # ['str1', '.', '!', 'word2']
    # word -> (0.123, 0.2314 ... -31)
# файл закрыт 

#Открытие файла стоп-слов
with open("C:/Users/GregDees/Documents/Python/Learn-Python/homeworks/01-07-26 text preprocessing/stopwords-ru.txt", 'r', encoding='utf-8') as file:
    stopwords = file.read().splitlines()
    stopword = set(stopwords)
    # stopword = list(stopwords)
# файл закрыт

#Создаём новый отфильтрованный список без стоп слов и в одном регистре
# как можно было сделать быстрее, НО жертвуем читаемостью
# filteredtext = []
# for word in textwords: 
#     wl = word.lower()
#     if wl not in stopword:
#         filteredtext.append(wl)

filteredtext = [word.lower() for word in textwords if word.lower() not in stopword] # O(N)

popular_words = defaultdict(int) # всем ключам по умолчанию выставляет значение = (int)
words_count = text_len = sentences = 0

# longest_word = max(filteredtext, key = len) # O(N)
longest_word = ""

for word in filteredtext: # O(N)
    text_len += len(word)
    if word in '.!?': 
        sentences += 1
    else:
        # if word not in '.!?': лишняя проверка
        words_count += 1

        # if word not in popular_words:
        #     popular_words[word] = 1
        # else:

        popular_words[word] += 1
        if len(word) > len(longest_word):
            longest_word = word

word_len_mean = (text_len - sentences) / words_count
toplist = dict(sorted(popular_words.items(), key = lambda x: x[1], reverse=True)[:10]) 

print('Количество символов: ', text_len)
print('Количество слов: ', words_count)
print('Количество предложений: ', sentences)
print('Самое длинное слово: ', longest_word)
print('- Длина самого длинного слова: ', len(longest_word))
print('Средняя длина слова: ', round(word_len_mean, 2))
print('Топ слов: ')
for word in toplist:
    print(word, '- ', toplist[word])

'''
ДО ИСПРАВЛЕНИЙ

#Открытие файла текста
import re
with open('C:/Users/GregDees/Documents/Python/Learn-Python/homeworks/01-07-26 text preprocessing/input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    textwords = text.split(sep=' ')
    textwords = re.findall(r'\w+|[!.?]', text) # ['str1', ...]

    #Открытие файла стоп-слов
    with open("C:/Users/GregDees/Documents/Python/Learn-Python/homeworks/01-07-26 text preprocessing/stopwords-ru.txt", 'r', encoding='utf-8') as file:
        stopwords = file.read().splitlines()
        stopword = set(stopwords)

        #Создаём новый отфильтрованный список без стоп слов и в одном регистре
        filteredtext = [word.lower() for word in textwords if word.lower() not in stopword]
        print(filteredtext)

        popular_words = {}
        words_count = 0
        text_len = 0 
        sentences = 0
        longest_word = max(filteredtext, key = len)
        for word in filteredtext:
            text_len += len(word)
            if word in '.!?': 
                sentences += 1
                continue
            if word not in '.!?':
                words_count += 1
            if word not in popular_words:
                popular_words[word] = 1
            else:
                popular_words[word] += 1
        
        word_mid_len = (text_len - sentences) / words_count
        toplist = dict(sorted(popular_words.items(), key = lambda x: x[1], reverse=True)[:10]) 

        print('Количество символов: ', text_len)
        print('Количество слов: ', words_count)
        print('Количество предложений: ', sentences)
        print('Самое длинное слово: ', longest_word)
        print('- Длина самого длинного слова: ', len(longest_word))
        print('Средняя длина слова: ', round(word_mid_len, 2))
        print('Топ слов: ')
        for word in toplist:
            print(word, '- ', toplist[word])
'''

# РЕШЕНИЕ В ОДНУ СТРОКУ(ЛЕГЕНДАРНОЕ)
#print(f'''Количество символов: {sum(map(len, [x for x in __import__('re').findall(r'\w+|[!.?]', open('input').read().lower()) if x not in set(open('stops').read().split())]))}\n\tКоличество слов: {len([x for x in [x for x in __import__('re').findall(r'\w+|[!.?]', open('input').read().lower()) if x not in set(open('stops').read().split())] if x not in '.!?'])}\n\tКоличество предложений: {sum(x in ".!?" for x in [x for x in __import__('re').findall(r'\w+|[!.?]', open('input').read().lower()) if x not in set(open('stops').read().split())])}\n\nСамое длинное слово: {max([x for x in [x for x in __import__('re').findall(r'\w+|[!.?]', open('input').read().lower()) if x not in set(open('stops').read().split())] if x not in '.!?'], key=len, default='')}\n\tДлина самого длинного слова: {len(max([x for x in [x for x in __import__('re').findall(r'\w+|[!.?]', open('input').read().lower()) if x not in set(open('stops').read().split())] if x not in '.!?'], key=len, default=''))}\n\nСредняя длина слова: {round(sum(map(len, [x for x in [x for x in __import__('re').findall(r'\w+|[!.?]', open('input').read().lower()) if x not in set(open('stops').read().split())] if x not in '.!?'])) / len([x for x in [x for x in __import__('re').findall(r'\w+|[!.?]', open('input').read().lower()) if x not in set(open('stops').read().split())] if x not in '.!?']), 2) if [x for x in [x for x in __import__('re').findall(r'\w+|[!.?]', open('input').read().lower()) if x not in set(open('stops').read().split())] if x not in '.!?'] else 0}\n\nТоп слов:\n''','\n'.join([(f'  {word} - {count}') for word, count in __import__('collections', fromlist=['Counter']).Counter([x for x in [x for x in __import__('re').findall(r'\w+|[!.?]', open('input').read().lower()) if x not in set(open('stops').read().split())] if x not in '.!?']).most_common(10)]))

'''
#Открытие файла текста
import re
from collections import defaultdict
with open('C:/Users/GregDees/Documents/Python/Learn-Python/homeworks/01-07-26 text preprocessing/input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    textwords = text.split(sep=' ')
    textwords = re.findall(r'\w+|[!.?]', text) # ['str1', '.', '!', 'word2']
    # word -> (0.123, 0.2314 ... -31)
# файл закрыт 

#Открытие файла стоп-слов
with open("C:/Users/GregDees/Documents/Python/Learn-Python/homeworks/01-07-26 text preprocessing/stopwords-ru.txt", 'r', encoding='utf-8') as file:
    stopwords = file.read().splitlines()
    stopword = set(stopwords)
    # stopword = list(stopwords)
# файл закрыт

#Создаём новый отфильтрованный список без стоп слов и в одном регистре
# как можно было сделать быстрее, НО жертвуем читаемостью
# filteredtext = []
# for word in textwords: 
#     wl = word.lower()
#     if wl not in stopword:
#         filteredtext.append(wl)

filteredtext = [word.lower() for word in textwords if word.lower() not in stopword] # O(N)

popular_words = defaultdict(int) # всем ключам по умолчанию выставляет значение = (int)
words_count = text_len = sentences = 0

# longest_word = max(filteredtext, key = len) # O(N)
longest_word = ""

for word in filteredtext: # O(N)
    text_len += len(word)
    if word in '.!?': 
        sentences += 1
    else:
        # if word not in '.!?': лишняя проверка
        words_count += 1

        # if word not in popular_words:
        #     popular_words[word] = 1
        # else:

        popular_words[word] += 1
        if len(word) > len(longest_word):
            longest_word = word

word_len_mean = (text_len - sentences) / words_count
toplist = dict(sorted(popular_words.items(), key = lambda x: x[1], reverse=True)[:10]) 

print('Количество символов: ', text_len)
print('Количество слов: ', words_count)
print('Количество предложений: ', sentences)
print('Самое длинное слово: ', longest_word)
print('- Длина самого длинного слова: ', len(longest_word))
print('Средняя длина слова: ', round(word_len_mean, 2))
print('Топ слов: ')
for word in toplist:
    print(word, '- ', toplist[word])

'''


