# Generated by Django 3.0.7 on 2020-07-02 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zper_api', '0003_auto_20200701_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('ticker', models.CharField(default='ZEC', max_length=4, primary_key=True, serialize=False)),
                ('last_block', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
