# Übung Tests - Lösungen

## 1
Es wird die Methode `snake.move()` aufgerufen obwohl `snake_grow()` getestet werden soll. Es ist nicht ersichtlich, wieso dies nötig ist. Testname passt nicht zum Code.
Wieso ist die Methode `snake.grow()` abhängig von `start_position` und `set_direction()`.

Eine Lösung kann anhand von diesem Code-Ausschnitt nicht vorgeschlagen werden. Allenfalls könnte `move()` einen Parameter erhalten, ob die Schlange wachsen soll oder nicht.
`grow()` könnte dann gekapselt werden.

```python
def test_snake_grow(self):

    start_position = [(0, 0), (1, 0), (2, 0)]

    snake = Snake(start_position)

    snake.set_direction('Down')

    # Act
    snake.move()
    actual_result_grow = snake.grow()
```

## 2
Der Methode `snake.set_direction` wird `None` als Parameterwert übergeben. Es ist nicht ersichtlich, wieso der Rückgabewert `Left` sein soll.

Der Test könnte umbenennt werden in `test_if_default_direction_is_left`. Um die default Richtung zu testen könnte `set_direction` weggelassen werden. 
Um `set_direction zu testen könnte ein anderer Wert als `None` für direction gewählt werden.

```python
def test_snake_direction(self):

    start_position = [(0, 0), (1, 0), (2, 0)]

    snake = Snake(start_position)

    direction = None

    # Act

    actual_result_direction = snake.set_direction(direction)

    # Assert
    self.assertEqual(actual_result_direction, 'Left')

    print(actual_result_direction)
```

## 3
Die Schnittstelle der Methoden ist wenig intuitiv weshalb der Code ausführlich kommentiert werden muss.

In einem ersten Schritt könnte die `player_input` Methode so geändert werden, dass sie die üblichen Feldbezeichner (B2) akzeptiert. 
Weiter könnten die Figuren einzeln auf die Felder gesetzt werden, damit wäre im Code sichtbar, auf welchem Feld sich welche Figuren befinden.
```python
board = Board()
board.player_input((1, 1))      # select white pawn B2
board.player_input((1, 3))      # move white pawn to B4
board.player_input((3, 6))      # select black pawn D7
board.player_input((3, 4))      # move black pawn to D5
board.player_input((1, 3))      # select white pawn B4
```

## 4
Es ist nicht verständlich, was hier getestet wird.

Anhand von diesem Code-Ausschnitt sind kaum mögliche Änderungen erkennbar.
Anstelle des Loops könnte eine Stichprobe an einem spezifischen Feld gemacht werden.
Der Test sollte über Methoden des Objekts `board` die Funktionalität Testen und nicht auf die internen Daten (`fields`) des Objekts zugreifen.

```python
expected_result = [[False, False, False, False], [False, False, True, False], [False, False, False, False]]

# Act
actual_result = [[], [], []]
for column in range(3):
    for row in range(2, 6):
        actual_result[column].append(board.fields[column][row].highlighted)

# Assert
self.assertEqual(expected_result, actual_result)
```

## 5
`field.build_game` gibt vier verschiedene Werte zurück. Für den Test wird jedoch nur einer verwendet, die anderen sind überflüssig.

Anstelle von vier Rückgabewerten könnten das Objekt `field` getter für die verschiedenen Werte anbieten.
```python
def test_build_game(self):

    expected_result_food = self.creat_field()
    field = Field()

    game = field.build_game(None)

    actual_result_game_snake, actual_result_game_food, counter, game_over = game

    # Assert

    print(actual_result_game_snake)

    expected_result_snake = [(-1, 0), (0, 0), (1, 0)]

    self.assertEqual(actual_result_game_snake, expected_result_snake)
    self.assertIn(actual_result_game_food, expected_result_food)
```

## 6
Dem Bauer muss beim Methodenaufruf von `get_possible_directions` die Farbe übergeben werden, obwohl diese für die Bewegungsrichtung nicht relevant ist.

Dem Bauer kann die Farbe beim Erstellen mitgegeben werden. Beim Methodenaufruf von `get_possible_directions` wird dies beim entsprechenden Feld abgerufen. 
Es müsste aber auch überprüft werden, wieso die Farbe für diese Methode überhaupt nötig ist. 
Dies ist vermutlich aufgrund dessen, dass der Bauer nur in eine Richtung bewegt werden kann. Dies ist jedoch nicht von der Farbe abhängig. 
```python
def test_get_possible_directions_move(self):
# Arrange
piece = Pawn(True)
is_attack = False
is_white = True
expected_result = [(0, 1)]

# Act
actual_result = piece.get_possible_directions(is_attack, is_white)

# Assert
self.assertEqual(expected_result, actual_result)
```