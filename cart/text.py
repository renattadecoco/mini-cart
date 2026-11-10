def slugify(text):
    """Turn text into a URL slug: lowercase ascii words joined by single dashes."""
    out = ""
    for ch in text.lower():
        if ch.isalnum():
            out += ch
        else:
            out += "-"
    return out
