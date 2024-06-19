Create a program that reads a text file containing runner names and their race completion times in seconds, calculates the total time for each runner, and then writes the runner names along with their total times to a new text file. Additionally, the program should print the runner with the shortest total time.

The format of the input file (**`times.txt`**) is as follows:


Anna 320 300 310
Ben 280 270 260
Cara 290 295 285


- Each line represents a runner's name followed by their race completion times in seconds for three races separated by spaces.
- The first time is for the first race, the second time is for the second race, and so on.

The output should be written to a file (**`totals.txt`**) in the following format:


Anna 930
Ben 810
Cara 870


Additionally, the program should print:


Runner with the shortest total time: Ben