data Option a = None | Some a
data BinTree a = Empty
	| Branch a (BinTree a) (BinTree a)
	deriving (Show, Eq)

size :: BinTree a -> Int
size Empty = 0
size (Branch x l r) = 1 + (size l) + (size r)

height :: BinTree a -> Int
height Empty = 0
height (Branch x l r) = 1 + max (height l) (height r)

data Direction = L | R
type Path = [Direction]

follow :: BinTree a -> Path -> Option BinTree
follow b [] = Some b 
follow (Branch _ _ r) [R : ds] = follow r ds
follow (Branch _ l _) [L : ds] = follow l ds
follow Empty _ = None
