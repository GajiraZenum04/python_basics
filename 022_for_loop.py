start = int(input("starting number: "))
end = int(input("ending number: "))
for num in range(start, end + 1):
    print("even number in range:")
    if num % 2 == 0:
        print(num)

