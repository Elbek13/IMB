# Generated by Django 5.2 on 2025-04-02 14:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
        ('information', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='darslik',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='dissertatsiya',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Filial'),
        ),
        migrations.AddField(
            model_name='dissertatsiya',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Filial'),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='loyiha',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Filial'),
        ),
        migrations.AddField(
            model_name='loyiha',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='maqola',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Filial'),
        ),
        migrations.AddField(
            model_name='maqola',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='monografiya',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Filial'),
        ),
        migrations.AddField(
            model_name='monografiya',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='other',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Filial'),
        ),
        migrations.AddField(
            model_name='other',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='qollanma',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Filial'),
        ),
        migrations.AddField(
            model_name='qollanma',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='risola',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Filial'),
        ),
        migrations.AddField(
            model_name='risola',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddIndex(
            model_name='xorijiy_tajriba',
            index=models.Index(fields=['title', 'author', 'military_organization'], name='information_title_24ce0a_idx'),
        ),
    ]
