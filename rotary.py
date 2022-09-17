#!/usr/bin/env python3
# Author: Ellie V
# Title: Rotary Interpreter in Python
# Language: Rotary 1.2 by User:InputUsername

# TODO: Add CIRCP wrapping using modulo on n circles
# TODO: change values to unsigned 0-255

import random
import sys

TOKENS = (">", "<", "/", "\\", "+", "-", ".", ",",
          "v", "^", "#", "?", "*", "$", "~", "@", "!", "r", "s", "%", "x")

codesegments = []
instrLocs = [                 # 34 instrs
   [5, 6, 7, 8, 9, 10],
   [2, 3, 4, 11, 12, 13],
   [1, 14],
   [0, 15],
   [0, 15],
   [0, 15],
   [1, 14],
   [2, 3, 4, 11, 12, 13],
   [5, 6, 7, 8, 9, 10]
]

class Circle:
      def __init__(self, instr: list):
         self.instr = instr

      def __str__(self):
         return " ".join(self.instr)

def programLoop(circles):
   inpp = 0 # input ptr
   outp = 0 # output ptr
   cirp = 0 # circle ptr
   tape = {0: 0}
   stack = []

   instrPtr = 0
   while instrPtr < 34:
      token = circles[cirp].instr[instrPtr]
      if token == ">":
         inpp += 1
      elif token == "<":
         inpp -= 1
      elif token == "/":
         outp += 1
      elif token == "\\":
         outp -= 1
      elif token == "+":
         tape[inpp] += 1
      elif token == "-":
         tape[inpp] -= 1
      elif token == ".":
         print(chr(tape[outp]), end="")
      elif token == ",":
         chrInp = input("INPUT: ")
         if chrInp == "":
            chrInp = "\n"
         tape[inpp] = ord(chrInp)
      elif token == "v":
         cirp += 1
         if cirp >= len(circles):
            print("\nERROR: circle pointer out of bounds " + str(cirp))
            sys.exit(1)
         instrPtr = -1 # reset instruction pointer
      elif token == "^":
         cirp -= 1
         if cirp < 0:
            print("\nERROR: circle pointer out of bounds " + str(cirp))
            sys.exit(1)
         instrPtr = -1
      elif token == "#":
         print(tape[outp], end="\n")
      elif token == "?" and instrPtr != 33:               # if outp is not 0 skip next instr
         if tape[outp] != 0:
            instrPtr+=1
      elif token == "*" and instrPtr != 33:              # if outp is 0 skip next instr
         if tape[outp] == 0:
            instrPtr+=1
      elif token == "$":
         stack.append(tape[outp])
      elif token == "~":
         if len(stack) == 0:
            inpp = 0
         else:
            tape[inpp] = stack.pop()
      elif token == "@":
         stack.reverse()
      elif token == "r":
         tape[inpp] = random.randint(0, 255)
      elif token == "s":
         if len(stack) != 0:
            n = stack.pop()
            for i in range(1, n):
               print(chr(tape[outp+i]), end="")
      elif token == "%":
         if len(stack) != 0:
            n = stack.pop()
            stack.append(n % tape[outp])
      elif token == "x":
         if len(stack) != 0:
            cirp = stack.pop() - 1
            if cirp >= len(circles):
               print("\nERROR: circle pointer out of bounds")
               sys.exit(1)
            instrPtr = -1

      # Simulate infinite tape
      if inpp not in tape:
         tape[inpp] = 0
      if outp not in tape:
         tape[outp] = 0

      instrPtr += 1
   print("\n")


def getFromFile(filename):
   circles = []
   circle = [[],[],[],[],[],[],[],[],[]]
   with open(filename) as f:
      lines = f.readlines()
      circleLine = 0
      for i in range(0, len(lines)):
         if circleLine == 9:
            circles.append(circle)
            circle = [[],[],[],[],[],[],[],[],[]]
            circleLine = 0
            continue
         lines[i] = lines[i].replace("\n", "")
         for char in lines[i]:
            circle[circleLine].append(char)
         circleLine += 1
      if circleLine != 0:
         circles.append(circle)
   return circles


def getInstrFromCircle(circle):
   instructions = []
   count=0
   for i in range(len(instrLocs)):
      for j in range(len(instrLocs[i])):
         if circle[i][instrLocs[i][j]] in TOKENS:
            count+=1
            instructions.append(circle[i][instrLocs[i][j]])
         else:
            print("Error: invalid token in circle", circle[i][instrLocs[i][j]])
            sys.exit(1)
   fixed_instructions = [
      instructions[3], instructions[4], instructions[5],
      instructions[9], instructions[10], instructions[11],
      instructions[13],instructions[15], instructions[17],
      instructions[19], instructions[21],
      instructions[27], instructions[26], instructions[25],
      instructions[33], instructions[32], instructions[31], instructions[30], instructions[29], instructions[28],
      instructions[24], instructions[23], instructions[22],
      instructions[20], instructions[18], instructions[16],
      instructions[14], instructions[12],
      instructions[6], instructions[7], instructions[8],
      instructions[0], instructions[1], instructions[2],
   ]
   return fixed_instructions


if __name__ == "__main__":
   if len(sys.argv) != 2:
      print("Usage: python getcircle.py <filename>")
      sys.exit(1)

   circles = getFromFile(sys.argv[1])
   for circle in circles:
      newCircle = Circle(getInstrFromCircle(circle))
      codesegments.append(newCircle)

   programLoop(codesegments)
