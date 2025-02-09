# [YouTube Playlist Downloader ✨](https://github.com/DhananjayPorwal/youtube-playlist-downloader/releases/download/v2.0/youtube-playlist-downloader.zip)

![youtube-playlist-downloader](https://socialify.git.ci/DhananjayPorwal/youtube-playlist-downloader/image?font=Jost&forks=1&issues=1&language=1&logo=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F0%2F09%2FYouTube_full-color_icon_%25282017%2529.svg%2F120px-YouTube_full-color_icon_%25282017%2529.svg.png&name=1&owner=1&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Auto)

This repository contains a Python project for downloading all the videos from a YouTube playlist. The project now includes both a Command Line Interface (CLI) and a Graphical User Interface (GUI) built with PyQt5. The original script has been updated to use `yt_dlp` (instead of the outdated `pytube`) to handle the download and conversion process.

## Features

- **Playlist Downloads:** Downloads all videos from a given YouTube playlist URL.
- **Folder Naming:** Converts the playlist title into an alphanumeric folder name to store downloaded videos.
- **High Resolution:** Downloads each video with the highest available resolution.
- **CLI and GUI:** Choose between the CLI version (using `playlist_downloader.py`) or the GUI version (`app.py`) for intuitive operation.
- **Real-Time Updates:** The GUI provides real-time download progress and error reporting.
- **Executable Build:** Easily build an executable using PyInstaller.

<p align="center" width="100%">
  <img src="https://raw.githubusercontent.com/DhananjayPorwal/youtube-playlist-downloader/main/image.png" alt="GUI Screenshot" />
</p>

## Installation

1. Clone the repository:

```bash
git clone https://github.com/DhananjayPorwal/youtube-playlist-downloader.git
```

2. Change into the project directory:

```bash
cd youtube-playlist-downloader/youtube-playlist-downloader
```

3. Set up a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface (CLI)

1. Run the CLI script:

```bash
python playlist_downloader.py
```

2. Follow the prompt:

   + Enter the YouTube playlist URL when prompted.
   + The script will create a folder (named by the sanitized playlist title and download all videos into it.
   + Progress updates and video size details are displayed in the terminal.

### Graphical User Interface (GUI)

1. Run the GUI application:

```bash
python app.py
```

2. Using the GUI:

   + Enter the YouTube playlist URL in the provided input field.
   + Click the "Download" button.
   + The GUI displays real-time progress in a log area.
   + A success message is shown when the process is complete.

### Creating an Executable

Since I'm on Ubuntu, you can build an executable for your environment as follows:

1. Build the executable with PyInstaller:

```bash
pyinstaller --onefile app.py
```

2. Executable:

   + This will generate an executable file in the `dist` folder.
   + Note: The executable is platform-specific. To create executables for Windows or macOS, you need to build the project on those platforms.

## Known Errors

### CLI

+ **Folder Already Exists**:

If a folder with the same name as the playlist already exists, the script will throw an error because it cannot recreate the folder. To resolve, delete or rename the existing folder before running the script.

### GUI

+ **Unresponsive Behavior**:

The GUI may appear unresponsive during long downloads. This is due to heavy processing in the background thread. Please be patient while the process completes; the GUI logs and final success message indicate completion.

## Additional Notes
+ The project now uses `yt_dlp` for improved compatibility and performance compared to the legacy `pytube` library.
+ For cross-platform builds, remember that executables are OS specific. Currently, only the Ubuntu executable is provided (built with PyInstaller on Ubuntu).

## Resources
+ [yt_dlp Documentation](https://github.com/yt-dlp/yt-dlp)
+ [PyQt5 Documentation](https://www.riverbankcomputing.com/software/pyqt/intro)
