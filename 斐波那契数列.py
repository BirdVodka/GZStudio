n = input('请输入数字，此计算程序得出结果数列从1开始')
def fib_recur(n):
  assert int(n) >= 0, "n > 0"
  if n <= 1:
    return n
  return fib_recur(n-1) + fib_recur(n-2)
print('斐波那契数列的第' + str(n) + '个数字是' + str(fib_recur(int(n))))
input()