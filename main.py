# Problem 1.  Repres
import pathlib
import random
from os import PathLike


class State:
    def __init__(self, values: list[int]):
        """!
        Representation of a state.  No value is represented by 0.
        """
        self.values_ = values

    def __getitem__(self, key):
        return self.values_[3 * key[0] + key[1]]


class EightPuzzle:
    def __init__(self, rng_seed=0):
        """!
        @brief An eight-puzzle instance.
        """

        # Current state.
        self.current_state_ = State([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.non_tile_ = 0
        random.seed(rng_seed)

    def ExecuteCommand(self, command: str) -> bool:
        """!
        @brief Parse a command.
        @param command: A valid command or a comment.  See README.md for more.
        @return False if an invalid command is encountered.  Returns True
        otherwise.
        """
        opcode_to_func_ = {
            "move": self.Move,
            "setState": self.SetState,
            "printState": self.PrintState,
            "scrambleState": self.ScrambleState,
        }

        command = command.strip(" ")
        # Check for comment.
        if command.startswith("//|#") | (command == ""):
            return True

        # Give 0-ary operators a fake operand.
        if command.count(" ") == 0:
            opcode = command
            operand = ""
        else:
            opcode, operand = command.split(" ", 1)

        if opcode not in opcode_to_func_:
            print(f"Error: Invalid Command: {opcode}")
            return False

        # Opcode defined.
        opcode_to_func_[opcode](operand)
        return True

    def CommandFile(self, path: PathLike) -> bool:
        """!
        @brief Sequentially execute the commands contained in "path".
        @param path: A filepath pointint to a list of valid commands.
        @return False if any command fails to execute for any reason.  Returns
        True otherwise.
        """
        # Check for bad filepath.
        path = pathlib.Path(path)
        try:
            path = path.resolve()
        except:
            print(f"Failed to resolve path {path}")
            return False

        data = path.read_text()
        commands = data.split("\n")
        for command in commands:
            if not self.ExecuteCommand(command):
                return False

        return True

    def ValidateState(self, values: list[int]) -> bool:
        """
        @brief Determine validity of a state.
        """
        # 1. All values must be between 0 and 8 (inclusive).
        for val in values:
            if val > 8:
                return False
        # 2. All values must be unique.
        S = set(values)
        if len(S) < 9:
            return False

        return True

    # Set current state.
    def SetState(self, operand: str) -> bool:
        values = list(map(int, operand.split()))
        if not self.ValidateState(values):
            print("Error: Invalid State.")
            return False

        self.current_state_.values_ = values
        return True

    # Move.
    def Move(self, direction, suppress_output=False) -> bool:
        # Swap the tiles in positions p and q
        p = 1 * self.non_tile_  # Need to modify
        q = 0

        # Difference between the q and p such that q is the position of the
        # non-tile after the move.
        diff = {
            "left": -1,
            "right": 1,
            "up": -3,
            "down": 3,
        }

        # Determine membership in set of indices where the non-tile can't move
        # in <direction>.
        is_invalid_index = {
            "left": lambda x: x % 3 == 0,
            "right": lambda x: x % 3 == 2,
            "up": lambda x: x < 3,
            "down": lambda x: x > 5,
        }

        # Error handling.
        if direction not in diff:
            if not suppress_output:
                print(f"Error: Invalid move {direction}).")
            return False
        if is_invalid_index[direction](p):
            if not suppress_output:
                print(f"Error: Invalid move (cannot shift {direction}).")
            return False

        # Perform move.
        q = p + diff[direction]
        vals = self.current_state_.values_
        vals[p], vals[q] = vals[q], vals[p]
        self.non_tile_ = q
        return True

    # Randomize puzzle.
    def ScrambleState(self, n, suppress_output=False) -> bool:
        try:
            n = int(n)
        except:
            print(f"Not a number: {n}")
            return False

        directions = ["left", "right", "up", "down"]
        for _ in range(n):
            r = random.randint(0, 3)
            self.Move(direction=directions[r], suppress_output=True)

        return True

    # Print puzzle as a grid.
    def PrintState(self, operand: str):
        def tile(val: int):
            if val != 0:
                return str(val)
            else:
                return " "

        s = self.current_state_
        # Kinda cool how the pipes got lined up like that!
        print("┏━━━┯━━━┯━━━┓")
        print("┃ " + " │ ".join([tile(s[0, i]) for i in range(3)]) + " ┃")
        print("┠───┼───┼───┨")
        print("┃ " + " │ ".join([tile(s[1, i]) for i in range(3)]) + " ┃")
        print("┠───┼───┼───┨")
        print("┃ " + " │ ".join([tile(s[2, i]) for i in range(3)]) + " ┃")
        print("┗━━━┷━━━┷━━━┛")


# For testing purposes.
def Run(seed=0):
    movemap = {
        "w": "move down",
        "a": "move right",
        "s": "move up",
        "d": "move left",
    }

    ep = EightPuzzle(rng_seed=seed)

    # Run.
    ep.ScrambleState(100)
    ep.PrintState("")
    cmd = input(">> ")
    while cmd != "Exit":
        try:
            ep.ExecuteCommand(movemap[cmd])
        except:
            pass
        print(50 * "\n")
        ep.PrintState("")
        cmd = input(">> ")


def Test():
    # Rng seed set to 0.
    sample = EightPuzzle()

    test_script = pathlib.Path("scripts/test.txt")
    sample.CommandFile(test_script)


if __name__ == "__main__":
    Run(0)
