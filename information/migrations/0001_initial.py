# Generated by Django 5.2 on 2025-04-02 14:26

import django.core.validators
import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dissertatsiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muallif(hammualliflar)')),
                ('institution_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muassasa Nomi(kafedra)')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kalit So'zlar")),
                ('publication_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nashr turi')),
                ('publication_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nashr Yili')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name="Ilm-fan yo'nalishi")),
                ('content_type', tinymce.models.HTMLField(blank=True, db_index=True, null=True, verbose_name='Anotatsiya')),
                ('degree', models.CharField(blank=True, choices=[('LEVEL1', 'Maxfiy'), ('LEVEL2', 'Nomaxfiy'), ('LEVEL3', 'XDFU')], max_length=6, null=True, verbose_name='Daraja')),
                ('issn_isbn', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{4}|\\d{9}[\\d|X]$', "ISSN yoki ISBN noto'g'ri formatda")], verbose_name='ISSN/ISBN')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan Vaqt")),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Dissertatsiya',
                'verbose_name_plural': 'Dissertatsiyalar',
            },
        ),
        migrations.CreateModel(
            name='Jurnal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muallif(hammualliflar)')),
                ('institution_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muassasa Nomi(kafedra)')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kalit So'zlar")),
                ('publication_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nashr turi')),
                ('publication_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nashr Yili')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name="Ilm-fan yo'nalishi")),
                ('content_type', tinymce.models.HTMLField(blank=True, db_index=True, null=True, verbose_name='Anotatsiya')),
                ('degree', models.CharField(blank=True, choices=[('LEVEL1', 'Maxfiy'), ('LEVEL2', 'Nomaxfiy'), ('LEVEL3', 'XDFU')], max_length=6, null=True, verbose_name='Daraja')),
                ('issn_isbn', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{4}|\\d{9}[\\d|X]$', "ISSN yoki ISBN noto'g'ri formatda")], verbose_name='ISSN/ISBN')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan Vaqt")),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Jurnal',
                'verbose_name_plural': 'Jurnallar',
            },
        ),
        migrations.CreateModel(
            name='Loyiha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muallif(hammualliflar)')),
                ('institution_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muassasa Nomi(kafedra)')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kalit So'zlar")),
                ('publication_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nashr turi')),
                ('publication_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nashr Yili')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name="Ilm-fan yo'nalishi")),
                ('content_type', tinymce.models.HTMLField(blank=True, db_index=True, null=True, verbose_name='Anotatsiya')),
                ('degree', models.CharField(blank=True, choices=[('LEVEL1', 'Maxfiy'), ('LEVEL2', 'Nomaxfiy'), ('LEVEL3', 'XDFU')], max_length=6, null=True, verbose_name='Daraja')),
                ('issn_isbn', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{4}|\\d{9}[\\d|X]$', "ISSN yoki ISBN noto'g'ri formatda")], verbose_name='ISSN/ISBN')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan Vaqt")),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Loyiha',
                'verbose_name_plural': 'Loyihalar',
            },
        ),
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muallif(hammualliflar)')),
                ('institution_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muassasa Nomi(kafedra)')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kalit So'zlar")),
                ('publication_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nashr turi')),
                ('publication_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nashr Yili')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name="Ilm-fan yo'nalishi")),
                ('content_type', tinymce.models.HTMLField(blank=True, db_index=True, null=True, verbose_name='Anotatsiya')),
                ('degree', models.CharField(blank=True, choices=[('LEVEL1', 'Maxfiy'), ('LEVEL2', 'Nomaxfiy'), ('LEVEL3', 'XDFU')], max_length=6, null=True, verbose_name='Daraja')),
                ('issn_isbn', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{4}|\\d{9}[\\d|X]$', "ISSN yoki ISBN noto'g'ri formatda")], verbose_name='ISSN/ISBN')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan Vaqt")),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Hisobot',
                'verbose_name_plural': 'Hisobotlar',
            },
        ),
        migrations.CreateModel(
            name='Monografiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muallif(hammualliflar)')),
                ('institution_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muassasa Nomi(kafedra)')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kalit So'zlar")),
                ('publication_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nashr turi')),
                ('publication_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nashr Yili')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name="Ilm-fan yo'nalishi")),
                ('content_type', tinymce.models.HTMLField(blank=True, db_index=True, null=True, verbose_name='Anotatsiya')),
                ('degree', models.CharField(blank=True, choices=[('LEVEL1', 'Maxfiy'), ('LEVEL2', 'Nomaxfiy'), ('LEVEL3', 'XDFU')], max_length=6, null=True, verbose_name='Daraja')),
                ('issn_isbn', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{4}|\\d{9}[\\d|X]$', "ISSN yoki ISBN noto'g'ri formatda")], verbose_name='ISSN/ISBN')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan Vaqt")),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Monografiya',
                'verbose_name_plural': 'Monografiyalar',
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muallif(hammualliflar)')),
                ('institution_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muassasa Nomi(kafedra)')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kalit So'zlar")),
                ('publication_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nashr turi')),
                ('publication_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nashr Yili')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name="Ilm-fan yo'nalishi")),
                ('content_type', tinymce.models.HTMLField(blank=True, db_index=True, null=True, verbose_name='Anotatsiya')),
                ('degree', models.CharField(blank=True, choices=[('LEVEL1', 'Maxfiy'), ('LEVEL2', 'Nomaxfiy'), ('LEVEL3', 'XDFU')], max_length=6, null=True, verbose_name='Daraja')),
                ('issn_isbn', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{4}|\\d{9}[\\d|X]$', "ISSN yoki ISBN noto'g'ri formatda")], verbose_name='ISSN/ISBN')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan Vaqt")),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Boshqalar',
                'verbose_name_plural': 'Boshqalar',
            },
        ),
        migrations.CreateModel(
            name='Qollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muallif(hammualliflar)')),
                ('institution_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muassasa Nomi(kafedra)')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kalit So'zlar")),
                ('publication_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nashr turi')),
                ('publication_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nashr Yili')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name="Ilm-fan yo'nalishi")),
                ('content_type', tinymce.models.HTMLField(blank=True, db_index=True, null=True, verbose_name='Anotatsiya')),
                ('degree', models.CharField(blank=True, choices=[('LEVEL1', 'Maxfiy'), ('LEVEL2', 'Nomaxfiy'), ('LEVEL3', 'XDFU')], max_length=6, null=True, verbose_name='Daraja')),
                ('issn_isbn', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{4}|\\d{9}[\\d|X]$', "ISSN yoki ISBN noto'g'ri formatda")], verbose_name='ISSN/ISBN')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan Vaqt")),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Hisobot',
                'verbose_name_plural': 'Hisobotlar',
            },
        ),
        migrations.CreateModel(
            name='Risola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muallif(hammualliflar)')),
                ('institution_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muassasa Nomi(kafedra)')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kalit So'zlar")),
                ('publication_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nashr turi')),
                ('publication_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nashr Yili')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name="Ilm-fan yo'nalishi")),
                ('content_type', tinymce.models.HTMLField(blank=True, db_index=True, null=True, verbose_name='Anotatsiya')),
                ('degree', models.CharField(blank=True, choices=[('LEVEL1', 'Maxfiy'), ('LEVEL2', 'Nomaxfiy'), ('LEVEL3', 'XDFU')], max_length=6, null=True, verbose_name='Daraja')),
                ('issn_isbn', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{4}|\\d{9}[\\d|X]$', "ISSN yoki ISBN noto'g'ri formatda")], verbose_name='ISSN/ISBN')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan Vaqt")),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Risola',
                'verbose_name_plural': 'Risolalar',
            },
        ),
        migrations.CreateModel(
            name='Xorijiy_Tajriba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('LEVEL1', 'Level 1'), ('LEVEL2', 'Level 2'), ('LEVEL3', 'Level 3')], max_length=6, verbose_name='Daraja')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Material mavzusi')),
                ('author', models.CharField(db_index=True, max_length=255, verbose_name='Mualliflar(hammualliflar)')),
                ('country', models.CharField(max_length=255, verbose_name='Mamlakat nomi')),
                ('military_organization', models.CharField(db_index=True, max_length=255, verbose_name='Harbiy tashkilot')),
                ('material', models.CharField(max_length=255, verbose_name='Material turi')),
                ('made_in', models.CharField(max_length=255, verbose_name='Ishlab chiqardan tashkilot')),
                ('anotation', models.CharField(max_length=255, verbose_name='Anotatsiya')),
                ('keys', models.CharField(max_length=255, verbose_name="Kalit so'z")),
                ('file', models.FileField(blank=True, null=True, upload_to='reports_files/', verbose_name='Xorijiy_Tajriba Fayli')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name="O'zgartirilgan Vaqt")),
            ],
        ),
        migrations.CreateModel(
            name='Darslik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muallif(hammualliflar)')),
                ('institution_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Muassasa Nomi(kafedra)')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name="Kalit So'zlar")),
                ('publication_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nashr turi')),
                ('publication_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nashr Yili')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name="Ilm-fan yo'nalishi")),
                ('content_type', tinymce.models.HTMLField(blank=True, db_index=True, null=True, verbose_name='Anotatsiya')),
                ('degree', models.CharField(blank=True, choices=[('LEVEL1', 'Maxfiy'), ('LEVEL2', 'Nomaxfiy'), ('LEVEL3', 'XDFU')], max_length=6, null=True, verbose_name='Daraja')),
                ('issn_isbn', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{4}|\\d{9}[\\d|X]$', "ISSN yoki ISBN noto'g'ri formatda")], verbose_name='ISSN/ISBN')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Yaratilgan Vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan Vaqt")),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Rasm')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Filial')),
            ],
            options={
                'verbose_name': 'Darslik',
                'verbose_name_plural': 'Darsliklar',
            },
        ),
    ]
