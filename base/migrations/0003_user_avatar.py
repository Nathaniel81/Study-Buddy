from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Database migration adding the 'avatar' field to the 'User' model.
    """

    dependencies = [
        ('base', '0002_auto_20210921_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]
