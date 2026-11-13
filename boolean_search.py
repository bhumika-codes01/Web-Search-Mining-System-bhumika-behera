  
import re
from indexer import build_inverted_index
from linguistic_processing import process_text


def evaluate_query(query, inverted_index, all_documents):

    # Identify Boolean operators and search terms
    tokens = re.findall(
        r'\(|\)|\bAND\b|\bOR\b|\bNOT\b|[a-zA-Z]+',
        query,
        re.IGNORECASE
    )

    if not tokens:
        raise ValueError("Please enter a valid query.")

    # Convert terms to normalized tokens.
    # Keep Boolean operators unchanged.
    processed_tokens = []

    for token in tokens:

        upper_token = token.upper()

        if upper_token in {"AND", "OR", "NOT", "(", ")"}:
            processed_tokens.append(upper_token)

        else:
            stemmed = process_text(token)

            if len(stemmed) != 1:
                raise ValueError(
                    f"Invalid or unsupported search term: {token}"
                )

            processed_tokens.append(stemmed[0])

    # Insert implicit AND between adjacent operands/groups.
    # This allows queries such as: machine learning
    expanded_tokens = []

    for token in processed_tokens:

        if expanded_tokens:
            previous = expanded_tokens[-1]

            if (
                (previous not in {"AND", "OR", "NOT", "("})
                and (token not in {"AND", "OR", ")"})
            ):
                expanded_tokens.append("AND")

        expanded_tokens.append(token)

    # Convert infix Boolean expression to postfix notation.
    precedence = {
        "OR": 1,
        "AND": 2,
        "NOT": 3
    }

    output = []
    operators = []

    for token in expanded_tokens:

        if token in {"AND", "OR", "NOT"}:

            while (
                operators
                and operators[-1] != "("
                and (
                    precedence[operators[-1]] > precedence[token]
                    or (
                        precedence[operators[-1]] == precedence[token]
                        and token != "NOT"
                    )
                )
            ):
                output.append(operators.pop())

            operators.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":

            while operators and operators[-1] != "(":
                output.append(operators.pop())

            if not operators:
                raise ValueError("Mismatched parentheses.")

            operators.pop()

        else:
            output.append(token)

    while operators:

        operator = operators.pop()

        if operator == "(":
            raise ValueError("Mismatched parentheses.")

        output.append(operator)

    # Evaluate postfix expression using document sets.
    stack = []

    for token in output:

        if token == "NOT":

            if not stack:
                raise ValueError("Invalid NOT operation.")

            operand = stack.pop()
            stack.append(all_documents - operand)

        elif token in {"AND", "OR"}:

            if len(stack) < 2:
                raise ValueError("Invalid Boolean expression.")

            right = stack.pop()
            left = stack.pop()

            if token == "AND":
                stack.append(left & right)

            else:
                stack.append(left | right)

        else:
            stack.append(inverted_index.get(token, set()))

    if len(stack) != 1:
        raise ValueError("Invalid Boolean query.")

    return stack[0]


if __name__ == "__main__":

    index = build_inverted_index()

    all_docs = set()

    for documents in index.values():
        all_docs.update(documents)

    print("\n========== BOOLEAN SEARCH ENGINE ==========")

    while True:

        query = input("\nEnter Boolean Query (or 'exit'): ")

        if query.lower() == "exit":
            break

        try:
            results = evaluate_query(query, index, all_docs)

            if results:
                print("\nMatching Documents:")

                for document in sorted(results):
                    print(document)

            else:
                print("\nNo matching documents found.")

        except ValueError as error:
            print("\nQuery Error:", error)
