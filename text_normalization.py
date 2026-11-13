
import re
from nltk.stem import PorterStemmer
from tokenizer import tokenize

stemmer = PorterStemmer()

STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "am", "be", "been", "being", "and", "or", "but",
    "if", "then", "else", "of", "at", "by", "for",
    "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above",
    "below", "to", "from", "up", "down", "in", "out",
    "on", "off", "over", "under", "again", "further",
    "once", "here", "there", "when", "where", "why",
    "how", "all", "any", "both", "each", "few", "more",
    "most", "other", "some", "such", "no", "nor",
    "not", "only", "own", "same", "so", "than",
    "too", "very", "can", "will", "just", "should",
    "now", "this", "that", "these", "those", "it",
    "its", "i", "you", "he", "she", "we", "they",
    "them", "his", "her", "our", "your", "their"
}

def normalize_tokens(tokens):
    normalized_tokens = []

    for token in tokens:
        word = token.lower()
        word = re.sub(r"[^a-z]", "", word)

        if word and word not in STOP_WORDS:
            normalized_tokens.append(stemmer.stem(word))

    return normalized_tokens


def normalize_text(text):
    tokens = tokenize(text)
    return normalize_tokens(tokens)


if __name__ == "__main__":
    sample_text = """
    Artificial Intelligence is changing the world.
    Computers are learning new technologies rapidly!
    """

    print("========== TEXT NORMALIZATION ==========")
    print("\nOriginal Text:")
    print(sample_text)

    tokens = tokenize(sample_text)
    print("\nAfter Tokenization:")
    print(tokens)

    normalized = normalize_tokens(tokens)
    print("\nAfter Normalization:")
    print(normalized)
