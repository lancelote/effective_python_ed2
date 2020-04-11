from typing import Union

# examples of str / bytes sequences in Python
###############################################################################


def sequence_examples() -> None:
    bytes_sequence = b'h\x65llo'
    print(list(bytes_sequence))
    print(bytes_sequence)

    str_sequence = 'a\u0300 propos'
    print(list(str_sequence))
    print(str_sequence)


# helper functions for bytes / str conversion
###############################################################################


def to_str(bytes_or_str: Union[bytes, str]) -> str:
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str: Union[bytes, str]) -> bytes:
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


if __name__ == '__main__':
    sequence_examples()

    print('\n# covert to str')
    print(repr(to_str(b'foo')))
    print(repr(to_str('bar')))

    print('\n# convert to bytes')
    print(repr(to_bytes(b'foo')))
    print(repr(to_bytes('bar')))

    print('foo' == b'bar')
