primes :: [Integer]
primes = 2 : filter isPrime [3,5 ..]

isPrime :: Integer -> Bool
isPrime 1 = False
isPrime n = all (\p -> mod n p /= 0) . takeWhile (\p -> p ^ 2 <= n) $ primes

isqrt :: Integer -> Integer
isqrt = floor . sqrt . fromIntegral

smallNum :: Integer
smallNum = 13195

bigNum :: Integer
bigNum = 600851475143

main :: IO ()
main = do
  print $
    last [x | x <- takeWhile (\x -> x < isqrt bigNum) primes, mod bigNum x == 0]
  print
    (maximum [x | x <- takeWhile (< isqrt bigNum) primes, mod bigNum x == 0])
