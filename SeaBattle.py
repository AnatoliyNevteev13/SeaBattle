class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Exceptions(Options):
    pass

class OutOfBoard(Exceptions):
    def __str__(self):
        return "Out of the board"

class RepetativeShoot(Exceptions):
    def __str__(self):
        return "You have shooten there"

class WrongPositioning(Exceptions):
    pass


class Ship:
    def __init__(self, front, l, o):
    self.front = front
    self.l = l
    self.o = 0
    self.lives = l

    def dots(self):
        ship_dots = []
        for i in range(self.l)
            cur_x = self.front.x
            cur_y = self.front.y

            if self.o == 0
                cur_x += 1

            elif self.o == 1
                cur_y += 1

            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots

    def shooten(self, shot)
        return shot in self.dots
        print("Score")

class Board:
    def __init__(self, hid = False, size = 6):
       self.size = size
       self.hid = hid

       self.count = 0

       self.field = [ ["0"]*size for _ in range(size) ]

       self.busy = []
       self.ships = []

    def __str__(self):
       res = ""
       res += " | 1 | 2 | 3 | 4 | 5 | 6 |"
       for i, row in enumerate(self.field):
           res += f"\n{i+1} | " + " | ".join(row) + " |"

       if self.hid
           res = res.replace("◻︎", 0"")
       return res

    def out(self, d):
       return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def deck(self, ship, verb = False):
       near = [
        (-1, -1), (-1, 0), (-1, -1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
       ]
       for d in ship.dots:
          for dx, dy in near:
              cur = Dot(d.x + dx, d.y +dy)
              if not (self.out(cur)) and cur not in self.busy:
                 if verb:
                     self.field[cur.x][cur.y] = "."
                 self.busy.append(cur)

    def new_ship(self, ship):
       for d in ship.dots:
           if self.out(d) or d in self.busy:
               raise BoardMispossition()
       for d in ship.dots:
           self.field[d.x][d.y] = "◼"
           self.busy.append(d︎)

       self.ships.append(ship)
       self.deck(ship)

    def shot(self, d):
        if self.out(d):
           raise OutOfBoard()

        if d in self.busy:
         raise RepetativeShoot()

        self.busy.append(d)

        for ship in self.ships:
           if d in ship.dots:
               ship.lives -= 1
               self.field[d.x][d.y] = "X"
               if ship.lives == 0:
                  self.count += 1
                  self.deck(ship, verb = True)
                  print("Ship destroyed")
                  return False
               else:
                   print("Ship hit")
                   return True

        self.field[d.x][d.y] = "."
        print("Missed")
        return False

    def begin(self):
        self.busy = []

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(selfself):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot.(target)
                return repeat
            except Exception as e:
                print(e)

class AI(Player):
    def ask(selfself):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Computer turn: {d.x + 1}{d.y + 1}")
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input("Your turn: ").split()

            if len(cords) != 2:
                 print(" 2 coordinates ")
                 continue
            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                 print(" Need digits ")
                continue

            x, y = int(x), int(y)

             return Dot(x - 1, y - 1)

class Game:
    def try_board(self):
         lens = [3, 2, 2, 1, 1, 1, 1]
         board = Board(size=self.size)
         attempts = 0
        for l in lens:
            while True:
                attemps += 1
                if attempts > 100:
                     return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size), l, randint(0, 1)))
                try:
                    board.add_ship(ship)
                    break
                except WrongPositioning:
                    pass
        board.begin()
        return board

     def random_board(self)
        board = None
        while board is None:
            board = self.try_board()
         return board

    def __inint__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.user = User(pl, co)

    def greeting(self):
        print("-------------------")
        print("     Greetings     ")
        print(---------------------)
        print("    X for rows     ")
        print("    Y for columns  ")

    def loop(self):
        num = 0
        while True:
            print("-" * 10)
            print("User board")
            print(self.user.board)
            print("-" * 20)
            print(" AI board ")
            print(self.ai.board)
            print("-" * 10)
            if num % 2 == 0:
                print("Your turn")
                repeat = self.user.move()
            else:
                print("AI turn")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 10)
                print(" You Win! ")
                break

            if self.user.board.count == 7:
                print("-" * 10)
                print(" AI Win! ")
                break
            num += 1

    def start(self):
        self.greeting()
        self.loop

g = Game()
g.start()
