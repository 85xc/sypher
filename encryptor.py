def text_to_hex(text):
    return ''.join(f"{ord(c):02X}" for c in text)

def hex_to_params(hex_str):
    params = []
    for i in range(0, len(hex_str), 2):
        value = int(hex_str[i:i+2], 16)
        freq = 1500 + (value % 40) * 50
        dur = 0.2 + (value % 5) * 0.1
        params.append((freq, dur))
    return params