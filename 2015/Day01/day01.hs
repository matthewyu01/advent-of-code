import System.IO

endFloor :: String -> Int -> Int
endFloor remainingStr currFloor
  | remainingStr == "" = currFloor
  | (head remainingStr) == '(' = endFloor (tail remainingStr) (currFloor + 1)
  | (head remainingStr) == ')' = endFloor (tail remainingStr) (currFloor - 1)

endFloorXS :: String -> Int -> Int
endFloorXS "" currFloor = currFloor
endFloorXS ( '(':xs ) currFloor = endFloorXS xs (currFloor + 1)
endFloorXS ( ')':xs ) currFloor = endFloorXS xs (currFloor - 1)

part1 :: [String] -> Int
part1 lines = endFloor (head lines) 0


part2Floor :: String -> Int -> Int -> Int
part2Floor "" _ _ = -1
part2Floor ( ')':xs ) 0 index = index
part2Floor ( ')':xs ) curr_floor index = part2Floor xs (curr_floor - 1) (index + 1)
part2Floor ( '(':xs ) curr_floor index = part2Floor xs (curr_floor + 1) (index + 1)

part2 :: [String] -> Int
part2 lines = part2Floor (head lines) 0 1

main :: IO ()
main = do
    inputContents <- readFile "input.txt"
    let linesFromInput = lines inputContents

    -- putStrLn "Lines from input.txt:"
    -- mapM_ putStrLn linesFromInput

    testContents <- readFile "test.txt"
    let linesFromTest = lines testContents

    let p1TestResult = part1 linesFromTest
    putStr "Part 1 Test Output: "
    print p1TestResult

    let p1ActualResult = part1 linesFromInput
    putStr "Part 1 ACTUAL: "
    print p1ActualResult


    let p2TestResult = part2 linesFromTest
    putStr "Part 2 Test Output: "
    print p2TestResult

    let p2ActualResult = part2 linesFromInput
    putStr "Part 2 ACTUAL: "
    print p2ActualResult
