from django.db import models
from django.core.validators import URLValidator

class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField()
    github = models.URLField()
    tryhackme = models.URLField(blank=True)
    tryhackme_user_id = models.CharField(max_length=100, blank=True, default='728215')
    summary = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    
    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    graduation_date = models.CharField(max_length=50)
    grade = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    icon = models.CharField(max_length=50, default='shield-check')
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('security', 'Security Testing'),
        ('programming', 'Programming'),
        ('cloud', 'Cloud & Infrastructure'),
        ('siem', 'SIEM & Monitoring'),
        ('frameworks', 'Security Frameworks'),
        ('os', 'Operating Systems'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=50)
    icon = models.CharField(max_length=50, default='terminal')
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
