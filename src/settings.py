from PyQt5.QtCore import QSettings


class Settings:
    def __init__(self):
        super().__init__()

        self.module = "settings"

        self.darkmode = True
        self.image_tagger_folder = ""

        self.settings = QSettings("./settings.ini", QSettings.IniFormat)
        self.load_settings()

    def save_settings(self):
        print("Saving Settings...")
        self.settings.setValue("darkmode", self.darkmode)
        self.settings.sync()

    def load_settings(self):
        self.darkmode = self.settings.value("darkmode") == "true"
        self.image_tagger_folder = self.settings.value("image_tagger_folder")
