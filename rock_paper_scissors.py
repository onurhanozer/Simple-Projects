import random

# Basit ASCII sanatı görselleri
ASCII_ART = {
    'r': """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
    'p': """     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)""",
    's': """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""",
}

def get_user_choice():
    """Prompt the user for a valid move and return it."""
    choices = {'r': 'Taş', 'p': 'Kağıt', 's': 'Makas'}
    while True:
        user_input = input("(R) Taş, (P) Kağıt, (S) Makas seçiniz: ").lower().strip()
        if user_input in choices:
            return user_input, choices[user_input]
        print("Geçersiz seçim. Lütfen tekrar deneyin.")

def get_computer_choice():
    """Randomly select a move for the computer."""
    choices = {'r': 'Taş', 'p': 'Kağıt', 's': 'Makas'}
    key = random.choice(list(choices.keys()))
    return key, choices[key]

def determine_winner(user_key, comp_key):
    """Return result string: 'Kullanıcı', 'Bilgisayar' veya 'Berabere'."""
    if user_key == comp_key:
        return 'Berabere'
    wins = {('r', 's'), ('p', 'r'), ('s', 'p')}
    return 'Kullanıcı' if (user_key, comp_key) in wins else 'Bilgisayar'

def main():
    print("Taş Kağıt Makas Oyununa Hoş Geldiniz!")
    scores = {'Kullanıcı': 0, 'Bilgisayar': 0, 'Berabere': 0}
    while True:
        user_key, user_move = get_user_choice()
        comp_key, comp_move = get_computer_choice()
        print(f"Siz: {user_move}\n{ASCII_ART[user_key]}")
        print(f"Bilgisayar: {comp_move}\n{ASCII_ART[comp_key]}")
        winner = determine_winner(user_key, comp_key)
        scores[winner] += 1
        if winner == 'Berabere':
            print('Sonuç: Berabere!')
        else:
            print(f'Sonuç: {winner} kazandı!')
        cont = input("Devam etmek için Enter'a basın, çıkmak için q yazın: ").lower().strip()
        if cont == 'q':
            break
    print("\nSkorlar:")
    print(f"Kullanıcı: {scores['Kullanıcı']}")
    print(f"Bilgisayar: {scores['Bilgisayar']}")
    print(f"Berabere: {scores['Berabere']}")

if __name__ == '__main__':
    main()
