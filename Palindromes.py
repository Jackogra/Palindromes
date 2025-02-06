"""
Zadanie: palindromy
Pamiętaj, że wszystkie zadania, które wysyłasz Mentorowi powinny być umieszczone w Twoim zdalnym repozytorium,
jako osobne projekty. W czasie pracy zapisuj więc kolejne commity i prześlij całość na serwer w serwisie GitHub.

Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem.
Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.

Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False,
mówiącą czy podany tekst jest palindromem.

Podpowiedź
Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji,
które pozwalają odnosić się do elementów indeksowanych od początku i od końca.

Do zadania dodaj krótką dokumentację i umieść je w zdalnym repozytorium. Link prześlij Mentorowi.
"""

def palindrome(word):
    """
    The palindrome function checks whether a given word is a palindrome
    (a word that reads the same forwards and backwards).
    :param word:
    :return: Bool
    """
    # Create reversed word using string indexation
    return bool(word == str(word[::-1]))
"""
    # Compare original word to a reversed one
    if word == reversed_word:
        # If there is a match, they are Palindrome
        return True
    else:
        # If there is NO match, they are NOT Palindrome
        return False
"""
# Print output to check functionality
print(palindrome("mamam"))