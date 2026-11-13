
import tkinter as tk
from tkinter import scrolledtext, messagebox

from inverted_index import build_inverted_index
from query_processor import evaluate_query
from wildcard_processor import search_wildcard


inverted_index, documents = build_inverted_index()
all_documents = set(documents.keys())


def display_results(query):
    result_area.config(state=tk.NORMAL)
    result_area.delete("1.0", tk.END)

    try:
        if not query.strip():
            raise ValueError("Please enter a search query.")

        if "*" in query:
            if len(query.split()) != 1:
                raise ValueError(
                    "For now, enter one wildcard pattern at a time."
                )

            terms, results = search_wildcard(
                query, inverted_index
            )

            result_area.insert(
                tk.END, "WILDCARD SEARCH RESULTS\n"
            )
            result_area.insert(
                tk.END, f"\nExpanded terms: {', '.join(terms)}\n"
            )

        else:
            results = evaluate_query(
                query, inverted_index, all_documents
            )

            result_area.insert(
                tk.END, "BOOLEAN SEARCH RESULTS\n"
            )

        result_area.insert(
            tk.END, "\nMatching Documents:\n"
        )
        result_area.insert(
            tk.END, "-" * 40 + "\n"
        )

        if results:
            for filename in sorted(results):
                result_area.insert(
                    tk.END, filename + "\n"
                )
        else:
            result_area.insert(
                tk.END, "No matching documents found.\n"
            )

        result_area.insert(
            tk.END,
            f"\nTotal matching documents: {len(results)}"
        )

    except ValueError as error:
        result_area.insert(
            tk.END, f"Search Error:\n{error}"
        )

    result_area.config(state=tk.DISABLED)


def search():
    query = search_entry.get()
    display_results(query)


def clear():
    search_entry.delete(0, tk.END)
    result_area.config(state=tk.NORMAL)
    result_area.delete("1.0", tk.END)
    result_area.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Web Search Mining System")
root.geometry("850x600")
root.minsize(650, 450)
root.configure(bg="#e8eef7")

title_label = tk.Label(
    root,
    text="WEB SEARCH MINING SYSTEM",
    font=("Arial", 22, "bold"),
    bg="#e8eef7",
    fg="#172554"
)
title_label.pack(pady=(25, 8))

subtitle_label = tk.Label(
    root,
    text="Search across 20 documents using Boolean and Wildcard queries",
    font=("Arial", 11),
    bg="#e8eef7",
    fg="#526581"
)
subtitle_label.pack(pady=(0, 20))

search_frame = tk.Frame(root, bg="#f0f2f5")
search_frame.pack(fill=tk.X, padx=40)

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 14),
    relief=tk.FLAT,
    bd=0,
    bg="#ffffff",
    fg="#172554"
)
search_entry.pack(
    side=tk.LEFT, fill=tk.X, expand=True,
    ipady=12, padx=(0, 10)
)

search_button = tk.Button(
    search_frame,
    text="SEARCH",
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief=tk.FLAT,
    padx=22,
    pady=10,
    command=search
)
search_button.pack(side=tk.LEFT)

clear_button = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 10, "bold"),
    bg="#dbeafe",
    fg="#1e3a8a",
    relief=tk.FLAT,
    padx=20,
    pady=8,
    command=clear
)
clear_button.pack(pady=12)

result_label = tk.Label(
    root,
    text="SEARCH RESULTS",
    font=("Arial", 12, "bold"),
    bg="#e8eef7",
    fg="#172554"
)
result_label.pack(anchor="w", padx=40, pady=(12, 8))

result_area = scrolledtext.ScrolledText(
    root,
    font=("Consolas", 11),
    wrap=tk.WORD,
    relief=tk.FLAT,
    padx=15,
    pady=12,
    bg="#f8fafc",
    fg="#24344d"
)
result_area.pack(
    fill=tk.BOTH, expand=True,
    padx=40, pady=(0, 25)
)

result_area.insert(
    tk.END,
    "Welcome to the Web Search Mining System!\n\n"
    "Enter a query and click SEARCH.\n\n"
    "Examples:\n"
    "cloud AND computing\n"
    "cloud OR blockchain\n"
    "machine learning\n"
    "mach*\n"
    "comput*\n"
)
result_area.config(state=tk.DISABLED)

search_entry.bind("<Return>", lambda event: search())

root.mainloop()
