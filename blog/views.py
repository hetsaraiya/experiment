import json
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from yaml import serialize
from .models import *
import mimetypes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.db.models import Q
import json


@csrf_exempt
def bloghome(request):
        
    if request.method == 'GET':
        allPosts = Post.objects.filter(status='Approved').order_by('-timeStamp') 
        data = serializers.serialize("json", allPosts)
        return HttpResponse(data, content_type="application/json")
        
# def bloghome(request):
#     allPosts = Post.objects.filter(status='Approved').order_by('-timeStamp') 

#     context = {'allPosts' : allPosts}
#     return render(request,'blog/home.html',context)


def blogPost(request):
    if request.method == 'GET':
        id1=request.GET.get("id") 
        post = Post.objects.filter(pk=id1)
        data = serializers.serialize("json", post)
        return HttpResponse(data, content_type="application/json")

# def blogPost(request):
#     if request.method == "GET":
#         id1=request.GET.get("id") 
#         post = Post.objects.filter(pk=id1)
#         post_data = serializers.serialize("json", post)
#         ads = Ad.objects.filter(post=id1).all()
#         data_ads = serializers.serialize("json",ads)
#         response1 = {
#             "post_data": json.loads(post_data),
#             "data_ads" : json.loads(data_ads),
#         }
#         json_response = json.dumps(response1)
#         return HttpResponse(json_response, content_type="application/json")

def isDeletedCheck(request):
    allpost = Post.objects.filter(isDeleted=True).all()
    data = serializers.serialize("json", allpost)
    print("done")
    return HttpResponse(data, content_type="application/json")

def fetch_category(request):
    category = BlogCategory.objects.all()
    data = serializers.serialize("json", category)
    print("category done")
    return HttpResponse(data, content_type="application/json")

def cars(request):
    allpost = Post.objects.filter(Category = "cars").all()
    data = serializers.serialize("json", allpost)
    return HttpResponse(data, content_type="application/json")

def education(request):
    
    allpost = Post.objects.filter(Category = "Education").all()
    data = serializers.serialize("json", allpost)
    print("cars")
    return HttpResponse(data, content_type="application/json")

def money(request):
    allpost = Post.objects.filter(Category = "Money").all()
    data = serializers.serialize("json", allpost)
    print("cars")
    return HttpResponse(data, content_type="application/json")

def news(request):
    allpost = Post.objects.filter(Category = "News & Culture").all()
    data = serializers.serialize("json", allpost)
    print("cars")
    return HttpResponse(data, content_type="application/json")

def science(request):
    allpost = Post.objects.filter(Category = "Science").all()
    data = serializers.serialize("json", allpost)
    print("cars")
    return HttpResponse(data, content_type="application/json")

def tech(request):
    allpost = Post.objects.filter(Category = "Tech").all()
    data = serializers.serialize("json", allpost)
    print("cars")
    return HttpResponse(data, content_type="application/json")

def other(request):
    allpost = Post.objects.filter(Category = "Other").all()
    data = serializers.serialize("json", allpost)
    print("cars")
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def searchPosts(request):
    if request.method == "GET":
        searchQuery = request.GET.get("searchQuery")
        result = {"posts": []}

        # Search for posts based on title, author, and content, and filter by status
        posts = Post.objects.filter(
            Q(title__icontains=searchQuery) |
            Q(author__icontains=searchQuery) |
            Q(content__icontains=searchQuery),
            status="Approved"
        ).all()

        for post in posts:
            result["posts"].append({
                "title": post.title,
                "author": post.author,
                "thumbnail": post.thumbnail.url if post.thumbnail else '',
                "slug": post.slug,
                "timeStamp": str(post.timeStamp) ,
                "status": post.status,
                "content": post.content,
                "pk": post.pk,
            })

        result = {"posts": result["posts"][:5]}
        return HttpResponse(json.dumps({"data": result}),content_type="application/json")

    return HttpResponse(
        json.dumps({"error": "You were not supposed to be here."}),
        content_type="application/json",
    )  

@csrf_exempt
def ad_fetch(request):
    if request.method == "GET":
        id1=request.GET.get("id") 
        all_ads = Ad.objects.filter(post=id1).all()

        data = serializers.serialize("json", all_ads)
        print("done")
        return HttpResponse(data, content_type="application/json")