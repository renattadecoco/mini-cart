import re

_UNITS = {"h": 3600, "m": 60, "s": 1}


def parse_duration(text):
    """Parse strings like '1h30m', '45s', '1h 5m 10s' into total seconds (int).

    Raise ValueError for empty, unknown units, repeated units, or garbage.
    """
    if text is None or not text.strip():
        raise ValueError("empty duration")

    # The whole string (ignoring surrounding whitespace) must be one or
    # more "<integer><unit>" tokens, each unit used at most once.
    # This rejects decimals ("1.5h"), signs ("-3m"), bare units ("h"),
    # unknown units ("5x"), and any other garbage ("abc").
    if not re.fullmatch(r"\s*(?:\d+\s*[hmsHMS]\s*)+", text):
        raise ValueError(f"invalid duration: {text!r}")

    seen = set()
    total = 0
    for amount, unit in re.findall(r"(\d+)\s*([hmsHMS])", text):
        unit = unit.lower()
        if unit in seen:
            raise ValueError(f"repeated unit: {unit!r}")
        seen.add(unit)
        total += int(amount) * _UNITS[unit]
    return total
