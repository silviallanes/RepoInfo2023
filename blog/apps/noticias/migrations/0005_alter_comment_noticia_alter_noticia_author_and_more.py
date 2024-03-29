# Generated by Django 4.2.3 on 2023-07-16 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticias', '0004_alter_comment_noticia_alter_noticia_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='noticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='noticias.noticia'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='categoria_noticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.categoria'),
        ),
    ]
