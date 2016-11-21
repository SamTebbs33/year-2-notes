# Operators
Operators can be defined by declaring associativity, precedence and the operator.

```haskell
infixl 6 <->
```
Declares the infix `<->` operator with left associativity and precedence 6.

It can then be defined with normal function declaration syntax.
```haskell
(<->) :: Num a => a -> a -> a
a <-> b = a + b
```
