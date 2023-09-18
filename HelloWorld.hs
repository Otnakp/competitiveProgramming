main :: IO ()
main = do
  let myList = [1, 5, 3, 8, 2]
  let maxElement = findMax myList
  print "Numbers"
  print myList
  print "Max"
  print maxElement
  print "Reversed"
  print (reverseList myList)  -- Corrected this line

findMax :: [Int] -> Int
findMax [x] = x
findMax (x1:x2:xs)
  | x1 > x2 = findMax (x1:xs)
  | otherwise = findMax (x2:xs)

reverseList :: [Int] -> [Int]
reverseList [] = []  -- Added base case for empty list
reverseList [x] = [x]
reverseList (x:xs) = reverseList xs ++ [x]  -- Corrected this line

