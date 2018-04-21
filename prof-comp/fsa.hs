data Response = Acc | Rej deriving Eq
type State = (Response, [Transition])
type Transition = (Char, Int)
type FSA = (State, [State])

unpack (Just x) = x
unpack Nothing = undefined

findTransition :: Char -> [Transition] -> Maybe Transition
findTransition c (t@(c2, _) : ts) | c2 == c = Just t
    | otherwise = findTransition c ts
findTransition _ [] = Nothing 

getPath :: String -> State -> [Transition] -> [State] -> [State]
getPath [] s _ _ = [s]
getPath (c : cs) s ts ss = case tm of 
    Nothing -> []
    Just t -> s : getPath cs s2 ts2 ss
        where sid = snd t
              s2 = ss !! sid
              ts2 = snd s2
    where tm = findTransition c ts

getResponse :: String -> FSA -> Response
getResponse w ((r, ts), ss) = if null path then Rej else res
    where path = getPath w (r, ts) ts ss
          (res, _) = last path

acceptable :: String -> FSA -> Bool
acceptable w fsa = getResponse w fsa == Acc

initial :: State
initial = (Acc, [('a', 1)])
states :: [State]
states = [initial, (Rej, [('b', 2)]), (Rej, [('c', 3)]), (Acc, [])]
fsa :: FSA
fsa = (initial, states)

