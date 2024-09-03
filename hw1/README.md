
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

Hence, if `values[3] = 6`, the tile labeled `6` is positioned at the center of the puzzle.

### Exercise 3: Command Interface.
The `EightPuzzle` class has a method named `ExecuteCommand` which takes a string `command` as input. `ExecuteCommand` splits `command` into an opcode and an operand. The opcode (first word of the `command`) is mapped to a function which executes with the operand as input.

Any command beginning with "#" or "//" is considered a comment and ignored by the execution engine.

### Exercise 4: Reading Command Files (Scripting).
The `EightPuzzle` class has a method named `CommandFile` which takes a filepath `path` as input. `path` should contain a sequence of commands separated by line breaks. `CommandFile` reads commands in order, sequentially calling `ExecuteCommand` each line.
<span style="font-size:0.5em;">

| opcode | operands | domain | explaination |
|---|---|---|---|
| move | `direction` | "up", "down", "left", right" | swap the non-tile with the tile below, above, right or left (respectively). |
| setState | `values` | A space-separated list. <br> $0 <=$ `values[i]` $<= 8$, <br> `len(values)` $= 9$, <br>`values[i] != values[j]` <br> ($0 <= i, j <= 8$). | Set the state of the eight-puzzle. | scrambleState | `n` | An integer. `n >= 0`. | Perform `n` random moves on the eight-puzzle. |
| printState | N/A | N/A | Print the current state of the eight-puzzle as a grid. |
| print | any | N/A | Print the rest of the line. This is simply a call to python's `print` builtin. |
</span>

## Written Questions

### Exercise 1: How you personally use AI. 
Try to give a complete account of the AI you use on a regular basis. These can be explicit examples 
like ChatGPT or Copilot, AI-based image generation, or they can be implicit
within other apps like speech recognition or route finding. For each example describe 1) your experience (e.g.
how you use it, why you find it useful), their 2) strengths and 3) limitations, and 4) where you see these
heading over the next several years.


1. Generate comments for code: I'll occasionally tell chat GPT to rewrite my code descriptions/comments.  For ome of the more technical documentation I write, GPT improves readability and allows me to control the verbosity of the output (e.g. "Make it shorter"). Unfortunately, GPT often misunderstands my intention and fails to generate a useful description. I don't have much hope for any imporvement in the near future.  GPT does a great job on tasks it's already seen. However, for new problems, I'll probably be better off doing my own technical writing.

2. Generate counter-arguments for argumentative writing. This is probably my favorite use for LLMs, as the output doesn't have to be that great, it just has to give me an idea of how I'm wrong. The main benifit is that GPT has probably processed any counterargument I'd come across in the real world. This means GPT usually covers any logical gaps I'd need to contend with in a rhetorical piece. In the same vein, GPT usually won't provide good responses with further prodding, which can be annoying if I'm not satisfied with the first response. I also encounter an issue where GPT will respond to an adjacent topic, not addressing my prompt directly. I don't see the former limitation getting resolved in the near future. I do, however, believe that responses will become more relevant as better models are developed.

### Exercise 2: Intelligence tests. 
Perform your own Turing-like test on ChatGPT or similar large language
models to assess different aspects of the system’s intelligence. Describe and document (in terms of examples)
five distinct ways in which the model exhibits aspects of intelligence and five ways in which it does not.
Grading will be on the distinctness of your queries and how well each is designed to test specific aspects of
intelligence. Be sure to explain your reasoning behind your choices.

To the best of my understanding, LLMs are basically context-sensitive (in the informal sense) function approximators where the function in question maps a sequence of tokens (the last chunk of a conversation) to the next sequence of tokens (the expected response - also a sequence of tokens).  Thus, asking classic "Turing-test" questions about emotional experience or social scenarios won't be the most effective measure of "human intelligence". Instead, I will try to trigger "robot" errors by messing with GPT's ability to solve math problems. Of course, I won't judge based on correctness (as many humans are bad at math), but on how GPT responds. Things like wild inconsistencies in knowledge level will be penalized.

#### Queries:

Q: "List the first three numbers between 1 and 2"

A: "The first three numbers between 1 and 2 are:

   1.1, 1.2, and 1.3.

   There are infinitely many numbers between 1 and 2, so you can select any set of three numbers between them."

Analysis: (+) GPT tries to explain itself rather than just spitting out an answer. I would expect a human to do this in order to save face. (-) However, GPT also makes an unlikely combination of beginner-mistakes and (relatively) advanced references. Not many people would reference the infinite set of numbers between 1 and 2 while confidently stating that "the first the" are "1.1, 1.2 and 1.3".

Q: "Solve the following: six times 2 plus the number after twenty times nine + 43? You may only answer with the
   numerical answer."

A: "2."

Analysis: $6 \times 2 + (20 + 1) \times 9 + 43$ is most certainly not equal to 2. Apparently this happens when you don't allow GPT to work it out one step at a time (it messes with the attention mechanism). I'd expect a human to give the correct answer (since the text is in front of them and they can solve sequentially), give up, or give an incorrect answer a lot greater than 2 (even if you were to guess, all operations in the described expression increase the value, and all are greater than or equal to 2).



| Q | A | Analysis |
| --- | --- | --- |
| "List the first three numbers between 1 and 2" | "The first three numbers between 1 and 2 are: <br> 1.1, 1.2, and 1.3. <br>There are infinitely many numbers between 1 and 2, so you can select any set of three numbers between them." | (+) GPT tries to explain itself rather than just spitting out an answer. I would expect a human to do this in order to save face. (-) However, GPT also makes an unlikely combination of beginner-mistakes and (relatively) advanced references. Not many people would reference the infinite set of numbers between 1 and 2 while confidently stating that "the first the" are "1.1, 1.2 and 1.3".|
| "Solve the following: six times 2 plus the number after twenty times nine + 43? You may only answer with the
   numerical answer." | "2." | $6 \times 2 + (20 + 1) \times 9 + 43$ is most certainly not equal to 2. Apparently this happens when you don't allow GPT to work it out one step at a time (it messes with the attention mechanism). I'd expect a human to give the correct answer (since the text is in front of them and they can solve sequentially), give up, or give an incorrect answer a lot greater than 2 (even if you were to guess, all operations in the described expression increase the value, and all are greater than or equal to 2). |
