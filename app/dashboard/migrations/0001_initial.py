# Generated by Django 2.1.3 on 2018-12-08 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SteppsResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(max_length=1023)),
                ('freq_h', models.IntegerField(default=255)),
                ('px_h', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('freq_m', models.IntegerField(default=255)),
                ('px_m', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('freq_l', models.IntegerField(default=255)),
                ('px_l', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
