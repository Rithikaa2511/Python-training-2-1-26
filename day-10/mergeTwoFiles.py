with open("Day-10/merge1.txt",'r')as f1, open("Day-10/merge2.txt",'r')as f2, open("Day-10/mergedFile.txt",'w')as fw:
    text = f1.read() + f2.read()
with open("Day-10/mergedFile.txt",'w')as f:
    f.write(text)
    