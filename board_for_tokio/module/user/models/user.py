from django.db import models

class SeparatedValuesField(models.TextField):
    """
    store values like list structure
    """
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)


class User(models.Model):

    class Meta:
        app_label = 'user'

    id = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    following_topic = SeparatedValuesField()
    follower = SeparatedValuesField()
    following = SeparatedValuesField()
    created_at = models.DateTimeField()
    


