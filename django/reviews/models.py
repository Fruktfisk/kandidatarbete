from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.conf import settings
from django.urls import reverse
from tags.models import Tag
from django.db.models import F
User = settings.AUTH_USER_MODEL

## ADDED A BUNCH OF BLANKS SHUDN*T B BLANKS
class Review(models.Model):
    CHOICES = [(i, i) for i in range(1,11)]

    author      = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title       = models.CharField(max_length=120)
    location    = models.ForeignKey("locations.Location", on_delete=models.DO_NOTHING, db_column='location')

    rating      = models.IntegerField(default=0, choices = CHOICES)
    upvotes     = models.ManyToManyField(User, blank=True, related_name='review_upvotes')
    downvotes   = models.ManyToManyField(User, blank=True, related_name='review_downvotes')

    text        = models.CharField(max_length=500, null=True, blank=True)
    tags        = models.ManyToManyField(Tag, blank=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    lat         = models.ForeignKey("locations.Location", on_delete=models.DO_NOTHING, to_field='lat', related_name='reviews_lat')
    lng         = models.ForeignKey("locations.Location", on_delete=models.DO_NOTHING, to_field='lng', related_name='reviews_lng')
    slug        = models.SlugField(null=True, blank=True)

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): #Defines which url to redirect to after made review
        #return f"/reviews/{self.slug}"
        return reverse("reviews:detail", kwargs = {'slug': self.slug}) #kwargs are always dicitonaries

    def get_upvote_url(self):
        return reverse("reviews:upvote-toggle", kwargs={"slug": self.slug})

    def get_downvote_url(self):
        return reverse("reviews:downvote-toggle", kwargs={"slug": self.slug})

    def get_api_like_url(self):
        return reverse("reviews:like-api-toggle", kwargs={"slug": self.slug})
    
    def votes(self):
        obj = Review.objects.get(id__iexact=self.id)
        return obj.upvotes.count()-obj.downvotes.count()

def pre_save_receiver(sender, instance, *args, **kwargs):
    print("Saving...")
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Review)

