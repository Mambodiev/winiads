from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Faq(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = RichTextUploadingField()
    status=models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = "Faq" 



class Setting(models.Model):
   
    header_one = models.CharField(max_length=200,  blank=True, null=True)
    text = RichTextUploadingField( blank=True, null=True)
    what_we_do_h1 = models.CharField(max_length=200,  blank=True, null=True)
    what_we_do_text = RichTextUploadingField( blank=True, null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header_one


class Privacy(models.Model):
   
    header = models.CharField(max_length=200,  blank=True, null=True)
    text = RichTextUploadingField( blank=True, null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Privacies"



class Term(models.Model):
   
    header = models.CharField(max_length=200,  blank=True, null=True)
    text = RichTextUploadingField( blank=True, null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text