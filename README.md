# PyMyaNLP

A Python library for Myanmar (Burmese) language processing and natural language processing tasks.

မြန်မာဗျည်းအက္ခရာအခြေခံသော ဘာသာစကားများအတွက် NLP အရာ၌ အထွေထွေသုံးစွဲနိုင်ရန်ရည်ရွယ်၍ ရေးသားဖြစ်ခဲ့သည်။

## Installation

```bash
pip install pymyanlp
```

## Quick Start

```python
import pymyanlp

# Word segmentation
segments = pymyanlp.segment_word("ရေပုံမှန်သောက်ပါ") # ['ရေ', 'ပုံမှန်', 'သောက်', 'ပါ']

# Part-of-speech tagging
tags = pymyanlp.pos_tag("မြန်မာ ဘာသာ") # [('မြန်မာ', <PartOfSpeech.Noun: 'n'>), ('ဘာသာ', <PartOfSpeech.Noun: 'n'>)]

# Text detection and validation
pymyanlp.is_burmese("မြန်မာ ဘာသာ")  # True

pymyanlp.contains_burmese("Hello မြန်မာ")  # True

pymyanlp.get_burmese_script("မြန်မာ")  # burmese
pymyanlp.get_burmese_script("တမၟာ")  # mon
pymyanlp.get_burmese_script("ၡးခွ့မဲၢ်")  # sgaw_karen
pymyanlp.get_burmese_script("ႁိူဝ်းမိၼ်")  # shan

# Number transliteration
pymyanlp.transliterate_numbers("2024")  # ၂၀၂၄

# Text processing pipeline
processed = pymyanlp.apply_written_suite("Hello 2024, မြန်မာ!") # Normalized text
```

## Features

| Feature | Description |
|---------|-------------|
| Word Segmentation | Multiple models (Viterbi, CRF-based) |
| POS Tagging | Part-of-speech tagging for Myanmar text |
| Text Normalization | Clean and standardize text |
| Transliteration | Convert English  to Myanmar |
| Script Detection | Identify Burmese text and script variants |
| Punctuation Handling | Remove or process punctuation |
| Spacing Normalization | Handle mixed script spacing |
| Text Style Detection | Identify different Myanmar text styles |
| Sentiment Analysis* | Score-based sentiment classification |
| Grammar Analysis* | Myanmar particle and grammar detection |
| Spell Checking* | Basic spell checking functionality |

*means not yet implemented

## Constants and Enums

```python
# POS tag enums
pymyanlp.PartOfSpeech.Noun.value  # "n"

# Built-in constants
pymyanlp.NUMBER_MAP  # {'0': '၀', '1': '၁', ...}
pymyanlp.PUNCTUATION  # ['။', '၊', ',', '.', ...]
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest tests/
```

## Documentation

- **API Reference**: See module docstrings for detailed API documentation
- **Test Examples**: Check `tests/` directory for usage examples

## Project Structure

```
pymyanlp/
├── text/           # Text processing modules
├── analysis/       # Analysis and NLP modules
├── utils/          # Utility functions
├── resources/      # Language resources
└── lib/            # Core algorithms and models
```

## License

MIT License - see LICENSE.txt for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Run the test suite
5. Submit a pull request

For bug reports and feature requests, please use the GitHub issue tracker.

