# -*- coding: UTF-8 -*- 


def prepData(filename):
    d = {}
    f = open(filename)
    #f = open("专硕/专硕.txt")             # 返回一个文件对象
    line = f.readline()             # 调用文件的 readline()方法
    while line:
        sp = line.split("\t",1);
        if(len(sp)!=2):
            print len(sp),line,"--------"
            continue;
        num = sp[1].strip();
        idx = sp[0].strip();
        d[num] = idx;
        line = f.readline();
    return d;

   
def eachFile(filepath):
    pathDir =  os.listdir(filepath);
    return pathDir
    #for allDir in pathDir:
        #child = os.path.join('%s/%s' % (filepath, allDir))
        #print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题


def getStdNo(listFileName):
    import re;
    # 读取文件进来
    p = re.compile("\\d{10}");
    d ={}
    for fileName in listFileName:
        result = p.search(fileName)
        if(result):
            num = result.group()
            #print 'success:' , num
            d[num] = fileName
        else:
            print 'erroR!!!  ', fileName.decode('gbk')
    return d

zhuanshuo = prepData("专硕/专硕.txt");
xueshuo = prepData("学硕/学硕.txt");
#print("学硕长度: ",len(xueshuo),"  专硕长度: ",len(zhuanshuo));
fileList =  eachFile('res');
numFileNameDic = getStdNo(fileList);

for key in numFileNameDic.keys():
    import shutil;
    fileName = numFileNameDic[key]
    isZhuanshuo = zhuanshuo.has_key(key)
    isXueshuo = xueshuo.has_key(key)
    if isZhuanshuo and not isXueshuo:
        idx = zhuanshuo[key]
        # print fileName.decode('gbk');
        shutil.copy('res/'+fileName,'专硕/'+idx+"-"+fileName);
    elif not isZhuanshuo and isXueshuo:
        idx = xueshuo[key]
        shutil.copy('res/'+fileName,'学硕/'+idx+"-"+fileName);
    else:
        print "erroorr!!!!",key,fileName.decode('gbk'),isZhuanshuo,isXueshuo
    

