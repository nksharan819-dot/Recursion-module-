# Word Fractal

A Python program that generates a *fractal-like text pattern* from a given word using recursion.  
This project demonstrates how recursion can be applied in string manipulation to create visually interesting outputs.

---

##  Example

### Input
```python
def word_fractal(word):
    if len(word) == 1:
        return word
    inner_pattern = word_fractal(word[1:-1])
    return word + "\n" + inner_pattern + "\n" + word

print(word_fractal("PYTHON"))
