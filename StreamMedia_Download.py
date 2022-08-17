import urllib.request
import urllib.parse
import re
from tqdm import tqdm
import os


def geturl():
    file = open(r"C:\Users\杨明菲\Desktop\replay.1660365722.27668076.m3u8",'r')
    urllist=[]
    #获取m3u8的url
    while True:
        line=file.readline()
        if not line:
            break
        else:
            if not re.search("#EXT",line):
                urllist.append(line.replace("\n",""))
    return urllist

def getts(urllist,dir_path):
    i=0
    for url in tqdm(urllist):
        if i<=973:
            i=i+1
            continue
        else:
            urllib.request.urlretrieve(url, "%s%s" % (dir_path, str(i)))
            i=i+1

if __name__=="__main__":
    filePath = "F:/ts_file/"
    #list=geturl()
    #getts(urllist=list,dir_path=filePath)
    file_list = os.listdir(filePath)
    file_list.sort(key=lambda x:int(x))
    with open("F:/ts_file/file_list.txt","w+") as f:
        for file in file_list:
            f.write("file '{}'\n".format(file))

    #cmd:ffmpeg -f concat -i file_list.txt -c copy output.mp4