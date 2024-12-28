rep = 'y'
while rep == 'y':
    userInput = int(input('\nKetik 1 untuk plaintext to ascii\nKetik 2 untuk ascii to plaintext\n----------------------\npilihan anda ... '))

    def plaintext():
        p = input('masukkan plaintext ... ')
        enc = [ord(char) for char in p]
        print(enc)

    def asci():
        a = input('masukkan ascii (pisahkan dengan comma) ... ')
        ascii_value = map(int, a.split(','))
        dec = ''.join(chr(num) for num in ascii_value)
        print(dec)

    if userInput == 1:
        plaintext()

    elif userInput == 2:
        asci()
        
    rep = input('\ningin mengulangi? y/n .. ').lower()