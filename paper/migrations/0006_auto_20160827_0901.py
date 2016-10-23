# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-27 09:01
from __future__ import unicode_literals

from django.db import migrations, models, IntegrityError, transaction


def subject_to_tag(apps, schema_editor):
    """
    Migrates the subjects data to the tag model
    """
    Paper = apps.get_model('paper', 'Paper')
    Subject = apps.get_model('paper', 'Subject')
    Tag = apps.get_model('paper', 'Tag')

    papers = Paper.objects.all()

    for paper in papers:
        try:
            with transaction.atomic():
                paper.tags.create(name=paper.subject.name)
                paper.save()
        except IntegrityError:
            print "Tag already exists"


def reverse_subject_to_tag(apps, schema_editor):
    """
    Reversing the actions done by the function subject_to_tag
    """
    Paper = apps.get_model('paper', 'Paper')
    Subject = apps.get_model('paper', 'Subject')
    Tag = apps.get_model('paper', 'Tag')


    papers = Paper.objects.all()

    for paper in papers:
        tag = paper.tags.first()
        try:
            with transaction.atomic():
                paper.subject = Subject.objects.create(name=tag.name)
                paper.save()
        except IntergrityError:
            print "Subject already exists"


def print_help_info(apps, schema_editor):
    print "Here there is some help ful info: DOING"

def reverse_print_help_info(apps, schema_editor):
    print "Here there is some help ful infor: UNDOING"

class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0005_paper_created_date'),
    ]



    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),

        migrations.AddField(
            model_name='paper',
            name='tags',
            field=models.ManyToManyField(to='paper.Tag'),
        ),

        migrations.RunPython(subject_to_tag, reverse_subject_to_tag),



        migrations.RunPython(print_help_info, reverse_print_help_info),
        migrations.RunPython(print_help_info, reverse_print_help_info),
        migrations.RunPython(print_help_info, reverse_print_help_info),


        migrations.RunPython(print_help_info, reverse_print_help_info),

        migrations.AlterField(
            model_name='paper', 
            name='subject',
            field=models.ForeignKey(to='paper.Subject', null=True),
        ),

        migrations.RemoveField(
            model_name='paper',
            name='subject',
        ),

	      
        migrations.RunPython(print_help_info, reverse_print_help_info),
        
        migrations.DeleteModel(
            name='Subject',
        ),


    ]