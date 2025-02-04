from RealtimeSTT import AudioToTextRecorder

def process_text(text):
    print(text)


if __name__ == '__main__':
    # recorder = AudioToTextRecorder(model="model")
    recorder = AudioToTextRecorder(model="small", download_root="model")
    # recorder = AudioToTextRecorder(model="Salama1429/KalemaTech-Arabic-STT-ASR-based-on-Whisper-Small")

    while True:
        recorder.text(process_text)