import os
from moviepy.editor import VideoFileClip
import glob

def convert_avi_to_mp4(input_avi, output_mp4):
    video = VideoFileClip(input_avi)
    video.write_videofile(output_mp4)

# ------------------------------------------------------------------------
# INSTRUCTIONS FOR SETTING THE PATH TO FFMPEG:
#
# For Mac:
# 1. Install ffmpeg using Homebrew (if you haven't already):
#    Open Terminal and run: brew install ffmpeg
# 2. Locate the path of the installed ffmpeg executable:
#    Run the following command in Terminal: which ffmpeg
#    Copy the path returned by the command.
#
# For Windows:
# 1. Download the ffmpeg executable from the official website: https://ffmpeg.org/download.html
# 2. Extract the downloaded archive to a folder (e.g., C:\ffmpeg)
# 3. Locate the path of the ffmpeg.exe file inside the 'bin' folder (e.g., C:\ffmpeg\bin\ffmpeg.exe)
#    Copy the path of the ffmpeg.exe file.
# ------------------------------------------------------------------------

# Set the path to the ffmpeg executable
os.environ["IMAGEIO_FFMPEG_EXE"] = "/path/to/ffmpeg"

# ------------------------------------------------------------------------
# INSTRUCTIONS FOR SETTING THE INPUT FOLDER PATH:
#
# For Mac:
# 1. Locate the folder containing the AVI files in Finder
# 2. Right-click the folder and select 'Get Info'
# 3. Copy the path displayed in the 'Where' field
#
# For Windows:
# 1. Locate the folder containing the AVI files in File Explorer
# 2. Click on the address bar to reveal the folder path
# 3. Copy the folder path
# ------------------------------------------------------------------------

input_folder = "input_folder"
output_folder = f"{input_folder} MP4"

print(f"Input folder: {input_folder}")
print(f"Output folder: {output_folder}")

input_files = os.listdir(input_folder)
print("Files in the input folder:")
for file in input_files:
    print(file)

# Ensure the output folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Find all AVI files in the input folder
avi_files = glob.glob(os.path.join(input_folder, "*.avi"))

# Convert each AVI file to MP4
for avi_file in avi_files:
    file_name = os.path.basename(avi_file)
    file_name_without_ext = os.path.splitext(file_name)[0]
    output_mp4_file = os.path.join(output_folder, f"{file_name_without_ext}.mp4")
    
    print(f"Converting {file_name} to MP4...")
    convert_avi_to_mp4(avi_file, output_mp4_file)
    print(f"Conversion completed for {file_name}")

print("All videos have been converted.")
