# Generated by Django 3.0.6 on 2020-05-06 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneytransfer',
            old_name='enter_the_amount_to_be_transferred_in_KSHS',
            new_name='amount_in_kshs',
        ),
        migrations.RenameField(
            model_name='moneytransfer',
            old_name='enter_the_destination_account_number',
            new_name='recipient_account_no',
        ),
        migrations.RenameField(
            model_name='moneytransfer',
            old_name='enter_your_user_name',
            new_name='sender',
        ),
    ]
