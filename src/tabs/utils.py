import sys
import os
import spacy

from spacy.tokens import Token

# Load spacy model
nlp = spacy.load("en_core_web_trf")


# Function to check if token is a proper noun
def is_proper_noun(token):
    """Check if token is a proper noun using POS, tag, dep, shape"""
    if token.pos_ == "PROPN" and token.tag_ == "NNP":
        if token.dep_ == "compound" or token.dep_.startswith("nsubj"):
            return True
        if token.shape_ == "Xxxxxx":
            return True
    return False


def delete_proper_nouns(image_dir):
    for text_file in os.listdir(image_dir):
        print(text_file)
        if text_file.endswith(".txt"):
            file_path = os.path.join(image_dir, text_file)

            # Open and process file
            with open(file_path) as f:
                text = f.read()

            doc = nlp(text)

            cleaned_text = []
            for token in doc:
                if not is_proper_noun(token):
                    cleaned_text.append(token.text_with_ws)

            cleaned_text = "".join(cleaned_text)

            # Save cleaned text
            with open(file_path, "w") as f:
                f.write(cleaned_text)
