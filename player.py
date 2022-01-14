from  pygame import  mixer
import random ,os, sys, mutagen
import getpass  
from PyQt5 import uic
from PyQt5.QtWidgets import  QMainWindow , QApplication

class player(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/player.ui", self)
        self.btnPlay.clicked.connect(self.reproducir)
        self.btnPause.clicked.connect(self.pausar)



        self.direction = "C:/Users/" + str(getpass.getuser()) + "/mymusic"
        self.fileCreation(self.direction)
        self.printData(self.direction)

        self.playingMusic = False

        

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


    def reproducir(self):
        files = os.listdir(self.direction)
        item = self.lstScreen.currentRow()
        pathSong = self.direction + "/" +  files[item]
        mixer.init()
        mixer.music.load(pathSong)
        mixer.music.play()
        self.playingMusic = True

        audioLeng = mutagen.File(pathSong)
        time_song = audioLeng.info.length
        minuts, seconds = divmod(time_song, 60)
        time = int(minuts) * 60 + int(seconds)
        print(time)
        print(str(minuts) + " : " + str(seconds)) 

    
    def pausar(self):
        if self.playingMusic:
            mixer.music.pause()
            self.playingMusic = False
        else:
            mixer.music.unpause()
            self.playingMusic = True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = player()
    obj.show()
    sys.exit(app.exec_())
