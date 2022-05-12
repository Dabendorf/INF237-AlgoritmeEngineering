{-# LANGUAGE Strict #-}
import Control.Monad
-- https://uib.kattis.com/problems/inversefactorial
{--
For a number n!, find the original number n

Solution:
- Logarithm tricks

--}

main :: IO ()
main = do
    n <- getLine
    let inp = read n :: Integer
    let result = invfac (lenNumber (inp)) 1.0 inp 4.0
    print result

lenNumber :: Integer -> Integer
lenNumber n = fromIntegral (length (show n))

invfac :: Integer -> Float -> Integer -> Float -> Integer
invfac _ _ 5040 _ = 7
invfac _ _ 720 _ = 6
invfac _ _ 120 _ = 5
invfac _ _ 24 _ = 4
invfac _ _ 6 _ = 3
invfac _ _ 2 _ = 2
invfac _ _ 1 _ = 1
invfac len_orig len_new orig_num i
    | len_orig == (ceiling (len_new)) = round (i - 1.0)
    | otherwise = invfac len_orig ((+) len_new (logBase 10.0 i)) (orig_num) ((+) i 1)

 -- | otherwise = invfac len_orig ((+) len_new (ceiling (logBase (fromIntegral 10) (fromIntegral i)))) (orig_num) ((+) i 1)