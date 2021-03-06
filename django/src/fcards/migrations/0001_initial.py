# Generated by Django 3.2.5 on 2021-07-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreign', models.CharField(max_length=200)),
                ('meaning', models.CharField(max_length=200)),
                ('pronunciation', models.CharField(max_length=200, null=True)),
                ('context', models.CharField(max_length=2000, null=True)),
                ('notes', models.TextField(null=True)),
                ('last_review', models.DateTimeField(null=True)),
                ('n', models.IntegerField(default=0, help_text='The repetition number n, which is the number of times the card has been\n    successfully recalled in a row since the last time it was not.', verbose_name='Repetition number')),
                ('i', models.IntegerField(default=0, help_text='The inter-repetition interval I, which is the length of time (in days)\n    SuperMemo will wait after the previous review before asking the user to review the card again.', verbose_name='Interval')),
                ('ef', models.FloatField(default=2.5, help_text='The easiness factor EF, which loosely indicates how easy the card is\n    (more precisely, it determines how quickly the inter-repetition interval grows).\n    The initial value of EF is 2.5.', verbose_name='Easiness Factor')),
            ],
            options={
                'db_table': 'card',
            },
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=2000)),
                ('cards', models.ManyToManyField(to='fcards.Card')),
            ],
            options={
                'db_table': 'deck',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('decks', models.ManyToManyField(to='fcards.Deck')),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddConstraint(
            model_name='card',
            constraint=models.UniqueConstraint(fields=('foreign', 'meaning'), name='unique_foreign_meaning'),
        ),
    ]
