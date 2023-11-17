from PyQt5.QtWidgets import (
    QWidget,
    QCheckBox,
    QFrame,
    QPushButton,
    QGridLayout,
    QLayout,
)

from src.styles.dark_styles import dark_stylesheet
from src.styles.light_styles import light_stylesheet


class SettingsTab(QWidget):
    def __init__(self, app, configuration):
        super().__init__()

        self.module = "settings_tab"

        self.app = app

        self.configuration = configuration

        # Dark mode
        self.dark_mode = QCheckBox("Dark Mode")

        # Separator
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        # Buttons
        self.save_button = QPushButton("Save")

        # Create layout
        layout = QGridLayout()
        self.initUI(layout)

        # Connect signals
        self.connect_signals()

        # Set layout
        self.setLayout(layout)
        self.reloadUI()

    def initUI(self, layout):
        layout.setSizeConstraint(QLayout.SetFixedSize)
        layout.addWidget(self.dark_mode, 1, 0, 1, 3)
        layout.addWidget(self.separator, 2, 0, 1, 3)
        layout.addWidget(self.save_button, 3, 0)

        layout.setVerticalSpacing(10)
        layout.setHorizontalSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

    # noinspection PyUnresolvedReferences
    def connect_signals(self):
        # Connect dark mode checkbox
        self.dark_mode.clicked.connect(self.toggle_darkmode)
        self.save_button.clicked.connect(self.save_clicked)

    def save_clicked(self):
        self.configuration.darkmode = self.dark_mode.isChecked()
        self.configuration.save_settings()

    def reloadUI(self):
        print("Reloading UI...")
        self.dark_mode.setChecked(self.configuration.darkmode)
        self.toggle_darkmode(self.dark_mode.isChecked())

    def toggle_darkmode(self, darkmode):
        if darkmode:
            self.app.setStyleSheet(dark_stylesheet)
        else:
            self.app.setStyleSheet(light_stylesheet)
