def interrupciones_recursivas(a, b):
    if b == 0:
        return 0

    return a + interrupciones_recursivas(a, b - 1)