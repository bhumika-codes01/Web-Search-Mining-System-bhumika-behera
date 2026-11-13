
import re
from text_normalization import normalize_text


def tokenize_query(query):
    return re.findall(r"\(|\)|[^\s()]+", query)


def insert_implicit_and(tokens):
    result = []
    operators = {"AND", "OR"}

    for i, token in enumerate(tokens):
        if i > 0:
            previous = tokens[i - 1]

            previous_is_term = (
                previous not in operators
                and previous != "NOT"
                and previous != "("
            )

            current_starts_expression = (
                token not in operators
                and token != ")"
            )

            if previous == ")" or previous_is_term:
                if current_starts_expression or token == "(":
                    result.append("AND")

        result.append(token)

    return result


def to_postfix(tokens):
    precedence = {"OR": 1, "AND": 2, "NOT": 3}
    output = []
    stack = []

    for token in tokens:
        upper = token.upper()

        if upper == "(":
            stack.append(upper)

        elif upper == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            if not stack:
                raise ValueError("Mismatched parentheses.")

            stack.pop()

        elif upper in precedence:
            while (
                stack
                and stack[-1] != "("
                and (
                    precedence[stack[-1]] > precedence[upper]
                    or (
                        precedence[stack[-1]] == precedence[upper]
                        and upper != "NOT"
                    )
                )
            ):
                output.append(stack.pop())

            stack.append(upper)

        else:
            output.append(token)

    while stack:
        if stack[-1] == "(":
            raise ValueError("Mismatched parentheses.")
        output.append(stack.pop())

    return output


def evaluate_postfix(postfix, inverted_index, all_documents):
    result_stack = []
    all_docs = set(all_documents)

    for token in postfix:
        if token == "AND":
            if len(result_stack) < 2:
                raise ValueError("Invalid AND expression.")

            right = result_stack.pop()
            left = result_stack.pop()
            result_stack.append(left & right)

        elif token == "OR":
            if len(result_stack) < 2:
                raise ValueError("Invalid OR expression.")

            right = result_stack.pop()
            left = result_stack.pop()
            result_stack.append(left | right)

        elif token == "NOT":
            if not result_stack:
                raise ValueError("Invalid NOT expression.")

            operand = result_stack.pop()
            result_stack.append(all_docs - operand)

        else:
            terms = normalize_text(token)

            if len(terms) != 1:
                raise ValueError(
                    f"Invalid search term: {token}"
                )

            result_stack.append(
                set(inverted_index.get(terms[0], set()))
            )

    if len(result_stack) != 1:
        raise ValueError("Invalid search query.")

    return result_stack[0]


def evaluate_query(query, inverted_index, all_documents):
    tokens = tokenize_query(query)

    if not tokens:
        return set()

    tokens = insert_implicit_and(tokens)
    postfix = to_postfix(tokens)

    return evaluate_postfix(
        postfix,
        inverted_index,
        all_documents
    )


if __name__ == "__main__":
    from inverted_index import build_inverted_index

    index, documents = build_inverted_index()
    all_documents = set(documents.keys())

    print("========== QUERY PROCESSING ==========")

    while True:
        query = input("\nEnter Boolean query (or 'exit'): ")

        if query.lower() == "exit":
            break

        try:
            results = evaluate_query(
                query,
                index,
                all_documents
            )

            print("\nMatching Documents:")
            for filename in sorted(results):
                print(filename)

            print("Total results:", len(results))

        except ValueError as error:
            print("Query Error:", error)
