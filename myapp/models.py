from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    cr_at = models.DateField(auto_now_add=True)


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=50)
    avatar = models.FileField(upload_to='avatars/', max_length=100)


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    views = models.IntegerField()
    cr_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    cr_at = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
                fields=['user', 'post'],
                name='unique_user_post_like'
            )
        ]


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    cr_at = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'post'],
                name='unique_user_post_favorite'
            )
        ]



