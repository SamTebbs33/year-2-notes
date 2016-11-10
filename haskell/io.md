# IO in haskell
Pure functions don't have any side-effects, so writing interactive programs is a little harder.

An interactive function signature may look like `f :: a -> IO b`. `IO a` is the type of action that returns a value of type `a`.

The equivalent of `void` in C-style languages is `unit` in Haskell, which is represented by `()` and could be defined as `data () = ()` (it's called `unit` as the only valid value is itself/empty tuple).
`IO ()` is the type of action that only has side-effects and has no return value.

## Example IO 'functions'
`getChar :: IO Char`
`putChar :: Char -> IO ()`

## Sequencing actions
Actions can be sequenced as a single composed action with `do`.
`return v` returns `IO v`.

```haskell
act :: IO (Char, Char)
act = do x <- getChar
	getChar
	y <- getChar
	return (x, y)
```
Returns first and third characters entered and ignores second one.

```haskell
getline :: IO String
getLine = do c <- getChar
	if c == '\n' then
		return []
	else
		do cs <- getLine
			return (c : cs)
```
Gets a line from input.

```haskell
putStr :: String -> IO ()
putStr "" = return ()
putStr (c : cs) = do putChar c
	putStr cs
```
Prints string.

# Extracting value from IO a
```
do let iostr = getLine
	str <- iostr
```
Below are the types
```
iostr :: IO String
str :: String
```
