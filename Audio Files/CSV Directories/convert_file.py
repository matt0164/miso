from pydub import AudioSegment
import os

#convert .m4a to .wav
def convert_m4a_to_wav(input_path, output_path):
    try:
        #load the .m4a file
        audio = AudioSegment.from_file(input_path, format="m4a")
        #export as .wav
        audio.export(output_path, format="wav")
        print(f"Converted: {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

#directory with .m4a files
input_directory = '/Users/cameronalevy/Documents/research miso/audio clips/m4a files'
output_directory = '/Users/cameronalevy/Documents/research miso/audio clips/Clips'

os.makedirs(output_directory, exist_ok=True)

#loops through .m4a files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".m4a"):
        input_file = os.path.join(input_directory, filename)
        output_file = os.path.join(output_directory, os.path.splitext(filename)[0] + ".wav")
        convert_m4a_to_wav(input_file, output_file)
