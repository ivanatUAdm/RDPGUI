#!/usr/bin/env python3
import sys
from PyQt4 import QtCore, QtGui
import os, time
import re
import subprocess
import urllib
import configparser
import psutil
#import wnck


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RDPGUI(object):
    def __init__(self,UI_RDPGUI,usesection=None):
        self.RDPGUI=UI_RDPGUI
        print ("RDPGUI")
        self.config = configparser.ConfigParser()
        self.config.read('./rdpgui.ini')
        self.versionbuild=11
        self.FillDefaults('./rdpgui.ini')
        if usesection is None:
           try:
             usesection = self.config.get("DEFAULT", "Section", fallback='DEFAULT')
           except:
             usesection="DEFAULT"
        self.section=usesection
        self.RDPGUI.setObjectName(_fromUtf8("RDPGUI"))
        self.RDPGUI.resize(628, 482)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("selectuser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RDPGUI.setWindowIcon(icon)
        self.RDPGUI.setStyleSheet(_fromUtf8("background-color: rgb(24, 93, 123);"))
        self.image = QtGui.QLabel(self.RDPGUI)
        self.image.setGeometry(QtCore.QRect(220, 30, 191, 191))
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8("selectuser.png")))
        self.image.setObjectName(_fromUtf8("image"))
        self.enterButton = QtGui.QPushButton(self.RDPGUI)
        self.enterButton.setGeometry(QtCore.QRect(430, 340, 31, 31))
        self.enterButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.enterButton.setText(_fromUtf8(""))
        self.exitButton = QtGui.QPushButton(self.RDPGUI)
        self.exitButton.setGeometry(QtCore.QRect(430, 400, 31, 31))
        self.exitButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 100, 100);"))
        self.exitButton.setText(_fromUtf8("Exit"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("enter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.enterButton.setIcon(icon1)
        self.enterButton.setIconSize(QtCore.QSize(40, 40))
        self.enterButton.setObjectName(_fromUtf8("enterButton"))
        self.DOstore = QtGui.QCheckBox(self.RDPGUI)
        self.DOstore.setGeometry(QtCore.QRect(430, 370, 31, 31))
        self.DOstore.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.DOstore.setObjectName(_fromUtf8("Store"))
        
        self.RDPusername = QtGui.QLineEdit(self.RDPGUI)
        self.RDPusername.setGeometry(QtCore.QRect(190, 290, 231, 31))
        self.RDPusername.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.RDPusername.setObjectName(_fromUtf8("RDPusername"))
        self.RDPpassword = QtGui.QLineEdit(self.RDPGUI)
        self.RDPpassword.setGeometry(QtCore.QRect(190, 340, 231, 31))
        self.RDPpassword.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.RDPpassword.setEchoMode(QtGui.QLineEdit.Password)
        self.RDPpassword.setObjectName(_fromUtf8("RDPpassword"))
        self.version = QtGui.QLabel(self.RDPGUI)
        self.version.setGeometry(QtCore.QRect(520, 460, 101, 20))
        self.version.setStyleSheet(_fromUtf8("color: rgb(193, 193, 193);"))
        self.version.setObjectName(_fromUtf8("version"))
        self.label = QtGui.QLabel(self.RDPGUI)
        self.label.setGeometry(QtCore.QRect(130, 230, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(self.RDPGUI)
        self.widget.setGeometry(QtCore.QRect(190, 380, 231, 44))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.serverlabel = QtGui.QLabel(self.widget)
        self.serverlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.serverlabel.setObjectName(_fromUtf8("serverlabel"))
        self.gridLayout.addWidget(self.serverlabel, 0, 0, 1, 1)
        self.serverBox = QtGui.QComboBox(self.widget)
        self.serverBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.serverBox.setObjectName(_fromUtf8("serverBox"))
        self.serverBox.setEditable(True)
        self.gridLayout.addWidget(self.serverBox, 0, 1, 1, 1)
        self.domainlabel = QtGui.QLabel(self.widget)
        self.domainlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.domainlabel.setObjectName(_fromUtf8("domainlabel"))
        self.gridLayout.addWidget(self.domainlabel, 1, 0, 1, 1)
        self.RDPdomain = QtGui.QLabel(self.widget)
        self.RDPdomain.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.RDPdomain.setObjectName(_fromUtf8("RDPdomain"))
        self.gridLayout.addWidget(self.RDPdomain, 1, 1, 1, 1)
        self.FillSRVBox()
        self.retranslateUi()
        QtCore.QObject.connect(self.RDPpassword, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.enterButton.click)
        QtCore.QObject.connect(self.RDPusername, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.checkdomain)
#        QtCore.QObject.connect(self.serverBox,   QtCore.SIGNAL(_fromUtf8("selectionChanged()")), self.handleChanged)

        self.serverBox.currentIndexChanged['QString'].connect(self.handleChanged)
        QtCore.QMetaObject.connectSlotsByName(self.RDPGUI)
        centreWidget(self.RDPGUI)
        print ("RDPGUI init - done")

    def FillSRVBox(self, section=None):
        print ("FillSRVBox wwith:: ",section)
        if section is None:
           section = self.config.get("DEFAULT", "Section", fallback='DEFAULT')
        count=0
        self.serverBox.setCurrentIndex(count)
        print ("init count value:",self.serverBox.currentIndex())
        self.serverBox.addItem(_fromUtf8(""))
        self.serverBox.setItemText(count, _translate("RDPGUI", "default..", None))

        self.serverBox.setCurrentIndex(count)     
        print("value for ServerBox")
        print ("Count:", count)
        for n in self.config.sections():
                count=count+1
                print ("DBG ",count," Value", n)
                self.serverBox.addItem(_fromUtf8(""))
                self.serverBox.setItemText(count, _translate("RDPGUI", str(n), None))
                self.changeSBIndex()
                print ("DBG3:",self.serverBox.currentIndex())
                
#                if section is n:
#        self.changeIndex()
        print ("DBG4:",self.serverBox.currentIndex())
        
        
    def retranslateUi(self):
        print ("retranslateUi wwith: ", self.section)
        self.RDPGUI.setWindowTitle(_translate("RDPGUI", "RDPGUI", None))
        self.RDPusername.setPlaceholderText(_translate("RDPGUI", "Username", None))
        self.RDPpassword.setToolTip(_translate("RDPGUI", "Insert username", None))
        self.RDPpassword.setPlaceholderText(_translate("RDPGUI", "Password", None))
        self.version.setText(_translate("RDPGUI", "rpi-tc rdp gui v3", None))
        self.serverlabel.setText(_translate("RDPGUI", "Server:", None))
        self.domainlabel.setText(_translate("RDPGUI", "Domain:", None))
        self.RDPdomain.setText(_translate("RDPGUI", "DOMAIN", None))
        self.enterButton.clicked.connect(self.handleEnterButton)
        self.exitButton.clicked.connect(self.doExitNow)
        self.FillProfile(self.serverBox.currentText())
        print ("retranslateUi back, section:", self.section)
        self.serverBox.currentIndexChanged['QString'].connect(self.handleChanged)
        
#        self.changeIndex()
##        self.serverBox.activated['QString'].connect(self.handleActivated)

##        self.serverBox.handle['QSting'].connect(self.handleChangedBox)
#        self.changeSBIndex()
    def FillDefaults(self,config_location):
        if self.versionbuild > int(self.config.get("DEFAULT", "VersionBuild", fallback=0 )):
           self.config["DEFAULT"]={ 'RDPBinary' : 'xfreerdp',
                                    'RDPDomain' : '',
                                    'RDPServer' : '',
                                    'RDPusername' : '',
                                    'RDPpassword' : '',
                                    'RDPDefaulfFlags' : '/cert-ignore',
                                    'RDPExtraFlags' : '',
                                    'RDPGeomMode' : 'WorkSpace',
                                    'VersionBuild' : self.versionbuild
           }
        with open(config_location, 'w') as configfile:
           self.config.write(configfile)
        
    def FillProfile(self, section=None):
        if section is None:
           section = self.config.get("DEFAULT", "RDPDomain", fallback='DEFAULT')
        else: 
           section.strip()
        print ("fillprofile, section: ",section)
        try:
          newRDPusername=self.config.get(section,"RDPusername")
          newRDPpassword=self.config.get(section,"RDPpassword")
          newRDPdomain=self.config.get(section,"RDPdomain")
          newRDPServer=self.config.get(section,"RDPServer")
        except (RuntimeError, TypeError, NameError):
          print ("no section ",section)
        except (configparser.NoSectionError):
          print ("no section skip >",section,"<")
          newRDPusername=""
          newRDPdomain=""
          newRDPpassword=""
          newRDPServer=""
        self.RDPusername.setText(newRDPusername)
        self.RDPpassword.setText (newRDPpassword)
        print  ("Fill dbg: ",self.RDPpassword.EchoMode())
        self.RDPpassword.setEchoMode(2)
        print  ("Fill dbg chg: ",self.RDPpassword.EchoMode())
        self.RDPdomain.setText(_translate("RDPGUI",newRDPdomain,None))
        self.RDPprinter   = self.config.getboolean(section,'printer',fallback=True)
        self.RDPBinary    = self.config.get(section, "RDPBinary"        ,fallback=self.config.get("DEFAULT", "RDPBinary"))
        self.RDPExtraFlag = self.config.get(section, "RDPExtraFlags"    ,fallback=self.config.get("DEFAULT", "RDPExtraFlags"))
        self.RDPGeomMode  = self.config.get(section, "RDPGeomMode"      ,fallback=self.config.get("DEFAULT", "RDPGeomMode"))
        self.RDPTaskName  = self.config.get(section, "RDPTaskName"      ,fallback=self.serverBox.currentText())
        self.VariusFlags  = ""
        
        self._RDPDomainFlag   = {
          'rdesktop': "-d ",
          'xfreerdp-old': "-d ",
          'xfreerdp': "/d:"
        }
        self._RDPPasswordFlag = {
          'rdesktop': "-p ",  
          'xfreerdp-old': "-p ",
          'xfreerdp': "/p:"
        }
        self._RDPUserFlag     = {
          'rdesktop': "-u ",
          'xfreerdp-old': "-u ",
          'xfreerdp': "/u:"
        }
        self._RDPServerFlag   = {
          'rdesktop': "",
          'xfreerdp-old': "",
          'xfreerdp': "/v:"
        }        
#TODO
        self._RDPunsecureFlag  = {
          'rdesktop': " ",
          'xfreerdp-old': "--ignore-certificate",
          'xfreerdp': "/cert-ignore"
        }
#TODO
        self._RDPallprinterFlag  = {
          'rdesktop': " ",
          'xfreerdp-old': "",
          'xfreerdp': "/printer"
        }
        self._RDPDefaulfFlag  = {
          'rdesktop': " ",
          'xfreerdp-old': "",
          'xfreerdp': "+clipboard -decorations"
        }
        self._RDPWinTitleFlag  = {
          'rdesktop': "-T",
          'xfreerdp-old': "-T",
          'xfreerdp': "/t:"
        }
        self.RDPExec         = {
          'rdesktop': "rdesktop",
          'xfreerdp-old': "xfreerdp",
          'xfreerdp': 'xfreerdp'
        }

        if self.RDPBinary=='xfreerdp':
          try:
             with open('/etc/systemd/system/sockets.target.wants/pcscd.socket') as f:
               self.VariusFlags  = "/smartcard"
          except IOError as e:
             print('no systemd socket for pcscd file')
        if self.RDPprinter:
           self.VariusFlags=self.VariusFlags + " " + self._RDPallprinterFlag.get(self.RDPBinary, '') + " " + self._RDPWinTitleFlag.get(self.RDPBinary, '') + self.RDPTaskName
        self.VariusFlags=self.VariusFlags + " " + self._RDPunsecureFlag.get(self.RDPBinary,'')
        self.FillGeomArgs()

    def handleChanged(self, text):
                print('handleChanged: %s' % text)
                print ("index value:", self.serverBox.currentIndex())
                self.FillProfile(text)


    def changeSBIndex(self):
        index = self.serverBox.currentIndex()
        print ("changeIndex started for ",index)        
        if index < self.serverBox.count() - 1:
            self.serverBox.setCurrentIndex(index + 1)
        else:
            self.serverBox.setCurrentIndex(0)
        

    def handleActivated(self, text):
        print('handleActivated: %s' % text)


    def handleChangedBox(self, text):
        print('handleChangedBOX: %s' % text)

    def checkdomain(self):
        print ("chkdomain")
	#updating DOMAIN label if domain in. ex: DOMAIN\username
        if str(self.RDPusername.text()).find("\\") > 0:
                self.RDPdomain.setText(_translate("RDPGUI", str(self.RDPusername.text()).split('\\')[0], None))
        else:
                config = configparser.ConfigParser()
                config.read('rdpgui.ini')
                self.RDPdomain.setText(_translate("RDPGUI", config.get("DEFAULT", "RDPDomain"), None))

    def doExitNow(self):
        print ("DoExitNow")
        sys.exit(app.exec_());

    def FillGeomArgs(self):
        if (self.RDPGeomMode == "FullScreen"):
            RDPFS_choices = {'xfreerdp': '/f', 'xfreerdp-old': '-f', 'rdesktop': '-f'}
            self._RDPGeomFlags=RDPFS_choices.get(self.RDPBinary, '')
        elif ( self.RDPGeomMode == "WorkSpace"):
            panh=0
            panw=0
            for panelwindow in 'lxqt-panel', 'xfce4-panel', 'Plasma':
                PG_cmd="xwininfo -name "+panelwindow
                print ("will run: ",PG_cmd)
                try:
                    proc = subprocess.Popen(PG_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                except:
                   print ("no window "+panelwindow)
                else:
                   count=0
                   for output in proc.stdout.readlines():
                      count=count+1
                      if output == '' and proc.poll() is not None:
                        break
                      if count == 20:
                        print ("outCount+++", rc)
                        break
                      if output:
                        result = output.decode().strip().split(':')
##                        print ("==== K=V","key","=",result)
                        if result[0]=="Width":
                            cw=int(result[1])
#                            print ("found Width", str(cw),'/',result[1])
                            if cw > panw:
                               panw=cw
                        if result[0]=="Height":
#                            print ("found Width", str(cw),'/',result[1])
                            ch=int(result[1])
                            if ch > panh:
                              panh=ch
                      rc = proc.poll()

                print ("------------------------"+panelwindow+"-----------------------------------")
            RWG_cmd="xwininfo -root"
            print ("will run: ",RWG_cmd)
            try:
                    proc = subprocess.Popen(RWG_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            except:
                   print ("no window --root")
            else:
              count=0
              rooth=0
              rootw=0
              for output in proc.stdout.readlines():
                 count=count+1
                 if output == '' and proc.poll() is not None:
                        break
                 if count == 20:
                        print ("outCount+++", rc)
                        break
                 if output:
                        result = output.decode().strip().split(':')
#                        print ("==== K=V","key","=",result)
                        if result[0]=="Width":
                            cw=int(result[1])
                            if cw > rootw:
                               rootw=cw
                        if result[0]=="Height":
                            ch=int(result[1])
                            if ch > rooth:
                              rooth=ch
                 rc = proc.poll()
              print ("------------------------ root window -----------------------------------")
              print ('following values: panel HxW',panh,'x',panw,' Root window HxW',rooth,'x',rootw)
            ew=rootw-panw
            eh=rooth-panh
            if ew>eh:
               eh=rooth
            else:
               ew=rootw
            print ('result values: app HxW',eh,'x',ew,' Root window HxW',rooth,'x',rootw)               
            RDPWS_choices = {'xfreerdp': "/w:"+str(ew)+" /h:"+str(eh), 
			     'xfreerdp-old': "-g"+str(ew)+"x"+str(eh),
			     'rdesktop': "-g"+str(ew)+"x"+str(eh)
			    }
            self.RDPGeomFlags=RDPWS_choices.get(self.RDPBinary, '')

          
    def handleEnterButton(self):
        print ("run handleButton")
#        config = configparser.ConfigParser()
#        config.read('rdpgui.ini')
#               

#       if [ -L /etc/systemd/system/sockets.target.wants/pcscd.socket ];then
#          XADD="$XADD /smartcard"
##        LServerValue=self.RDPServerFlag + str(self.config.get(self.serverBox.currentText(),"RDPServer",fallback=str(self.serverBox.currentText())))
        commandline=self.RDPExec.get(self.RDPBinary, '') +' '+self.RDPGeomFlags +' ' + self._RDPDomainFlag.get(self.RDPBinary, '') + str(self.RDPdomain.text())  + ' ' + self._RDPUserFlag.get(self.RDPBinary, '') + str(self.RDPusername.text()) + ' '+ self._RDPPasswordFlag.get(self.RDPBinary, '') + str(self.RDPpassword.text()) + ' ' + self.RDPExtraFlag + ' ' + self._RDPDefaulfFlag.get(self.RDPBinary, '') + self.VariusFlags + ' ' + self._RDPServerFlag.get(self.RDPBinary, '') + str(self.config.get(self.serverBox.currentText(),"RDPServer",fallback=str(self.serverBox.currentText()))) 
	#cleaning dquote from confi.ini params
        commandline = re.sub('["]','',commandline)
        print ("Will run:", commandline)
        proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out, err) = proc.communicate()
        print ("-------------------------------------------------------------")
        print (out)
        if out.decode().find("Authentication failure, check credentials") > 0:
                print ("Authentication failure!")
                self.version.setText(_translate("RDPGUI", "Auth Error...", None))
                self.label.setText(_fromUtf8("Wrong username or password!"))
        elif out.decode().find("getaddrinfo (System error)") > 0 or out.decode().find("getaddrinfo: System error") >= 0:
                print ("Error connecting to server!")
                self.version.setText(_translate("RDPGUI", "Server Error...", None))
                self.label.setText(_fromUtf8("Server Error, call your sysadmin"))
        elif out.decode().find("unable to connect to") >= 0 or out.decode().find("A Remote Desktop Protocol client") >= 0:
                print ("Error connecting to server!")
                self.version.setText(_translate("RDPGUI", "Server Error...", None))
                self.label.setText(_fromUtf8("Server Error, call your sysadmin"))
        else:
                self.RDPusername.setText(_translate("RDPGUI", "", None))
                self.RDPpassword.setText(_translate("RDPGUI", "", None))
                self.version.setText(_translate("RDPGUI", "rpi-tc rdp gui v1", None))
                self.RDPdomain.setText(_translate("RDPGUI", config.get("DEFAULT", "RDPDomain"), None))
                self.label.setText(_fromUtf8(""))

def centreWidget(self):
    screen = QtGui.QDesktopWidget().screenGeometry()
    mysize = self.geometry()
    hpos = ( screen.width() - mysize.width() ) / 2
    vpos = ( screen.height() - mysize.height() ) / 2
    self.move(hpos, vpos)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RDPGUI = QtGui.QWidget()
    ui = Ui_RDPGUI(RDPGUI)
#    ui.setupUi(RDPGUI)
    print ("setup done")
    RDPGUI.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    RDPGUI.show()
    print ("RDPG show done")
    RDPGUI.setFixedSize(RDPGUI.size());
    sys.exit(app.exec_())
