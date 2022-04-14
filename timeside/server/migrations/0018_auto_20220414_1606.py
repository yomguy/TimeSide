# Generated by Django 2.2.24 on 2022-04-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeside_server', '0017_auto_20220315_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysis',
            options={'ordering': ['title'], 'verbose_name': 'Analysis', 'verbose_name_plural': 'Analyses'},
        ),
        migrations.AlterModelOptions(
            name='preset',
            options={'ordering': ['processor__pid'], 'verbose_name': 'Preset', 'verbose_name_plural': 'Presets'},
        ),
        migrations.AlterModelOptions(
            name='processor',
            options={'ordering': ['pid', '-version'], 'verbose_name': 'processor'},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'ordering': ['-date_added'], 'verbose_name': 'Result', 'verbose_name_plural': 'Results'},
        ),
        migrations.AlterModelOptions(
            name='subprocessor',
            options={'ordering': ['sub_processor_id'], 'verbose_name': 'Subprocessor'},
        ),
        migrations.AddField(
            model_name='analysistrack',
            name='color',
            field=models.CharField(blank=True, max_length=6, verbose_name='RVB color'),
        ),
    ]
