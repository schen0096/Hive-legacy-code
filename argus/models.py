from django.db import models

# Create your models here.
# String Check tables
class StringCheckDeveloperNameUnification(models.Model):
    developer_1 = models.CharField(db_column='Developer 1', max_length=191, blank=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    developer_2 = models.CharField(db_column='Developer 2', max_length=191, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'string_check_developer_name_unification'
        verbose_name = "Developer Name Unification"


class StringCheckPublisherNameUnification(models.Model):
    publisher_1 = models.CharField(db_column='Publisher 1', max_length=191, blank=True,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publisher_2 = models.CharField(db_column='Publisher 2', max_length=191, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'string_check_publisher_name_unification'
        verbose_name = "Publisher Name Unification"


class StringCheckTitleCaseSensitivity(models.Model):
    segment = models.CharField(max_length=191, blank=True, primary_key=True)
    title = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'string_check_title_case_sensitivity'
        verbose_name = "Title Case Sensitivity"


class StringCheckWhitespace(models.Model):
    problem = models.CharField(max_length=255, blank=True, primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    segment = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    developer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'string_check_whitespace'
        verbose_name = "Whitespace"

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
        verbose_name = "Market Level"


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
        verbose_name = "Market Level Genre"


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
        verbose_name = "Market Level Platform"


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
        verbose_name = "Title Level"

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
        verbose_name = "Market Level"


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
        verbose_name = "Market Level Genre"


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
        verbose_name = "Market Level Platform"


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
        verbose_name = "Title Level"


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
        verbose_name = "Conversion Ingame"


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
        verbose_name = "Conversion Micro"


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
        verbose_name = "MAU vs Lifetime Downloads Excess"


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
        verbose_name = "In-Game Spending"


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
        verbose_name = "F2P Console MAU"


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
        verbose_name = "F2P Console Revenue"


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
        verbose_name = "F2P PC MAU"


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
        verbose_name = "F2P PC Revenue"


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
        verbose_name = "Mobile MAU"


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
        verbose_name = "Mobile Revenue"


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
        verbose_name = "P2P PC MAU"


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
        verbose_name = "P2P PC Revenue"


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
        verbose_name = "Premium Console MAU"


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
        verbose_name = "Premium Console Revenue"


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
        verbose_name = "Premium PC MAU"


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
        verbose_name = "Premium PC Revenue"


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
        verbose_name = "F2P Console MAU"


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
        verbose_name = "F2P Console Revenue"


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
        verbose_name = "F2P PC MAU"


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
        verbose_name = "F2P PC Revenue"


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
        verbose_name = "F2P Console MAU"


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
        verbose_name = "F2P Console Revenue"


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
        verbose_name = "F2P PC MAU"


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
        verbose_name = "F2P PC Revenue"


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
        verbose_name = "P2P PC MAU"


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
        verbose_name = "P2P PC Revenue"


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
        verbose_name = "Premium Console MAU"


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
        verbose_name = "Premium Console Revenue"


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
        verbose_name = "Title Level"


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
        verbose_name = "Market Level"


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
        verbose_name = "Market Level Genre"


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
        verbose_name = "Market Level Platform"


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
        verbose_name = "Title Level"


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
        verbose_name = "Title Level"


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
        verbose_name = "Market Level"


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
        verbose_name = "Market Level Genre"


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
        verbose_name = "Market Level Platform"
