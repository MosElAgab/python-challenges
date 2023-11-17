import string


def alphabet_position(test_string):
    if isinstance(test_string, str) and len(test_string) == 0:
        return test_string
    test_string = test_string.lower()
    position_dict = {string.ascii_lowercase[i]: i + 1
                     for i in range(len(string.ascii_lowercase))}
    position_list = [str(position_dict[letter]) for letter in
                     test_string if letter.isalpha()]
    output = ' '.join(position_list)
    return output
