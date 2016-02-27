#!/usr/bin/python
#coding:utf-8
import os,re
import time
import json
def getdirsize(dir):
    size = 0L
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


def GetCurPathInfo():
    CurPath = '/data/mirrors/'
    ChildrenList = os.listdir(CurPath)
    ChildrenList.sort()

    InfoDict = dict()

    last_modify_file_dict = {
        'centos' : '/timestamp.txt',
        'android' :'/repository',
        'epel':'/fullfilelist',
        'pypi':'/status'
    }

    help_dict={
        'npm':'http://docs.mirrors.opencas.org/latest/npm/',
        'pypi':'http://docs.mirrors.opencas.org/latest/pypi/'
    }

    official = ["apache","archlinux","centos","cran","ctan","deepin","deepin-cd","eclipse","epel","ezgo","mariadb","raspbian"]

    for Name in ChildrenList:
        tempDict={}
        if Name=='fancin':
            continue
        if os.path.isdir(CurPath + os.path.sep + Name):
            if os.path.exists("/tmp" + os.path.sep + Name):
                tempDict["state"] = "syncing"
            else:
                tempDict["state"] = "success"
            if Name in official:
                tempDict["official"]=True;
            else:
                tempDict["official"]=False;
            if Name in help_dict:
                tempDict["doc"]=help_dict[Name]
            tempInfo = os.stat(CurPath + os.path.sep + Name)
            if Name in last_modify_file_dict:
                tempInfo = os.stat(CurPath + os.path.sep + Name + last_modify_file_dict[Name])
            tempDict["up_time"] = time.ctime(tempInfo.st_mtime)
            timeArray = time.localtime(tempInfo.st_mtime)
            tempDict["up_time"]=time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
            tempDict["link"] = 'http://mirrors.opencas.cn/' + Name
            InfoDict[Name] = tempDict
    return InfoDict


def ContentGen(InfoDict):
    # keys = InfoDict.keys()
    # keys.sort()
    return json.dumps(InfoDict)

def main():
    InfoDict = GetCurPathInfo()
    dict= sorted(InfoDict.iteritems(), key=lambda d:d[0])
    Content = ContentGen(dict)


    with open(os.path.split(os.path.realpath(__file__))[0]+"/state.json", "w") as outFile:
        outFile.write(Content)

if __name__ == '__main__':
    main()