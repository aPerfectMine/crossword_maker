#!/usr/bin/python3

import random
import datetime
import sys
import test_intersect


#### USAGE #######################################
# ./make_a_crossword.py should work              #
# To change the grid, pick the clue_lengths[]    #
#  you want, change the grid number (which is    #
#  passed to test_intersect.py) at the same      #
#  place in the code                             #
# You'll probably also need to change the tens   #
#  things in the outer-loop for statement        #
#                                                #
##################################################

# set defaults for the number of attempts
outer_attempts   = 1999 # number of times to restart
inner_attempts   = 399 # how many goes before giving up on an attempt
successive_fails = 399  # if we get this many fails in a row, start again
# allow them to be changed from the command line
if len(sys.argv) == 3:
  try:
    outer_attempts = int(sys.argv[1])
  except ValueError:
    print("outer_attempts must be an integer")
    exit(1)
  try:
    inner_attempts = int(sys.argv[2])
  except ValueError:
    print("inner_attempts must be an integer")
    exit(1)

# seed the random
random.seed(datetime.datetime.now().timestamp())

# declare pointers for the files
filePtr03 = open("all03.txt","r")
filePtr04 = open("all04.txt","r")
filePtr05 = open("all05.txt","r")
filePtr06 = open("all06.txt","r")
filePtr07 = open("all07.txt","r")
filePtr08 = open("all08.txt","r")
filePtr09 = open("all09.txt","r")
filePtr10 = open("all10.txt","r")
filePtr11 = open("all11.txt","r")
filePtr12 = open("all12.txt","r")
filePtrTens = open("tens_solutions.out","r")
# read the files into memory
lines03 = filePtr03.readlines()
lines04 = filePtr04.readlines()
lines05 = filePtr05.readlines()
lines06 = filePtr06.readlines()
lines07 = filePtr07.readlines()
lines08 = filePtr08.readlines()
lines09 = filePtr09.readlines()
lines10 = filePtr10.readlines()
lines11 = filePtr11.readlines()
lines12 = filePtr12.readlines()
linesTens = filePtrTens.readlines()
# close the files
filePtr03.close()
filePtr04.close()
filePtr05.close()
filePtr06.close()
filePtr07.close()
filePtr08.close()
filePtr09.close()
filePtr10.close()
filePtr11.close()
filePtr12.close()
filePtrTens.close()

# lengths of clues starting with across clues
#  and the grid number (for test_intersect.py)
grid_number  = 0
clue_lengths = [4,4,4,5,9,7,7,9,5,5,9,7,7,9,5,4,4,4, \
                5,7,7,7,5,7,8,8,8,8,7,7,7,7,5,5] # 34-clue crossword
#
grid_number  = 1
clue_lengths = [7,7,9,5,6,7,4,10,10,4,7,6,5,9,7,7, \
                4,9,6,9,5,8,5,10,10,9,9,8,6,5,5,4] # 32-clue crossword
#
grid_number  = 2
clue_lengths = [8,5,5,4,6,6,4,5,5,8, \
                5,4,6,5,7,7,6,5,5,4] # 20-clue crossword
#
grid_number  = 3             # just the tens, ma'am
clue_lengths = [10,10,10,10] # for the 20-clue grids
#
grid_number  = 4
clue_lengths = [6,4,5,5,10,10,5,5,4,6, \
                4,5,10,5,6,10,6,5,5,4] # 20-clue jimboword A
#
grid_number  = 5
clue_lengths = [6,4,5,5,10,10,5,5,4,6, \
                4,7,10,3,6,10,7,6,4,3] # 20-clue jimboword B
#
grid_number  = 6
clue_lengths = [6,6,8,4,6,6,4,3,4,6,6,4,8,6,6, \
                7,5,7,5,7,5,7,7,7,5,5,5] # 27-clue 13x13 crossword
#
grid_number  = 7
clue_lengths = [4,8,6,6,5,7,7,5,6,6,8,4, \
                6,6,5,7,6,6,3,3,7,6,6,6,6,5] # 26-clue 13x13 crossword
#
grid_number  = 8
clue_lengths = [4,8,6,6,5,7,7,5,6,6,8,4, \
                6,6,5,7,6,6,7,6,6,6,6,5] # as 7, but with the length-3 clues removed
#
grid_number  = 9
clue_lengths = [5,5,6,4,3,7,7,3,4,6,5,5, \
                4,6,9,9,9,6,4] # 19-clue 11x11 grid
#
grid_number  = 10
clue_lengths = [4,8,6,6,5,7,7,5,6,6,8,4, \
                6,6,5,7,6,6,7,6,6,6,6,5] # as 7, but with the length-3 clues removed
#
grid_number  = 11
clue_lengths = [4,8,5,7,6,6,6,6,6,6,7,5,8,4, \
                5,5,4,12,7,7,12,7,7,5,5,4] # two length-12 clues
#
grid_number  = 12
clue_lengths = [10,6,6,4,8,5,5,8,4,6,6,10, \
                7,5,5,7,7,5,7,7,7,5,5,5] # two length-10 clues top and bottom

# when doing the tens, give up quicker on the inner
#  loop
if grid_number == 3:
  inner_attempts   = 99
  successive_fails = 99

random_upper_limit = len(clue_lengths)

max_clue_count = 0
crossword = [None] * len(clue_lengths)

# try a certain number of times
for ii in range(outer_attempts):
#for ii in range(len(linesTens)):
  #tens = linesTens[ii]
  clue_count = 0
  for ll in range(len(clue_lengths)):
    if crossword[ll] != None:
      clue_count = clue_count + 1
  if clue_count > max_clue_count:
    best_crossword = crossword
    max_clue_count = clue_count
    print("biggest so far has", str(max_clue_count), "clues")
    print(crossword)
  if clue_count == max_clue_count and clue_count > 0:
    print("Also ...", str(max_clue_count), "...", crossword)

  # initialise the list of words in the crossword to None
  crossword = [None] * len(clue_lengths)
  if grid_number == 4 or \
     grid_number == 5:
    crossword[4]  = tens[0:10]
    crossword[5]  = tens[11:21]
    crossword[12] = tens[22:32]
    crossword[15] = tens[33:43]

  # print an update on how we're getting on
  if ii%100 == 0:
    #print "Trial", str(ii), "of", str(outer_attempts)
    print("Trial", str(ii), "of", str(len(linesTens)))

  # for the grid with the length-12 clues, fill them first
  if grid_number == 11:
    current_list = list(lines12)
    list_indx = random.randint(1,len(current_list))
    chosen_word = current_list[list_indx-1]
    crossword[17] = chosen_word[:-1] # remove the '\n'
    list_indx = random.randint(1,len(current_list))
    chosen_word = current_list[list_indx-1]
    crossword[20] = chosen_word[:-1] # remove the '\n'

# # for grid 12, force the two 10-letter solutions
# if grid_number == 12:
#   crossword[0]  = "RAMPRAKASH"
#   crossword[11] = "KLEINVELDT"

  # initialise inner counter
  jj = 0

  while jj < inner_attempts:
    fail_count = 0
    # increment the inner counter
    jj = jj + 1

    fail_count = 0

    while fail_count < successive_fails:
      # create distinct copies of the word lists so that entries
      #  can be deleted
      empty_list = []
      temp_list03 = list(lines03)
      temp_list04 = list(lines04)
      temp_list05 = list(lines05)
      temp_list06 = list(lines06)
      temp_list07 = list(lines07)
      temp_list08 = list(lines08)
      temp_list09 = list(lines09)
      temp_list10 = list(lines10)
#     temp_list11 = list(lines11)
#     temp_list12 = list(lines12)
      # create a list that allows looking up by word length
      list_of_temp_lists = [empty_list, \
                            empty_list, \
                            empty_list, \
                            temp_list03, \
                            temp_list04, \
                            temp_list05, \
                            temp_list06, \
                            temp_list07, \
                            temp_list08, \
                            temp_list09, \
                            temp_list10]
#                           temp_list10, \
#                           temp_list11, \
#                           temp_list12]

      # pick a clue number that hasn't already been used
      empty_clue = False
      while not empty_clue:
        chosen_clue  = random.randint(1,random_upper_limit) - 1
        if crossword[chosen_clue] == None:
          empty_clue = True

      # now get a word of the right length for that clue
      length_of_words = clue_lengths[chosen_clue]
      current_list = list_of_temp_lists[length_of_words]
      list_indx = random.randint(1,len(current_list))
      chosen_word = current_list[list_indx-1]
      chosen_word = chosen_word[:-1] # remove the '\n'

      # check if this new word fits in with the others
      possible_word = test_intersect.test_intersect(chosen_clue, \
                                                    chosen_word, \
                                                    crossword, \
                                                    grid_number)
      # check it's not an error
      if possible_word == 99:
        exit(1)
      if possible_word:
        # put the new word into the crossword
        crossword[chosen_clue] = chosen_word
        del current_list[list_indx-1]
        fail_count = 0
      else:
        fail_count = fail_count + 1

      # check if we have words everywhere
      solution = True
      for kk in range(len(clue_lengths)):
        if crossword[kk] == None:
          solution = False
          break
      # if we have a solution (i.e. every gap has
      #  been filled) print the solution and stop
      #  ... unless we're doing the tens
      if solution:
        if grid_number == 3:
          # for the tens, we want multiple solutions
          print("SOLUTION >>>", crossword)
          crossword = [None] * len(clue_lengths)
          break
        else:
          exit(0)

  # end inner loop
# end outer loop

print("no solution found ... try increasing the number of attempts")
print(str(max_clue_count), "clues is as far as we got >>>", best_crossword)

exit(0)
