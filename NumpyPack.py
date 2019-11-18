# numpy is, is its a very powerful package that allows you to process numbers, records, and objects 
# gives an associated weight and the weight has to deal with a number criteria.
# Usually, the popularity of it has quite a bit to do with it,
#  numpy allows you to process large collections of data in a very efficient manner
# numpy has those processes built directly in the library and you can simply call them and then use them in your own programs. 


# import in terminal
import numpy as np

num_range = np.arange(16)

num_range

# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])


# can crate matrix of values with slicing and nesting arrays
num_range.reshape(4, 4)

# array
      ([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])