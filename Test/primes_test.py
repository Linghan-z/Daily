import unittest

from primes import primes


class TestPrimes(unittest.TestCase):
    def test_prims(self):
        self.assertEqual(primes(10), [2, 3, 5, 7])


if __name__ == "__main__":
    unittest.main()
