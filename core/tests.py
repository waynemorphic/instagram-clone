from time import timezone
from django.test import TestCase
from core.models import Image_Model, Profile_Model, User_Model

# Create your tests here.

# user model tests
class UserTestClass(TestCase):
    
    def setUp(self):
        self.new_user = User_Model(email = 'one@gmail.com', username = 'John')
    
    def test_instance(self):
        self.assertTrue(self.new_user, User_Model)
        
    def test_save_user(self):
        self.new_user.save_user()
        users = User_Model.objects.all()
        self.assertTrue(len (users) > 0 )

# profile model tests 
class ProfileTestClass(TestCase):
    
    def setUp(self):
        self.new_user = User_Model(email = 'one@gmail.com', username = 'John')
        self.new_user.save()
        self.new_profile = Profile_Model(profile_photo = 'img.jpg', bio = 'i am me', user = self.new_user)
        
    def test_instance(self):
        self.assertTrue(self.new_profile, Profile_Model)
        
    def test_save_profile(self):
        self.new_profile.save_profile()
        profile = Profile_Model.objects.all()
        self.assertTrue(len (profile) > 0) 
        
    def test_update_profile(self):
        updated_profile_photo = 'img.avif'
        updated_bio = 'new bio of me'
        id = int(1)
        self.profile = Profile_Model.objects.filter(id = id).update(profile_photo = updated_profile_photo, bio = updated_bio)
        
    def test_delete_profile(self):
        id = int(2)
        self.new_profile_query = Profile_Model.objects.filter(id = id).delete()
             
        
# image model tests
class ImageTestClass(TestCase):
    
    def setUp(self):
        self.new_user = User_Model(email = 'one@gmail.com', username = 'John')
        self.new_user.save()
        self.new_profile = Profile_Model(profile_photo = 'img.jpg', bio = 'i am me', user = self.new_user)
        self.new_profile.save()
        self.new_image = Image_Model(image = 'img.jpg', image_name = 'first pic', image_caption = 'travel', likes = 2, comments = 'nice one', post_date = timezone, profile = self.new_profile, user = self.new_user)
        self.new_image.save()
        
    def test_instance(self):
        self.assertTrue(self.new_image, Image_Model)
        
    def test_save_image(self):
        self.new_image.save_image()
        images = Image_Model.objects.all()
        self.assertTrue(len (images) > 0)
        
    def test_update_caption(self):
        caption = 'new caption'
        self.new_image = Image_Model.objects.filter(image_caption = caption).update()
        
    def test_delete_image(self):
        image_id = int(1)
        self.new_image = Image_Model.objects.filter(image = image_id).delete()
    
    @classmethod
    def test_search_image(cls):
        search_term = 'travel'
        cls.search = Image_Model.search_image(search_term)
        
    def tearDown(self):
        Image_Model.objects.all().delete()
        Profile_Model.objects.all().delete()
        User_Model.objects.all().delete()
        
        
        
