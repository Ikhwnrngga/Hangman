import random

def choose_word():
    words = ["pisang", "mangga", "rambutan", "durian", "stroberry", "alpukat", "nangka", "anggur"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Selamat datang di permainan Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    while True:
        current_display = display_word(secret_word, guessed_letters)
        print("Kata saat ini:", current_display)
        guess = input("Tebak huruf: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("Anda sudah menebak huruf ini sebelumnya. Coba lagi.")
            elif guess in secret_word:
                print("Selamat! Huruf benar.")
                guessed_letters.append(guess)
            else:
                print("Tebakan salah. Coba lagi.")
                attempts += 1
                print("Sisa kesempatan:", max_attempts - attempts)
                if attempts == max_attempts:
                    print("Maaf, Anda kalah. Kata yang benar adalah:", secret_word)
                    break
        else:
            print("Masukan tidak valid. Mohon masukkan satu huruf.")

        if "_" not in display_word(secret_word, guessed_letters):
            print("Selamat! Anda berhasil menebak kata:", secret_word)
            break

if __name__ == "__main__":
    hangman()
