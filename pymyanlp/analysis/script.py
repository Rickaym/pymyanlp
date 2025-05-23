from typing import Literal


def is_burmese(text: str):
    """
    Check if all of the characters in the text belongs to the Myanmar Unicode block (U+1000-U+109F) or a space character.

    Args:
        text (str): A string to check

    Returns:
        bool: True if the character is in the Myanmar Unicode block, False otherwise
    """
    if not isinstance(text, str) or len(text) < 1:
        return False

    return all(0x1000 <= ord(char) <= 0x109F or char == " " for char in text)


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


def fix_medial(text, position: Literal["before", "after"] = "before"):
    """
    Rearrange Myanmar text by moving dependent consonant medial signs (ya, ra, ကျ, ကြ) before or after their base characters.

    In Myanmar script, medial consonant signs (like ya and ra) typically follow their base
    consonants in Unicode representation, but sometimes this is skewed and needs to be
    fixed for proper rendering.

    This function identifies and reorders these signs to match the correct visual order.

    Args:
        text (str): Myanmar text to rearrange
        position (Literal["before", "after"]): Whether to place dependent signs before or after base characters.
            Defaults to "before" for proper visual rendering.

    Returns:
        str: Text with medial consonant signs moved to the specified position relative to base characters

    Example:
        >>> fix_medial("ကျ")
        >>> "ျက"
        >>> fix_medial("ကျ", position="after")
        >>> "ကျ"
    """
    if not text:
        return text

    dependent_consonant_signs = {
        0x1031,  # MYANMAR VOWEL SIGN E
        0x103B,  # MYANMAR CONSONANT SIGN MEDIAL YA
        0x103C,  # MYANMAR CONSONANT SIGN MEDIAL RA
    }

    result = []
    i = 0

    while i < len(text):
        current_char = text[i]
        current_code = ord(current_char)

        if is_burmese(current_char) and current_code not in dependent_consonant_signs:
            dependent_chars = []
            j = i + 1

            while j < len(text):
                next_char = text[j]
                next_code = ord(next_char)

                if is_burmese(next_char) and next_code in dependent_consonant_signs:
                    dependent_chars.append(next_char)
                    j += 1
                else:
                    break

            if position == "before":
                # Add dependent symbols first, then base character
                result.extend(dependent_chars)
                result.append(current_char)
            else:  # position == "after"
                # Add base character first, then dependent symbols
                result.append(current_char)
                result.extend(dependent_chars)

            # Move index past the processed characters
            i = j
        else:
            # For non-base characters or characters already in correct position
            result.append(current_char)
            i += 1

    return "".join(result)
