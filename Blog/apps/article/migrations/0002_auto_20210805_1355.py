# Generated by Django 3.2.5 on 2021-08-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_cate',
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cate', models.CharField(max_length=100)),
                ('id_cate', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.category')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='id_sub_cate',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.subcategory'),
        ),
    ]
