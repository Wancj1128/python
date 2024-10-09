fp = open('note.txt','w') #打开文件w
print('北京欢迎您',file=fp)
#将“北京欢迎您写入到了note.txt文件当中了”
fp.close() #关闭文件