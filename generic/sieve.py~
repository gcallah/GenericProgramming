marks = []


def mark_sieve(marks, start, factor):
    #  print("For start of %i we are using factor %i" % (start, factor))
    for i in range(start, len(marks), factor):
        #  print("And we are marking index of %i; value of %i"
              #  % (i, 2 * i + 3))
        marks[i] = False


def sift(n):
    global marks
    for b in range(n):
        marks.append(True)
    i = 0
    index_square = 3
    factor = 3
    while index_square < n:
        #  print("i = %i; index_square = %i; factor = %i"
              #  % (i, index_square, factor))
        if marks[i]:  # a prime
            mark_sieve(marks, index_square, factor)
        i += 1
        index_square += factor
        factor += 2
        index_square += factor


def rpt_primes():
    print("Prime 1 = 2")
    n = 2
    for i in range(len(marks)):
        if marks[i]:
            print("Prime %i = %i" % (n, 2 * i + 3))
            n += 1
