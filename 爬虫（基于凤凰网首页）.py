#-*-encoding:utf-8-*-

from urllib import urlopen
import chardet
import re
net=[]
urlfeng='http://www.ifeng.com'
textfeng=urlopen(urlfeng).read()
textfeng=str(textfeng)
patternnet=re.compile('http://news.ifeng.com/a/.{8}/.{8}_0.shtml|http://ent.ifeng.com/a/.{8}/.{8}_0.shtml|http://fashion.ifeng.com/a/.{8}/.{8}_0.shtml|http://sports.ifeng.com/a/.{8}/.{8}_0.shtml|http://tech.ifeng.com/a/.{8}/.{8}_0.shtml')
net0=re.findall(patternnet,textfeng)
for i in net0:
    if not(i in net):#防止网址重复，加快查找速度。
        net.append(i)
        print i
net0[:]=net[:]
for i in net0:
    textfeng=urlopen(i).read()
    textfeng=str(textfeng)
    net1=re.findall(patternnet,textfeng)
    for j in net1:
        if not(j in net):
            net.append(j)
            print j
num=len(net)
print num
#获取网址
for k in net:
        text = urlopen(k).read()
        charset=chardet.detect(text)
        code=charset['encoding']
        text=str(text).decode(code,'ignore').encode("utf-8")

        patterntitle='<title>(.*)</title>'#获取新闻标题
        patterntitle=re.compile(patterntitle)
        title=re.search(patterntitle,text)
        title=title.group()
        if title=='<title>404-页面不存在</title>':continue#通过标题判断网页是否存在
        title=title.replace('<title>','').replace('</title>','').replace('|','_').replace('/','_').replace('"','“').replace('?','？').replace(':','：')
        print 'tittle:'+title

        patternbegin=re.compile('<!--mainContent begin-->|<!--文章内容 begin-->')#获取新闻内容
        passage=re.split(patternbegin,text)
        if len(passage)==1:
            continue
        else:
            passage=passage[1]
        patternend=re.compile('<!--mainContent end-->|<!--文章内容 end-->')
        passage=(re.split(patternend,passage))[0]

        patterncode=re.compile('<p>(.*?)</p>')#将新闻分段，并去除部分代码
        code=re.findall(patterncode,passage)

        patterntarget=re.compile('<span.*?</span>')#去掉图片
        target=re.findall(patterntarget,passage)
        for i in target:
            for j in range(len(code)):
                code[j]=code[j].replace(i,'')
        for i in range(len(code)):
            code[i]=code[i].replace('<strong>','').replace('</strong>','').replace('&rdquo;','').replace('&ldquo;','').replace('&lsquo;','').replace('&&nbsp;','')
            code[i]=code[i].replace('<strong style="text-indent: 2em;">','').replace('&hellip;','').replace('</span>','').replace('&mdash;','').replace('&middot;','')
            code[i]='    '+code[i]
        patternlink=re.compile('<a.*?>')#去掉文字链接
        link=re.findall(patternlink,passage)
        for i in link:
            for j in range(len(code)):
                code[j]=code[j].replace(i,'')
                code[j]=code[j].replace('</a>','')

        net=('F:\\newsss\\'+title+'.text')#创建文本文件，并存入新闻
        f=open(net.decode('utf-8'),'w')
        f.write('                             '+title+'\n')
        for i in code:
            f.write(i+'\n')
        f.close()
        print 'OK'
