from django.db.models import Model, CharField, DateTimeField, BooleanField

# Create your models here.
class Todo(Model):
    title = CharField(max_length=200)
    description = CharField(max_length=500, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    due_date = DateTimeField()
    completed = BooleanField(default=False)
