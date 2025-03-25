# Generated by Django 5.1.3 on 2025-03-01 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('passport_number', models.CharField(db_index=True, max_length=15, unique=True, verbose_name='Pasport Raqami')),
                ('password', models.CharField(max_length=255, verbose_name='Parol')),
                ('username', models.CharField(blank=True, db_index=True, max_length=20, null=True, unique=True, verbose_name='Foydalanuvchi Nomi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faolmi')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin Panelga Kirish Huquqi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan Vaqt')),
                ('role', models.CharField(choices=[('administrator', 'Administrator'), ('moderator', 'Moderator'), ('user1', 'User1'), ('user2', 'User2'), ('user3', 'User3')], default='user3', max_length=20, verbose_name='User Role')),
                ('user_status', models.CharField(choices=[('block', 'Bloklash'), ('active', 'Aktivlashtirish'), ('waiting', 'Kutib turing')], default='waiting', max_length=10, verbose_name='Foydalanuvchi Holati')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='branch.branch', verbose_name='Filial')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
