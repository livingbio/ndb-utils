from gcloudorm import model as ndb
from django.db import models
from django.forms.models import model_to_dict
import datetime

class Datastore(ndb.Model):
    @classmethod
    def update(cls, id, data):
        # update or replace
        obj = cls.get_by_id(id)
        if not obj:
            return cls.replace(id, data)

        return obj.patch(data)

    def patch(self, data):
        for attr in data:
            setattr(self, attr, data[attr])

        return self

    @classmethod
    def replace(cls, id, data):
        obj = cls(id=id)
        return obj.patch(data)

    @classmethod
    def remove(cls, id):
        obj = cls(id=id)
        obj.delete()



class DatastoreMixin(models.Model):
    last_sync = models.DateTimeField(null=True, blank=True)

    _ndb_model = None

    class Meta:
        abstract = True

    @property
    def datastore_id(self):
        return self.pk

    def to_datastore_dict(self):
        return model_to_dict(self)

    @property
    def ndb_model(self):
        return self._ndb_model

    def save(self, *args, **kwargs):
        super(DatastoreMixin, self).save(*args, **kwargs)

        obj = self.ndb_model.replace(
            id=self.datastore_id,
            data=self.to_datastore_dict()
        )
        obj.put()
        self.last_sync = datetime.datetime.utcnow()


    def delete(self):
        self.ndb_model.remove(self.datastore_id)
        super(DatastoreMixin, self).delete()

