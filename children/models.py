from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from classes.models import PhClass
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    """
    This is an abstract model to store common information between the models
    """
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()

    class Meta:
        abstract = True


class Parent(Person):
    neighbourhood = models.CharField(max_length=64)
    primary_phone = PhoneNumberField(
        region="KE"
    )
    secondary_phone = PhoneNumberField(
        region="KE",
        null=True
    )

    class Meta:
        abstract = False


class Child(Person):
    """
    This is model class for children in the ph class
    """
    dob = models.DateField(verbose_name="Date Of Birth")
    ph_class = models.ForeignKey(to=PhClass,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name="children",
                                 related_query_name="child",
                                 verbose_name="Project Heritage Class",
                                 editable=False
                                 )
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey(to=Parent,
                               on_delete=models.PROTECT,
                               related_name="children",
                               related_query_name="child"
                               )

    class Meta:
        verbose_name_plural = "Children"
        abstract = False

    def age(self):
        # get the age as it can be derived from the dob
        return datetime.now().year - self.dob.year


# Set the ph Class before the Child is Saved in the Database
@receiver(pre_save, sender=Child)
def set_phClass(sender, instance, *args, **kwargs):
    # for class in classes
    for ph_class in PhClass.objects.all():
        # if the age withing range set as ph and break
        if ph_class.min_age <= instance.age() <= ph_class.max_age:
            instance.ph_class = ph_class
            break
