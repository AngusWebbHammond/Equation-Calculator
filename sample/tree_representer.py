from equation_classes import Expression, Integer, Operator


def return_tree_representation(lexeme_list: list, token_list: list) -> Expression:
    compressed_lists: list[list, list] = list(zip(lexeme_list, token_list))
    second_compressed_list: list[list, list] = list(zip(lexeme_list, token_list))
    bidmas_index: int = 0
    operator_order = [
        "INTEGER",
        "INDICIE",
        "DIVISION",
        "MULTIPLY",
        "ADDITION",
        "SUBTRACT",
    ]
    while len(compressed_lists) != 1:
        index_to_remove_list: list = []
        for index, [lexeme, token] in enumerate(compressed_lists):
            if (
                operator_order[bidmas_index] == "INTEGER"
                and operator_order[bidmas_index] == token
            ):
                second_compressed_list[index] = [Integer(lexeme), "INTEGER"]
                continue
            if token == operator_order[bidmas_index]:
                second_compressed_list[index] = [
                    Operator(
                        compressed_lists[index - 1][0],
                        compressed_lists[index + 1][0],
                        token,
                    ),
                    "OPERATOR",
                ]
                index_to_remove_list.append(index - 1)
                index_to_remove_list.append(index + 1)

        for index in sorted(index_to_remove_list, reverse=True):
            second_compressed_list.pop(index)
        bidmas_index += 1
        compressed_lists = second_compressed_list

    return Expression(compressed_lists[0][0])
