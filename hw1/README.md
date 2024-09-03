
# CSDS 391 (Intro to AI) Homework 1

## Requirements

## Usage

## Programming Questions

### Exercise 3: State Representation.
See the class "State" in main.py. A state is represented as a list `values` of 9 integers (0-9). The index of a value determines the position of the tile whose number is given by the value. Indices correspond to positions of the eight puzzle as follows.

| <!-- -->    | <!-- -->   | <!-- -->    |
|---|---|---|
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

Hence, if `values[0] = 3`, the tile labeled `3` is positioned at the center of the puzzle.

### Exercise 3: Command Interface.
The `EightPuzzle` class has a method named `ExecuteCommand` which takes a string `command` as input. `ExecuteCommand` splits `command` into an opcode and an operand. The opcode (first word of the `command`) is mapped to a function which executes with the operand as input.

Any command beginning with "#" or "//" is considered a comment and ignored by the execution engine.

### Exercise 4: Reading Command Files (Scripting).
The `EightPuzzle` class has a method named `CommandFile` which takes a filepath `path` as input. `path` should contain a sequence of commands separated by line breaks. `CommandFile` reads commands in order, sequentially calling `ExecuteCommand` each line.


| opcode | operands | domain | explaination |
|---|---|---|---|
| move | `direction` | "up", "down", "left", right" | swap the non-tile with the tile below, above, right or left (respectively). |
| setState | `values` | A space-separated list. $0 <=$ `values[i]` $<= 8$ for $i = 1, ..., 8$. `len(values)` $= 9$. `values[i] != values[j]` for $0 <= i, j <= 8$ | Set the state of the eight-puzzle. |
| scrambleState | `n` | An integer. `n \geq 0`. | Perform `n` random moves on the eight-puzzle. |
| printState | N/A | N/A | Print the current state of the eight-puzzle as a grid. |

#### move
#### setState
#### scrambleState
#### printState




## Written Questions

### Exercise 1: How you personally use AI. 
Try to give a complete account of the AI you use on a regular basis. These can be explicit examples 
like ChatGPT or Copilot, AI-based image generation, or they can be implicit
within other apps like speech recognition or route finding. For each example describe 1) your experience (e.g.
how you use it, why you find it useful), their 2) strengths and 3) limitations, and 4) where you see these
heading over the next several years.

1. Generate comments for code: I'll occasionally tell chat GPT to rewrite my code descriptions/comments.  For ome of the more technical documentation I write, GPT improves readability and allows me to control the verbosity of the output (e.g. "Make it shorter"). Unfortunately, GPT often misunderstands my intention and fails to generate a useful description.  In complete honesty, I don't have much hope for any imporvement in the near future.  GPT does a great job on tasks it's already seen.  However, for new problems, I'll probably be better off doing my own technical writing.

### Exercise 2: Intelligence tests. 
Perform your own Turing-like test on ChatGPT or similar large language
models to assess different aspects of the system’s intelligence. Describe and document (in terms of examples)
five distinct ways in which the model exhibits aspects of intelligence and five ways in which it does not.
Grading will be on the distinctness of your queries and how well each is designed to test specific aspects of
intelligence. Be sure to explain your reasoning behind your choices.
