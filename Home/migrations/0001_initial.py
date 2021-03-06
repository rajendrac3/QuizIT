# Generated by Django 2.0.6 on 2018-06-10 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct answer')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(max_length=50, unique=True)),
                ('exam_type', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, verbose_name='InterviewTopic')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='iquestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000, verbose_name='iquestions')),
                ('answer', models.CharField(max_length=10000, verbose_name='iquestions')),
                ('interviewtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qna', to='Home.InterviewTopic')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Question')),
                ('answer_1', models.CharField(max_length=1000)),
                ('answer_2', models.CharField(max_length=1000)),
                ('answer_3', models.CharField(max_length=1000)),
                ('answer_4', models.CharField(max_length=1000)),
                ('correct_answer', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=50, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='Home.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SubcategoriesOfTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subcategories', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='sv', max_length=100)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer_1', models.CharField(default='avd', max_length=1000)),
                ('answer_2', models.CharField(default='avdv', max_length=1000)),
                ('answer_3', models.CharField(default='avdsdc', max_length=1000)),
                ('answer_4', models.CharField(default='avdedfcfws', max_length=1000)),
                ('correct_answer', models.CharField(default='avqfed', max_length=1000)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cstx', to='Home.SubcategoriesOfTests')),
            ],
        ),
        migrations.CreateModel(
            name='Tests_Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_id', models.CharField(max_length=10)),
                ('correct_answer', models.CharField(max_length=1000)),
                ('answer_by_user', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='subcategoriesoftests',
            name='testcategories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cst', to='Home.TestCategories'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='Home.Quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='Home.Question'),
        ),
    ]
