"""摄氏度 -> 华氏度"""
def c2f(c):
    f = c * 1.8 + 32
    return f

"""华氏度 ->摄氏度"""
def f2c(f):
    c = (f - 32) / 1.8
    return c

def printX():
    import TC
    print(TC.x)
    
print(f"__name__ 的值是 {__name__}")

"""测试"""
if __name__ == "__main__":
    print(f"测试，0 摄氏度 = {c2f(0):.2f} 华氏度")
    print(f"测试，0 华氏度 = {f2c(0):.2f} 摄氏度")
    printX()
