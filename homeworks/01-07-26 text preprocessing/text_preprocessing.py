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
        
        
        print('Количество символов: ', text_len)
        print('Количество слов: ', words_count)
        print('Количество предложений: ', sentences)
        print('Самое длинное слово: ', 0)
        print('- Длина самого длинного слова: ', 0)
        print('Средняя длина слова: ', (text_len - sentences) / words_count)
        print('Топ слов: ')
        # [1,8,4,2,56,9,-5] - вывести 3 самых больших числа
        # вопрос - как найти N самых больших значения
        for word in popular_words:
            print(word, '- ', popular_words[word])