# Generated by Django 5.1.1 on 2024-11-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyRecommend',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256, verbose_name='노래 제목')),
                ('link', models.URLField(max_length=256, verbose_name='노래 주소')),
                ('cover_image', models.URLField(max_length=256, verbose_name='커버 이미지 링크')),
            ],
            options={
                'verbose_name': '스포티파이 추천 노래',
                'verbose_name_plural': '스포티파이 추천 노래 목록',
                'db_table': 'spotify_recommend',
            },
        ),
    ]
