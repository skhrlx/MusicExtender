import os
from pydub import AudioSegment

def extend_music_files(input_folder, output_folder, fade_duration=1000, num_concatenations=2):

    os.makedirs(output_folder, exist_ok=True) 
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            sound = AudioSegment.from_file(input_path)
            sound_with_fades = sound.fade_in(fade_duration).fade_out(fade_duration)

            extended_sound = sound_with_fades
            for _ in range(num_concatenations - 1):
                extended_sound += sound_with_fades

            extended_sound.export(output_path, format="mp3")
            print(f"Extended '{filename}' and saved to '{output_path}'")

if __name__ == "__main__":
    input_folder = "musics_to_extend"
    output_folder = "extended_musics"
    fade_duration = 2000 # in ms (2000ms = 2s) monke monke
    num_concatenations = 30

    extend_music_files(input_folder, output_folder, fade_duration, num_concatenations)
