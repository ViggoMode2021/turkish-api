from words.models import Word
import csv

def run():
    with open('turkish.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Word.objects.all().delete()

        for row in reader:
            print(row)

            dictionary = Word(word=row[0],
                        turkish_word=row[1])

            dictionary.save()
