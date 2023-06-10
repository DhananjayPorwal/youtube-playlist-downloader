# YouTube Playlist Downloader ✨

This repository contains a Python script for downloading all the videos from a YouTube playlist. The script utilizes the `pytube` library to handle the downloading process.

## Features

- Downloads all videos from a given YouTube playlist URL.
- Converts the playlist name into an alphanumeric folder name.
- Displays the total number of videos in the playlist 🎦.
- Downloads each video with the highest resolution available.
- Displays the size of each video before downloading 🗜.
- Provides progress updates during the download process.
- Notifies when all videos have been successfully downloaded 🎉.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/username/repository.git
   ```

2. Change into the project directory:

   ```
   cd repository
   ```

3. Install the required dependencies:

   ```
   pip install pytube
   ```

## Usage

### Command Line Interface (CLI)

1. Run the script:

   ```
   python playlist_downloader.py
   ```

2. Enter the URL of the YouTube playlist when prompted ✨.

3. The script will create a folder with an alphanumeric name based on the playlist title.

4. The script will display the total number of videos in the playlist 🎦.

5. Each video will be downloaded with the highest resolution available and saved in the created folder.

6. The script will display the size of each video before downloading 🗜 and provide progress updates.

7. Once all videos have been downloaded, a success message will be displayed 🎉.

### Graphical User Interface (GUI)

1. Run the executable file `app.exe` from **Windows Executable** (available only for Windows).

2. The GUI window will open.

3. Enter the URL of the YouTube playlist in the provided input field.

4. Click the "Download" button.

5. The script will create a folder with an alphanumeric name based on the playlist title within the **Windows Executable** directory.

6. The script will display the total number of videos in the playlist 🎦.

7. Each video will be downloaded with the highest resolution available and saved in the created folder.

8. The GUI will display the size of each video before downloading 🗜 and provide progress updates.

9. Once all videos have been downloaded, a success message will be displayed 🎉.

## Known Errors

### CLI

If a folder with the same name as the playlist already exists, the script will throw an error. This is because the script tries to create a new folder with an alphanumeric name based on the playlist title to store the downloaded videos. However, if a folder with the same name already exists, the operating system will not allow the creation of another folder with the same name, resulting in an error.

> To resolve this issue, you can either delete the existing folder or rename it before running the script.

### GUI

In the GUI version, there might be instances where the program appears to be unresponsive or not updating while it's performing the download process. This can happen because the download process might take some time, especially for larger playlists or when downloading videos with high resolutions.

Please be patient and wait for the program to complete its job. Even if it seems unresponsive, it's still working in the background. Avoid clicking or interacting with the program during the download process to ensure a smooth operation.

Once the download process is finished, the program will display a success message, indicating that all the videos have been successfully downloaded.
