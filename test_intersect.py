def test_intersect(clue_no, \
                   current_word, \
                   crossword, \
                   grid):

  possible_grids = [0,1,2,3,4,5,6,7,8]

  if not grid in possible_grids:
    print "ERROR : grid number is not in the possible_grids[] array"
    return 99

  # A is the number of the clue (zero-up) that the current
  #   entry intersects with
  # B is the letter number of the current clue
  # C is the letter number of the intersected clue
  # ---
  # clues are numbered across first then down
  if grid == 0:  #34-clue grid
    #                   A  B C A  B C  ...
    intersect_table = [[18,0,0,19,2,0], \
                       [20,1,0,21,3,0], \
                       [22,0,0,23,2,0], \
                       [18,0,2,19,2,2,24,4,1], \
                       [20,0,2,21,2,2,22,4,2,23,6,2,25,8,1], \
                       [18,0,4,19,2,4,24,4,3,20,6,4], \
                       [21,0,4,22,2,4,23,4,4,25,6,3], \
                       [26,0,0,19,2,6,24,4,5,20,6,6,21,8,6], \
                       [27,0,0,23,2,6,25,4,5], \
                       [26,0,2,28,2,0,24,4,7], \
                       [29,0,0,30,2,0,27,4,2,31,6,0,25,8,7], \
                       [26,0,4,28,2,2,32,4,0,29,6,2], \
                       [30,0,2,27,2,4,31,4,2,33,6,0], \
                       [26,0,6,28,2,4,32,4,2,29,6,4,30,8,4], \
                       [27,0,6,31,2,4,33,4,2], \
                       [28,1,6,32,3,4], \
                       [29,0,6,30,2,6], \
                       [31,1,6,33,3,4], \
                       [0 ,0,0,3 ,2,0,5 ,4,0], \
                       [0 ,0,2,3 ,2,2,5 ,4,2,7 ,6,2], \
                       [1 ,0,1,4 ,2,0,5 ,4,6,7 ,6,6], \
                       [1 ,0,3,4 ,2,2,6 ,4,0,7 ,6,8], \
                       [2 ,0,0,4 ,2,4,6 ,4,2], \
                       [2 ,0,2,4 ,2,6,6 ,4,4,8 ,6,2], \
                       [3 ,1,4,5 ,3,4,7 ,5,4,9 ,7,4], \
                       [4 ,1,8,6 ,3,6,8 ,5,4,10,7,8], \
                       [7 ,0,0,9 ,2,0,11,4,0,13,6,0], \
                       [8 ,0,0,10,2,4,12,4,2,14,6,0], \
                       [9 ,0,2,11,2,2,13,4,2,15,6,1], \
                       [10,0,0,11,2,6,13,4,6,16,6,0], \
                       [10,0,2,12,2,0,13,4,8,16,6,2], \
                       [10,0,6,12,2,4,14,4,2,17,6,1], \
                       [11,0,4,13,2,4,15,4,3], \
                       [12,0,6,14,2,4,17,4,3]]
  if grid == 1:  #32-clue grid
    #                   A  B C A  B C  ...
    intersect_table = [[16,0,0,17,2,0,18,4,0,19,6,0], \
                       [20,0,0,21,2,0,22,4,0,23,6,0], \
                       [16,0,2,17,2,2,18,4,2,19,6,2,20,8,2], \
                       [21,0,2,22,2,2,23,4,2], \
                       [17,1,4,18,3,4,19,5,4], \
                       [20,0,4,21,2,4,22,4,4,23,6,4], \
                       [24,0,1,17,2,6], \
                       [19,1,6,25,3,0,21,5,6,26,7,0,23,9,6], \
                       [24,0,3,17,2,8,27,4,1,19,6,8,25,8,2], \
                       [26,1,2,23,3,8], \
                       [24,0,5,29,2,0,27,4,3,30,6,0], \
                       [25,0,4,28,2,1,26,4,4], \
                       [24,0,7,29,2,0,27,4,5], \
                       [30,0,2,25,2,6,28,4,3,26,6,6,31,8,1], \
                       [24,0,9,29,2,4,27,4,7,30,6,4], \
                       [25,0,8,28,2,5,26,4,8,31,6,3], \
                       [0 ,0,0,2 ,2,0], \
                       [0 ,0,2,2 ,2,2,4 ,4,1,6 ,6,2,8 ,8,2], \
                       [0 ,0,4,2 ,2,4,4 ,4,3], \
                       [0 ,0,6,2 ,2,6,4 ,4,5,7 ,6,1,8 ,8,6], \
                       [1 ,0,0,2 ,2,8,5 ,4,0], \
                       [1 ,0,2,3 ,2,0,5 ,4,2,7 ,6,5], \
                       [1 ,0,4,3 ,2,2,5 ,4,4], \
                       [1 ,0,6,3 ,2,4,5 ,4,6,7 ,6,9,9 ,8,3], \
                       [6 ,1,0,8 ,3,0,10,5,0,12,7,0,14,9,0], \
                       [7 ,0,3,8 ,2,8,11,4,0,13,6,2,15,8,0], \
                       [7 ,0,7,9 ,2,1,11,4,4,13,6,6,15,8,4], \
                       [8 ,1,4,10,3,4,12,5,4,14,7,4], \
                       [11,1,2,13,3,4,15,5,2], \
                       [10,0,2,12,2,2,14,4,2], \
                       [10,0,6,13,2,0,14,4,6], \
                       [13,1,8,15,3,6]]
  if grid == 2:  # 20-clue grid
    #                   A  B C A  B C  ...
    intersect_table = [[10,1,0,11,3,0,12,5,0,13,7,0], \
                       [14,0,0,10,2,2,11,4,2], \
                       [12,0,2,13,2,2,15,4,0], \
                       [14,0,2,10,2,4], \
                       [12,1,4,13,3,4,15,5,2], \
                       [14,0,4,17,2,0,16,4,1], \
                       [18,1,0,15,3,4], \
                       [14,0,6,17,2,2,16,4,3], \
                       [19,0,1,18,2,2,15,4,6], \
                       [17,0,4,16,2,5,19,4,3,18,6,4], \
                       [0 ,0,1,1 ,2,2,3 ,4,2], \
                       [0 ,0,3,1 ,2,4], \
                       [0 ,0,5,2 ,2,0,4 ,4,1], \
                       [0 ,0,7,2 ,2,2,4 ,4,3], \
                       [1 ,0,0,3 ,2,0,5 ,4,0,7 ,6,0], \
                       [2 ,0,4,4 ,2,5,6 ,4,3,8 ,6,4], \
                       [5 ,1,4,7 ,3,4,9 ,5,2], \
                       [5 ,0,2,7 ,2,2,9 ,4,0], \
                       [6 ,0,1,8 ,2,2,9 ,4,6], \
                       [8 ,1,0,9 ,3,4]]
  if grid == 3:  # just the tens for the 20-clue grids
    #                   A  B C A  B C  ...
    intersect_table = [[2, 3,4,3, 5,3], \
                       [2, 4,6,3, 6,5], \
                       [0, 4,3,1, 6,4], \
                       [0, 3,5,1, 5,6]]
  if grid == 4:  # 20-clue grid jimbo A
    #                   A  B C A  B C  ...
    intersect_table = [[10,0,0,11,2,0,12,4,0], \
                       [13,1,0,14,3,0], \
                       [10,0,2,11,2,2,12,4,2], \
                       [15,0,1,13,2,2,14,4,2], \
                       [11,1,4,12,3,4,15,5,3,13,7,4,14,9,4], \
                       [16,0,1,17,2,0,12,4,6,15,6,5,18,8,0], \
                       [16,0,3,17,2,2,12,4,8], \
                       [15,0,7,18,2,2,19,4,1], \
                       [16,0,5,17,2,4], \
                       [15,1,9,18,3,4,19,5,3], \
                       [0 ,0,0,2 ,2,0], \
                       [0 ,0,2,2 ,2,2,4 ,4,1], \
                       [0 ,0,4,2 ,2,4,4 ,4,3,5 ,6,4,6 ,8,4], \
                       [1 ,0,1,3 ,2,2,4 ,4,7], \
                       [1 ,0,3,3 ,2,4,4 ,4,9], \
                       [3 ,1,0,4 ,3,5,5 ,5,6,7 ,7,0,9 ,9,1], \
                       [5 ,1,0,6 ,3,0,8 ,5,0], \
                       [5 ,0,2,6 ,2,2,8 ,4,2], \
                       [5 ,0,8,7 ,2,2,9 ,4,3], \
                       [7 ,1,4,9 ,3,5]]
  if grid == 5:  # 20-clue grid jimbo B
    #                   A  B C A  B C  ...
    intersect_table = [[10,0,0,11,2,0,12,4,0], \
                       [13,1,0,14,3,0], \
                       [10,0,2,11,2,2,12,4,2], \
                       [15,0,1,13,2,2,14,4,2], \
                       [11,1,4,12,3,4,15,5,3,16,7,0,14,9,4], \
                       [17,0,1,11,2,6,12,4,6,15,6,5,16,8,2], \
                       [17,0,3,19,2,0,12,4,8], \
                       [15,0,7,16,2,4,18,4,1], \
                       [17,0,5,19,2,2], \
                       [15,1,9,16,3,6,18,5,3], \
                       [0 ,0,0,2 ,2,0], \
                       [0 ,0,2,2 ,2,2,4 ,4,1,5 ,6,2], \
                       [0 ,0,4,2 ,2,4,4 ,4,3,5 ,6,4,6 ,8,4], \
                       [1 ,0,1,3 ,2,2], \
                       [1 ,0,3,3 ,2,4,4 ,4,9], \
                       [3 ,1,0,4 ,3,5,5 ,5,6,7 ,7,0,9 ,9,1], \
                       [4 ,0,7,5 ,2,8,7 ,4,2,9 ,6,3], \
                       [5 ,1,0,6 ,3,0,8 ,5,0], \
                       [7 ,1,4,9 ,3,5], \
                       [6 ,0,2,8 ,2,2]]
  if grid == 6:  # 27-clue grid jimbo01
    #                   A  B C A  B C  ...
    intersect_table = [[15,1,0,16,3,0,17,5,0], \
                       [18,0,0,19,2,0,20,4,0], \
                       [15,1,2,16,3,2,17,5,2,18,7,2], \
                       [19,0,2,20,2,2], \
                       [15,1,4,16,3,4,17,5,4], \
                       [18,0,4,19,2,4,20,4,4], \
                       [15,1,6,21,3,0], \
                       [17,0,6,22,2,0], \
                       [19,0,6,23,2,0], \
                       [24,1,0,21,3,2,25,5,0], \
                       [22,0,2,26,2,0,23,4,2], \
                       [24,1,2,21,3,4], \
                       [25,0,2,22,2,4,26,4,2,23,6,4], \
                       [24,1,4,21,3,6,25,5,4], \
                       [22,0,6,26,2,4,23,4,6], \
                       [0 ,0,1,2 ,2,1,4 ,4,1,6 ,6,1], \
                       [0 ,0,3,2 ,2,3,4 ,4,3], \
                       [0 ,0,5,2 ,2,5,4 ,4,5,7 ,6,0], \
                       [1 ,0,0,2 ,2,7,5 ,4,0], \
                       [1 ,0,2,3 ,2,0,5 ,4,2,8 ,6,0], \
                       [1 ,0,4,3 ,2,2,5 ,4,4], \
                       [6 ,0,3,9 ,2,3,11,4,3,13,6,3], \
                       [7 ,0,2,10,2,0,12,4,2,14,6,0], \
                       [8 ,0,2,10,2,4,12,4,6,14,6,4], \
                       [9 ,0,1,11,2,1,13,4,1], \
                       [9 ,0,5,12,2,0,13,4,5], \
                       [10,0,2,12,2,4,14,4,2]]
  if grid == 7:  # 26-clue grid jimbo02
    #                   A  B C A  B C  ...
    intersect_table = [[12,1,1,13,3,1], \
                       [14,0,1,15,2,1,16,4,1,17,6,1], \
                       [12,1,3,13,3,3,14,5,3], \
                       [15,0,3,16,2,3,17,4,3], \
                       [18,0,0,12,1,5,13,3,5], \
                       [15,1,5,16,3,5,17,5,5,19,6,0], \
                       [18,0,2,21,1,0,22,3,0,20,5,1], \
                       [23,1,0,24,3,0,19,4,2], \
                       [21,1,2,22,3,2,20,5,3], \
                       [25,0,1,23,2,2,24,4,2], \
                       [21,1,4,22,3,4,20,5,5,25,7,3], \
                       [23,0,4,24,2,4], \
                       [0,1,1,2,3,1,4,5,1], \
                       [0,1,3,2,3,3,4,5,3], \
                       [1,1,0,2,3,5], \
                       [1,1,2,3,3,0,5,5,1], \
                       [1,1,4,3,3,2,5,5,3], \
                       [1,1,6,3,3,4,5,5,5], \
                       [4,0,0,6,2,0], \
                       [5,0,6,7,2,4], \
                       [6,1,5,8,3,5,10,5,5], \
                       [6,0,1,8,2,1,10,4,1], \
                       [6,0,3,8,2,3,10,4,3], \
                       [7,0,1,9,2,2,11,4,0], \
                       [7,0,3,9,2,4,11,4,2], \
                       [9,1,0,10,3,7]]
  if grid == 8:  # 26-clue grid jimbo02
    #                   A  B C A  B C  ...
    intersect_table = [[12,1,1,13,3,1], \
                       [14,0,1,15,2,1,16,4,1,17,6,1], \
                       [12,1,3,13,3,3,14,5,3], \
                       [15,0,3,16,2,3,17,4,3], \
                       [12,1,5,13,3,5], \
                       [15,1,5,16,3,5,17,5,5], \
                       [19,1,0,20,3,0,18,5,1], \
                       [21,1,0,22,3,0], \
                       [19,1,2,20,3,2,18,5,3], \
                       [23,0,1,21,2,2,22,4,2], \
                       [19,1,4,20,3,4,18,5,5,23,7,3], \
                       [21,0,4,22,2,4], \
                       [0,1,1,2,3,1,4,5,1], \
                       [0,1,3,2,3,3,4,5,3], \
                       [1,1,0,2,3,5], \
                       [1,1,2,3,3,0,5,5,1], \
                       [1,1,4,3,3,2,5,5,3], \
                       [1,1,6,3,3,4,5,5,5], \
                       [6,1,5,8,3,5,10,5,5], \
                       [6,0,1,8,2,1,10,4,1], \
                       [6,0,3,8,2,3,10,4,3], \
                       [7,0,1,9,2,2,11,4,0], \
                       [7,0,3,9,2,4,11,4,2], \
                       [9,1,0,10,3,7]]
  # A is the number of the clue (zero-up) that the current
  #   entry intersects with
  # B is the letter number of the current clue
  # C is the letter number of the intersected clue
  # ---
  # clues are numbered across first then down

  # initialise counter and flag
  ii = 0
  word_OK = True

  # pick the entry in the table
  intersections = intersect_table[clue_no]
  while ii<len(intersections):
    check_word = crossword[intersections[ii]]
    ii = ii+1
    # can't compare if word not yet entered
    if check_word == None:
      ii = ii+2
    else:
      try:
        current_letter = current_word[intersections[ii]]
      except IndexError:
        print "ii =", str(ii), ":: intersect[ii] =", str(intersections[ii])
        print "current_word =", current_word
        print "clue_no =", str(clue_no)
        current_letter = "Z"
      ii = ii+1
      try:
        check_letter = check_word[intersections[ii]]
      except IndexError:
        print "ii =", str(ii), ":: intersect[ii] =", str(intersections[ii])
        print "check_word =", check_word
        print "clue_no =", str(clue_no)
        check_letter = "Z"
      ii = ii+1
      # check that the letters match
      if not current_letter == check_letter:
        word_OK = False
        break

  return word_OK
