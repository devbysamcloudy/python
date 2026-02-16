# def sum_receipt (a,b,c):
    # sum = a + b + c
    # print("sum is ", sum)
    # return sum

def new_sum_receipt(*args):
    print(args)
    sum = 0
    for n in args:
        print("n is ", n)
        sum = sum + n
        print("sum is ", sum)

new_sum_receipt(10,20,30)
new_sum_receipt()

def main ():
    prices_list = []
    while True:
        user_input = input("Enter a price or type 'done' to end:").lower()

        if user_input =='done':
            break

        try:
            price = float(user_input)
            prices_list.append(price)

        except Exception as e:
            print("Invalid Input. Enter a number")
            print(prices_list)
    new_sum_receipt(*prices_list)


main()
