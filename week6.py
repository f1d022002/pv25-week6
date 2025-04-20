import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSlider, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class FontColorApp(QWidget):
    def __init__(self):
        super().__init__()
        
      
        self.setWindowTitle('Penyesuaian')
        self.setGeometry(100, 100, 500, 300)
        
        # Create layout and label
        self.layout = QVBoxLayout()
        self.label = QLabel('NIM: F1D022002', self)  # Change NIM to your own
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

    
        self.font_size_slider = QSlider(Qt.Horizontal)
        self.font_size_slider.setRange(20, 60)
        self.font_size_slider.setValue(20)
        self.font_size_slider.setTickPosition(QSlider.TicksBelow)
        self.font_size_slider.setTickInterval(5)
        self.font_size_slider.valueChanged.connect(self.update_font_size)
        self.layout.addWidget(self.font_size_slider)
        
       
        self.font_color_slider = QSlider(Qt.Horizontal)
        self.font_color_slider.setRange(0, 255)
        self.font_color_slider.setValue(0)
        self.font_color_slider.valueChanged.connect(self.update_font_color)
        self.layout.addWidget(self.font_color_slider)

        
        self.bg_color_slider = QSlider(Qt.Horizontal)
        self.bg_color_slider.setRange(0, 255)
        self.bg_color_slider.setValue(255)
        self.bg_color_slider.valueChanged.connect(self.update_bg_color)
        self.layout.addWidget(self.bg_color_slider)

       
        self.student_info = QLabel('Nama: Andi Sibwayiq Abi Mahmud | NIM: F1D022002', self)
        self.student_info.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.student_info)

       
        self.setLayout(self.layout)

    def update_font_size(self):
        font_size = self.font_size_slider.value()
        self.label.setStyleSheet(f'font-size: {font_size}pt;')

    def update_font_color(self):
        color_value = self.font_color_slider.value()
        font_color = QColor(color_value, color_value, color_value).name()
        self.label.setStyleSheet(f'color: {font_color};')

    def update_bg_color(self):
        color_value = self.bg_color_slider.value()
        bg_color = QColor(color_value, color_value, color_value).name()
        self.label.setStyleSheet(f'background-color: {bg_color};')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontColorApp()
    window.show()
    sys.exit(app.exec_())
