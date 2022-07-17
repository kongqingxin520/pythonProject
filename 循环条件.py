def bmi(name, height, weight):
    print(name + '身高是：' + str(height) + "m\t体重是：" + str(weight) + 'kg')
    kong = weight / (height * height)
    print(name + '的BMI是：' + str(kong))
    if kong < 18.5:
        print("您的体重过轻")
    if 18.5 <= kong <= 24.9:
        print("您的体重是正常范围")
    if kong >= 24.9:
        print("您的体重过重，请注意减肥")


print("请输入您的名字，身高，体重")
qing = input("姓名：")
xin = float(input("请输入你的身高："))
xing = int(input("体重："))
bmi("qing", xin, xing)
