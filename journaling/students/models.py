from django.db import models


from django.utils.translation import gettext_lazy

class Student(models.Model):

    class Meta:
        verbose_name_plural = gettext_lazy("Tələbələr")

    name = models.CharField(max_length=250, verbose_name=gettext_lazy('Ad'))
    surname = models.CharField(max_length=250, verbose_name=gettext_lazy('Soyad'))
    patronymic = models.CharField(max_length=250, blank=True, verbose_name=gettext_lazy('Ata adı'), null=True, default=None)
    gender = models.CharField(max_length=10, verbose_name=gettext_lazy('Cinsi'), null=True, choices=(('male', gettext_lazy('Kişi')), ('female', gettext_lazy('Qadın'))))

    def __str__(self):
        return self.name + ' ' + self.surname

class StudentGroup(models.Model):

    students = models.ManyToManyField(Student, related_name="students")

    class Meta:
        verbose_name_plural = gettext_lazy("Qruplar")

    name = models.CharField(max_length=250, verbose_name=gettext_lazy('Qrupun adı'))
    starosta = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=gettext_lazy('Starosta'))

    def __str__(self):
        return self.name
