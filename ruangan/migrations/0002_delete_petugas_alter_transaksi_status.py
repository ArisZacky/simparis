# Generated by Django 4.2.9 on 2024-01-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruangan', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Petugas',
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='status',
            field=models.CharField(choices=[('prs', 'proses'), ('lns', 'lunas'), ('btl', 'batal')], max_length=10),
        ),
    ]
