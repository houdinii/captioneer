import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget,
    QFileDialog,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QTextEdit,
)


class ImageTaggerTab(QWidget):
    def __init__(self, app, configuration):
        super().__init__()

        self.module = "image_tagger_tab"

        self.app = app
        self.configuration = configuration

        self.image_dir = self.configuration.image_tagger_folder

        self.index = 0
        self.text_modified = False
        self.image_text_map = {}

        # Track image/text pairs
        if self.image_dir:
            for f in os.listdir(self.image_dir):
                if f.endswith(".jpg") or f.endswith(".png"):
                    name, ext = os.path.splitext(f)
                    text_file = name + ".txt"
                    self.image_text_map[f] = text_file

        # UI elements
        self.image_label = QLabel()
        self.text_edit = QTextEdit()

        self.prev_button = QPushButton("Previous")
        self.save_button = QPushButton("Save")
        self.next_button = QPushButton("Next")

        # Layout
        image_text_layout = QHBoxLayout()
        image_text_layout.addWidget(self.image_label)
        image_text_layout.addWidget(self.text_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.next_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(image_text_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Folder selection
        self.folder_text = QLineEdit()
        self.folder_button = QPushButton("Browse")

        self.folder_text.setText(self.configuration.image_tagger_folder)

        folder_layout = QHBoxLayout()
        folder_layout.addWidget(self.folder_text)
        folder_layout.addWidget(self.folder_button)

        main_layout.insertLayout(0, folder_layout)

        # Connect signals
        # noinspection PyUnresolvedReferences
        self.prev_button.clicked.connect(self.prev_image)
        # noinspection PyUnresolvedReferences
        self.next_button.clicked.connect(self.next_image)
        # noinspection PyUnresolvedReferences
        self.text_edit.textChanged.connect(self.set_text_modified)
        # noinspection PyUnresolvedReferences
        self.save_button.clicked.connect(self.save_text)
        # noinspection PyUnresolvedReferences
        self.folder_button.clicked.connect(self.select_folder)

        # Display first image
        self.display_image()

    def select_folder(self):
        dialog = QFileDialog()
        start_dir = self.folder_text.text()
        folder = dialog.getExistingDirectory()
        self.folder_text.setText(folder)

        self.configuration.folder = folder
        # self.settings.setValue("folder", folder)

        print(f"New folder: {self.configuration.folder}")

        self.display_image()
        self.configuration.save_settings()
        # self.settings.sync()

    def save_text(self, text):
        pass

    def display_image(self):
        text_file = ""
        text = ""
        # Load image and text

        if self.index < len(self.image_text_map):
            filename = sorted(self.image_text_map)[self.index]
            text_file = self.image_text_map[filename]
            pixmap = QPixmap(os.path.join(self.image_dir, filename))
            self.image_label.setPixmap(pixmap)

        if text_file:
            try:
                with open(os.path.join(self.image_dir, text_file)) as f:
                    text = f.read()
            except FileNotFoundError as e:
                print(e)

        self.text_edit.setPlainText(text)

    def prev_image(self):
        pass

    def next_image(self):
        pass

    def set_text_modified(self):
        pass
