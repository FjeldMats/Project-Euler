fib :: Int -> Int
fib 0 = undefined
fib 1 = 1
fib 2 = 2
fib x = fib (x - 1) + fib (x - 2)

fourMillion :: Int
fourMillion = 4000000

main :: IO ()
main =
  print $
  sum $
  filter
    even
    [fib x | x <- takeWhile (\x -> fib x < fourMillion) [1 .. fourMillion]]
