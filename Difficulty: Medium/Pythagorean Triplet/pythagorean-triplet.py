class Solution:
	def pythagoreanTriplet(self, arr):
	    n = len(arr)
        squares = [x*x for x in arr]
        squares_set = set(squares)

        for i in range(n):
          for j in range(i+1, n):
            if squares[i] + squares[j] in squares_set:
                return True
        return False
    