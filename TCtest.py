import TC

print(f"32 摄氏度 = {TC.tc.c2f(0):.2f} 华氏度")
print(f"99 华氏度 = {TC.tc.f2c(0):.2f} 摄氏度")
TC.tc.printX()
print(f"TC.s = {TC.s}")


TC.x = 250
TC.tc.printX()
