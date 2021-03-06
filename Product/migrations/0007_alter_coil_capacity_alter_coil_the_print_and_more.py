# Generated by Django 4.0 on 2022-01-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_alter_coil_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coil',
            name='capacity',
            field=models.CharField(blank=True, choices=[(None, '---------'), ('MINI', 'Mini'), ('SMALL', 'Petit Modèle'), ('MEDIUM', 'Moyen Modèle'), ('BIG', 'Grand Modèle'), ('GGM', 'Grand Modèle +')], max_length=255, null=True, verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='coil',
            name='the_print',
            field=models.CharField(blank=True, choices=[('MANTOUDJ_BLADI', 'Mantoudj Bladi'), ('BEST_MARKET', 'Best Market'), ('SUPERETTE', 'Superette'), ('SUPER_MARKET', 'Super Market'), ('LIKE', 'Like'), ('Q&P', 'Qualité/Prix'), ('THANKS', 'Thanks'), ('BEST_OF_SHOPPING', 'Best Of Shopping'), ('BIG_SHOP', 'Big Shop'), ('THANK_YOU', 'Thank You'), ('FAMILY_STORE', 'Family Store'), ('TASSAOUK_AL_AFDAL', 'Tassaouk Al Afdal'), ('FRUITS_ET_LEGUMES', 'Fruits Et Légumes'), ('SHOP_EXPRESS', 'Shop Express'), ('SHOPPING', 'Shopping'), ('FAST_FOOD', 'Fast Food'), ('SURPRISE', 'Surprise'), ('FRED_PERRY', 'Fred Perry'), ('I_LOVE_SHOPPING', 'I Love Shopping'), ('TOMMY_HILFIGER', 'Tommy Hilfiger'), ('HACKETT', 'Hackett'), ('PHARMACIE', 'Pharmacie'), ('PIZZA', 'Pizza'), ('BOUCHERIE', 'Boucherie'), ('WELCOME', 'Welcome'), ('CUSTOM', 'Personnalisé'), (None, '--------')], max_length=250, null=True, verbose_name='Impression'),
        ),
        migrations.AlterField(
            model_name='coiltype',
            name='capacity',
            field=models.CharField(blank=True, choices=[(None, '---------'), ('MINI', 'Mini'), ('SMALL', 'Petit Modèle'), ('MEDIUM', 'Moyen Modèle'), ('BIG', 'Grand Modèle'), ('GGM', 'Grand Modèle +')], max_length=255, null=True, verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='coiltype',
            name='the_print',
            field=models.CharField(blank=True, choices=[('MANTOUDJ_BLADI', 'Mantoudj Bladi'), ('BEST_MARKET', 'Best Market'), ('SUPERETTE', 'Superette'), ('SUPER_MARKET', 'Super Market'), ('LIKE', 'Like'), ('Q&P', 'Qualité/Prix'), ('THANKS', 'Thanks'), ('BEST_OF_SHOPPING', 'Best Of Shopping'), ('BIG_SHOP', 'Big Shop'), ('THANK_YOU', 'Thank You'), ('FAMILY_STORE', 'Family Store'), ('TASSAOUK_AL_AFDAL', 'Tassaouk Al Afdal'), ('FRUITS_ET_LEGUMES', 'Fruits Et Légumes'), ('SHOP_EXPRESS', 'Shop Express'), ('SHOPPING', 'Shopping'), ('FAST_FOOD', 'Fast Food'), ('SURPRISE', 'Surprise'), ('FRED_PERRY', 'Fred Perry'), ('I_LOVE_SHOPPING', 'I Love Shopping'), ('TOMMY_HILFIGER', 'Tommy Hilfiger'), ('HACKETT', 'Hackett'), ('PHARMACIE', 'Pharmacie'), ('PIZZA', 'Pizza'), ('BOUCHERIE', 'Boucherie'), ('WELCOME', 'Welcome'), ('CUSTOM', 'Personnalisé'), (None, '--------')], max_length=250, null=True, verbose_name='Impression'),
        ),
        migrations.AlterField(
            model_name='combinedrange',
            name='the_print',
            field=models.CharField(blank=True, choices=[('MANTOUDJ_BLADI', 'Mantoudj Bladi'), ('BEST_MARKET', 'Best Market'), ('SUPERETTE', 'Superette'), ('SUPER_MARKET', 'Super Market'), ('LIKE', 'Like'), ('Q&P', 'Qualité/Prix'), ('THANKS', 'Thanks'), ('BEST_OF_SHOPPING', 'Best Of Shopping'), ('BIG_SHOP', 'Big Shop'), ('THANK_YOU', 'Thank You'), ('FAMILY_STORE', 'Family Store'), ('TASSAOUK_AL_AFDAL', 'Tassaouk Al Afdal'), ('FRUITS_ET_LEGUMES', 'Fruits Et Légumes'), ('SHOP_EXPRESS', 'Shop Express'), ('SHOPPING', 'Shopping'), ('FAST_FOOD', 'Fast Food'), ('SURPRISE', 'Surprise'), ('FRED_PERRY', 'Fred Perry'), ('I_LOVE_SHOPPING', 'I Love Shopping'), ('TOMMY_HILFIGER', 'Tommy Hilfiger'), ('HACKETT', 'Hackett'), ('PHARMACIE', 'Pharmacie'), ('PIZZA', 'Pizza'), ('BOUCHERIE', 'Boucherie'), ('WELCOME', 'Welcome'), ('CUSTOM', 'Personnalisé'), (None, '--------')], max_length=250, null=True, verbose_name='Impression'),
        ),
        migrations.AlterField(
            model_name='finishedproduct',
            name='capacity',
            field=models.CharField(blank=True, choices=[(None, '---------'), ('MINI', 'Mini'), ('SMALL', 'Petit Modèle'), ('MEDIUM', 'Moyen Modèle'), ('BIG', 'Grand Modèle'), ('GGM', 'Grand Modèle +')], max_length=255, null=True, verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='finishedproduct',
            name='the_print',
            field=models.CharField(blank=True, choices=[('MANTOUDJ_BLADI', 'Mantoudj Bladi'), ('BEST_MARKET', 'Best Market'), ('SUPERETTE', 'Superette'), ('SUPER_MARKET', 'Super Market'), ('LIKE', 'Like'), ('Q&P', 'Qualité/Prix'), ('THANKS', 'Thanks'), ('BEST_OF_SHOPPING', 'Best Of Shopping'), ('BIG_SHOP', 'Big Shop'), ('THANK_YOU', 'Thank You'), ('FAMILY_STORE', 'Family Store'), ('TASSAOUK_AL_AFDAL', 'Tassaouk Al Afdal'), ('FRUITS_ET_LEGUMES', 'Fruits Et Légumes'), ('SHOP_EXPRESS', 'Shop Express'), ('SHOPPING', 'Shopping'), ('FAST_FOOD', 'Fast Food'), ('SURPRISE', 'Surprise'), ('FRED_PERRY', 'Fred Perry'), ('I_LOVE_SHOPPING', 'I Love Shopping'), ('TOMMY_HILFIGER', 'Tommy Hilfiger'), ('HACKETT', 'Hackett'), ('PHARMACIE', 'Pharmacie'), ('PIZZA', 'Pizza'), ('BOUCHERIE', 'Boucherie'), ('WELCOME', 'Welcome'), ('CUSTOM', 'Personnalisé'), (None, '--------')], max_length=250, null=True, verbose_name='Impression'),
        ),
        migrations.AlterField(
            model_name='finishedproducttype',
            name='capacity',
            field=models.CharField(blank=True, choices=[(None, '---------'), ('MINI', 'Mini'), ('SMALL', 'Petit Modèle'), ('MEDIUM', 'Moyen Modèle'), ('BIG', 'Grand Modèle'), ('GGM', 'Grand Modèle +')], max_length=255, null=True, verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='finishedproducttype',
            name='the_print',
            field=models.CharField(blank=True, choices=[('MANTOUDJ_BLADI', 'Mantoudj Bladi'), ('BEST_MARKET', 'Best Market'), ('SUPERETTE', 'Superette'), ('SUPER_MARKET', 'Super Market'), ('LIKE', 'Like'), ('Q&P', 'Qualité/Prix'), ('THANKS', 'Thanks'), ('BEST_OF_SHOPPING', 'Best Of Shopping'), ('BIG_SHOP', 'Big Shop'), ('THANK_YOU', 'Thank You'), ('FAMILY_STORE', 'Family Store'), ('TASSAOUK_AL_AFDAL', 'Tassaouk Al Afdal'), ('FRUITS_ET_LEGUMES', 'Fruits Et Légumes'), ('SHOP_EXPRESS', 'Shop Express'), ('SHOPPING', 'Shopping'), ('FAST_FOOD', 'Fast Food'), ('SURPRISE', 'Surprise'), ('FRED_PERRY', 'Fred Perry'), ('I_LOVE_SHOPPING', 'I Love Shopping'), ('TOMMY_HILFIGER', 'Tommy Hilfiger'), ('HACKETT', 'Hackett'), ('PHARMACIE', 'Pharmacie'), ('PIZZA', 'Pizza'), ('BOUCHERIE', 'Boucherie'), ('WELCOME', 'Welcome'), ('CUSTOM', 'Personnalisé'), (None, '--------')], max_length=250, null=True, verbose_name='Impression'),
        ),
        migrations.AlterField(
            model_name='labelling',
            name='capacity',
            field=models.CharField(blank=True, choices=[(None, '---------'), ('MINI', 'Mini'), ('SMALL', 'Petit Modèle'), ('MEDIUM', 'Moyen Modèle'), ('BIG', 'Grand Modèle'), ('GGM', 'Grand Modèle +')], max_length=255, null=True, verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='labelling',
            name='the_print',
            field=models.CharField(blank=True, choices=[('MANTOUDJ_BLADI', 'Mantoudj Bladi'), ('BEST_MARKET', 'Best Market'), ('SUPERETTE', 'Superette'), ('SUPER_MARKET', 'Super Market'), ('LIKE', 'Like'), ('Q&P', 'Qualité/Prix'), ('THANKS', 'Thanks'), ('BEST_OF_SHOPPING', 'Best Of Shopping'), ('BIG_SHOP', 'Big Shop'), ('THANK_YOU', 'Thank You'), ('FAMILY_STORE', 'Family Store'), ('TASSAOUK_AL_AFDAL', 'Tassaouk Al Afdal'), ('FRUITS_ET_LEGUMES', 'Fruits Et Légumes'), ('SHOP_EXPRESS', 'Shop Express'), ('SHOPPING', 'Shopping'), ('FAST_FOOD', 'Fast Food'), ('SURPRISE', 'Surprise'), ('FRED_PERRY', 'Fred Perry'), ('I_LOVE_SHOPPING', 'I Love Shopping'), ('TOMMY_HILFIGER', 'Tommy Hilfiger'), ('HACKETT', 'Hackett'), ('PHARMACIE', 'Pharmacie'), ('PIZZA', 'Pizza'), ('BOUCHERIE', 'Boucherie'), ('WELCOME', 'Welcome'), ('CUSTOM', 'Personnalisé'), (None, '--------')], max_length=250, null=True, verbose_name='Impression'),
        ),
        migrations.AlterField(
            model_name='package',
            name='capacity',
            field=models.CharField(blank=True, choices=[(None, '---------'), ('MINI', 'Mini'), ('SMALL', 'Petit Modèle'), ('MEDIUM', 'Moyen Modèle'), ('BIG', 'Grand Modèle'), ('GGM', 'Grand Modèle +')], max_length=255, null=True, verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='package',
            name='the_print',
            field=models.CharField(blank=True, choices=[('MANTOUDJ_BLADI', 'Mantoudj Bladi'), ('BEST_MARKET', 'Best Market'), ('SUPERETTE', 'Superette'), ('SUPER_MARKET', 'Super Market'), ('LIKE', 'Like'), ('Q&P', 'Qualité/Prix'), ('THANKS', 'Thanks'), ('BEST_OF_SHOPPING', 'Best Of Shopping'), ('BIG_SHOP', 'Big Shop'), ('THANK_YOU', 'Thank You'), ('FAMILY_STORE', 'Family Store'), ('TASSAOUK_AL_AFDAL', 'Tassaouk Al Afdal'), ('FRUITS_ET_LEGUMES', 'Fruits Et Légumes'), ('SHOP_EXPRESS', 'Shop Express'), ('SHOPPING', 'Shopping'), ('FAST_FOOD', 'Fast Food'), ('SURPRISE', 'Surprise'), ('FRED_PERRY', 'Fred Perry'), ('I_LOVE_SHOPPING', 'I Love Shopping'), ('TOMMY_HILFIGER', 'Tommy Hilfiger'), ('HACKETT', 'Hackett'), ('PHARMACIE', 'Pharmacie'), ('PIZZA', 'Pizza'), ('BOUCHERIE', 'Boucherie'), ('WELCOME', 'Welcome'), ('CUSTOM', 'Personnalisé'), (None, '--------')], max_length=250, null=True, verbose_name='Impression'),
        ),
    ]
