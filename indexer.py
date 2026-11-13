import os
from linguistic_processing import process_document


DOCUMENT_FOLDER = "documents"


def build_inverted_index():
    inverted_index = {}

    for filename in sorted(os.listdir(DOCUMENT_FOLDER)):

        if filename.endswith(".txt"):

            file_path = os.path.join(DOCUMENT_FOLDER, filename)

            words = process_document(file_path)

            for word in words:

                if word not in inverted_index:
                    inverted_index[word] = set()

                inverted_index[word].add(filename)

    return inverted_index


def display_index(inverted_index):

    print("\n========== INVERTED INDEX ==========\n")

    for word in sorted(inverted_index):
        documents = sorted(inverted_index[word])

        print(f"{word} -> {', '.join(documents)}")


if __name__ == "__main__":

    index = build_inverted_index()

    display_index(index)