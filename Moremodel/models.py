from django.db import models


# Create your models here.
#用户
class User(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=100, unique=True)
    sex = models.BooleanField(default=True)
    icon = models.CharField(max_length=200, default='')
    introduct = models.CharField(max_length=255, default='')

    class Meta:
        db_table = "more_user"


#关注
class Focus(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    focuuser = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_focu")
    class Meta:
        db_table = "more_focus"

#文章
class Article(models.Model):
    artititle = models.CharField(max_length=200)
    artidescribe = models.CharField(max_length=200)
    articontent = models.CharField(max_length=255)
    artiimg = models.CharField(max_length=200)
    artirelation = models.CharField(max_length=255)
    artirelationico = models.CharField(max_length=255)
    artidatetime = models.DateTimeField(auto_now_add=True)
    artitype = models.CharField(max_length=200)

    class Meta:
        db_table = "more_article"

#收藏
class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    lastreadtime = models.DateTimeField()
    class Meta:
        db_table = "more_collection"

#评论
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    commentscontent = models.CharField(max_length=200)
    commentsdatetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "more_comments"

#评论点赞
class Commentszan(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comments = models.ForeignKey(Comments, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = "more_commentszan"

#历史阅读
class Historyread(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hisreaddatetime = models.DateTimeField()
    class Meta:
        db_table = "more_historyread"


#导航页图片
class GuideImg(models.Model):
    img = models.CharField(max_length=256)
    class Meta:
        db_table = "guide_img"