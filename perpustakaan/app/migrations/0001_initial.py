# Generated by Django 4.2.10 on 2024-02-21 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('penulis', models.CharField(max_length=255)),
                ('penerbit', models.CharField(max_length=255)),
                ('tahun_terbit', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ulasan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulasan', models.TextField()),
                ('rating', models.IntegerField(max_length=11)),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.buku')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pinjam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_peminjaman', models.DateField(auto_now_add=True)),
                ('tanggal_pengembalian', models.DateField()),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.buku')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Koleksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.buku')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori_Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.buku')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kategori')),
            ],
        ),
    ]
