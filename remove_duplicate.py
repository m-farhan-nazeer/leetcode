def remove_adjacent_duplicates(s: str) -> str:
    # Convert to mutable list for in-place modification
    chars = list(s)
    if not chars:
        return ""

    write_index = 1

    # Scan the string starting from the second character
    for read_index in range(1, len(chars)):
        # If current char is different from the previous unique char
        if chars[read_index] != chars[write_index - 1]:
            chars[write_index] = chars[read_index]
            write_index += 1

    # Join only the unique prefix back into a string
    return "".join(chars[:write_index])


# Example: "aaabbcdd" -> "abcd"
print(remove_adjacent_duplicates("aaabbcdd"))
