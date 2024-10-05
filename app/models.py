from django.db.models import Q
from django.db import models
from django_cryptography.fields import encrypt


class Password(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(blank=True, max_length=255)
    username = models.CharField(blank=True, max_length=255)
    nickname = models.CharField(blank=True, max_length=255)
    password = encrypt(models.CharField(max_length=255, blank=True))
    site_name = models.CharField(blank=True, max_length=255)
    site_url = models.TextField(blank=True,
                                max_length=4096)
    notes = models.CharField(blank=True,
                             max_length=4096)

    class Meta:
        ordering = ["id"]

    def search(query):
        """
        """
        entries_found = Password.objects.filter(
            Q(nickname__iexact=query) | Q(nickname__icontains=query) | Q(site_name__iexact=query) | Q(site_name__icontains=query)
        )
        return entries_found
