import jieba
import codecs
import re
f=codecs.open('hlm.txt', "a+",'utf-8')
for line in open(r"hongloumeng.txt",'r',encoding='utf-8'):
    for i in re.sub("[\s+\.\!\/_,$%-<>^*(+\"\']+|[+——！，。？、~@#￥%……&*（）？《》、．：“”]+", "",line).split(' '):
        if i!='':

            data=list(jieba.cut(i,cut_all=False))
            readline=' '.join(data)+'\n'
            f.write(readline)
f.close()

