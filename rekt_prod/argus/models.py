from django.db import models

# Create your models here.
# String Check tables
class StringCheckDeveloperNameUnification(models.Model):
    developer_1 = models.CharField(db_column='Developer 1', max_length=191, blank=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    developer_2 = models.CharField(db_column='Developer 2', max_length=191, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'string_check_developer_name_unification'

class StringCheckPublisherNameUnification(models.Model):
    publisher_1 = models.CharField(db_column='Publisher 1', max_length=191, blank=True,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publisher_2 = models.CharField(db_column='Publisher 2', max_length=191, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'string_check_publisher_name_unification'

class StringCheckTitleCaseSensitivity(models.Model):
    segment = models.CharField(max_length=191, blank=True, primary_key=True)
    title = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'string_check_title_case_sensitivity'

class StringCheckWhitespace(models.Model):
    problem = models.CharField(max_length=255, blank=True, primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    developer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'string_check_whitespace'

# Duplicate Check tables
class DuplicateRowCheckMarketLevel(models.Model):
    segment = models.CharField(max_length=255, blank=True, primary_key=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    row_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'duplicate_row_check_market_level'

class DuplicateRowCheckMarketLevelGenre(models.Model):
    segment = models.CharField(max_length=255, blank=True, primary_key=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    row_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'duplicate_row_check_market_level_genre'

class DuplicateRowCheckMarketLevelPlatform(models.Model):
    segment = models.CharField(max_length=255, blank=True, primary_key=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    row_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'duplicate_row_check_market_level_platform'

class DuplicateRowCheckTitleLevel(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    row_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'duplicate_row_check_title_level'

# Negative Check tables

class NegativeCheckMarketLevel(models.Model):
    metric = models.CharField(max_length=255, blank=True, primary_key=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'negative_check_market_level'


class NegativeCheckMarketLevelGenre(models.Model):
    metric = models.CharField(max_length=255, blank=True, primary_key=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'negative_check_market_level_genre'


class NegativeCheckMarketLevelPlatform(models.Model):
    metric = models.CharField(max_length=255, blank=True, primary_key=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'negative_check_market_level_platform'

class NegativeCheckTitleLevel(models.Model):
    metric = models.CharField(max_length=255, blank=True, primary_key=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'negative_check_title_level'

class TitleLevelConversionIngame(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_in_game_spending_conversion = models.FloatField(db_column='Worldwide In-Game Spending Conversion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_in_game_spending_conversion = models.FloatField(db_column='Regions In-Game Spending Conversion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    in_game_spending_conversion_difference_percentage = models.FloatField(db_column='In-Game Spending Conversion Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_conversion_ingame'

class TitleLevelConversionMicro(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_micro_conversion = models.FloatField(db_column='Worldwide Micro Conversion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_micro_conversion = models.FloatField(db_column='Regions Micro Conversion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    micro_conversion_difference_percentage = models.FloatField(db_column='Micro Conversion Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_conversion_micro'


class TitleLevelMauVsLifetimeDownloadsExcess(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    mau = models.BigIntegerField(db_column='MAU', blank=True, null=True)  # Field name made lowercase.
    downloads_ltd = models.DecimalField(db_column='downloads_LTD', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mau_over_lifetime_downloads_percentage = models.DecimalField(db_column='Mau Over Lifetime Downloads Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_mau_vs_lifetime_downloads_excess'

class TitleLevelPlatformVsSubplatformF2PConsoleMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_mau = models.BigIntegerField(db_column='All Platforms MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_mau = models.DecimalField(db_column='Subplatform MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_f2p_console_mau'

class TitleLevelPlatformVsSubplatformF2PConsoleRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_revenue = models.FloatField(db_column='All Platforms Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_revenue = models.FloatField(db_column='Subplatform Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_f2p_console_revenue'

class TitleLevelPlatformVsSubplatformF2PPcMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_mau = models.BigIntegerField(db_column='All Platforms MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_mau = models.DecimalField(db_column='Subplatform MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_f2p_pc_mau'

class TitleLevelPlatformVsSubplatformF2PPcRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_revenue = models.FloatField(db_column='All Platforms Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_revenue = models.FloatField(db_column='Subplatform Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_f2p_pc_revenue'


class TitleLevelPlatformVsSubplatformMobileMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_mau = models.BigIntegerField(db_column='All Platforms MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_mau = models.DecimalField(db_column='Subplatform MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_mobile_mau'

class TitleLevelPlatformVsSubplatformMobileRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_revenue = models.FloatField(db_column='All Platforms Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_revenue = models.FloatField(db_column='Subplatform Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_mobile_revenue'

class TitleLevelPlatformVsSubplatformP2PPcMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_mau = models.BigIntegerField(db_column='All Platforms MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_mau = models.DecimalField(db_column='Subplatform MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_p2p_pc_mau'


class TitleLevelPlatformVsSubplatformP2PPcRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_revenue = models.FloatField(db_column='All Platforms Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_revenue = models.FloatField(db_column='Subplatform Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_p2p_pc_revenue'

class TitleLevelPlatformVsSubplatformPremiumConsoleMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_mau = models.BigIntegerField(db_column='All Platforms MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_mau = models.DecimalField(db_column='Subplatform MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_premium_console_mau'

class TitleLevelPlatformVsSubplatformPremiumConsoleRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_revenue = models.FloatField(db_column='All Platforms Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_revenue = models.FloatField(db_column='Subplatform Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_premium_console_revenue'

class TitleLevelPlatformVsSubplatformPremiumPcMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_mau = models.BigIntegerField(db_column='All Platforms MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_mau = models.DecimalField(db_column='Subplatform MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_premium_pc_mau'

class TitleLevelPlatformVsSubplatformPremiumPcRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    all_platforms_revenue = models.FloatField(db_column='All Platforms Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subplatform_revenue = models.FloatField(db_column='Subplatform Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_platform_vs_subplatform_premium_pc_revenue'


class TitleLevelRegionVsSubregionF2PConsoleMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    total_region_mau = models.IntegerField(db_column='Total Region MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_region_mau = models.IntegerField(db_column='Sub Region MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_region_vs_subregion_f2p_console_mau'

class TitleLevelRegionVsSubregionF2PConsoleRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    total_region_revenue = models.FloatField(db_column='Total Region Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_region_revenue = models.FloatField(db_column='Sub Region Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_region_vs_subregion_f2p_console_revenue'

class TitleLevelRegionVsSubregionF2PPcMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    total_region_mau = models.IntegerField(db_column='Total Region MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_region_mau = models.IntegerField(db_column='Sub Region MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_region_vs_subregion_f2p_pc_mau'

class TitleLevelRegionVsSubregionF2PPcRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    total_region_revenue = models.FloatField(db_column='Total Region Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_region_revenue = models.FloatField(db_column='Sub Region Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_region_vs_subregion_f2p_pc_revenue'

class TitleLevelWwVsRegionsF2PConsoleMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_mau = models.BigIntegerField(db_column='Worldwide MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_mau = models.DecimalField(db_column='Regions MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_ww_vs_regions_f2p_console_mau'

class TitleLevelWwVsRegionsF2PConsoleRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_revenue = models.FloatField(db_column='Worldwide Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_revenue = models.FloatField(db_column='Regions Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_ww_vs_regions_f2p_console_revenue'


class TitleLevelWwVsRegionsF2PPcMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_mau = models.BigIntegerField(db_column='Worldwide MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_mau = models.DecimalField(db_column='Regions MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_ww_vs_regions_f2p_pc_mau'

class TitleLevelWwVsRegionsF2PPcRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_revenue = models.FloatField(db_column='Worldwide Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_revenue = models.FloatField(db_column='Regions Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_ww_vs_regions_f2p_pc_revenue'

class TitleLevelWwVsRegionsP2PPcMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_mau = models.BigIntegerField(db_column='Worldwide MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_mau = models.DecimalField(db_column='Regions MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_ww_vs_regions_p2p_pc_mau'

class TitleLevelWwVsRegionsP2PPcRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_revenue = models.FloatField(db_column='Worldwide Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_revenue = models.FloatField(db_column='Regions Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_ww_vs_regions_p2p_pc_revenue'

class TitleLevelWwVsRegionsPremiumConsoleMau(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_mau = models.BigIntegerField(db_column='Worldwide MAU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_mau = models.DecimalField(db_column='Regions MAU', max_digits=41, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mau_difference_percentage = models.DecimalField(db_column='MAU Difference Percentage', max_digits=50, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_ww_vs_regions_premium_console_mau'


class TitleLevelWwVsRegionsPremiumConsoleRevenue(models.Model):
    title = models.CharField(max_length=191, blank=True, primary_key=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    worldwide_revenue = models.FloatField(db_column='Worldwide Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regions_revenue = models.FloatField(db_column='Regions Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_ww_vs_regions_premium_console_revenue'


class HighConversionRateMarketLevel(models.Model):
    metric = models.CharField(max_length=255, blank=True, null=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'high_conversion_rate_market_level'

class HighConversionRateMarketLevelGenre(models.Model):
    metric = models.CharField(max_length=255, blank=True, null=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'high_conversion_rate_market_level_genre'


class HighConversionRateMarketLevelPlatform(models.Model):
    metric = models.CharField(max_length=255, blank=True, null=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'high_conversion_rate_market_level_platform'


class HighConversionRateTitleLevel(models.Model):
    metric = models.CharField(max_length=255, blank=True, null=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'high_conversion_rate_title_level'

class TitleLevelIngameRevenueAggregate(models.Model):
    title = models.CharField(max_length=191, blank=True, null=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    digital_micro_revenue = models.FloatField(blank=True, null=True)
    digital_subscription_revenue = models.FloatField(blank=True, null=True)
    digital_season_pass_revenue = models.FloatField(blank=True, null=True)
    digital_dlc_revenue = models.FloatField(blank=True, null=True)
    digital_micro_ac_revenue = models.FloatField(blank=True, null=True)
    revenue_addup = models.FloatField(blank=True, primary_key=True)
    digital_ingame_revenue = models.FloatField(blank=True, null=True)
    revenue_difference_percentage = models.FloatField(db_column='Revenue Difference Percentage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'title_level_ingame_revenue_aggregate'


class HighArpmauTitleLevel(models.Model):
    title = models.CharField(max_length=191, blank=True, null=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    arpmau = models.FloatField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'high_arpmau_title_level'

class HighIngameArppuMarketLevel(models.Model):
    segment = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    ingame_arppu = models.FloatField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'high_ingame_arppu_market_level'

class HighIngameArppuMarketLevelPlatform(models.Model):
    segment = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    ingame_arppu = models.FloatField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'high_ingame_arppu_market_level_platform'


class HighIngameArppuTitleLevel(models.Model):
    title = models.CharField(max_length=191, blank=True, null=True)
    segment = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    ingame_arppu = models.FloatField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'high_ingame_arppu_title_level'

class HighIngameArppuMarketLevelGenre(models.Model):
    segment = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    ingame_arppu = models.FloatField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'high_ingame_arppu_market_level_genre'