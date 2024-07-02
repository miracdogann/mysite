from django.db import models

# Create your models here.

class Questions(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'questions'
    
    def __str__(self):
        return self.question_text

        
class Choices(models.Model):
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    choice_text = models.TextField()
    points = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'choices'

class UserAnswers(models.Model):
    username = models.TextField()
    total_score = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'user_answers'


