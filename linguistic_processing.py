
import re
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

STOP_WORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by",
    "can", "could", "did", "do", "does", "doing", "down", "during",
    "each", "few", "for", "from", "further", "had", "has", "have",
    "having", "he", "her", "here", "hers", "herself", "him",
    "himself", "his", "how", "i", "if", "in", "into", "is", "it",
    "its", "itself", "just", "me", "more", "most", "my", "myself",
    "no", "nor", "not", "now", "of", "off", "on", "once", "only",
    "or", "other", "our", "ours", "ourselves", "out", "over", "own",
    "same", "she", "should", "so", "some", "such", "than", "that",
    "the", "their", "theirs", "them", "themselves", "then", "there",
    "these", "they", "this", "those", "through", "to", "too", "under",
    "until", "up", "very", "was", "we", "were", "what", "when",
    "where", "which", "while", "who", "whom", "why", "will", "with",
    "you", "your", "yours", "yourself", "yourselves", "using", "used"
}


def process_text(text):
    text = text.lower()

    # Remove possessive 's
    text = re.sub(r"'s\b", "", text)

    # Tokenization
    tokens = re.findall(r'\b[a-zA-Z]+\b', text)

    # Stop-word removal
    tokens = [
        word for word in tokens
        if word not in STOP_WORDS
    ]

    # Stemming
    stemmed_tokens = [
        stemmer.stem(word)
        for word in tokens
    ]

    return stemmed_tokens


def process_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return process_text(text)


if __name__ == "__main__":
    file_path = "documents/doc01.txt"

    processed = process_document(file_path)

    print("Processed doc01.txt:")
    print(processed)
