from django.db import models


class New(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    text = models.CharField(max_length=250)
    news = models.ForeignKey(New, on_delete=models.CASCADE)    

    def __str__(self):
        return f"{self.text}"
