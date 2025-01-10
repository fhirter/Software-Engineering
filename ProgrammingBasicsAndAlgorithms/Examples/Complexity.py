def return_first(values):
  return values[0]


def search(values, key):
    for value in values:
        if key == value:
            return True

    return False


def find_doublettes(values):
    doublettes = {}
    for value in values:
        doublettes[value] = 0
        for other_value in values:
            if value == other_value:
                doublettes[value] =  doublettes[value] + 1
        if doublettes[value] == 1:
            del doublettes[value]
    return doublettes

def find_in_tree(tree, key):
    if tree['value'] == key:
        return True

    elif key > tree['value']:
        return find_in_tree(tree.get('greater'), key)

    else:
        return find_in_tree(tree.get('smaller'), key)