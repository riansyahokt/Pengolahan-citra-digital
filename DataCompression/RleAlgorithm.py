import msvcrt


def pause():
    print("Press any key to continue . . .")
    msvcrt.getch()

def compress_rle(text):
    compressed_text = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            compressed_text += str(count) + text[i-1]
            count = 1
    compressed_text += str(count) + text[-1]
    return compressed_text

text = input("Masukkan teks yang ingin dikompresi: ")
compressed_text = compress_rle(text)
print("Teks setelah dikompresi: ", compressed_text)

pause()