import time


def time_cost(fn):
    def inner():
        start_time = time.time()  # 得到开始时间
        fn()  # 调用被装饰的 函数
        end_time = time.time()  # 得到结束时间
        print(end_time - start_time)

    return inner


def print_some(fn):  # 这里的fn是他的上一个装饰器返回的内部函数的对象
    def inner2():
        fn()
        print('我是后来的randomfn')

    return inner2


@print_some
@time_cost  # 监听当前函数执行花费的时间
# 函数功能  在1-10001范围 内所有数字的和
def sum_fn():
    sums = 0
    for i in range(1, 10001):
        sums += i
    print(sums)


# sum_fn() #调用功能函数得到 值为50005000
# 把sum_fn函数当作参数，传到装饰器函数内
# 并用一个同名变量接收装饰器返回的函数对象
# 这样调用这个功能函数还是使用sum_fn()
# 这就是装饰器的变向操作
# sum_fn = time_cost(sum_fn)  #相当于 @time_cost
# sum_fn()
# 50005000
# 0.0014972686767578125

# 使用@time_cost后调用sum_fn  结果同上
# sum_fn()
# 50005000
0.0009975433349609375

# 当一个函数有多个装饰器装饰时  调用sum_fn()
# 装饰器执行顺序是 由下往上执行
# 只有最下面的装饰器直接装饰了  被装饰 函数
# 其他装饰器 相当于 间接 装饰
# sum_fn()
# 50005000
# 0.0004990100860595703
# 我是后来的randomfn
