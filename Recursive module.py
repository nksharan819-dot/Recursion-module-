def word_fractal(word):
    if len(word) == 1:
        return word
    inner_pattern = word_fractal(word[1:-1])
    return word + "\n" + inner_pattern + "\n" + word

print(word_fractal("PYTHON"))
