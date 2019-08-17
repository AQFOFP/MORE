from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    sex = models.BooleanField(default=True)
    icon = models.CharField(max_length=200)
    introduct = models.CharField(max_length=255)

    class Meta:
        db_table = "more_user"

class Focus(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    focuuser = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_focu")
    class Meta:
        db_table = "more_focus"


class Article(models.Model):
    artititle = models.CharField(max_length=200)
    artidescribe = models.CharField(max_length=200)
    articontent = models.CharField(max_length=255)
    artiimg = models.CharField(max_length=200)
    artirelation = models.CharField(max_length=255)
    artidatetime = models.DateTimeField(auto_now_add=True)
    artitype = models.CharField(max_length=200)

    class Meta:
        db_table = "more_article"


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    lastreadtime = models.DateTimeField()
    class Meta:
        db_table = "more_collection"


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    commentscontent = models.CharField(max_length=200)
    commentsdatetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "more_comments"


class Commentszan(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comments = models.ForeignKey(Comments, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = "more_commentszan"


class Historyread(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hisreaddatetime = models.DateTimeField()
    class Meta:
        db_table = "more_historyread"