-- https://uib.kattis.com/problems/greetings2

main = do
    hey <- getLine
    putStrLn(doubleEs hey)

doubleEs :: String -> String
doubleEs original = "h" ++ replicate ((length original - 2)*2) 'e' ++ "y"