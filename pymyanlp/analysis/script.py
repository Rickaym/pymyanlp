def is_burmese(text: str):
    """
    Check if a single character belongs to the Myanmar Unicode block (U+1000-U+109F).

    Args:
        char (str): A single character to check

    Returns:
        bool: True if the character is in the Myanmar Unicode block, False otherwise
    """
    if not isinstance(text, str) or len(text) < 1:
        return False

    return all(0x1000 <= ord(char) <= 0x109F for char in text)


def get_burmese_script(char):
    """
    Determine the specific script variant for a Myanmar character.

    Args:
        char (str): A single Myanmar character

    Returns:
        str: The script name or "unknown" if not in Myanmar block or unrecognized
    """
    if not is_burmese(char):
        return "unknown"

    code_point = ord(char)

    # Core Burmese characters (consonants, vowels, basic signs)
    if 0x1000 <= code_point <= 0x104F:
        return "burmese"

    # Pali and Sanskrit extensions
    elif 0x1050 <= code_point <= 0x1059:
        return "pali_sanskrit"

    # Mon extensions
    elif code_point in [0x105A, 0x105B, 0x105C, 0x105D, 0x105E, 0x105F, 0x1060]:
        return "mon"

    # S'gaw Karen extensions
    elif code_point in [0x1061, 0x1062, 0x1063, 0x1064]:
        return "sgaw_karen"

    # Western Pwo Karen extensions
    elif 0x1065 <= code_point <= 0x106D:
        return "western_pwo_karen"

    # Eastern Pwo Karen extensions
    elif code_point in [0x106E, 0x106F, 0x1070]:
        return "eastern_pwo_karen"

    # Geba Karen extension
    elif code_point == 0x1071:
        return "geba_karen"

    # Kayah extensions
    elif 0x1072 <= code_point <= 0x1074:
        return "kayah"

    # Shan extensions (including letters, signs, and digits)
    elif 0x1075 <= code_point <= 0x1099:
        return "shan"

    # Khamti Shan extensions
    elif code_point in [0x109A, 0x109B]:
        return "khamti_shan"

    # Aiton and Phake extensions
    elif code_point in [0x109C, 0x109D]:
        return "aiton_phake"

    # Shan symbols
    elif code_point in [0x109E, 0x109F]:
        return "shan"

    else:
        return "unknown"
