# Find-R-Arithmetic-Triples
Implementation of algorithm in On the Arithmetic Dimension of Triangle Groups (https://arxiv.org/abs/1510.04637), Mathematics of Computation 86(306)

To list all 1- to r-arithmetic triangle groups, run:

main.py r

e.g. main.py 2, to list 1- and 2-arithmetic triangle groups.

If r is not specified, only 1-arithmetic triangle groups will be listed.

Be advised that this algorithm is exponential in r. My personal computer can only compute up to r=2 (~10min), though using Dartmouth College's clusters we have computed up to r=15.
