from django.db import models

# Create your models here.

# user model
class User_Model(models.Model):
    '''
    Args
        email, username
    '''
    
    email = models.EmailField(blank = False)
    username = models.CharField(max_length = 40, blank = False)

    def __str__(self):
        return self.email
    
    def save_user(self):
        self.save()

# profile model
class Profile_Model(models.Model):
    '''
    Args
        profile_photo, bio, user
    '''

    profile_photo = models.ImageField(upload_to = 'static/media', default = '')
    bio = models.TextField()
    user = models.ForeignKey(User_Model, on_delete = models.CASCADE)

    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
        
    def update_profile(self, new_profile_photo, new_bio):
        self.objects.all().update(update_profile_photo = new_profile_photo, update_bio = new_bio)
        
    def delete_profile(self):
        self.objects.all().delete()

# image model
class Image_Model(models.Model):
    '''Args
        image, image_name, image_caption, likes, comments, post_date, profile, user
    '''
    
    image = models.ImageField(upload_to = 'static/media', default = '')
    image_name = models.CharField(max_length = 50)
    image_caption = models.TextField()
    likes = models.IntegerField()
    comments = models.TextField()
    post_date = models.DateTimeField(auto_now = True)
    profile = models.ForeignKey(Profile_Model, on_delete = models.CASCADE)
    user = models.ForeignKey(User_Model, on_delete = models.CASCADE)    
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.objects.filter(id = id).delete()
    
    def update_caption(self, image_caption):
        self.objects.filter(id = id).update(image_caption = image_caption)
        
    @classmethod
    def search_image(cls, search_term):
        find_image = cls.objects.filter(image_name__icontains = search_term)
        return find_image