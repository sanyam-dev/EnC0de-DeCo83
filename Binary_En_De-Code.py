"""
Author : Sanyam Jha
Code : Play around with your friends OR store your secrets with this Binary Encoder - Decoder

"""
# This Code Converts String to Binary


def str_to_bin(s):
    res_str = ""
    for i in range(len(s)):
        bin1 = '{0:08b}'.format(ord(s[i]))
        res_str = res_str + " " + bin1
    return res_str[1:]

# This Code Converts Binary to String


def binary_string(n):
    num = 0
    count = 0
    l = [0, 1]
    for _ in range(len(n)):
        if int(n[-1]) not in l:
            break
        elif n[-1] == " ":
            return int(0000000)
        else:
            num += pow(2, count)*int(n[-1])
            n = n[:-1]
            count += 1
    return int(num)


N = input("Convert String to Binary?")
if N == "Y":
    s = input("Enter String: ")
    res = str_to_bin(s)
    print(res)
elif N == "N":
    bin_str = input("Enter Binary String:")
    l1 = list(map(str, bin_str.split()))

    res = []
    for i in range(len(l1)):
        res.append(chr(binary_string(l1[i])))
    res_str = ''
    res_str = res_str.join(res)

    print(res_str)
else:
    print("Run Again and write either 'Y' or 'N'")