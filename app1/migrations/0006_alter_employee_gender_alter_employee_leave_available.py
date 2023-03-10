# Generated by Django 4.1.5 on 2023-03-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='leave_available',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
