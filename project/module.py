import cv2
import shutil
from bs4 import BeautifulSoup
import os
import pprint
DIR="static/"

# cv2 variables
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# RED color in BGR
color = (0, 0, 255)
  
# Line thickness of 2 px
thickness = 2
# cv2 variables


class Process():
    def read_xml_obj(self,filexml):
        infile = open(filexml,"r")
        contents = infile.read()
        # load xml
        soup = BeautifulSoup(contents,'xml')
        objects=soup.find_all('object')
        return objects
    
    def read_image(self,fileimg):
        img=cv2.imread(fileimg)
    def checktemp():
        if os.path.exists(DIR):
            pass
        else:
            os.mkdir(DIR)        

    def plotkar(data,filename):
        img=cv2.imread(filename)
        cv2.rectangle(img,
                    (data["xmin"], data["ymin"]),
                    (data["xmax"],data["ymax"]), 
                    (0,0,255),2)
        cv2.putText(img,data["name"],(data["xmin"],data["ymin"]),font,
                    fontScale, color, thickness, cv2.LINE_AA)
        cv2.imwrite(filename,img)
    
    def get_data_xml(self,objects,fileimg,fn,tm,exacttime):
        
        Process.checktemp()

        dirhai=os.path.splitext(DIR+fileimg)[0]+"/"


        if os.path.exists(dirhai):
            pass
        else:
            os.mkdir(dirhai)

        
        # output file
        dst=dirhai+"output.jpg"
        
        shutil.copy(fileimg,dst)
        shutil.copy(fileimg, dirhai+fileimg)
        shutil.copy(fn,dirhai+fn)
        todb={}
        todb["proc_img"]=dst
        todb["img"]=dirhai+fileimg
        todb["obj"]=[]
        todb["timemmddyy"]=tm
        todb["timstamp"]=int(exacttime)

        for ob in objects:
            name=ob.find('name').get_text()
            xmin= ob.find('xmin').get_text()
            xmax=ob.find('xmax').get_text()
            ymin=ob.find('ymin').get_text()
            ymax=ob.find('ymax').get_text()
            data={
                "name":name,
                "xmin":int(xmin),
                "xmax":int(xmax),
                "ymin":int(ymin),
                "ymax":int(ymax)
            }
            todb["obj"].append(data)
            Process.plotkar(data,dst)
        pprint.pprint(todb)
        return todb

    def getDatadb(start_time,end_time):
        

        return 

    