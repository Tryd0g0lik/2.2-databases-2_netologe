<<<<<<< HEAD
# Generated by Django 4.1.2 on 2022-10-06 09:27
=======
# Generated by Django 4.1.2 on 2022-10-06 09:18
>>>>>>> v-2

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('subject', models.CharField(max_length=10, verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('group', models.CharField(max_length=10, verbose_name='Класс')),
<<<<<<< HEAD
                ('teacher', models.ManyToManyField(to='school.teacher', verbose_name='Студент')),
=======
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher')),
>>>>>>> v-2
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
    ]
