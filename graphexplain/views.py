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

            art_list.append(art)
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

            art_list.append(art)
            art_list.sort(key=artdetail['artinum'])
        data = {
            'art_list': art_list,
        }
        return JsonResponse(data)
    return JsonResponse({})


def usercomment(request):
    comments = Comments.objects.all()

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















