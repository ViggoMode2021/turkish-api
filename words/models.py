from django.db import models
import csv

class Word(models.Model):
    word = models.CharField(max_length=30)
    turkish_word = models.CharField(max_length=50)

    def __str__(self):
        return self.word + ' ' + self.turkish_word

class all_words(models.Model):
    def get_all_words(self):
        words = []
        with open('C:/Users/ryans/pythonProject6/django-api/turkish.csv', 'r', encoding='utf-8-sig') as fp:
            # You can also put the relative path of csv file
            # with respect to the manage.py file
            reader1 = csv.reader(fp, delimiter=',')
            for word in reader1:
                words.append(word)
        return words
