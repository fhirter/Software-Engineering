# Übung Komplexität

Ordne folgende Code Beispiele einer Komplixitätsklasse (z.B. O(1), O(n), etc) zu. Schreibe die Klasse dazu auf die
Rückseite des Codes und pinne dieses verdeckt an die Wandtafel.

## Beispiele

---

```python
def return_first(values):
    return values[0]
```

---

```python
def search(values, key):
    for value in values:
        if key == value:
            return True

    return False
```

---

```python
def find_doublettes(values):
    doublettes = {}
    for value in values:
        doublettes[value] = 0
        for other_value in values:
            if value == other_value:
                doublettes[value] = doublettes[value] + 1
        if doublettes[value] == 1:
            del doublettes[value]
    return doublettes
```

---

```python
def find_in_tree(tree, key):
    if tree['value'] == key:
        return True

    elif key > tree['value']:
        return find_in_tree(tree.get('greater'), key)

    else:
        return find_in_tree(tree.get('smaller'), key)
```

---