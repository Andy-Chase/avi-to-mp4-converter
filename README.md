# avi-to-mp4-converter
A simple AVI to MPEG convertor with simple instructions

AVI to MP4 ConverterThis is a simple Python script to convert AVI video files to MP4 format using the moviepy library and ffmpeg.

RequirementsPython 3.6 or later
moviepy library
ffmpeg executable
InstallationInstall the moviepy library using pip:

Copy code
pip install moviepy


Install ffmpeg:

For Mac, use Homebrew:

Copy code
brew install ffmpeg


For Windows, download the ffmpeg executable from the official website: https://ffmpeg.org/download.html
Extract the downloaded archive to a folder (e.g., C:\ffmpeg).

UsageSet the path to the ffmpeg executable in the Python script:

For Mac, run which ffmpeg in the Terminal to find the path.
For Windows, locate the ffmpeg.exe file inside the 'bin' folder of the extracted archive (e.g., C:\ffmpeg\bin\ffmpeg.exe).
Replace the placeholder /path/to/ffmpeg in the script with the appropriate path on your system.

Set the input folder path in the Python script:

Locate the folder containing the AVI files.
Copy the folder path and replace the placeholder Input_File in the script with the appropriate path on your system.
Run the Python script:

Copy code
python avi_to_mp4_converter.py


The script will convert all AVI files in the input folder to MP4 format and save them in a new folder named "input_folder MP4"
