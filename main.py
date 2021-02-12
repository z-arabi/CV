import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import arabic_reshaper
from bidi.algorithm import get_display

def _(text):
    return get_display(
        arabic_reshaper.reshape(u'%s'%str(text))
    )

mainForm = uic.loadUiType(os.path.join(os.getcwd(),"mainForm.ui"))[0]
PrForm = uic.loadUiType(os.path.join(os.getcwd(),"PrForm.ui"))[0]
EngForm = uic.loadUiType(os.path.join(os.getcwd(),"EngForm.ui"))[0]

class MainIntroWindow(QMainWindow,mainForm):  
    def __init__(self):
        super( MainIntroWindow, self).__init__()
        self.setupUi(self)

        self.PrButton.clicked.connect(self.Prcreate)
        self.EngButton.clicked.connect(self.Engcreate)

    def Prcreate(self):
        self.t=PrIntroWindow()
        self.t.show()
        self.close()
    
    def Engcreate(self):
        self.t=EngIntroWindow()
        self.t.show()
        self.close()


class PrIntroWindow(QMainWindow, PrForm):
    def __init__(self):
        super(PrIntroWindow,self).__init__()
        self.setupUi(self)

        self.name,self.family,self.degree,self.email,self.description,self.mediakey1,self.mediavalue1,self.mediakey2,self.mediavalue2 = None,None,None,None,None,None,None,None,None
        self.skills , self.projects = [0,0,0] , [0,0,0]
        self.fontfamily = 'Tahoma'
        self.fontsize = 18

        self.Name.textChanged.connect(self.setName)
        self.Family.textChanged.connect(self.setFamily)
        self.Degree.textChanged.connect(self.setDegree)
        self.Email.textChanged.connect(self.setEmail)
        self.Description.textChanged.connect(self.setDescription)
        self.Media1.textChanged.connect(self.setMediaKey1)
        self.Media1add.textChanged.connect(self.setMediavalue1)
        self.Media2.textChanged.connect(self.setMediakey2)
        self.Media2add.textChanged.connect(self.setMediavalue2)
        self.Skill1.textChanged.connect(self.addSkill0)
        self.Skill2.textChanged.connect(self.addSkill1)
        self.Skill3.textChanged.connect(self.addSkill2)
        self.Project1.textChanged.connect(self.addProject0)
        self.Project2.textChanged.connect(self.addProject1)
        self.Project3.textChanged.connect(self.addProject2)
        self.Fontsize.textChanged.connect(self.changeFontSize)

        self.Font1.clicked.connect(self.changeFont1)
        self.Font2.clicked.connect(self.changeFont2)

        self.pushButton.clicked.connect(self.makeCV)
        self.backButton.clicked.connect(self.goBack)

    def setName(self,name):
        self.name = name
    def setFamily(self,family):
        self.family = family
    def setDegree(self,degree):
        self.degree = degree
    def setEmail(self,email):
        self.email = email
    def setDescription(self,description):
        self.description = description
    def setMediaKey1(self,key):
        self.mediakey1 = key
    def setMediavalue1(self,value):
        self.mediavalue1 = value
    def setMediakey2(self,key):
        self.mediakey2 = key
    def setMediavalue2(self,value):
        self.mediavalue2 = value
    def addSkill0(self,skill):
        self.skills[0] = skill
    def addProject0(self,project):
        self.projects[0] = project
    def addSkill1(self,skill):
        self.skills[1] = skill
    def addProject1(self,project):
        self.projects[1] = project
    def addSkill2(self,skill):
        self.skills[2] = skill
    def addProject2(self,project):
        self.projects[2] = project
    def changeFontSize(self,fontsize):
        self.fontsize = int(fontsize)
    def changeFont1(self):
        self.fontfamily = 'Tahoma'
    def changeFont2(self):
        self.fontfamily = 'DejaVu Sans'
    

    def makeCV(self):
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = [self.fontfamily]
        fig, ax = plt.subplots(figsize=(9, 11))
        plt.axvline(x=0, color='cornflowerblue', alpha=0.5, linewidth=300)
        plt.axhline(y=0.8, xmin=0, xmax=1, color='#ffffff', linewidth=3)
        ax.set_facecolor('white')
        plt.axis('off')
        plt.annotate(_(self.name+' '+self.family), (0.9,0.9), weight='bold', fontsize=self.fontsize,ha='right')
        plt.annotate(_(self.degree),(.9,.85), weight='regular', fontsize=self.fontsize-5,ha='right')
        plt.annotate(self.email,(.9,.75), weight='regular', fontsize=self.fontsize-5,ha='right')
        if (self.mediakey1): plt.annotate(self.mediavalue1,(.9,.7), weight='regular', fontsize=self.fontsize-5,ha='right')
        if (self.mediakey2): plt.annotate(self.mediavalue2,(.9,.65), weight='regular', fontsize=self.fontsize-5,ha='right')
        plt.annotate(_(self.description),(.9,.55), weight='regular', fontsize=self.fontsize-5,ha='right')
        
        s = 'پروژه ها'+':'
        plt.annotate(_(s),(.9,0.45), weight='bold', fontsize=self.fontsize-2,ha='right')
        if self.projects[0]: plt.annotate(_(self.projects[0]),(0.9,.4), weight='regular', fontsize=self.fontsize-5,ha='right')
        if self.projects[1]: plt.annotate(_(self.projects[1]),(0.9,.35), weight='regular', fontsize=self.fontsize-5,ha='right')
        if self.projects[2]: plt.annotate(_(self.projects[2]),(0.9,.3), weight='regular', fontsize=self.fontsize-5,ha='right')

        s = 'مهارت ها'+':'
        plt.annotate(_(s),(0.28,.6), weight='bold', fontsize=self.fontsize-2,ha='right')
        if self.skills[0]: plt.annotate(_(self.skills[0]),(0.28,.5), weight='regular', fontsize=self.fontsize-5,ha='right')
        if self.skills[1]: plt.annotate(_(self.skills[1]),(.28,.4), weight='regular', fontsize=self.fontsize-5,ha='right')
        if self.skills[2]: plt.annotate(_(self.skills[2]),(.28,.3), weight='regular', fontsize=self.fontsize-5,ha='right')

        ax.axvline(x=0, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
        profile = mpimg.imread('pic.png')
        imagebox = OffsetImage(profile, zoom=0.1)
        ab = AnnotationBbox(imagebox, (0.15, 0.9))
        ax.add_artist(ab)

        plt.savefig('PersianResume.pdf', dpi=300, bbox_inches='tight')

    def goBack(self):
        self.t=MainIntroWindow()
        self.t.show()
        self.close()
        

class EngIntroWindow(QMainWindow, EngForm):
    def __init__(self):
        super(EngIntroWindow,self).__init__()
        self.setupUi(self)

        self.name,self.family,self.degree,self.email,self.description,self.mediakey1,self.mediavalue1,self.mediakey2,self.mediavalue2 = None,None,None,None,None,None,None,None,None
        self.skills , self.projects = [0,0,0] , [0,0,0]
        self.fontfamily = 'Tahoma'
        self.fontsize = 18

        self.Name.textChanged.connect(self.setName)
        self.Family.textChanged.connect(self.setFamily)
        self.Degree.textChanged.connect(self.setDegree)
        self.Email.textChanged.connect(self.setEmail)
        self.Description.textChanged.connect(self.setDescription)
        self.Media1.textChanged.connect(self.setMediaKey1)
        self.Media1add.textChanged.connect(self.setMediavalue1)
        self.Media2.textChanged.connect(self.setMediakey2)
        self.Media2add.textChanged.connect(self.setMediavalue2)
        self.Skill1.textChanged.connect(self.addSkill0)
        self.Skill2.textChanged.connect(self.addSkill1)
        self.Skill3.textChanged.connect(self.addSkill2)
        self.Project1.textChanged.connect(self.addProject0)
        self.Project2.textChanged.connect(self.addProject1)
        self.Project3.textChanged.connect(self.addProject2)
        self.Fontsize.textChanged.connect(self.changeFontSize)

        self.Font1.clicked.connect(self.changeFont1)
        self.Font2.clicked.connect(self.changeFont2)

        self.pushButton.clicked.connect(self.makeCV)
        self.backButton.clicked.connect(self.goBack)

    def setName(self,name):
        self.name = name
    def setFamily(self,family):
        self.family = family
    def setDegree(self,degree):
        self.degree = degree
    def setEmail(self,email):
        self.email = email
    def setDescription(self,description):
        self.description = description
    def setMediaKey1(self,key):
        self.mediakey1 = key
    def setMediavalue1(self,value):
        self.mediavalue1 = value
    def setMediakey2(self,key):
        self.mediakey2 = key
    def setMediavalue2(self,value):
        self.mediavalue2 = value
    def addSkill0(self,skill):
        self.skills[0] = skill
    def addProject0(self,project):
        self.projects[0] = project
    def addSkill1(self,skill):
        self.skills[1] = skill
    def addProject1(self,project):
        self.projects[1] = project
    def addSkill2(self,skill):
        self.skills[2] = skill
    def addProject2(self,project):
        self.projects[2] = project
    def changeFontSize(self,fontsize):
        self.fontsize = int(fontsize)
    def changeFont1(self):
        self.fontfamily = 'Tahoma'
    def changeFont2(self):
        self.fontfamily = 'DejaVu Sans'

    def makeCV(self):
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = [self.fontfamily]
        fig, ax = plt.subplots(figsize=(9, 11))
        plt.axvline(x=.99, color='cornflowerblue', alpha=0.5, linewidth=300)
        plt.axhline(y=.8, xmin=0, xmax=1, color='#ffffff', linewidth=3)
        ax.set_facecolor('white')
        plt.axis('off')
        plt.annotate(self.name+' '+self.family, (0.1,0.9), weight='bold', fontsize=self.fontsize)
        plt.annotate(self.degree,(.1,.85), weight='regular', fontsize=self.fontsize-5)
        plt.annotate(self.email,(.1,.75), weight='regular', fontsize=self.fontsize-5)
        if (self.mediakey1): plt.annotate(self.mediavalue1,(.1,.7), weight='regular', fontsize=self.fontsize-5)
        if (self.mediakey2): plt.annotate(self.mediavalue2,(.1,.65), weight='regular', fontsize=self.fontsize-5)
        plt.annotate(self.description,(.1,.55), weight='regular', fontsize=self.fontsize-5)
        
        s = 'Projects:'
        plt.annotate(s,(.1,0.45), weight='bold', fontsize=self.fontsize-2)
        if self.projects[0]: plt.annotate(self.projects[0],(0.1,.4), weight='regular', fontsize=self.fontsize-5)
        if self.projects[1]: plt.annotate(self.projects[1],(0.1,.35), weight='regular', fontsize=self.fontsize-5)
        if self.projects[2]: plt.annotate(self.projects[2],(0.1,.3), weight='regular', fontsize=self.fontsize-5)

        s = 'Skills:'
        plt.annotate(s,(0.7,.6), weight='bold', fontsize=self.fontsize-2)
        if self.skills[0]: plt.annotate(self.skills[0],(0.7,.5), weight='regular', fontsize=self.fontsize-5)
        if self.skills[1]: plt.annotate(self.skills[1],(.7,.4), weight='regular', fontsize=self.fontsize-5)
        if self.skills[2]: plt.annotate(self.skills[2],(.7,.3), weight='regular', fontsize=self.fontsize-5)

        ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
        profile = mpimg.imread('pic.png')
        imagebox = OffsetImage(profile, zoom=0.1)
        ab = AnnotationBbox(imagebox, (0.85, 0.9))
        ax.add_artist(ab)

        plt.savefig('EnglishResume.pdf', dpi=300, bbox_inches='tight')
    
    def goBack(self):
        self.t=MainIntroWindow()
        self.t.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainIntroWindow()
    w.show()
    sys.exit(app.exec_()) 