from django.db import models
from django_summernote.fields import SummernoteTextField
from django.contrib.auth.models import User

#Model for the Documents
class Article(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = SummernoteTextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title

#Model for the questions
class Question(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    question=SummernoteTextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.author

#Model for the Answers
class Answer(models.Model):
    answer= models.CharField(max_length=600,blank =True)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes= models.IntegerField(blank=True)

    def __str__(self):
        return self.author

#Model for the Upvotes
class Upvote(models.Model):
    reader=models.ForeignKey(User,on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)

    def __str_(self):
        return self.reader