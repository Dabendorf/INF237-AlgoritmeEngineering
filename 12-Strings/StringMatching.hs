import Data.List
import Control.Monad
-- https://uib.kattis.com/problems/stringmatching

main = do
    s <- getContents 
    let a = lines s
    splitListToOutput a

splitListToOutput :: [[Char]] -> IO ()
splitListToOutput (x:y:xs) = putStrLn((getPositions 0 y x [])) >> splitListToOutput xs
splitListToOutput (x:xs) = return ()
splitListToOutput [] = return ()

getPositions :: Int -> [Char] -> [Char] -> [Int] -> [Char]
getPositions currIndex [] toSearch foundPos = unwords (map show foundPos)
getPositions currIndex (x:xs) toSearch foundPos
    | isPrefixOf toSearch (x:xs) = getPositions (currIndex+1) xs toSearch (foundPos ++ [currIndex])
    | otherwise = getPositions (currIndex+1) xs (toSearch) foundPos

-- findIndex ('b' `elem`)
-- all@(x:xs)
