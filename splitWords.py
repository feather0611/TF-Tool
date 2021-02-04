import jieba
import os
from os import listdir
import sys
import jieba.analyse

def split(path, output):
    # path = '/Users/firefeatherangel/Desktop/國企系/files/' #directory
    # output='/Users/firefeatherangel/Desktop/國企系/files/mode4/'
    file = sorted(listdir(path))
    if '.DS_Store' in file:
        file.remove('.DS_Store')      #清除.DS_Store檔
    jieba.set_dictionary('res/dict.txt.big')
    jieba.load_userdict('res/myDictionary.txt')
    for f in file:
        filepath = path + f
        if os.path.isdir(filepath):
            continue
        with open(filepath, 'rb') as i: #以bytes形式開啟檔案
            ch = i.read()
            if(ch.hex()[:4]=='fffe'): #文檔開頭為0xff0xfe時編碼為UTF-16
                encode = 'utf-16'
            elif(ch.hex()[:2]=='aa' or ch.hex()[:2]=='c0'): #文檔開頭為0xaa或0xc0時編碼為Big5
                encode = 'Big5'
            else:       #其餘是UTF-8
                encode = 'utf-8'

        #正式讀取文字
        with open(filepath, 'r', encoding=encode) as i, open(output+'s_'+f, 'w', encoding='utf-8') as o:
            try:
                rows = i.read()
            except UnicodeDecodeError:      #依然有編碼問題時
                print('file: '+f+' cannot be decoded.')
                sys.exit(0)
            text = '|'.join(jieba.cut(rows, cut_all=False, HMM=True))   #mode1
            #text = '|'.join(jieba.cut(rows, cut_all=False, HMM=False))   #mode2
            #text = '|'.join(jieba.cut(rows, cut_all=True, HMM=False))   #mode3
            #text = '|'.join(jieba.cut(rows, cut_all=True, HMM=True))    #mode4
            o.write(text)
    print('Split Words Done!')
