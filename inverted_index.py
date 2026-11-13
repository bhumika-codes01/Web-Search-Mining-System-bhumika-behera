
from document_loader import load_documents
from text_normalization import normalize_text


def build_inverted_index():
    documents = load_documents()
    inverted_index = {}

    for filename, content in documents.items():
        terms = normalize_text(content)

        for term in terms:
            if term not in inverted_index:
                inverted_index[term] = set()

            inverted_index[term].add(filename)

    return inverted_index, documents


def display_index(inverted_index):
    print("\n========== INVERTED INDEX ==========")

    for term in sorted(inverted_index):
        filenames = sorted(inverted_index[term])
        print(f"{term}: {', '.join(filenames)}")

    print("\nTotal unique terms:", len(inverted_index))


if __name__ == "__main__":
    index, documents = build_inverted_index()

    print("Total documents loaded:", len(documents))
    display_index(index)
