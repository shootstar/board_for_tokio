from django.db import models

class Board(models.Model):

    class Meta:
        app_label = 'board'

    id = models.CharField(max_length=255,primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class BoardContent(models.Model):

    class Meta:
        app_label = 'board'

    id = models.CharField(max_length=255,primary_key=True)
    board_id = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
