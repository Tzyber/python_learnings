class AudioPlayer:
    def Mp3_Player(self, file):
        print(f"Playing MP3 file: {file}")


class WavPlayer:
    def Wav_Player(self, file):
        print(f"Playing WAV file: {file}")


class AudioAdapter:
    def __init__(self, audio_player):
        self.audio_player = audio_player

    def Play_Wav(self, file):
        print(f"--- Adapter-Log: Starte Konvertierung von '{file}' ---")
        print(f"--- Status: Transformiere MP3-Signal zu WAV-Signal... ---")
        mp3_format = file.replace(".wav", ".mp3")
        print(f"--- Adapter-Log: Konvertierung abgeschlossen. ---")
        self.audio_player.Mp3_Player(mp3_format)


def main():
    neuer_wav_player = AudioPlayer()
    adapter = AudioAdapter(neuer_wav_player)
    adapter.Play_Wav("hochzeit_aufnahme.wav")

if __name__ == "__main__":
    main()
