# Generated by Django 4.2.4 on 2023-08-07 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to='Users.contributor')),
                ('contributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.contributor')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1200, null=True)),
                ('type', models.CharField(choices=[('BE', 'Back-end'), ('FE', 'Front-end'), ('IO', 'IOS'), ('AN', 'Android')], max_length=2)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_author', to='Users.anyuser')),
                ('contributors', models.ManyToManyField(blank=True, related_name='project_contributors', to='Users.contributor')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('OP', 'Open'), ('IP', 'In Progress'), ('CL', 'Closed')], max_length=2)),
                ('priority', models.CharField(choices=[('HI', 'High'), ('ME', 'Medium'), ('LO', 'Low')], max_length=2)),
                ('tag', models.CharField(choices=[('BU', 'Bug'), ('TA', 'Task'), ('IM', 'Improvement')], max_length=2)),
                ('description', models.CharField(blank=True, max_length=1200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('affected_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affected_contributor', to='Users.contributor')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to='Users.contributor')),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.comment')),
            ],
        ),
    ]
