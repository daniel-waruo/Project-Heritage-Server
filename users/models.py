from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    def is_parent(self):
        if self.parent:
            return True
        return False

    def is_facilitator(self):
        if self.facilitator:
            return True
        return False


# from classes.models import PhClass
# Create your models here.
# TODO: Enquire why do we user name fields while we can store them on User models by default
class Person(models.Model):
    """
    Abstract Person Class:
    This class has all fields that are similar to all the user types in this
    Group
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Parent(Person):
    pri_phone_no = models.CharField(max_length=64, null=True)
    sec_phone_no = models.CharField(max_length=64, null=True)
    neighbourhood = models.CharField(max_length=64, null=True)


class Facilitator(Person):
    ph_class = models.ManyToManyField('classes.PhClass')


# TODO: find out if the child is a user of the platform because he does not log in
class Child(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    dob = models.DateTimeField(default=timezone.datetime.now)
    school = models.CharField(max_length=64)
    # ASK:what does stage store
    stage = models.CharField(max_length=64)
    special_needs = models.TextField(null=True)

    ph_class = models.ForeignKey('classes.PhClass', default=1, on_delete=models.CASCADE, related_name='children')

    created_at = models.DateTimeField(auto_now_add=True)
    # ph_class_id = models.ForeignKey('classes.PhClass',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Children"
    def age(self):
        # code for getting the current age from the datetime now
        current_year = timezone.datetime.now().year
        # subtract dob from the current year
        return current_year - self.dob.year


class ProgressReport(models.Model):
    notes = models.TextField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    # TODO: find out why facilitator is many to many field if only one facilitator can write the report
    facilitator = models.ManyToManyField('Facilitator')
