class Solution:
    def fib(self, n: int) -> int:
        fib_before_priv, fib_priv = 0, 1
        if n in (0, 1):
            return n
        while n > 1:
            fib_new = fib_before_priv + fib_priv
            fib_before_priv, fib_priv = fib_priv, fib_new
            n -= 1
        return fib_priv