import Data.List
import Control.Monad
-- https://uib.kattis.com/problems/nine
{--
For every number d, find how many numbers with d digits there are which are not including a 9

Solution:
- 8*mod(9, d-1, modulo-value)
- modulo operation can be applied after every multiplication (due to the fancy math rules of our trust)
- Haskell standard library does not have modPow, so one needed to implement it

--}

main :: IO ()
main = do
    line <- getLine
    let numLines = read line :: Int
    inputs <- getMultipleLines numLines
    splitListToOutput inputs

-- modPow: base^pow mod m
-- basecase: if exponent is 1, just do modulo of base and m
-- otherwise dependent if exponent is even or odd
-- uses math tricks like the fact that y^2x = y^x * y^x
-- does not work for odd numbers, therefore it is y^(2x+1) = x * y^x * y^x
modPow :: Integer -> Integer -> Integer -> Integer
modPow base 1 m = mod base m
modPow base pow m
    | even pow = mod ((modPow base (div pow 2) m) ^ 2) m
    | odd  pow = mod ((modPow base (div (pow-1) 2) m) ^ 2 * base) m

-- has a basecase for one digit numbers
-- otherwise, the number is of digits without 9 in it is 8*pow(9,d-1)
-- since we can modulo number, one uses modpow
iHateNines :: Integer -> Integer
iHateNines 1 = 8
iHateNines numDigits = (mod) ((modPow 9 (numDigits - 1) 1000000007) * 8) 1000000007

-- splits n lines into several lines and produces the output
splitListToOutput :: [[Char]] -> IO ()
splitListToOutput x = mapM_ (print . iHateNines . read) x

-- helper method to more effectively read n lines
-- from stackoverflow
-- https://stackoverflow.com/questions/10858346/haskell-read-first-n-lines
getMultipleLines :: Int -> IO [String]
getMultipleLines n
    | n <= 0 = return []
    | otherwise = do
        x <- getLine
        xs <- getMultipleLines (n-1)
        return (x:xs)
