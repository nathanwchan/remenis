from django.db import models

class User(models.Model):
    fbid = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    is_registered = models.BooleanField()
    first_date = models.DateTimeField(blank=True, null=True)
    last_date = models.DateTimeField(blank=True, null=True)
    page_views = models.IntegerField(default=0)
    unsubscribe_email = models.BooleanField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    class Admin:
        pass

class Story(models.Model):
    authorid = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True)
    story = models.TextField()
    story_date_year = models.IntegerField(blank=True, null=True)
    story_date_month = models.IntegerField(blank=True, null=True)
    story_date_day = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)
    is_private = models.BooleanField()
    page_views = models.IntegerField(default=0)
    
    class Admin:
        pass
    
class TaggedUser(models.Model):
    storyid = models.ForeignKey(Story)
    taggeduserid = models.ForeignKey(User, blank=True, null=True)
        
    class Admin:
        pass

class StoryComment(models.Model):
    storyid = models.ForeignKey(Story)
    authorid = models.ForeignKey(User, blank=True, null=True)
    comment = models.TextField()
    post_date = models.DateTimeField(blank=True, null=True)
    
    class Admin:
        pass

class StoryLike(models.Model):
    storyid = models.ForeignKey(Story)
    authorid = models.ForeignKey(User)
    
    class Admin:
        pass

class Notification(models.Model):
    storyid = models.ForeignKey(Story)
    userid = models.ForeignKey(User)
    type = models.CharField(max_length=20) # tagged, comment, like
    count = models.IntegerField(default=0)
    post_date = models.DateTimeField(blank=True, null=True)
    seen = models.BooleanField()
    
    class Admin:
        pass
    
class StoryOfTheDay(models.Model):
    text = models.TextField()
    
    class Admin:
        pass
    
class PageView(models.Model):
    page = models.CharField(max_length=40)
    count = models.IntegerField(default=0)
    
    class Admin:
        pass

class Information(models.Model):
    type = models.CharField(max_length=40)
    text = models.TextField()
    
    class Admin:
        pass
    
class BetaEmail(models.Model):
    email = models.EmailField(blank=True, null=True)
    submit_date = models.DateTimeField(blank=True, null=True)
    
    class Admin:
        pass
