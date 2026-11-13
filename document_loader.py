
import os


# Path of the documents folder
DOCUMENT_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "documents"
)


def load_documents():

    documents = {}

    # Check whether the folder exists
    if not os.path.isdir(DOCUMENT_FOLDER):
        raise FileNotFoundError(
            "Documents folder not found!"
        )

    # Read all text files
    for filename in sorted(os.listdir(DOCUMENT_FOLDER)):

        if filename.lower().endswith(".txt"):

            file_path = os.path.join(
                DOCUMENT_FOLDER,
                filename
            )

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                documents[filename] = file.read()

    return documents


# Test document loading
if __name__ == "__main__":

    loaded_documents = load_documents()

    print("========== DOCUMENT LOADER ==========")

    print(
        "Total documents loaded:",
        len(loaded_documents)
    )

    for filename, content in loaded_documents.items():

        print("\nDocument:", filename)
        print("Content:", content[:100], "...")
