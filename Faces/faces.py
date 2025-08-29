def main():
    sentence = input("Sentence: ")
    print(convert(sentence))

def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

main()
