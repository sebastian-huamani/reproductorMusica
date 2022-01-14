import sys
import playsound
import os
import getpass  
from PyQt5 import uic
from PyQt5.QtWidgets import  QMainWindow , QApplication

class player(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/player.ui", self)
        self.btnActionPlayPause.clicked.connect(self.actionPlayPause)
        self.direction = "C:/Users/" + str(getpass.getuser()) + "/mymusic"
        self.fileCreation(self.direction)
        self.printData(self.direction)
        self.__selectSong = 0
        

    def fileCreation(self, path):
        try:
            os.mkdir(path)
            print("Bienvenido por Primera Vez")
        except OSError:
            print("Bienvenido de nuevo")
            return

    def printData(self,path):       
        files = os.listdir(path)
        for file in files:
            position = files.index(file)
            self.lstScreen.insertItem(position,file)


    def actionPlayPause(self):
        files = os.listdir(self.direction)
        item = self.lstScreen.currentRow()
        # playsound.playsound('music.mp3', True)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = player()
    obj.show()
    sys.exit(app.exec_())
