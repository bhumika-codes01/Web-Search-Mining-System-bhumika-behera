
import re
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()


def expand_wildcard(pattern, inverted_index):
    pattern = pattern.lower().strip()

    if not pattern or "*" not in pattern:
        raise ValueError("Enter a valid wildcard pattern containing *.")

    parts = pattern.split("*")
    stemmed_parts = [
        stemmer.stem(part) if part else ""
        for part in parts
    ]

    regex_pattern = "^" + ".*".join(
        re.escape(part) for part in stemmed_parts
    ) + "$"

    regex = re.compile(regex_pattern)

    matching_terms = [
        term for term in inverted_index
        if regex.fullmatch(term)
    ]

    return sorted(matching_terms)


def search_wildcard(pattern, inverted_index):
    matching_terms = expand_wildcard(
        pattern, inverted_index
    )

    matching_documents = set()

    for term in matching_terms:
        matching_documents.update(inverted_index[term])

    return matching_terms, matching_documents


if __name__ == "__main__":
    from inverted_index import build_inverted_index

    index, documents = build_inverted_index()

    print("========== WILDCARD PROCESSING ==========")

    while True:
        pattern = input("\nEnter wildcard query (or 'exit'): ")

        if pattern.lower() == "exit":
            break

        try:
            terms, results = search_wildcard(pattern, index)

            print("\nExpanded Terms:", terms)
            print("\nMatching Documents:")

            for filename in sorted(results):
                print(filename)

            print("Total results:", len(results))

        except ValueError as error:
            print("Error:", error)
