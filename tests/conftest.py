"""Pytest configuration and fixtures for pymyanlp tests."""

import pytest
import tempfile
import os


@pytest.fixture
def sample_mon_text():
    """Sample Burmese script for testing."""
    return "တမၟာ"


@pytest.fixture
def sample_sgaw_karen_text():
    """Sample Burmese script for testing."""
    return "ၡးခွ့မဲၢ်"


@pytest.fixture
def sample_shan_text():
    """Sample Burmese script for testing."""
    return "ႁိူဝ်းမိၼ်"


@pytest.fixture
def sample_burmese_text():
    """Sample Burmese text for testing."""
    return "မြန်မာ လူမျိုး ဖြစ် သည်"


@pytest.fixture
def sample_mixed_text():
    """Sample mixed Burmese and English text."""
    return "Hello မြန်မာ World ၂၀၂၄"


@pytest.fixture
def sample_english_text():
    """Sample English text for testing."""
    return "Hello World 2024"


@pytest.fixture
def sample_burmese_numbers():
    """Sample text with English numbers to convert."""
    return "၂၀၂၄ ခုနှစ် ၁၀ လ ၁၅ ရက်"


@pytest.fixture
def temp_csv_file():
    """Create a temporary CSV file for testing."""
    content = """word,sentiment
ကောင်း,positive
မကောင်း,negative
ပုံမှန်,neutral"""

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False, encoding="utf-8"
    ) as f:
        f.write(content)
        temp_path = f.name

    yield temp_path

    # Cleanup
    try:
        os.unlink(temp_path)
    except OSError:
        pass
