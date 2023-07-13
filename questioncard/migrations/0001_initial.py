# Generated by Django 3.2.19 on 2023-07-08 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deck', '0002_alter_deck_deck_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=300, verbose_name='問題文')),
                ('correct_answer', models.CharField(max_length=300, verbose_name='正解')),
                ('order', models.IntegerField(verbose_name='出題順')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='作成時間')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='更新時間')),
                ('in_deck', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='in_deck', to='deck.deck', verbose_name='デッキ')),
            ],
            options={
                'verbose_name': '問題カード',
                'verbose_name_plural': '問題カード',
            },
        ),
    ]