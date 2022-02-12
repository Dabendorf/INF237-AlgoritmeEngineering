import Data.List
import Control.Monad
-- https://uib.kattis.com/sessions/msjyoa/problems/stringmatching

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
getPositions currIndex overallStr toSearch foundPos
    | isPrefixOf toSearch overallStr = getPositions (currIndex+1) (tail overallStr) toSearch (foundPos ++ [currIndex])
    | otherwise = getPositions (currIndex+1) (tail overallStr) (toSearch) foundPos

-- findIndex ('b' `elem`)