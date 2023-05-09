# Generated by Django 4.2 on 2023-05-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_img', models.ImageField(upload_to='sliderimg/')),
                ('cms_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('cms_text', models.CharField(max_length=200, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
