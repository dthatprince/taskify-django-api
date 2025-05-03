from django.db.models import Model, CharField, DateTimeField, BooleanField, ForeignKey, CASCADE
from django.conf import settings

# Create your models here.
class Todo(Model):
    title = CharField(max_length=200)
    description = CharField(max_length=500, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    due_date = DateTimeField()
    completed = BooleanField(default=False)
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
