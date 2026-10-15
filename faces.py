
def convert():
    user = input()
    user = user.replace(":)", "🙂")
    user = user.replace(":(", "🙁")
    print(user)




def main():
    convert()
main()