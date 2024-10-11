#输出：人生苦短，我学python
#需求：使用print()函数将“人生苦短，我学python”输出到文本文件txt当中
fp = open('text.txt','w') #w指的是write的意思
print("人生苦短，我学python",file=fp) #将此话输出到text.txt文件当中
fp.close() #关闭该文件