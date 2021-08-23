#sets

a = set(map(int, input("Insert the elements of A: ").split()))
b = set(map(int, input("Insert the elements of B: ").split()))
x, y = a.union(b), a.intersection(b)

print("A is equal to B : {}".format(a==b), "\nA is empty: {}".format(not bool(a)), "\nA is unitary: {}".format(len(a)==1), \
    "\nB is empty: {}".format(not bool(b)), "\nB is unitary: {}".format(len(b)==1), "\nA is subset of B: {}".format(a.issubset(b)), \
    "\nB is subset of A: {}".format(b.issubset(a)), "\nA and B are disjoint: {}".format(a.isdisjoint(b)), \
    "\nNumber of subsets of A: {}".format(2**(len(a))), "\nNumber of subsets of B: {}".format(2**(len(b))), \
    "\nUnion of A and B: {}".format(x),"\nIntersection of A and B: {}".format(y),"\nDifference of A and B: {}".format(a.difference(b)),\
    "\nDifference of B and A: {}".format(b.difference(a)), "\nNumber of subsets of A union B: {}".format(2**len(x)), \
    "\nNumber of subsets of A intersection B: {}".format(2**len(y)))