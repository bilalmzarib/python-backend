
def generate_fibonacci(n):
    
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib



def factorial(n):
   
    if n < 0:
        raise ValueError("لا يمكن حساب مضروب بعدد سالب")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)



square = lambda x: x ** 2



def loop_example():
   
    i = 0
    while i < 10:
        if i == 3:
            i += 1
            continue  
        elif i == 7:
            break 
        elif i == 5:
            pass 
        print(f"العدد: {i}")
        i += 1



if __name__ == "__main__":
    
    try:
        num = int(input("أدخل عددًا صحيح: "))
        print(f"\n متتالية فيبوناتشي حتى {num} عنصر:")
        print(generate_fibonacci(num))

        print(f"\n مضروب {num} هو:")
        print(factorial(num))

        print(f"\n {num} باستخدام دالة lambda هو:")
        print(square(num))

        print("\n عرض مثال على أوامر التحكم في الحلقات:")
        loop_example()

    except ValueError:
        print(" ادخل عدد صحيح فقط.")
