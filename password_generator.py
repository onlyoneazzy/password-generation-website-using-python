from random import choice


def password_generator():
    character = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!-_@ "

    generated_password = f"{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}{choice(f"{character}")}"

    return generated_password

if __name__ == "__main__":
    print(f"\nThis app is here to generate a password for you, and here it is\n")

    password = password_generator()
    print(password)