# AVI to MP4 Video Converter

A simple AVI to MPEG convertor with simple instructions

This Python script converts AVI videos to MP4 format. It uses the `moviepy` library and `ffmpeg` to perform the conversion.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Setting the FFMPEG Path](#setting-the-ffmpeg-path)
  - [Setting the Input Folder Path](#setting-the-input-folder-path)
- [Usage](#usage)

## Requirements

- Python 3.6 or higher
- moviepy library
- ffmpeg

## Installation

1. Install Python 3.6 or higher if not already installed.

2. Install the moviepy library by running the following command in your terminal or command prompt: 
  pip install moviepy

3. Install FFmpeg:

- For Mac:
  1. Install Homebrew if you haven't already. Follow the instructions on the official website: https://brew.sh/
  2. Install FFmpeg using Homebrew. Run the following command in Terminal:
     
    brew install ffmpeg
     

- For Windows:
  1. Download the FFmpeg executable from the official website: https://ffmpeg.org/download.html
  2. Extract the downloaded archive to a folder (e.g., C:\ffmpeg)

## Usage

1. Edit the Python script, specifically the following lines:

- Set the path to the FFmpeg executable:

  os.environ["IMAGEIO_FFMPEG_EXE"] = "/path/to/ffmpeg"
  

- Set the path to the input folder containing your AVI files:
  
  input_folder = "/path/to/input/folder"
  

2. Run the script using a terminal or command prompt:

The script will create an output folder in the same location as the input folder with " MP4" added to the end. All converted videos will be saved in this folder.

## License

This project is licensed under the MIT License.


