# Adversarial Attacks Script

This script implements various adversarial attack techniques on text inputs. Users can select the attack type, provide a text blob as the payload, or submit a text file as input.

## Attack Types

1. **Capitalization Attack**: Randomly capitalizes characters in the text.
2. **Base64 Encoding**: Encodes the text in Base64 format.
3. **Typographic Attack**: Introduces random typographical errors.
4. **Language Substitution**: Replaces words with their synonyms.
5. **LRL Translation**: Translates text through multiple languages.
6. **Unicode Adoption**: Modifies characters to their Unicode variants.

## Installation

Ensure you have the required packages installed:
```
pip install googletrans==4.0.0-rc1 nltk faker
```
Usage
```
python adversarial_attacks.py -t <attack_type> -p <text_payload>
```
or
```
python adversarial_attacks.py -t <attack_type> -f <file_path>
```
Arguments
-t, --type: Type of attack to perform. Choices are capitalization, base64, typographic, language_substitution, lrl_translation, unicode.
-p, --payload: Text payload to process.
-f, --file: File containing text payload.
Examples
Using Payload:
```
python adversarial_attacks.py -t capitalization -p "This is a test payload."
```
Using File:
```
python adversarial_attacks.py -t base64 -f input.txt
```
License
This project is licensed under the MIT License.

### Additional Notes

Ensure you have NLTK data downloaded for wordnet:
```
import nltk
nltk.download('wordnet')
```
This script provides a simple way to experiment with various text manipulation techniques, useful for testing the robustness of AI models.
