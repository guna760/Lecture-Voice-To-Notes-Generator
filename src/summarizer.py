def generate_notes(text):

    if not text:
        return ""

    sentences = text.split(".")

    notes = ". ".join(sentences[:8])

    return notes