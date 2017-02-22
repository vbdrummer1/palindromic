alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "z", "0", "1",
              "2", "3", "4", "5", "6", "7", "8", "9"]


def is_palindrome(sentence):
    while sentence[0:]:
        for char in sentence:
            if char in alpha_list:
                if len(sentence) <= 1:
                    return True
                elif sentence[0] == sentence[-1]:
                    sentence.pop(0)
                    sentence.pop(-1)
                else:
                    return False
                return True
            else:
                return False


def main():
    sentence = input("Enter some text to determine if it is a palindrome")
    sentence.replace(" ", "")
    sentence = list(sentence.lower())
    print(is_palindrome(sentence))


if __name__ == '__main__':
    main()
