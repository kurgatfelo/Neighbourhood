from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    count = models.IntegerField(default=0,blank=False)
    description = models.TextField()
    image = CloudinaryField('images', blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True,name='admin')

    def __str__(self):
     return self.name


    def create_neigborhood(self):
         self.save()
    

    @classmethod
    def delete_neigborhood(cls,id):
            cls.objects.filter(id).delete()

    @classmethod
    def find_neigborhood(cls,searched_name):
        neigborhood = cls.objects.filter(name__icontains=searched_name)
        return neigborhood
    @classmethod
    def update_neighborhood(cls,id):
        cls.objects.filter(id=id).update()
    @classmethod
    def update_occupants(cls,id):
        cls.objects.filter(id=id).update()


class Profile(models.Model):
    name = models.CharField(max_length=200)
    profile_pic = CloudinaryField('image', blank=True)
    id_no = models.IntegerField(default=0,blank=False)
    email = models.EmailField()

    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, null=True)

    def __str__(self):
     return self.name

    def save_profile(self):
        self.save()

    @classmethod
    
    def delete_profile(cls,id):
        cls.objects.filter(id).delete()
    @classmethod
    def update_profile(cls, id):
        cls.objects.filter(id=id).uodate()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()




    
class Business(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    business_email = models.EmailField()
    business_description = models.TextField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)


    def __str__(self):
     return self.name
    def create_business(self):
        self.save()
    @classmethod
    def delete_business(cls,id):
        cls.objects.filter(id=id).delete()
    @classmethod
    def find_business(cls,business_id):
        business=cls.objects.filter(business_id)
        return business
    @classmethod
    def update_business(cls,id):
        cls.objects.filter(id=id).update()
class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    image = CloudinaryField('images')
    content = models.TextField(max_length=300,blank=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, default='', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def save_post(self):
        return self.save()

    def delete_post(self):
        self.delete()























