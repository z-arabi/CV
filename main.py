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

Form = uic.loadUiType(os.path.join(os.getcwd(),"Form.ui"))[0]

class IntroWindow(QMainWindow, Form):
    def __init__(self):
        super(IntroWindow,self).__init__()
        self.setupUi(self)

        self.name,self.family,self.degree,self.email,self.description,self.mediakey,self.mediavalue = None,None,None,None,None,None,None
        self.skills , self.projects = [0,0,0] , [0,0,0]

        self.Name.textChanged.connect(self.setName)
        self.Family.textChanged.connect(self.setFamily)
        self.Degree.textChanged.connect(self.setDegree)
        self.Email.textChanged.connect(self.setEmail)
        self.Description.textChanged.connect(self.setDescription)
        self.Media1.textChanged.connect(self.setMediaKey)
        self.Media1add.textChanged.connect(self.setMediavalue)
        self.Skill1.textChanged.connect(self.addSkill0)
        self.Skill2.textChanged.connect(self.addSkill1)
        self.Skill3.textChanged.connect(self.addSkill2)
        self.Project1.textChanged.connect(self.addProject0)
        self.Project2.textChanged.connect(self.addProject1)
        self.Project3.textChanged.connect(self.addProject2)

        self.pushButton.clicked.connect(self.makeCV)

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
    def setMediaKey(self,key):
        self.mediakey = key
    def setMediavalue(self,value):
        self.mediavalue = value
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

    def makeCV(self):
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = ['Tahoma']
        fig, ax = plt.subplots(figsize=(9, 11))
        plt.axvline(x=0, color='cornflowerblue', alpha=0.5, linewidth=300)
        plt.axhline(y=0.8, xmin=0, xmax=1, color='#ffffff', linewidth=3)
        ax.set_facecolor('white')
        plt.axis('off')
        plt.annotate(_(self.name+' '+self.family), (0.9,0.9), weight='bold', fontsize=20)
        plt.annotate(_(self.degree),(.9,.85), weight='regular', fontsize=14)
        plt.annotate(self.email,(.9,.75), weight='regular', fontsize=14)
        if (self.mediakey): plt.annotate(self.mediavalue,(.9,.7), weight='regular', fontsize=14)
        plt.annotate(_(self.description),(.8,.6), weight='regular', fontsize=14)
        s = 'پروژه ها'
        plt.annotate(_(s),(.9,0.5), weight='bold', fontsize=17)
        plt.annotate(_(self.projects[0]),(0.8,.45), weight='regular', fontsize=14)
        plt.annotate(_(self.projects[1]),(0.8,.4), weight='regular', fontsize=14)
        plt.annotate(_(self.projects[2]),(0.8,.35), weight='regular', fontsize=14)

        s = 'مهارت ها'
        plt.annotate(_(s),(0.18,.6), weight='regular', fontsize=14)
        plt.annotate(_(self.skills[0]),(0.01,.5), weight='regular', fontsize=14)
        plt.annotate(_(self.skills[1]),(.01,.4), weight='regular', fontsize=14)
        plt.annotate(_(self.skills[2]),(.01,.3), weight='regular', fontsize=14)

        # profile = mpimg.imread('pic.png')
        # imagebox = OffsetImage(profile, zoom=0.1)
        # ab = AnnotationBbox(imagebox, (0.15, 0.9))
        # ax.add_artist(ab)

        plt.savefig('resumeexample.pdf', dpi=300, bbox_inches='tight')
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_()) 