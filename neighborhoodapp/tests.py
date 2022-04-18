import datetime
from .models import Business, Neighborhood, Post, Profile 
from django.contrib.auth.models import User
from django.test import TestCase

class ProfileTest(TestCase):
    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighborhood =  Neighborhood(name = "felo75", location= "Laikipia ", admin = self.user,description='Home is best all the time', image="neighborhood5.jpg")
        self.neighborhood.save()
        self.profile = Profile(id=750,id_no=34931235,email='testingemail@g.com', profile_pic='profile.jpg', neighbourhood=self.neighborhood,
                                    user=self.user)
      
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        testsaved = Profile.objects.all()
        self.assertFalse(len(testsaved) < 0)    

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)

class NeighborhoodTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighborhood =  Neighborhood(neighborhood_name = "felo75", location= "Laikipia", admin = self.user,description='Home is best all the time', image="neighbourhood75.jpg")
        self.neighborhood.save()
   
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save_neighbourhood(self):
        self.neighbourhood.save_hood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_neighborhood(self):
        self.neighborhood.delete_hood()
        testsaved = Neighborhood.objects.all()
        self.assertFalse(len(testsaved) > 0)

class BusinessTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighborhood =  Neighborhood(name = "Sambu75", location= "Laikipia", admin = self.user,description='Home is best all the time', image="neighbourhood75.jpg")
        self.neighbourhood.save()
        self.bussiness = Business(user=self.user,name="Business", neighborhood=self.neighborhood,business_email="business@gmail.com", business_description="Business setup")
        self.bussiness.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.bussiness,Business))

    def test_save_business(self):
        self.bussiness.save_business()
        bussiness = Business.objects.all()
        self.assertTrue(len(bussiness) > 0)

    def test_delete_hood(self):
        self.bussiness.delete_business()
        bussiness = Business.objects.all()
        self.assertFalse(len(bussiness) > 0)

class PostTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighbourhood =  Neighbourhood(neighborhoodname = "Sambu75", neighborhood_location= "F-Society N", admin = self.user,neighborhood_description='Home is best all the time', image="neighbourhood75.jpg")
        self.neighbourhood.save()
        self.post = Post(user=self.user,title="User post",image="post.jpg" ,content ="user post", timestamp=datetime.datetime,neighbourhood=self.neighbourhood)
        self.post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.objects.all()
        self.assertFalse(len(post) > 0)