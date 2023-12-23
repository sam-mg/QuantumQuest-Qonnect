def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    n_list = []
    for i in matrix:
        for j in i:
            n_list.append(j)
    return bytearray(n_list)

# Since the matrix elemnets are in form of ASCII, we can convert it directly
def ascii2text(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(chr(mat[i][j]), end='')

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))
ascii2text(matrix)