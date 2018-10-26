#coding=utf-8
'''
import os,shutil

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print("move %s -> %s"%( srcfile,dstfile))



path = "D://3//"

rect = ['304','305','306','309','312','313','314','315','316','317','319','320','321','326','327','328','334','335','336','338','341','342','349','364','365','366','367','369','370','371','374','375','376','377','378','380','381','384','385','386','387','388','390','391','392','393','394','395','396','398','399','400','401','402','403','405','406','407','408','409','410','411','412','413','414','416','417','418','419','423','424','427','428','432','433','434','435','436','437','438','439','441','442','443','447','448','449','450','451','452','453','454','455','456','457','458','459','460','462','468','469','470','472','474','475','476','477','478','479','480','481','482','483','484','485','486','490','492','493','495','496','497','498','499','500','502','503','504','505','506','508','509','510']
for i1 in rect:
    #print(i)
    path1 = path+i1+".xml"
    path2 = path+"xml//"+i1+".xml"
    mymovefile(path1, path2)

'''


'''
#将特定文件夹下的文件移动到另一个文件夹
import os
import shutil

path_xml = "D://5"#windows系统用双斜线
filelist = os.listdir(path_xml)
path1 = "D:\\5"
path2 = "D:\\5\\xml\\"


for files in filelist:
    filename1 = os.path.splitext(files)[1]  # 读取文件名
    filename0 = os.path.splitext(files)[0]
    print(filename1)
    m = filename1 == '.xml'
    print(m)
    if m :
        full_path = os.path.join(path1, files)
        despath = path2 + filename0+'.xml'
        shutil.move(full_path, despath)

    else :
        continue
'''

#将特定文件夹下的文件移动到另一个文件夹
import os
import shutil

path_xml = "D://5"#windows系统用双斜线
filelist = os.listdir(path_xml)
path1 = "D:\\5"
path2 = "D:\\5\\jpg\\"


for files in filelist:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  #读取文件名
    print(filename1)
    m = filename1 == '.jpg'
    print(m)
    if m :
        full_path = os.path.join(path1, files)
        despath = path2 + filename0+'.jpg' #.jpg为你的文件类型，即后缀名，读者自行修改
        shutil.move(full_path, despath)

    else :
        continue









