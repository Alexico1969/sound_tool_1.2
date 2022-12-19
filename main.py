import wave
import numpy as np
import os

def fill_to_60(input):
    output = ""
    if len(input) < 60:
        output = (60 - len(input)) * " "
    return output

def fill_to_17(input):
    i_str = str(input)
    
    output = ""
    if len(i_str) < 17:
        output = (17 - len(i_str)) * " "
    return output

def centroid(file_path: str) -> float:
    # Open the wave file
    try:
        with wave.open(file_path, 'rb') as wave_file:
        # Read the audio data and sample rate from the wave file
            audio_data = wave_file.readframes(wave_file.getnframes())
            sample_rate = wave_file.getframerate()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0

    # Convert the audio data to a numpy array
    audio_data = np.frombuffer(audio_data, dtype=np.int16)

    # Compute the magnitude spectrum of the audio data
    magnitudes = np.abs(np.fft.rfft(audio_data))


    # Compute the spectral centroid of the audio data
    spectral_centroid = np.sum(magnitudes * np.arange(len(magnitudes))) / np.sum(magnitudes)

    # The spectral centroid is a measure of the "brightness" of the audio spectrum.
    # Speech tends to have a higher spectral centroid than music, so if the spectral
    # centroid is above a certain threshold, we can conclude that the audio is speech.
    return spectral_centroid



# Set the path to the folder containing the files
folder_path = 'wav_input/'

print()
print("File path " + fill_to_60("File path") + " | " + "Spectral Centroid" + " | " + "Prediction")
print("----------------------------------------------------------------------------------------------")

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        # Do something with the file, such as analyzing its contents or processing it in some way
        test_file = file_path
        c = int(centroid(test_file))
        if c > 2000000:
            pred = "music"
        else:
            pred = "speech"
        print(f"{file_path } {fill_to_60(test_file)} | {fill_to_17(int(c))}{int(c)} |   {pred}")




