import sys
from PyQt5 import QtGui

def window():
   app = QtGui.QApplication(sys.argv)
   tabs = QtGui.QTabWidget(None)
   tabs.setWindowTitle('OpenCV playgrounds')
   tabs.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()