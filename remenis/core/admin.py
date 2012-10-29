from django.contrib import admin
from models import User, Story, TaggedUser, StoryComment, StoryLike, Notification, StoryOfTheDay, PageView, Information, BetaEmail

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'fbid', 'first_name', 'last_name', 'full_name', 'email', 'is_registered', 'first_date', 'last_date', 'page_views', 'unsubscribe_email')
    search_fields = ('first_name', 'last_name', 'full_name', 'email')
    ordering = ('-is_registered', '-last_date')

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'title', 'story', 'story_date_year', 'story_date_month', 'story_date_day', 'post_date', 'is_private', 'page_views')
    list_filter = ('authorid',)
    date_hierarchy = 'post_date'
    ordering = ('-post_date',)
    raw_id_fields = ('authorid',)
    
    def author_name(self, instance):
        return instance.authorid.full_name

class TaggedUserAdmin(admin.ModelAdmin):
    list_display = ('story_id', 'tagged_user_name')
    search_fields = ('story_id', 'tagged_user_name')
    
    def story_id(self, instance):
        return instance.storyid.id
    
    def tagged_user_name(self, instance):
        return instance.taggeduserid.full_name
    
class StoryCommentAdmin(admin.ModelAdmin):
    list_display = ('story_id', 'author_name', 'comment', 'post_date')
    search_fields = ('story_id', 'author_name', 'comment', 'post_date')
    ordering = ('-post_date',)
    
    def story_id(self, instance):
        return instance.storyid.id
    
    def author_name(self, instance):
        return instance.authorid.full_name
    
class StoryLikeAdmin(admin.ModelAdmin):
    list_display = ('story_id', 'author_name')
    search_fields = ('story_id', 'author_name')
    
    def story_id(self, instance):
        return instance.storyid.id
    
    def author_name(self, instance):
        return instance.authorid.full_name
    
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('story_id', 'user_name', 'type', 'count', 'post_date', 'seen')
    search_fields = ('story_id', 'user_name', 'type', 'count', 'post_date', 'seen')
    ordering = ('-post_date',)
    
    def story_id(self, instance):
        return instance.storyid.id
    
    def user_name(self, instance):
        return instance.userid.full_name
    
class StoryOfTheDayAdmin(admin.ModelAdmin):
    list_display = ('text',)
    
class PageViewAdmin(admin.ModelAdmin):
    list_display = ('page', 'count')
    ordering = ('page',)

class InformationAdmin(admin.ModelAdmin):
    list_display = ('type', 'text')
            
class BetaEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'submit_date')
    date_hierarchy = 'submit_date'
    ordering = ('-submit_date',)
    
admin.site.register(TaggedUser, TaggedUserAdmin)
admin.site.register(StoryComment, StoryCommentAdmin)
admin.site.register(StoryLike, StoryLikeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(StoryOfTheDay, StoryOfTheDayAdmin)
admin.site.register(PageView, PageViewAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(BetaEmail, BetaEmailAdmin)
