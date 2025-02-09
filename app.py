import sys
import os
from PyQt5 import QtWidgets, QtCore
import yt_dlp

def make_alpha_numeric(string):
    return ''.join(char for char in string if char.isalnum())

class DownloadWorker(QtCore.QThread):
    progress = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(str)
    
    def __init__(self, link, parent=None):
        super().__init__(parent)
        self.link = link

    def run(self):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': False,
            'quiet': False,
            'postprocessors': [
                {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}
            ]
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Extract playlist info without downloading
                playlist_info = ydl.extract_info(self.link, download=False)
                playlist_title = make_alpha_numeric(playlist_info['title'])
                if not os.path.exists(playlist_title):
                    os.mkdir(playlist_title)
                    
                total_count = len(playlist_info['entries'])
                self.progress.emit(f"Total videos: {total_count}")
                
                ydl_opts['outtmpl'] = os.path.join(playlist_title, '%(title)s.%(ext)s')
                with yt_dlp.YoutubeDL(ydl_opts) as ydl2:
                    for i, video in enumerate(playlist_info['entries'], start=1):
                        title = video.get('title', 'Untitled')
                        self.progress.emit(f"Downloading ({i}/{total_count}): {title}")
                        try:
                            ydl2.download([video['webpage_url']])
                        except Exception as e:
                            self.progress.emit(f"Error downloading {title}: {e}")
            self.finished.emit()
        except Exception as e:
            self.error.emit(f"Download failed: {e}")

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Playlist Downloader")
        self.resize(600, 400)
        self.setup_ui()
        self.worker = None

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout()

        # URL input layout
        url_layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Playlist URL:")
        self.url_input = QtWidgets.QLineEdit()
        url_layout.addWidget(label)
        url_layout.addWidget(self.url_input)
        layout.addLayout(url_layout)

        # Download button
        self.btn_download = QtWidgets.QPushButton("Download")
        self.btn_download.clicked.connect(self.on_download)
        layout.addWidget(self.btn_download)

        # Log area
        self.log_area = QtWidgets.QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

        self.setLayout(layout)

    def log(self, message):
        self.log_area.append(message)
        self.log_area.verticalScrollBar().setValue(self.log_area.verticalScrollBar().maximum())

    def on_download(self):
        link = self.url_input.text().strip()
        if not link:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a valid playlist URL.")
            return

        # Disable the Download button while working
        self.btn_download.setEnabled(False)
        self.log("Starting download...")
        
        self.worker = DownloadWorker(link)
        self.worker.progress.connect(self.log)
        self.worker.error.connect(self.handle_error)
        self.worker.finished.connect(self.handle_finished)
        self.worker.start()

    def handle_error(self, err_msg):
        QtWidgets.QMessageBox.critical(self, "Error", err_msg)
        self.btn_download.setEnabled(True)

    def handle_finished(self):
        QtWidgets.QMessageBox.information(self, "Success", "All videos downloaded successfully!")
        self.log("Download complete!")
        self.btn_download.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())