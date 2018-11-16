import csv
texts = [ 'trade-wars-news1.txt',
                   'trade-wars-news2.txt',
                   'trade-wars-news3.txt',
                   'trade-wars-news4.txt',
                   'trade-wars-news5.txt' ]
all_texts = []   
for text in texts: 
    t = open (text,'r')
    word = t.read()
    all_texts.append(word)   
all_cells=[]
for z in range(5):               
    cells = all_texts[z].split()
    for all_cell in cells:
        all_cells.append(all_cell)
from collections import Counter
cnt = Counter()
for z in all_cells:
    cnt[z] += 1
print(cnt.most_common())      
word_list = [cnt.most_common()]
with open('c_keyword.csv','w') as f:
    mywriter=csv.writer(f)
    mylist=['word','frequency']
    result=[cnt.most_common()]
    mywriter.writerow(mylist)
    for i in range(0,len(word_list)):
        mywriter.writerows(word_list[i])             