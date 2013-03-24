#-*- coding: utf-8 -*-

from django.db import models
import datetime

class Tag(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    taglist = []

    def save(self, *args, **kwargs):
    	super(Blog, self).save()
    	for i in self.taglist:
    		p, created = Tag.objects.get_or_create(name=i)
    		self.tags.add(p)

    def __unicode__(self):
        return self.title

# class Comment(models.Model):
# 	blog = models.ForeignKey(Blog)
# 	name = models.CharField(max_length=20)
# 	content = models.TextField()
# 	pub_date = models.DateTimeField(default=datetime.datetime.now())

# 	def __unicode__(self):
# 		return self.content