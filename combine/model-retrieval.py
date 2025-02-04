from transformers import AutoProcessor
from transformers import AutoModelForSpeechSeq2Seq

# Load the Processor
processor = AutoProcessor.from_pretrained("Salama1429/KalemaTech-Arabic-STT-ASR-based-on-Whisper-Small")

# Load the Model
model = AutoModelForSpeechSeq2Seq.from_pretrained("Salama1429/KalemaTech-Arabic-STT-ASR-based-on-Whisper-Small")

# Save the model and processor locally
processor.save_pretrained("processor")
model.save_pretrained("model")