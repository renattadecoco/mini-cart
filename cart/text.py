import re
import unicodedata


def slugify(text):
    """Turn text into a URL slug: lowercase ascii words joined by single dashes."""
    # Strip accents (e.g. é -> e) by decomposing and dropping non-ASCII marks.
    ascii_text = (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    # Collapse any run of non-alphanumeric characters to a single dash,
    # then trim leading/trailing dashes.
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")
