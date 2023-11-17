import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from src.settings import Settings
from src.tab_layout import Tabs
from src.tabs.image_tagger_tab import ImageTaggerTab
from src.tabs.settings_tab import SettingsTab
from src.tabs.information_tab import InformationTab


class CaptioneerApp:
    def __init__(self, sys_argv):
        super().__init__()
        self.app = QApplication(sys_argv)

        self.module = "app"

        # Settings
        self.configuration = Settings()

        # Tabs
        self.tabs = Tabs(app=self.app, configuration=self.configuration)

        self.settings_tab = SettingsTab(app=self.app, configuration=self.configuration)
        self.tabs.settings_tab = self.settings_tab

        self.information_tab = InformationTab(
            app=self.app, configuration=self.configuration
        )
        self.tabs.information_tab = self.information_tab

        self.image_tagger_tab = ImageTaggerTab(
            app=self.app, configuration=self.configuration
        )
        self.tabs.image_tagger_tab = self.image_tagger_tab

        # Main window
        self.window = QMainWindow()
        self.window.setCentralWidget(self.tabs)

        self.initUI()

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())

    def initUI(self):
        # Set the minimum width and height of the window
        self.window.setMinimumWidth(800)  # Set the minimum width to 400 pixels
        self.window.setMinimumHeight(600)  # Set the minimum height to 300 pixels

        self.window.setWindowTitle("Captioneer - v.0.0.1")
        self.window.show()


app = CaptioneerApp(sys.argv)
app.run()
