from django.db import models
import datetime

# gonna represent the database tables
class Todo(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de Entrega", null=False, blank=False)
    finished_at = models.DateField(null=True, blank=False)

    class Meta():
        ordering = ["deadline"]
        # ordering = ["-deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = datetime.date.today()
            self.save()