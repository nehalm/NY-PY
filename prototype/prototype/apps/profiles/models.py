from django.db import models

# Create your models here.

class Profile(models.Model):
    URI = models.CharField(max_length=75)
    display_name = models.CharField(max_length=200)
    introduction = models.TextField(blank=True)
    description = models.TextField(blank=True)
    # web_presence = models.ManyToManyField(WebPresence)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.display_name

# class WebPresence(models.model):
#     profile = models.ForeignKey(Profile)

#     GITHUB = 1
#     TWITTER = 2
#     STACKOVERFLOW = 3

#     SOCIAL_SITE = [
#         (GITHUB, "Github"),
#         (TWITTER, "Twitter"),
#         (STACKOVERFLOW, "Stack Overflow"),
#     ]
#     site = models.IntegerField(choices=SOCIAL_SITE)
#     url = models.CharField(max_length=200)

class ProfileType(Profile):
    PROGRAMMER = 1
    RECRUITER = 2

    PROFILE_TYPE = [
        (PROGRAMMER, "Programmer"),
        (RECRUITER, "Recruiter"),
    ]
    profile_type = models.IntegerField(choices=PROFILE_TYPE)
