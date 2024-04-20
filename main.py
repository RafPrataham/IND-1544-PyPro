meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
            
# print(meme_dict)

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
# print(word)


if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print("kata yang anda masukan adalah", word)
    print(word, "artinya adalah ", meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("maaf kata tidak ditemukan")





# dictionary
# dictionary = {key:value}
