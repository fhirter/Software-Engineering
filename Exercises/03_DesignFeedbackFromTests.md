# Übung Tests
Tests geben uns wertvolles Feedback zu unserem Design. Tests die schwer zu schreiben oder schwer verständlich sind zeigen oft Missstände im Design auf.

Beantworte für die folgenden Code-Ausschnitte folgende Fragen:
1. Was sagt uns der Test hier?
2. Was sollte geändert werden?

## 1
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
```python
def test_snake_direction(self):

    start_position = [(0, 0), (1, 0), (2, 0)]

    snake = Snake(start_position)

    direction = None

    # Act

    actual_result_direction = snake.set_direction(direction)
```

## 3
```python
board = Board()
board.player_input((1, 1))      # select white pawn B2
board.player_input((1, 3))      # move white pawn to B4
board.player_input((3, 6))      # select black pawn D7
board.player_input((3, 4))      # move black pawn to D5
board.player_input((1, 3))      # select white pawn B4
```

## 4
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