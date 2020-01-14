from PyQt5.QtWidgets import QApplication, QGroupBox, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QScrollArea, QLabel, QLineEdit, QFrame
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap, QFontDatabase, QFont
from PyQt5 import QtGui, QtCore
import sys


class Colors(QWidget):
    def __init__(self):
        self.colorGRAY = "color:#7A7A7A;"
        self.colorRED = "color:#970000;"
        
class Fonts(QWidget):
    def __init__(self):
        _id = QFontDatabase.addApplicationFont("BwSeidoRound-Medium.ttf")
        Fonte = QtGui.QFontDatabase.applicationFontFamilies(_id)[0]
        
        self.font_14 = QtGui.QFont(Fonte, 14)
        self.font_14B = QtGui.QFont(Fonte, 14)
        self.font_14B.setBold(True)
        self.font_12 = QtGui.QFont(Fonte, 12)
        self.font_12B = QtGui.QFont(Fonte, 12)
        self.font_12B.setBold(True)


class Images(QWidget):
    def __init__(self):
        self.fonts = Fonts()
        self.colors = Colors()
        self.initImages()
        self.initLabels()
    
    def initImages(self):
        pixmapMercado = QPixmap("icons/mercado.png")
        self.lImgMercado = QLabel()
        self.lImgMercado.resize(50,50)
        self.lImgMercado.setPixmap(pixmapMercado.scaled(self.lImgMercado.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgMercado.setStyleSheet("background-color:white;")
            
        pixmapLanche = QPixmap("icons/lanche.png")
        self.lImgLanche = QLabel()
        self.lImgLanche.resize(50,50)
        self.lImgLanche.setPixmap(pixmapLanche.scaled(self.lImgLanche.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgLanche.setStyleSheet("background-color:white;")

        pixmapAcai = QPixmap("icons/acai.png")
        self.lImgAcai = QLabel()
        self.lImgAcai.resize(50,50)
        self.lImgAcai.setPixmap(pixmapAcai.scaled(self.lImgAcai.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgAcai.setStyleSheet("background-color:white;")

        pixmapPizza = QPixmap("icons/pizza.png")
        self.lImgPizza = QLabel()
        self.lImgPizza.resize(50,50)
        self.lImgPizza.setPixmap(pixmapPizza.scaled(self.lImgPizza.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgPizza.setStyleSheet("background-color:white;")

        pixmapConveniencia = QPixmap("icons/conveniencia.png")
        self.lImgConveniencia = QLabel()
        self.lImgConveniencia.resize(50,50)
        self.lImgConveniencia.setPixmap(pixmapConveniencia.scaled(self.lImgConveniencia.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgConveniencia.setStyleSheet("background-color:white;")

        pixmapPromo1 = QPixmap("icons/imgPromo1.png")
        self.lImgPromo1 = QLabel()
        self.lImgPromo1.resize(247,247)
        self.lImgPromo1.setPixmap(pixmapPromo1.scaled(self.lImgPromo1.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgPromo1.setStyleSheet("background-color:white;")

        pixmapPromo2 = QPixmap("icons/imgPromo2.png")
        self.lImgPromo2 = QLabel()
        self.lImgPromo2.resize(247,247)
        self.lImgPromo2.setPixmap(pixmapPromo2.scaled(self.lImgPromo2.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgPromo2.setStyleSheet("background-color:white;")

        pixmapPromo3 = QPixmap("icons/imgPromo3.png")
        self.lImgPromo3 = QLabel()
        self.lImgPromo3.resize(247,247)
        self.lImgPromo3.setPixmap(pixmapPromo3.scaled(self.lImgPromo3.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgPromo3.setStyleSheet("background-color:white;")

        pixmapInit = QPixmap("icons/home.png")
        self.lImgInit = QLabel()
        self.lImgInit.resize(30,30)
        self.lImgInit.setPixmap(pixmapInit.scaled(self.lImgInit.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgInit.setStyleSheet("background-color:white;")
        
        pixmapBuscar = QPixmap("icons/searchG.png")
        self.lImgBuscar = QLabel()
        self.lImgBuscar.resize(30,30)
        self.lImgBuscar.setPixmap(pixmapBuscar.scaled(self.lImgBuscar.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgBuscar.setStyleSheet("background-color:white;")

        pixmapPedidos = QPixmap("icons/lis.png")
        self.lImgPedidos = QLabel()
        self.lImgPedidos.resize(30,30)
        self.lImgPedidos.setPixmap(pixmapPedidos.scaled(self.lImgPedidos.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgPedidos.setStyleSheet("background-color:white;")

        pixmapPerfil = QPixmap("icons/perfil.png")
        self.lImgPerfil = QLabel()
        self.lImgPerfil.resize(30,30)
        self.lImgPerfil.setPixmap(pixmapPerfil.scaled(self.lImgPerfil.size(), QtCore.Qt.KeepAspectRatio))
        self.lImgPerfil.setStyleSheet("background-color:white;")

    def initLabels(self):

        self.labelMercado = QLabel("Mercado")
        self.labelMercado.setStyleSheet("background-color:white;")
        self.labelMercado.setFont(self.fonts.font_12B)

        self.labelLanche = QLabel("Lanche")
        self.labelLanche.setStyleSheet("background-color:white;")
        self.labelLanche.setFont(self.fonts.font_12B)

        self.labelAcai = QLabel("Açaiteria")
        self.labelAcai.setStyleSheet("background-color:white;")
        self.labelAcai.setFont(self.fonts.font_12B)

        self.labelPizza = QLabel("Pizza")
        self.labelPizza.setStyleSheet("background-color:white;")
        self.labelPizza.setFont(self.fonts.font_12B)

        self.labelConveniencia = QLabel("Coveniência")
        self.labelConveniencia.setStyleSheet("background-color:white;")
        self.labelConveniencia.setFont(self.fonts.font_12B)

        self.labelHome = QLabel("Início")
        self.labelHome.setStyleSheet("background-color:white;")
        self.labelHome.setFont(self.fonts.font_12B)
        self.labelHome.setStyleSheet(self.colors.colorGRAY)

        self.labelPesquisa = QLabel("Busca")
        self.labelPesquisa.setStyleSheet("background-color:white;")
        self.labelPesquisa.setFont(self.fonts.font_12B)
        self.labelPesquisa.setStyleSheet(self.colors.colorGRAY)

        self.labelPedidos = QLabel("Pedidos")
        self.labelPedidos.setStyleSheet("background-color:white;")
        self.labelPedidos.setFont(self.fonts.font_12B)
        self.labelPedidos.setStyleSheet(self.colors.colorGRAY)

        self.labelPerfil = QLabel("Perfil")
        self.labelPerfil.setStyleSheet("background-color:white;")
        self.labelPerfil.setFont(self.fonts.font_12B)
        self.labelPerfil.setStyleSheet(self.colors.colorGRAY)


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.title = "Ifood"
        self.top = 100
        self.left = 200
        self.width = 340
        self.height = 600 #altura
        
        self.initUI()
        self.imgs = Images()
        self.fonts = Fonts()
        self.colors = Colors()
        
        


        self.topleft = QFrame(self)
        self.topleft.move(11, 130)
        self.verticalBox = QVBoxLayout(self.topleft)        
        self.verticalBox.setContentsMargins(0,0,0,0)
        # self.verticalBox.setSpacing(-100)
        # self.verticalBox.spacing()
          

        self.initTop()
        self.initBoxTop()
        self.initBoxMiddle()
        self.initBoxBottom()
        self.initBottom()
            
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
 
    def initTop(self):
        labelEntrega = QLabel(self)
        labelEntrega.setText("Entrega")
        labelEntrega.move(20,5)
        labelEntrega.setFont(self.fonts.font_14B)
        labelEntrega.setStyleSheet(self.colors.colorRED)

        labelRua = QLabel(self)
        labelRua.setText("R. número tal")
        labelRua.resize(150,35)
        labelRua.move(20,30)
        labelRua.setFont(self.fonts.font_14B)
        

        bPesquisa = QPushButton(self)
        bPesquisa.setIcon(QtGui.QIcon("icons/search2.png"))
        bPesquisa.setIconSize(QtCore.QSize(30, 30))
        bPesquisa.resize(30,30)
        bPesquisa.setStyleSheet("border:0;")
        bPesquisa.move(20, 80)

        edit = QLineEdit(self)
        edit.resize(self.width-100, 30)
        edit.move(70, 80)

    def initBoxTop(self):
        groupBoxOpicoes = QGroupBox()
        scrollOpts = QScrollArea()
     
        gridLayout = QGridLayout()
        gridLayout.setHorizontalSpacing(15)
        
        gridLayout.addWidget(self.imgs.lImgMercado, 0,0, Qt.AlignCenter)
        gridLayout.addWidget(self.imgs.labelMercado, 1,0,Qt.AlignCenter)

        gridLayout.addWidget(self.imgs.lImgLanche, 0,1, Qt.AlignCenter)
        gridLayout.addWidget(self.imgs.labelLanche, 1,1,Qt.AlignCenter)

        gridLayout.addWidget(self.imgs.lImgAcai, 0,2, Qt.AlignCenter)
        gridLayout.addWidget(self.imgs.labelAcai, 1,2, Qt.AlignCenter)

        gridLayout.addWidget(self.imgs.lImgPizza, 0,3, Qt.AlignRight)
        gridLayout.addWidget(self.imgs.labelPizza, 1,3, Qt.AlignCenter)

        gridLayout.addWidget(self.imgs.lImgConveniencia, 0, 4, Qt.AlignCenter)
        gridLayout.addWidget(self.imgs.labelConveniencia, 1,4,Qt.AlignCenter)

        groupBoxOpicoes.setLayout(gridLayout)

        scrollOpts.setWidget(groupBoxOpicoes)
        
        self.verticalBox.addWidget(scrollOpts)

        scrollOpts.setWidgetResizable(True)
        scrollOpts.setFixedHeight(103)
        scrollOpts.setFixedWidth(self.width)
        scrollOpts.setFrameShape(0)
        scrollOpts.setStyleSheet("border:0;")
        scrollOpts.setStyleSheet("background-color:white;")

       
    def initBoxMiddle(self):
        groupBoxPromo = QGroupBox()
        hboxPromos = QHBoxLayout()
        scrollPromos = QScrollArea()
        
        hboxPromos.addWidget(self.imgs.lImgPromo1)
        hboxPromos.addWidget(self.imgs.lImgPromo2)
        hboxPromos.addWidget(self.imgs.lImgPromo3)
        
        groupBoxPromo.setLayout(hboxPromos)

        scrollPromos.setWidget(groupBoxPromo)

        self.verticalBox.addWidget(scrollPromos)

        scrollPromos.setWidgetResizable(True)
        scrollPromos.setFixedHeight(150)
        scrollPromos.setFixedWidth(self.width)
        scrollPromos.setFrameShape(0)
        scrollPromos.setStyleSheet("border:0;")
        scrollPromos.setStyleSheet("background-color:white;")
        
    def initBoxBottom(self):
        groupBoxRestaurantes = QGroupBox(" Últimos restaurantes")
        groupBoxRestaurantes.setFont(self.fonts.font_12B)
        hboxRests = QHBoxLayout()
        scrollRests = QScrollArea()
        
        bChurras = QPushButton("Churrascaria Bom Apetite", self)
        bChurras.setFont(self.fonts.font_12B)
        bChurras.setIcon(QtGui.QIcon("icons/espeto.png"))
        bChurras.setIconSize(QtCore.QSize(50, 50))
        bChurras.resize(50,100)
        bChurras.setStyleSheet("border:0;")

        bAlmoco = QPushButton("Almoço nota 10", self)
        bAlmoco.setFont(self.fonts.font_12B)
        bAlmoco.setIcon(QtGui.QIcon("icons/almoco.png"))
        bAlmoco.setIconSize(QtCore.QSize(50, 50))
        bAlmoco.resize(50,100)
        bAlmoco.setStyleSheet("border:0;")

        bCafe = QPushButton("Cafeteria Top", self)
        bCafe.setFont(self.fonts.font_12B)
        bCafe.setIcon(QtGui.QIcon("icons/cafeteria.png"))
        bCafe.setIconSize(QtCore.QSize(50, 50))
        bCafe.resize(50,100)
        bCafe.setStyleSheet("border:0;")


        hboxRests.addWidget(bChurras)
        hboxRests.addWidget(bAlmoco)
        hboxRests.addWidget(bCafe)        
        
        groupBoxRestaurantes.setLayout(hboxRests)

        scrollRests.setWidget(groupBoxRestaurantes)

        self.verticalBox.addWidget(scrollRests)

        scrollRests.setWidgetResizable(True)
        scrollRests.setFixedHeight(110)
        scrollRests.setFixedWidth(self.width)
        scrollRests.setFrameShape(0)
        scrollRests.setStyleSheet("border:0;")
        scrollRests.setStyleSheet("background-color:white;")

    def initBottom(self):
        bHome = QPushButton(self)
        bHome.setIcon(QtGui.QIcon("icons/home.png"))
        bHome.setIconSize(QtCore.QSize(30, 30))
        bHome.resize(30,30)
        bHome.setStyleSheet("border:0;")
              
        bPesq = QPushButton(self)
        bPesq.setIcon(QtGui.QIcon("icons/searchG.png"))
        bPesq.setIconSize(QtCore.QSize(30, 30))
        bPesq.resize(30,30)
        bPesq.setStyleSheet("border:0;")

        bPedido = QPushButton(self)
        bPedido.setIcon(QtGui.QIcon("icons/lis.png"))
        bPedido.setIconSize(QtCore.QSize(30, 30))
        bPedido.resize(30,30)
        bPedido.setStyleSheet("border:0;")

        bPerfil = QPushButton(self)
        bPerfil.setIcon(QtGui.QIcon("icons/perfil.png"))
        bPerfil.setIconSize(QtCore.QSize(30, 30))
        bPerfil.resize(30,30)
        bPerfil.setStyleSheet("border:0;")
        
        groupBoxMenu = QGroupBox()     
        gridMenu = QGridLayout()
        scrollMenu = QScrollArea()

        gridMenu.setHorizontalSpacing(1)
        
        gridMenu.addWidget(bHome, 0,0, Qt.AlignLeft)
        gridMenu.addWidget(self.imgs.labelHome, 1,0,Qt.AlignLeft)

        gridMenu.addWidget(bPesq, 0,1, Qt.AlignLeft)
        gridMenu.addWidget(self.imgs.labelPesquisa, 1,1,Qt.AlignLeft)

        gridMenu.addWidget(bPedido, 0,2, Qt.AlignCenter)
        gridMenu.addWidget(self.imgs.labelPedidos, 1,2, Qt.AlignCenter)

        gridMenu.addWidget(bPerfil, 0,3, Qt.AlignRight)
        gridMenu.addWidget(self.imgs.labelPerfil, 1,3, Qt.AlignRight)

        groupBoxMenu.setLayout(gridMenu)

        scrollMenu.setWidget(groupBoxMenu)
        
        self.verticalBox.addWidget(scrollMenu)

        scrollMenu.setWidgetResizable(True)
        scrollMenu.setFixedHeight(80)
        scrollMenu.setFixedWidth(self.width-10)
        scrollMenu.setFrameShape(0)
        scrollMenu.setStyleSheet("border:0;")
        scrollMenu.setStyleSheet("background-color:white;")
        scrollMenu.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

       

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())
