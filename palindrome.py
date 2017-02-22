import re
alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "z", "0", "1",
              "2", "3", "4", "5", "6", "7", "8", "9"]


def strip_punc(sentence):
    sentence = re.sub(r'[^A-Za-z0-9]', "", sentence)
    return sentence

def is_palindrome(sentence):
    sentence = strip_punc(sentence)
    sentence = sentence.lower()
    print(sentence)
    if len(sentence) <= 1:
        return True
    elif sentence[0] == sentence[-1]:
        sentence = list(sentence)
        sentence.pop(0)
        sentence.pop(-1)
        empty_string = ""
        sentence = empty_string.join(sentence)
        return is_palindrome(sentence)
    else:
        return False


def main():
    sentence = input("Enter some text to determine if it is a palindrome")
    print(is_palindrome(sentence))


if __name__ == '__main__':
    main()
