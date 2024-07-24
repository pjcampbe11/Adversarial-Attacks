import argparse
import base64
import random
import string
import os
from googletrans import Translator
from nltk.corpus import wordnet
from faker import Faker
import unicodedata

def capitalization_attack(text):
    return ''.join(random.choice([char.upper(), char.lower()]) for char in text)

def base64_encoding(text):
    return base64.b64encode(text.encode()).decode()

def typographic_attack(text):
    fake = Faker()
    words = text.split()
    return ' '.join([fake.word() if random.random() > 0.7 else word for word in words])

def language_substitution(text):
    words = text.split()
    substituted_text = []
    for word in words:
        synonyms = wordnet.synsets(word)
        if synonyms:
            substituted_text.append(synonyms[0].lemmas()[0].name())
        else:
            substituted_text.append(word)
    return ' '.join(substituted_text)

def lrl_translation(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='fr').text
    translated_back = translator.translate(translated, src='fr', dest='de').text
    final_translation = translator.translate(translated_back, src='de', dest='en').text
    return final_translation

def unicode_adoption(text):
    return ''.join([chr(ord(char) + random.randint(0, 10)) if char.isalpha() else char for char in text])

def process_text(text, attack_type):
    if attack_type == 'capitalization':
        return capitalization_attack(text)
    elif attack_type == 'base64':
        return base64_encoding(text)
    elif attack_type == 'typographic':
        return typographic_attack(text)
    elif attack_type == 'language_substitution':
        return language_substitution(text)
    elif attack_type == 'lrl_translation':
        return lrl_translation(text)
    elif attack_type == 'unicode':
        return unicode_adoption(text)
    else:
        return text

def main():
    parser = argparse.ArgumentParser(description="Adversarial Attacks Script")
    parser.add_argument('-t', '--type', required=True, choices=['capitalization', 'base64', 'typographic', 'language_substitution', 'lrl_translation', 'unicode'], help="Type of attack")
    parser.add_argument('-p', '--payload', help="Text payload to process")
    parser.add_argument('-f', '--file', help="File containing text payload")
    
    args = parser.parse_args()

    if args.payload:
        text = args.payload
    elif args.file:
        with open(args.file, 'r') as file:
            text = file.read()
    else:
        raise ValueError("Either payload or file must be provided")

    processed_text = process_text(text, args.type)
    print(f"Processed Text: {processed_text}")

if __name__ == "__main__":
    main()
