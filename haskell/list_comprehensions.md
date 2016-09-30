A list comprehension conists of an expression and comma separated generators, and returns a new list.

[ x*x | x <- [1..5] ]

This returns the squares of the numbers from 1 to 5.

They can also have guards, which restrict the values consumed by the expression.

[ x*x | x <- [1..5], even x ]

This returns the squares of the even numbers between 1 and 5.
