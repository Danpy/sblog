#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext


from blog.models import Blog, Tag


import datetime

def about(request):
	nav = 'about'
	return render_to_response('about.html', locals())


def blogs(request):
	blogs = Blog.objects.order_by('-id')
	tags = Tag.objects.all()

	nav = 'blogs'
	return render_to_response('blogs.html', locals())

def tag_to_blogs(request):
	tagname = request.GET.get('tag')
	tag = get_object_or_404(Tag, name=tagname)
	blogs = tag.blog_set.all()

	nav = 'blogs'
	return render_to_response('blogs.html', locals())

def blog(request, id):
	blog = Blog.objects.get(id=int(id))

	nav = 'blog'
	return render_to_response('blog.html', locals(), context_instance=RequestContext(request))


def readings(request):
	
	nav = 'readings'
	return render_to_response('readings.html', locals())
