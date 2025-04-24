import numpy as np
import soundfile as sf
import os
from datetime import datetime

def generate_birdsong(params, filename="output.wav"):
    sr = 44100
    audio = np.array([], dtype=np.float32)

    for freq, dur in params:
        t = np.linspace(0, dur, int(sr * dur), False)
        wave = 0.5 * np.sin(2 * np.pi * freq * t)
        audio = np.concatenate((audio, wave))

    if not os.path.exists("output"):
        os.makedirs("output")
        
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    full_path = f"output/{filename}_{timestamp}.wav"
    sf.write(full_path, audio, sr)
    return full_path