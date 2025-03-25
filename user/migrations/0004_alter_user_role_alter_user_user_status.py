# Generated by Django 5.1.3 on 2025-03-04 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_role_alter_user_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('administrator', 'Administrator'), ('moderator', 'Moderator'), ('user1', 'User1'), ('user2', 'User2'), ('user3', 'User3')], db_index=True, default='user3', max_length=20, verbose_name='User Role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_status',
            field=models.CharField(choices=[('block', 'Bloklash'), ('active', 'Aktivlashtirish'), ('waiting', 'Kutib turing')], db_index=True, default='waiting', max_length=10, verbose_name='Foydalanuvchi Holati'),
        ),
    ]
