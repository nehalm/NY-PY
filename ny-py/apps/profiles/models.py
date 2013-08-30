__author__ = 'gabe'

# Standard Library Imports
from collections import namedtuple
# Core Django Imports
from django.db import models
from django.contrib.auth.models import User
# Third Party Imports

# App Imports


# DRY -> we'll use this for any resource we create with a url.
class AddressableMixin(object):

    uri = models.SlugField(
        max_length=75,
    )


# Make this a mixin so we can define methods to summarize descriptions,
# reformat, etc all in one place.
class DescribedMixin(object):

    introduction = models.TextField(
        blank=True,
    )
    description = models.TextField(
        blank=True,
    )


class GenderedPronounMixin(object):

    GenderPronoun = namedtuple(
        'GenderPronoun',
        [
            'subject',
            'object',
            'determiner',
            'possessive',
            'reflexive',
        ]
    )
    PRONOUNS = {
        'female': GenderPronoun(
            'she',
            'her',
            'her',
            'hers',
            'herself',
        ),
        'male': GenderPronoun(
            'he',
            'him',
            'his',
            'his',
            'himself',
        ),
        'unspecified': GenderPronoun(
            'he or she',
            'him or her',
            'his or her',
            'his or hers',
            'himself or herself',
        ),
    }

    PRONOUN_CHOICES = (
        ('female', 'female'),
        ('male', 'male'),
        ('unspecified', 'prefer not to specify'),
    )
    preferred_pronoun = models.CharField(
        max_length=11,
        choices=PRONOUN_CHOICES,
        default='unspecified',
    )

    def pronoun(self, usage='subject'):
        item = self.PRONOUNS[self.preferred_pronoun]
        if usage == 'object':
            return item.object
        elif usage == 'determiner':
            return item.determiner
        elif usage == 'possessive':
            return item.possessive
        elif usage == 'reflexive':
            return item.reflexive
        return item.subject


class WebPresence(models.Model):

    service = models.CharField(
        max_length=60,
        default='unknown',
    )
    title = models.CharField(
        max_length=200,
        default='website',
    )
    _url = models.URLField(
        db_column='url',
        verbose_name='url',
    )

    def _set_from_url(self):
        # read in the url, and if it matches a pattern,
        # set the service and the title appropriately
        pass

    def _set_url(self, url):
        self.url = url
        self._set_from_url()

    def _get_url(self):
        return self._url
    url = property(_get_url, _set_url)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.service


class Profile(AddressableMixin, DescribedMixin, models.Model):

    # this can only be blank for now. When authentication is ready,
    # this becomes required.
    creator = models.ForeignKey(
        User,
        blank=True,
        related_name='created_%(class)s_profiles',
    )
    # this can always be blank. Unowned profiles are ok.
    owner = models.ForeignKey(
        User,
        blank=True,
        related_name='owned_%(class)s_profiles',
    )

    display_name = models.CharField(
        max_length=200,
    )

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.display_name


class Programmer(GenderedPronounMixin, Profile):

    # we can leave this as a text field and see what people say
    # once we have a good range, we can codify it a bit more
    status = models.TextField(
        blank=True,
    )


class NonProgrammer(GenderedPronounMixin, Profile):

    # as in, why are you here. Let's see what people say.
    # we'll require this in the actual js.
    looking_for = models.TextField(
        blank=True,
    )


# There is probably a better way to do this...
# https://docs.djangoproject.com/en/1.5/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType
class ProgrammerWebPresence(WebPresence):
    programmer = models.ForeignKey(
        Programmer,
        related_name='web_presence',
    )

    def __unicode__(self):
        return '%s for %s' % (self.service, self.programmer.display_name)


class NonProgrammerWebPresence(WebPresence):
    nonprogrammer = models.ForeignKey(
        NonProgrammer,
        related_name='web_presence',
    )

    def __unicode__(self):
        return '%s for %s' % (self.service, self.nonprogrammer.display_name)
