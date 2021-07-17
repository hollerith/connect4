"""
The proposed solution is to flatten the game array to a string and to
use perl compatible regular expressions to pattern match for rows,
columns and diagonals.

It doesn't ensure positions are legal for but could easily be adapted 
to do by adding regexes.

If the regex module is not available/limited to standard python re
then the row match must be performed on each line separately to 
ensure the row is not overlapping lines, the other expressions are 
compatible and don't need to change, standard re cannot perform a 
recursive (?1) to pad out the match. 

The code could be shortened by combining into a single regex with 
named groups and a single if statement but I have left it as is
for the sake of clarity and as it would not optimize much.
"""
import regex 

def find_winner(g):

    # flatten above
    g.reverse()
    f = [item for sublist in g for item in sublist]
    s = "".join([char or " " for char in f])

    #match a row of R 
    row = r"^(.{7})(?1)?(?:(?1){0,5}).{0,3}([R]{4}).{0,3}"

    #match a column of R 
    col = r"(R.{6}R.{6}R.{6}R)"

    #match a diagonal of R
    dia = r"(R.{7}R.{7}R.{7}R)|(R.{5}R.{5}R.{5}R)"

    if regex.match(row, s) or regex.search(col, s) or regex.search(dia, s): 
        print('yay - R wins')
        return 'R'

    # now do L
    row = row.replace('R', 'L')
    col = col.replace('R', 'L')
    dia = dia.replace('R', 'L')

    if regex.match(row, s) or regex.search(col, s) or regex.search(dia, s): 
        print('yay - L wins')
        return 'L'

    print('yay keep playing')
    return None

# R wins - row
g = [
    ["R", "R", "R", "R", "L", "L", "L"],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]
a = find_winner(g)
assert a=='R'

# L wins - row
g = [
    ["R", "R", "R", "L", "L", "L", "L"],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]
a = find_winner(g)
assert a=='L'

# R wins -  col
g = [
    ["R", "R", "R", "L", "L", "L", None],
    ["R", None, None, None, None, None, None],
    ["R", None, None, None, None, None, None],
    ["R", None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]
a = find_winner(g)
assert a=='R'

# R wins -  diagonal
g = [
    ["R", "R", "R", "L", "L", "L", None],
    [None, "R", None, None, None, None, None],
    [None, None, "R", None, None, None, None],
    [None, None, None, "R", None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]
a = find_winner(g)
assert a=='R'

# Nobody wins yet
g = [
    ["R", "R", "R", "L", "L", "L", None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]
a = find_winner(g)
assert a==None
