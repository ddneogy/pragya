# Generated by Django 3.1.5 on 2021-03-17 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_auto_20210317_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='member',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='Library.member'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(default='Available', editable=False, max_length=100),
        ),
    ]
