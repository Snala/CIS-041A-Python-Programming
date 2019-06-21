1. Convert this function to use a Map:

        def MapIt(nlist):
              alist = []
              for n in nlist:
                   alist.insert( len(alist), SquareIt(n) ) # SquareIt multiplies n*n
              return alist

2. Using Python regular expressions, write the statements to find all the numbers in a line of text. Example:

          "De Anza College, 21250 Stevens Creek Blvd., Cupertino, 95014"

3. Given this data:

          Diane's birthday is April 25, Kristin's birthday is June 1, Wayne's birthday is September 27 

using a Dictionary, code an algorithm to output the birthday of a user selected person.