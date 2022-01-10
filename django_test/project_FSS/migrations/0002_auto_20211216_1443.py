# Generated by Django 3.2.8 on 2021-12-16 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_FSS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement', models.CharField(max_length=200)),
                ('option', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='fssbook',
            name='affiliation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project_FSS.affiliation'),
            preserve_default=False,
        ),
    ]
