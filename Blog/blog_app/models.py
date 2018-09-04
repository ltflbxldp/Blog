from __future__ import unicode_literals
from DjangoUeditor.models import UEditorField
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(u"Blog Title",max_length = 100)        # Title
    category = models.CharField(u"Blog Tag",max_length = 50,blank = True)       # tag
    pub_date = models.DateTimeField(u"Issue Date",auto_now_add = True,editable=True)       # date
    update_time = models.DateTimeField(u'Update Time',auto_now=True,null=True)
    content = UEditorField(u"Main Body",height=300,width=1000,default=u'',blank=True,imagePath="uploads/blog/images/",
                           toolbars='besttome',filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:     # descending order
        ordering = ['-pub_date']
        verbose_name = "Article"
        verbose_name_plural = "Article"
