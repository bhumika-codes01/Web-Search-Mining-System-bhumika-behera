
import re


def tokenize(text):

    # Extract individual words from text
    tokens = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?", text)

    return tokens


# Test tokenization
if __name__ == "__main__":

    sample_text = """
    Machine Learning is changing the world!
    Artificial Intelligence helps computers solve problems.
    """

    print("========== TOKENIZATION ==========")

    print("\nOriginal Text:")
    print(sample_text)

    tokens = tokenize(sample_text)

    print("\nGenerated Tokens:")
    print(tokens)

    print("\nTotal Tokens:", len(tokens))
