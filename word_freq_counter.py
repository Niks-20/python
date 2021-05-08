# importing the text in docx format only
import textract
text = textract.process('sample.docx')
text = text.decode("utf-8")

#inserting the entire document to a list
sentence_list = []
sentence_list.append(text)

# splitting the sentences for spaces and removing . and ,
sentence_list = sentence_list[0].split()
sentence_list = [word.replace(".", "") for word in sentence_list]
sentence_list = [word.replace(",", "") for word in sentence_list]

# converting to a list for getting keys(words) and values(freq) pairs
dict = {}
def dict_maker(list):
    for i in range (1, len(sentence_list)):
        if list[i] not in dict.keys():
            dict[list[i]] = 1
        else: 
            dict[list[i]] = dict.get(list[i]) + 1
    return dict

dict_maker(sentence_list)
print(dict) 

# gettting the graph on matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
plt.style.use('fivethirtyeight')
words_x = dict.keys()
freq_y = dict.values()
plt.bar(words_x, freq_y, color='k', label='Words_freq_count')
plt.xlabel('Words used in the given text')
plt.ylabel('Freq of words')
plt.title('Text analyzer')

plt.show()
plt.tight_layout()
