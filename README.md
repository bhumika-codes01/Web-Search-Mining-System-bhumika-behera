# Web Search Mining System

A Python-based Web Search Mining (WSM) project that searches a
collection of text documents using an inverted index, Boolean queries,
and wildcard queries. It includes a simple Tkinter graphical user
interface.

## Features

-   Loads text documents from the `documents` folder.
-   Tokenizes text into individual words.
-   Normalizes text using lowercase conversion, stop-word removal, and
    Porter stemming.
-   Builds an inverted index mapping each normalized term to the
    documents containing it.
-   Supports Boolean search operators: `AND`, `OR`, and `NOT`.
-   Supports parentheses for grouping and implicit AND between adjacent
    terms.
-   Supports wildcard searches using `*`.
-   Provides a GUI with a search box, Search button, Clear button, and
    read-only results area.

## Project Structure

``` text
WSM_Assignment/
├── .venv/
├── documents/
│   ├── doc01.txt
│   ├── doc02.txt
│   ├── ...
│   └── doc20.txt
├── document_loader.py
├── tokenizer.py
├── text_normalization.py
├── inverted_index.py
├── query_processor.py
├── wildcard_processor.py
├── main.py
└── README.md
```

## Requirements

-   Python 3.9 or later
-   NLTK
-   Tkinter (usually included with Python)

## Setup

Open PowerShell in the `WSM_Assignment` project directory.

### 1. Create a virtual environment

``` powershell
python -m venv .venv
```

### 2. Activate it (Windows PowerShell)

``` powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run this in the current terminal
session and activate again:

``` powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Install NLTK

``` powershell
python -m pip install nltk
```

## Run the Application

With the virtual environment activated and the terminal in the project
directory, run:

``` powershell
python main.py
```

The GUI will open. Enter a query and click **SEARCH**, or press Enter.
Click **CLEAR** to clear the query and results.

## Query Examples

  --------------------------------------------------------------------------
  Query                                  Description
  -------------------------------------- -----------------------------------
  `cloud`                                Searches for a single term

  `cloud AND computing`                  Finds documents containing both
                                         terms

  `cloud OR blockchain`                  Finds documents containing either
                                         term

  `cloud AND NOT blockchain`             Finds documents containing `cloud`
                                         but not `blockchain`

  `(cloud OR blockchain) AND security`   Groups conditions using parentheses

  `machine learning`                     Treats adjacent terms as an
                                         implicit AND

  `mach*`                                Searches for indexed terms matching
                                         the wildcard

  `comput*`                              Searches for indexed terms matching
                                         the wildcard
  --------------------------------------------------------------------------

**Wildcard note:** The current GUI accepts one wildcard pattern at a
time. Wildcard matching is performed against the normalized, stemmed
vocabulary, so results follow the project's stemming rules.

## Module Description

  -----------------------------------------------------------------------
  File                                Responsibility
  ----------------------------------- -----------------------------------
  `document_loader.py`                Reads `.txt` files from the
                                      `documents` directory.

  `tokenizer.py`                      Splits text into individual word
                                      tokens.

  `text_normalization.py`             Applies lowercase conversion,
                                      stop-word removal, and Porter
                                      stemming.

  `inverted_index.py`                 Builds and displays the inverted
                                      index.

  `query_processor.py`                Parses and evaluates Boolean search
                                      queries.

  `wildcard_processor.py`             Expands wildcard patterns and
                                      retrieves matching documents.

  `main.py`                           Provides the Tkinter GUI and
                                      connects the search modules.
  -----------------------------------------------------------------------

## Test Individual Modules

Run these commands from the project root:

``` powershell
python document_loader.py
python tokenizer.py
python text_normalization.py
python inverted_index.py
python query_processor.py
python wildcard_processor.py
```

## How the System Works

1.  The document loader reads all `.txt` files from the `documents`
    folder.
2.  The tokenizer extracts word tokens.
3.  The normalization module converts tokens to lowercase, removes stop
    words, and applies stemming.
4.  The inverted-index module maps each normalized term to the documents
    containing it.
5.  The query processor evaluates Boolean expressions against the index.
6.  The wildcard processor expands wildcard patterns against the indexed
    vocabulary and collects matching documents.
7.  The GUI displays matching document names and the total number of
    results.

## Notes

-   Keep the `documents` folder in the project root.
-   Place the text files to be indexed inside the `documents` folder.
-   Run commands from the `WSM_Assignment` directory.
-   The inverted index is built when the application starts.
