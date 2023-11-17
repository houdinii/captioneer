from PyQt5.QtWidgets import QTabWidget

from src.tabs.image_tagger_tab import ImageTaggerTab
from src.tabs.information_tab import InformationTab
from src.tabs.settings_tab import SettingsTab


class Tabs(QTabWidget):
    def __init__(self, app, configuration):
        super().__init__()

        self.module = "tab_layout"

        self.app = app
        self.configuration = configuration

        self.settings_tab = SettingsTab(app=self.app, configuration=self.configuration)
        self.information_tab = InformationTab(
            app=self.app, configuration=self.configuration
        )
        self.image_tagger_tab = ImageTaggerTab(
            app=self.app, configuration=self.configuration
        )

        self.addTab(self.information_tab, "Information")
        self.addTab(self.image_tagger_tab, "Image Tagger")
        self.addTab(self.settings_tab, "Settings")
