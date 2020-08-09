from django.db import models

class Question(models.Model):
    questions=models.TextField()
    choice_1 = models.CharField(max_length=50)
    choice_2 = models.CharField(max_length=50)
    choice_3 = models.CharField(max_length=50)
    choice_4 = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)
class Quiz(models.Model):
    q_id=models.IntegerField()
    Title=models.CharField(max_length=100)
    Description=models.TextField(max_length=200)
    Question=models.ForeignKey(Question,related_name='Quiz_Questions',on_delete=models.CASCADE)
    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        print(self)
        #return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
