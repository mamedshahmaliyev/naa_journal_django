from django.db import models

from django.utils.translation import gettext_lazy

from students.models import *
from teachers.models import *

class Subject(models.Model):

    class Meta:
        verbose_name_plural = gettext_lazy("Fənlər")

    name = models.CharField(max_length=250, verbose_name=gettext_lazy('Ad'))
    code = models.CharField(max_length=250, verbose_name=gettext_lazy('Code'))

    def __str__(self):
        return self.name + ' [' + self.code + ']'

class Journal(models.Model):

    class Meta:
        verbose_name_plural = gettext_lazy("Jurnallar")

    kafedra = models.CharField(max_length=250, verbose_name=gettext_lazy('Kafedra'))
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, verbose_name=gettext_lazy('Qrup'))
    date_start = models.DateField(verbose_name=gettext_lazy('Başlama tarixi'))
    date_end = models.DateField(verbose_name=gettext_lazy('Başlama tarixi'))

    def __str__(self):
        return self.student_group.name + ' [' + self.date_start.strftime('%Y-%m-%d') + ', ' + self.date_end.strftime('%Y-%m-%d') + ']'

class JournalRecord(models.Model):

    class Meta:
        verbose_name_plural = gettext_lazy("Jurnallar Yazıları")

        ordering = ['-id']

    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, verbose_name=gettext_lazy('Jurnal'))
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, verbose_name=gettext_lazy('Qrup'))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=gettext_lazy('Müəllim'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=gettext_lazy('Fən'))
    record_type = models.CharField(
                        max_length=10, 
                        verbose_name=gettext_lazy('Tip'), 
                        choices=(
                            ('lecture', gettext_lazy('Mühazirə')), 
                            ('lab', gettext_lazy('Laboratoriya')), 
                            ('seminar', gettext_lazy('Seminar')), 
                            ('kollokvium', gettext_lazy('Kollokvium')),
                        )
                    )
    hour = models.SmallIntegerField(verbose_name=gettext_lazy('Saat'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=gettext_lazy('Tələbə'))
    is_present = models.BooleanField(verbose_name=gettext_lazy('İştirak etdi'))
    mark = models.IntegerField(null=True, blank=True, verbose_name=gettext_lazy('Qiymət'))


