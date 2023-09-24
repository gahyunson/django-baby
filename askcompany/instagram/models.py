from django.db import models
from django.conf import settings

class Users(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Post(models.Model):
    # 'auth.User'
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        # return f"Post Object ({self.id})"
        return self.message

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = 'message length num'
    
    class Meta:
        ordering=['-id']
        
class Comment(models.Model):
    # post_id
    # post는 가상의 필드 , 실제와 다르다. 
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             limit_choices_to={'is_public':True})
    
    # 다른 앱의 모델 지정시 'instagram.Post' 앱 명시,
    # Post 라고 써도, 'Post' 라고 써두 된다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post, blank=False)

    def __str__(self):
        return self.name