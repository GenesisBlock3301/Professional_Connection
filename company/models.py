from django.db import models
from accounts.models.users import User


class Company(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="companies_photo")
    industry = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Management(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_managements")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_managements")
    position = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.position


class Experience(models.Model):
    EMPLOYEE_TYPE = [
        ('full_time', "Full-Time"),
        ('part_time', "Part-Time"),
        ("contract", "Contract"),
        ("freelance", "Freelance"),
        ("seasonal", "Seasonal")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_experiences')
    title = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50, choices=EMPLOYEE_TYPE)
    start = models.DateField()
    end = models.DateField(null=True)
    position = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_experiences")

    @property
    def duration(self):
        return self.end - self.start
