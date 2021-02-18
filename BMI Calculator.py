from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIcon, QFont, QPixmap

class Calculator:
    def __init__(self):
        # Create frame
        frame = QFrame()
        vb.addWidget(frame)

        # Add label
        form = QFormLayout(frame)
        bmi = QLabel('Body Mass Index\nCalculator')
        bmi.setFont(QFont('Forte', 34))
        bmi.setStyleSheet('color:blue;')
        bmi.setAlignment(Qt.AlignCenter)
        form.addRow(bmi)
        Weight = QLabel('Weight in (kg): ')
        Height = QLabel('Height in (m): ')
        Result = QLabel('Result (kg/m²): ')

        # Add entry field
        self.weight = QLineEdit()
        form.addRow(Weight, self.weight)
        self.height = QLineEdit()
        form.addRow(Height, self.height)
        self.result = QLineEdit()
        self.result.setReadOnly(True)
        self.result.setMaxLength(6)

        # Add button
        btn = QPushButton('Submit', clicked=self.process)
        btn.setToolTip('click to submit')
        form.addRow(btn)
        form.addRow(Result, self.result)

    def process(self):
        if len(self.weight.text()) < 1 or len(self.height.text()) < 1:
            QMessageBox.critical(win, 'Error Message', 'Error: Input required!')
        else:
            w = float(self.weight.text())
            h = float(self.height.text())
            BMI = w/h**2
            self.result.setText(str(BMI))
            if BMI < 18.5:
                QMessageBox.information(win, 'Status', "You are 'Under Weight'")
            elif BMI < 24.9:
                QMessageBox.information(win, 'Status', "You are 'Normal Weight'")
            elif BMI < 29.9:
                QMessageBox.warning(win, 'Status', "Warning!: You are 'Pre-obesity'")
            elif BMI < 34.9:
                QMessageBox.warning(win, 'Status', "Risk!: You are 'Obesity Class 1'")
            elif BMI < 39.9:
                QMessageBox.critical(win, 'Status', "High Risk!: You are 'Obesity Class 2'")
            else:
                QMessageBox.critical(win, 'Status', "Danger!: You are 'Obesity Class 3'")
            self.result.clear()


app = QApplication([])
app.setStyle('Fusion')

# Set window and widget color
qp = QPalette()
qp.setColor(QPalette.Window, Qt.magenta)
qp.setColor(QPalette.Button, Qt.blue)
app.setPalette(qp)

# Create window
win = QWidget()
win.setFixedSize(400,350)
win.setWindowTitle('BMI Calculator')
win.setWindowIcon(QIcon('C:/Users/Hp/Desktop/BMI Calculator/images/BMI.png'))
win.setFont(QFont('Arial Bold', 20))

# Create menu bar
vb = QVBoxLayout(win)
bar = QMenuBar()
bar.setNativeMenuBar(False)
Menu = bar.addMenu("≡ Menu")
vb.addWidget(bar)

# Add menu item
def about():
    dialog = QDialog()
    dialog.setWindowTitle('About')
    dialog.setFont(QFont('Arial Bold', 10))
    dialog.setFixedSize(250,300)
    vb = QVBoxLayout(dialog)
    fme = QFrame()
    vb.addWidget(fme)
    grid = QGridLayout(fme)
    image = QPixmap("C:/Users/Hp/Desktop/BMI Calculator/images/BMI.png")
    iproduct = QLabel()
    iproduct.setPixmap(image)
    iproduct.setScaledContents(True)
    iproduct.setFixedSize(70,50)
    grid.addWidget(iproduct, 0,0)
    
    product = QLabel('Body Mass\nIndex Calc.')
    product.setFont(QFont('Forte', 18))
    product.setStyleSheet('color:blue;')
    grid.addWidget(product, 0,1)

    frame = QGroupBox('Developed by:')
    vb.addWidget(frame)
    form = QFormLayout(frame)
    details = QLabel('Name: Peter Oyelegbin \n\nWhatsApp: 08078828296 \n\nGmail: peteroyelegbin@gmail.com \n\n© 2020')
    form.addRow(details)

    close = QPushButton('Close', clicked=dialog.close)
    vb.addWidget(close)
    dialog.exec_()
    
About = QAction("About", triggered=about)
Menu.addAction(About)

Quit = QAction("Quit", triggered=win.close)
Quit.setShortcut('Ctrl+Q')
Quit.setStatusTip('Exit application')
Menu.addAction(Quit)

BMI = Calculator()

win.show()
app.exec_()
