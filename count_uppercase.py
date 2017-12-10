def count_uppercase(s):
  """Return the number of uppercase letters in s."""
  count = 0
  for c in s:
    if c.isupper():
      count += 1
  return count


# A string is a sequence of characters.
#
# This function treats each character only by its value, not by its position in the sequence.
#   It is interested in a property of the character,  so we consider mapping.
#   It is interested in a   subset of the characters, so we consider filtering.
# Mapping and filtering can be done with higher-order functions, or with list comprehensions.

# Let's create the sequence of characters having the property, with a list comprehension.
#   The list comprehension preserves order, but that's incidental.
def count_uppercase_1(s):
  return len([c for c in s if c.isupper()])


# Creating a whole new list, and then taking its length, sounds slow.

# But "slow" is MEANINGLESS.
# To have meaning it MUST include:
#   under what conditions, and
#   what is an acceptable amount of time

# Ok, so you've determined the conditions and acceptability.
# How well do you understand:
#   Your python compiler/interpreter?
#   Your machine architecture?

# When someone suggests something's slow, or could be slow and should be avoided:
#  most of the time you should ignore them,  unless they have profiling data.

# Let's profile!
L = ["A" for _ in range(10000000)]
print(count_uppercase(L))
print(count_uppercase_1(L))
# python -m cProfile count_uppercase.py
# 10000000
# 10000000
#          20000006 function calls in 4.493 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    1.310    1.310    1.938    1.938 count_uppercase.py:1(count_uppercase)
#         1    1.290    1.290    1.905    1.905 count_uppercase.py:19(count_uppercase_1)

# Surprised?
# Next time someone throws around speculative claims about efficiency, be suspicious!
# Challenge them for data!
