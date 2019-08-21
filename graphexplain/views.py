import time

from django.http import JsonResponse
from django.shortcuts import render, redirect,reverse

# Create your views here.
from Moremodel.models import *

#get进入图说界面
def latest(request):
    return redirect(reverse('relatest',args=('0')))


#0为最新，1为最热
def relatest(request,sort):
    arts = Article.objects.filter(graphexplain='graphexplain')

    #最新
    if sort == '0':
        art_list = []
        for art in arts:
            comment = Comments.objects.filter(article=art).count()
            arts.num = comment

            artdetail = {
                'artiimg': art.artiimg,
                'artidiscribe': art.artidiscribe,
                'artinum': arts.num,
                'artitime': art.commentsdatetime,
            }

            art_list.append(artdetail)
        data = {
            'art_list': art_list,
        }
        return JsonResponse(data)

    #最热
    if sort == '1':
        art_list = []
        for art in arts:
            zans = Comments.objects.filter(article=art).count()

            artdetail = {
                'artiimg': art.artiimg,
                'artidiscribe': art.artidiscribe,
                'artinum': zans,
                'artitime': art.commentsdatetime,
            }

            art_list.append(artdetail)
            art_list.sort(key=artdetail['artinum'])
        data = {
            'art_list': art_list,
        }
        return JsonResponse(data)
    return JsonResponse({})



#get进入图说详情
def picturedetail(request,artid):
    art = Article.objects.filter(id=artid)

    content = art.articontent
    img = art.artiimg
    title = art.artititle

    data = {
        'content' : content,
        'img' : img,
        'title' : title,
    }
    return JsonResponse(data)




#用户评论页面
def usercomments(request,artid):
    comments = Comments.objects.filter(article=artid)

    comment_list = []
    for comment in comments:
        users = comment.user_set.all()
        zans = Comments.objects.filter().count()

        data ={
            'comment':comment,
            'users':users,
            'zans':zans,
            'zanstime':comment.commentsdatetime,
        }
        comment_list.append(data)
    return JsonResponse({'data':comment_list})


#回复页面
def replyPage(request):

    msg = request.POST.get('msg')

    com = Comments()
    com.commentscontent = msg
    com.commentsdatetime = time.time()

    return JsonResponse({})



#用户收藏页面
def collection(request,userid):

    cols = Collection.objects.all()
    col_list = []
    for col in cols:
        col = Collection.objects.filter(userid=userid)
        lastreadtime = col.lastreadtime
        title = col.article_srt.artititle
        img = col.article_srt.img
        putin = col.article_srt.artititle


        coldetail = {
            'lastreadtime':lastreadtime,
            'title':title,
            'img':img,
            'putin':putin,
        }

        col_list.append(col)
        col_list.sort(key=coldetail['lastreadtime'])

    data = {
        'col_list':col_list,
    }

    return JsonResponse(data)


#用户观点
def userview(request,userid):

    data = {
    }

    return JsonResponse(data)









