# Übung Tests
Tests geben uns wertvolles Feedback zu unserem Design. Tests die schwer zu schreiben oder schwer verständlich sind zeigen oft Missstände im Design auf.

Beantworte für die folgenden Code-Ausschnitte folgende Fragen:
1. Was sagt uns der Test hier?
2. Was sollte geändert werden?

Achte dich insbesondere auf folgende Themen:
- Encapsulation
- Separation of Concerns
- Polymorphism
- Naming
- Comments
- Coupling / Cohesion

## 1
Es wird die Methode `snake.move()` obwohl `snake_grow()` getestet werden soll. Es ist nicht ersichtlich, wieso dies nötig ist.

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

    # Assert
    self.assertEqual(actual_result_direction, 'Left')

    print(actual_result_direction)
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

## 5
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