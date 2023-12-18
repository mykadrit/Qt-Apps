from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QCheckBox, QLabel
from PyQt6.QtCore import Qt

color = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#8B00FF']
bg_color = 'transparent'

app = QApplication([])

#Создание главного окна
window = QMainWindow()
window.setWindowTitle("Test_App v_0.0.1")
window.setGeometry(100, 100, 610, 360)
#window.setStyleSheet(f"background-color: {bg_color};")
window.setStyleSheet("QMainWindow { background-image: url('app/bg_img.jpg'); }")


sliders = []
checkboxes = []
labels = []


title_label = QLabel("Test App (v_0.0.0)", window)
title_label.setGeometry(235, 10, 610, 30)
title_label.setStyleSheet("""
QLabel {
background-color: transparent;
color: #ffffff;
font-size: 16px;
font-weight: bold;
padding: 5px;
}
""")


for i in range(7):
    slider = QSlider(Qt.Orientation.Vertical, window)
    slider.setGeometry(50 + i * 80, 60, 30, 200)
    sliders.append(slider)


    checkbox = QCheckBox(window)
    checkbox.setGeometry(59 + i * 80, 270, 20, 20)
    checkbox.setStyleSheet("QCheckBox {background-color: " + bg_color + ";border-radius: 10px;}\nQCheckBox::indicator {background-color: #888888;border-radius: 6px;}\nQCheckBox::indicator:checked {background-color: " + color[i] + "}")
    checkboxes.append(checkbox)


    label = QLabel("Slider " + str(i+1), window)
    label.setGeometry(40 + i * 80, 300, 60, 20)
    labels.append(label)


for i, slider in enumerate(sliders):
    slider.setStyleSheet("QSlider {background-color: " + bg_color + ";}\nQSlider::groove:vertical{background-color: #aaaaaa;width: 10px;border-radius: 5px;}\nQSlider::handle:vertical {background-color: " + color[i] + ";height: 20px;width: 20px;margin: 0 -5px;border-radius: 10px;}")


for label in labels:
    label.setStyleSheet("""
    QLabel {
    color: #ffffff;
    }
    """)


window.show()
app.exec()