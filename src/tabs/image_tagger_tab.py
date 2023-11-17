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
        self.app = app
        self.configuration = configuration
        self.initialize_variables()
        self.setup_ui()
        self.connect_signals()
        self.load_image_text_map()
        self.display_first_image()

    def initialize_variables(self):
        self.module = "image_tagger_tab"
        self.image_dir = self.configuration.image_tagger_folder
        self.index = 0
        self.text_modified = False
        self.image_text_map = {}

    def setup_ui(self):
        self.setup_image_text_ui()
        self.setup_button_ui()
        self.setup_folder_ui()
        self.setup_main_layout()

    def setup_image_text_ui(self):
        self.image_label = QLabel()
        self.text_edit = QTextEdit()
        self.image_text_layout = QHBoxLayout()
        self.image_text_layout.addWidget(self.image_label)
        self.image_text_layout.addWidget(self.text_edit)

    def setup_button_ui(self):
        self.prev_button = QPushButton("Previous")
        self.save_button = QPushButton("Save")
        self.next_button = QPushButton("Next")
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.next_button)

    def setup_folder_ui(self):
        self.folder_text = QLineEdit()
        self.folder_button = QPushButton("Browse")
        self.folder_text.setText(self.configuration.image_tagger_folder)
        self.folder_layout = QHBoxLayout()
        self.folder_layout.addWidget(self.folder_text)
        self.folder_layout.addWidget(self.folder_button)

    def setup_main_layout(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.image_text_layout)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.insertLayout(0, self.folder_layout)
        self.setLayout(self.main_layout)

    # noinspection PyUnresolvedReferences
    def connect_signals(self):
        self.prev_button.clicked.connect(self.prev_image)
        self.next_button.clicked.connect(self.next_image)
        self.text_edit.textChanged.connect(self.set_text_modified)
        self.save_button.clicked.connect(self.save_text)
        self.folder_button.clicked.connect(self.select_folder)

    def load_image_text_map(self):
        if self.image_dir:
            for f in os.listdir(self.image_dir):
                if f.endswith(".jpg") or f.endswith(".png"):
                    name, ext = os.path.splitext(f)
                    text_file = name + ".txt"
                    self.image_text_map[f] = text_file

    def display_first_image(self):
        self.display_image()

    def select_folder(self):
        dialog = QFileDialog()
        start_dir = self.folder_text.text()
        folder = dialog.getExistingDirectory(self, "Select Folder", start_dir)

        if folder:  # Check if a folder was selected
            self.folder_text.setText(folder)
            self.configuration.folder = folder
            print(f"New folder: {self.configuration.folder}")

            self.image_dir = folder  # Update the image directory
            self.index = 0  # Reset index to start from the first image
            self.load_image_text_map()  # Load new images and texts
            self.display_image()  # Display the first image from the new folder

            self.configuration.save_settings()

    def set_text_modified(self):
        self.text_modified = True

    def save_text(self):
        if not self.text_modified:
            return  # No changes to save

        if self.index < len(self.image_text_map):
            filename = sorted(self.image_text_map)[self.index]
            text_file = self.image_text_map[filename]
            text_path = os.path.join(self.image_dir, text_file)

            text_to_save = self.text_edit.toPlainText()

            try:
                with open(text_path, "w") as file:
                    file.write(text_to_save)
                print(f"Saved text for {filename}")
                self.text_modified = False  # Reset the flag after saving
            except Exception as e:
                print(f"Error saving text for {filename}: {e}")

    def display_image(self):
        text_file = ""
        text = ""
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
        self.text_modified = False  # Reset the modification flag

    def prev_image(self):
        if len(self.image_text_map) > 0:
            self.save_text()
            # Decrement index and wrap around if necessary
            self.index = (self.index - 1) % len(self.image_text_map)
            self.display_image()

    def next_image(self):
        if len(self.image_text_map) > 0:
            self.save_text()
            # Increment index and wrap around if necessary
            self.index = (self.index + 1) % len(self.image_text_map)
            self.display_image()
