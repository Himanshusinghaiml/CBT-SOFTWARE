# Generated manually to add metadata fields to Question model
from django.db import migrations, models


def generate_default_topic(apps, schema_editor):
    Question = apps.get_model('companylogin', 'Question')
    for q in Question.objects.all():
        if not q.topic:
            q.topic = ''
            q.save()


class Migration(migrations.Migration):

    dependencies = [
        ('companylogin', '0010_rename_centers_center_rename_questions_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(blank=True, help_text='Subject/topic of the question', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default='MCQ', help_text='MCQ, Descriptive, etc', max_length=64),
        ),
        migrations.AddField(
            model_name='question',
            name='generated_by',
            field=models.CharField(blank=True, help_text="set to 'ai' for auto-generated questions", max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RunPython(generate_default_topic, reverse_code=migrations.RunPython.noop),
    ]
