# print(f"NameError - {type(NameError)} - {issubclass(NameError,BaseException)}")
#
#
# a = 1
#
# b = 0
#
# try:
#     a/b
#
# except ZeroDivisionError:
#     print("You can't divide zero")
#
#
# from colorama import Fore
#
# try:
#     f = open("Table.exe", "r")
#
# except FileNotFoundError:
#     print(Fore.RED + "There isn't such file or directory!!")
#
#
#
#
#
#
#
# try:
#     a = 1
#     b = 0
#     a/b
#
# except ZeroDivisionError:
#     print("You can't divide zero")
#
#
# import warnings
#
# warnings.warn("There is no code here wtf!!", SyntaxWarning)
#
#
# warnings.simplefilter("ignore", SyntaxWarning)
#
# warnings.simplefilter("always", ImportWarning)
#
#
# warnings.warn("There is some code!!!", SyntaxWarning)
#
# warnings.warn("Warning, no module imported!!!", ImportWarning)
#
#
#
# import warnings
#
# warnings.simplefilter("ignore", SyntaxWarning)
#
# warnings.simplefilter("error", ImportWarning)
#
# warnings.warn("No code here!!", SyntaxWarning)
#
#
# try:
#     warnings.warn("No module imported!!!", ImportWarning)
#
# except:
#     print("Waning processed")


# 1
try:

    a = int(input("Num: "))

    b = int(input("Num: "))

    print(a // b)

except ZeroDivisionError:
    print("0")

# 2




try:
    list = ["among us", "brawl stars", "pubg", "fortnite"]
    a = input("index: ")
    print(list[int(a)])

except IndexError:
    print(f"There is no index {a}")


# 3
try:
    b = input("Num:")

    print(float(b))

except ValueError:
    print("it cannot be the text only number!!!")

