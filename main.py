from googletrans import Translator

translator = Translator()

sentence = "Yazılım öğrenmek isteyen insanların sayısı artmaya başladı."

sentence2 = "Sokağın köşesinde inebilir miyim lütfen ?"

example = translator.translate(text=sentence)

print(example.text)
print(translator.translate(sentence2).text)
print(translator.translate(sentence2,dest='de').text)
