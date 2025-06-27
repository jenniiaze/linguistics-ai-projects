# slang_decoder.py

slang_dict = {
    "el gordo": "drug boss",
    "verde": "marijuana",
    "nota": "high",
    "el vuelto": "cash from a deal",
    "paquetes": "drug packages",
    "ticket": "price per kilo",
    "envío": "shipment",
    "taller": "stash house",
    "bayamón": "Bayamón (city often coded to imply movement of goods)",
}

def decode_slang(transcript):
    decoded_lines = []
    for line in transcript.split("\n"):
        for slang, meaning in slang_dict.items():
            if slang in line.lower():
                line += f"  ⟶  ({slang}: {meaning})"
        decoded_lines.append(line)
    return "\n".join(decoded_lines)
