# Generated by Django 2.2.10 on 2020-07-04 17:09

from django.db import migrations, models
import django.db.models.deletion
import update_request.constants


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enviroinment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugTrackerTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=128)),
                ('ticket_number', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UpdateRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=128)),
                ('branch_name', models.CharField(max_length=128)),
                ('status', models.IntegerField(choices=[(update_request.constants.EnumUpdateRequestStatus(1), 'Pendente'), (update_request.constants.EnumUpdateRequestStatus(2), 'Cancelado'), (update_request.constants.EnumUpdateRequestStatus(3), 'Finalizado')], default=update_request.constants.EnumUpdateRequestStatus(1))),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enviroinment.Project')),
                ('tickets', models.ManyToManyField(to='update_request.BugTrackerTicket')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
