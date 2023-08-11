# Generated by Django 4.2.4 on 2023-08-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocGia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_doc_gia', models.CharField(max_length=10, unique=True)),
                ('ten_doc_gia', models.CharField(max_length=200)),
                ('ngay_sinh', models.DateField()),
                ('so_dien_thoai', models.CharField(max_length=20)),
                ('ngay_tao_the', models.DateField()),
                ('ngay_het_han', models.DateField()),
                ('dia_chi', models.TextField()),
            ],
        ),
    ]
