total_sum = 0
odd_even = input("Enter ODD or EVEN:").upper()
total_num = int(input("Enter the final number:"))
if odd_even == "EVEN":
    for i in range(1,total_num+1):
        sum_part = i * i
    if sum_part % 2 != 0:
        total_sum += sum_part
elif odd_even == "ODD":
    for i in range(1,total_num+1):
        sum_part = i * i
        if sum_part % 2 != 0:
            total_sum += sum_part
        else: 
            pass
else:
    print("Please Enter ODD or EVEN")
print(total_sum)