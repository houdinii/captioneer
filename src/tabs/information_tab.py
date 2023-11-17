from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser


class InformationTab(QWidget):
    def __init__(self, app, configuration):
        super().__init__()

        self.module = "information_tab"

        self.app = app
        self.configuration = configuration

        self.layout = QVBoxLayout()
        self.setup_ui(self.layout)
        self.setLayout(self.layout)

    def setup_ui(self, layout: QVBoxLayout):
        """Set up UI controls in the layout"""

        infoText = """
            <strong>This is the Information Tab</strong>
            <p>This tab shows general information about the program.</p>
            <p>You can add markdown text here to explain things.</p>
        """

        info_browser = QTextBrowser()
        info_browser.setHtml(infoText)
        self.layout.addWidget(info_browser)
