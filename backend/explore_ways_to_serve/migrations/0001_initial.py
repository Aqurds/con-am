# Generated by Django 2.2.28 on 2022-06-27 08:39

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerApplicationProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Title of the application process', max_length=255, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='Description of the application process', null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Career Application Process',
                'verbose_name_plural': 'Career Application Processes',
            },
        ),
        migrations.CreateModel(
            name='CareerQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.TextField(blank=True, help_text='Content of the qualification', null=True, verbose_name='Qualification')),
            ],
            options={
                'verbose_name': 'Career Qualification',
                'verbose_name_plural': 'Career Qualifications',
            },
        ),
        migrations.CreateModel(
            name='ExploreWaysToServe',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header_image_alt_text', models.CharField(blank=True, help_text='Alt text for the header image', max_length=100, null=True, verbose_name='Header Image Alt Text')),
                ('short_term_header_title', models.CharField(blank=True, help_text='Title text that will be shown in the header portion for when the user clicks the Short Term tab', max_length=255, null=True, verbose_name='Short Term Header Title')),
                ('short_term_section_title', models.CharField(blank=True, help_text='Text that will be shown below the 3 inner tabs of the short term section', max_length=255, null=True, verbose_name='Short Term Section Title')),
                ('short_term_first_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Short Term First Image', max_length=255, null=True, verbose_name='Short Term First Image Alt Text')),
                ('short_term_first_image_text', models.CharField(blank=True, help_text="Text that will be shown on the first image in the short term section. Example 'Reach the Unreached'", max_length=255, null=True, verbose_name='Short Term First Image Text')),
                ('short_term_second_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Short Term Second Image', max_length=255, null=True, verbose_name='Short Term Second Image Alt Text')),
                ('short_term_second_image_text', models.CharField(blank=True, help_text="Text that will be shown on the second image in the short term section. Example 'Refine Your Skills'", max_length=255, null=True, verbose_name='Short Term Second Image Text')),
                ('short_term_third_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Short Term Third Image', max_length=255, null=True, verbose_name='Short Term Third Image Alt Text')),
                ('short_term_third_image_text', models.CharField(blank=True, help_text="Text that will be shown on the third image in the short term section. Example 'Gain Real Experience'", max_length=255, null=True, verbose_name='Short Term Third Image Text')),
                ('short_term_first_tab_title', models.CharField(blank=True, help_text='Title text for the first tab of the short term trips', max_length=255, null=True, verbose_name='Short Term First Tab Title')),
                ('short_term_first_tab_bottom_text', models.CharField(blank=True, help_text='Text that will be shown under the first tab title', max_length=255, null=True, verbose_name='Short Term First Tab Bottom Text')),
                ('short_term_first_tab_first_section_title', models.CharField(blank=True, help_text="Title text that will be shown at the start of the page. Example 'Short-Term (Under 31 days)'", max_length=255, null=True, verbose_name='Short Term First Tab First Section Title')),
                ('short_term_first_tab_first_section_content', models.TextField(blank=True, help_text='Content text will be shown under the first section title of the page', null=True, verbose_name='Short Term First Tab First Section Content')),
                ('short_term_first_tab_qualifications_section_title', models.CharField(blank=True, help_text='Title text for the qualifications section of the page', max_length=255, null=True, verbose_name='Short Term First Tab Qualifications Section Title')),
                ('short_term_first_tab_qualifications_image_alt_text', models.CharField(blank=True, help_text='Alt text for the qualifications image', max_length=255, null=True, verbose_name='Short Term First Tab Qualifications Image Alt Text')),
                ('short_term_opportunity_section_title', models.CharField(blank=True, help_text='Text that will be shown as the title in the Opportunities section of the page', max_length=255, null=True, verbose_name='Short Term Opportunity Section Title')),
                ('first_opportunity_image_alt_text', models.CharField(blank=True, help_text='Alt text for the First Opportunity Image', max_length=255, null=True, verbose_name='First Opportunity Image Alt Text')),
                ('first_opportunity_title', models.CharField(blank=True, help_text='Title of the first opportunity', max_length=255, null=True, verbose_name='First Opportunity Title')),
                ('first_opportunity_button_url', models.TextField(blank=True, help_text='URL for the first button of the opportunities section of the page', null=True, verbose_name='First Opportunity Button URL')),
                ('first_opportunity_content', models.TextField(blank=True, help_text='Content for the first opportunity', null=True, verbose_name='First Opportunity Content')),
                ('second_opportunity_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Second Opportunity Image', max_length=255, null=True, verbose_name='Second Opportunity Image Alt Text')),
                ('second_opportunity_title', models.CharField(blank=True, help_text='Title of the second opportunity', max_length=255, null=True, verbose_name='Second Opportunity Title')),
                ('second_opportunity_content', wagtail.core.fields.RichTextField(blank=True, help_text='Content for the second opportunity', null=True, verbose_name='Second Opportunity Content')),
                ('second_opportunity_button_url', models.TextField(blank=True, help_text='URL for the second button of the opportunities section of the page', null=True, verbose_name='Second Opportunity Button URL')),
                ('last_section_title', models.CharField(blank=True, help_text="Title for the last section of the page. Example 'Invited Guests'", max_length=255, null=True, verbose_name='Last Section Title')),
                ('last_section_first_content', wagtail.core.fields.RichTextField(blank=True, help_text='Content under the last section title', null=True, verbose_name='Last Section First Content')),
                ('last_section_button_url', models.TextField(blank=True, help_text='URL for the button on the last section of the page', null=True, verbose_name='Last Section Button URL')),
                ('last_section_second_content', wagtail.core.fields.RichTextField(blank=True, help_text='Content under the button of the last section of the page', null=True, verbose_name='Last Section Second Content')),
                ('short_term_second_tab_title', models.CharField(blank=True, help_text='Title text for the second tab of the short term trips', max_length=255, null=True, verbose_name='Short Term Second Tab Title')),
                ('short_term_second_tab_bottom_text', models.CharField(blank=True, help_text='Text that will be shown under the second tab title', max_length=255, null=True, verbose_name='Short Term Second Tab Bottom Text')),
                ('short_term_second_tab_first_section_title', models.CharField(blank=True, help_text="Title text that will be shown at the start of the page. Example 'Ministers Abroad'", max_length=255, null=True, verbose_name='Short Term Second Tab First Section Title')),
                ('short_term_second_tab_first_section_content', wagtail.core.fields.RichTextField(blank=True, help_text='Content text will be shown under the title of the page', null=True, verbose_name='Short Term Second Tab First section Content')),
                ('short_term_second_tab_qualifications_section_title', models.CharField(blank=True, help_text='Title text for the qualifications section of the page', max_length=255, null=True, verbose_name='Short Term Second Tab Qualifications Section Title')),
                ('short_term_second_tab_qualifications_image_alt_text', models.CharField(blank=True, help_text='Alt text for the qualifications image', max_length=255, null=True, verbose_name='Short Term Second Tab Qualifications Image Alt Text')),
                ('short_term_second_tab_last_section_background_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Last Section Background Image', max_length=255, null=True, verbose_name='Short Term Second Tab Last Section Background Image Alt Text')),
                ('short_term_second_tab_last_section_title', models.CharField(blank=255, help_text='Title text that will be shown in the last section of the page', max_length=255, null=255, verbose_name='Short Term Second Tab Last Section Title')),
                ('short_term_second_tab_last_section_content', wagtail.core.fields.RichTextField(blank=True, help_text='Content text for the last section of the page', null=True, verbose_name='Short Term Second Tab Last Section Content')),
                ('short_term_second_tab_email', models.EmailField(blank=True, help_text='Email Address for the second tab of the page. This will be used as the email address for the button in the bottom section of the page', max_length=254, null=True, verbose_name='Short Term Second Tab Email')),
                ('short_term_third_tab_title', models.CharField(blank=True, help_text='Title text for the third tab of the short term trips', max_length=255, null=True, verbose_name='Short Term Third Tab Title')),
                ('short_term_third_tab_bottom_text', models.CharField(blank=True, help_text='Text that will be shown under the third tab title', max_length=255, null=True, verbose_name='Short Term Third Tab Bottom Text')),
                ('short_term_third_tab_first_section_title', models.CharField(blank=True, help_text="Title text that will be shown at the start of the page. Example 'Missions Abroad Placement Services (MAPS)'", max_length=255, null=True, verbose_name='Short Term Third Tab First Section Title')),
                ('short_term_third_tab_first_section_content', models.TextField(blank=True, help_text='Content text will be shown under the title of the page', null=True, verbose_name='Short Term Second Tab First Section Content')),
                ('short_term_third_tab_qualifications_section_title', models.CharField(blank=True, help_text='Title text for the qualifications section of the page', max_length=255, null=True, verbose_name='Short Term Third Tab Qualifications Section Title')),
                ('short_term_third_tab_qualifications_image_alt_text', models.CharField(blank=True, help_text='Alt text for the qualifications image', max_length=255, null=True, verbose_name='Short Term Third Tab Qualifications Image Alt Text')),
                ('short_term_third_tab_last_section_background_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Last Section Background Image', max_length=255, null=True, verbose_name='Short Term Third Tab Last Section Background Image Alt Text')),
                ('short_term_third_tab_last_section_title', models.CharField(blank=255, help_text='Title text that will be shown in the last section of the page', max_length=255, null=255, verbose_name='Short Term Third Tab Last Section Title')),
                ('short_term_third_tab_last_section_content', models.TextField(blank=True, help_text='Content text for the last section of the page', null=True, verbose_name='Short Term Third Tab Last Section Content')),
                ('short_term_third_tab_first_button_url', models.TextField(blank=True, help_text='URL for the first button', null=True, verbose_name='Short Term Third Tab First Button URL')),
                ('short_term_third_tab_second_button_url', models.TextField(blank=True, help_text='URL for the second button', null=True, verbose_name='Short Term Third Tab Second Button URL')),
                ('short_term_third_tab_third_button_url', models.TextField(blank=True, help_text='URL for the third button', null=True, verbose_name='Short Term Third Tab Third Button URL')),
                ('one_to_two_year_header_title', models.CharField(blank=True, help_text='Title text that will be shown in the header portion for when the user clicks the One to Two Year tab', max_length=255, null=True, verbose_name='One To Two Year Header Title')),
                ('one_to_two_year_header_content', models.TextField(blank=True, help_text='Text that will be shown under the header title', null=True, verbose_name='One To Two Year Header Content')),
                ('one_to_two_year_first_section_title', models.TextField(blank=True, help_text="Title of the first section of the page. Example 'Don't miss this moment etc..'", null=True, verbose_name='One To Two Year First Section Title')),
                ('one_to_two_year_first_section_content', wagtail.core.fields.RichTextField(blank=True, help_text='Content under the first section title', null=True, verbose_name='One To Two Year First Section Content')),
                ('one_to_two_year_video_thumbnail_alt_text', models.CharField(blank=True, help_text='Alt text for the video thumbnail of the 1-2 year page', max_length=255, null=True, verbose_name='One To Two Year Video Thumbnail Alt Text')),
                ('one_to_two_year_video_url', models.TextField(blank=True, help_text='URL for the featured video of the page. This needs to be the embed URL of the video or else the video player will not work', null=True, verbose_name='One To Two Year Video URL')),
                ('one_to_two_year_start_today_button_url', models.TextField(blank=True, help_text='URL for the start today button of the page', null=True, verbose_name='One To Two Year Start Today Button URL')),
                ('one_to_two_year_second_section_title', models.CharField(blank=True, help_text="Title text for the second section of the page. Example 'Missionary Associate'", max_length=255, null=True, verbose_name='One To Two Year Second Section Title')),
                ('one_to_two_year_second_section_content', wagtail.core.fields.RichTextField(blank=True, help_text='Content for the second section', null=True, verbose_name='One To Two Year Second Section Content')),
                ('one_to_two_year_image_section_first_image_alt_text', models.CharField(blank=True, help_text='Alt text for the first image in the image section', max_length=255, null=True, verbose_name='One To Two Year Image Section First Image Alt Text')),
                ('one_to_two_year_image_section_first_image_text', models.CharField(blank=True, help_text='Text that will be shown in the first image of the image section', max_length=255, null=True, verbose_name='One To Two Year Image Section First Image Text')),
                ('one_to_two_year_image_section_second_image_alt_text', models.CharField(blank=True, help_text='Alt text for the second image in the image section', max_length=255, null=True, verbose_name='One To Two Year Image Section Second Image Alt Text')),
                ('one_to_two_year_image_section_second_image_text', models.CharField(blank=True, help_text='Text that will be shown in the second image of the image section', max_length=255, null=True, verbose_name='One To Two Year Image Section Second Image Text')),
                ('one_to_two_year_image_section_third_image_alt_text', models.CharField(blank=True, help_text='Alt text for the third image in the image section', max_length=255, null=True, verbose_name='One To Two Year Image Section Third Image Alt Text')),
                ('one_to_two_year_image_section_third_image_text', models.CharField(blank=True, help_text='Text that will be shown in the third image of the image section', max_length=255, null=True, verbose_name='One To Two Year Image Section Third Image Text')),
                ('one_to_two_year_application_section_title', models.CharField(blank=True, help_text="Title text for the application section of the page. Example 'The Application Process'", max_length=255, null=True, verbose_name='One To Two Year Application Section Title')),
                ('one_to_two_year_apply_now_button_url', models.TextField(blank=True, help_text="URL for the 'Apply Now' button", null=True, verbose_name='One To Two Year Apply Now Button URL')),
                ('one_to_two_year_qualifications_section_title', models.CharField(blank=True, help_text='Title text for the qualifications section of the page', max_length=255, null=True, verbose_name='One To Two Year Qualifications Section Title')),
                ('one_to_two_year_qualifications_image_alt_text', models.CharField(blank=True, help_text='Alt text for the qualifications image', max_length=255, null=True, verbose_name='One To Two Year Qualifications Image Alt Text')),
                ('one_to_two_year_qualifications_button_url', models.TextField(blank=True, help_text='URL for the qualifications button', null=True, verbose_name='One To Two Year Qualifications Button URL')),
                ('one_to_two_year_last_section_background_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Last Section Background Image', max_length=255, null=True, verbose_name='One To Two Year Last Section Background Image Alt Text')),
                ('one_to_two_year_last_section_title', models.CharField(blank=255, help_text='Title text that will be shown in the last section of the page', max_length=255, null=255, verbose_name='One To Two Year Last Section Title')),
                ('one_to_two_year_last_section_content', models.TextField(blank=True, help_text='Content text for the last section of the page', null=True, verbose_name='One To Two Year Last Section Content')),
                ('one_to_two_year_last_section_first_button_url', models.TextField(blank=True, help_text='URL for the first button', null=True, verbose_name='One To Two Year Last Section First Button URL')),
                ('one_to_two_year_last_section_second_button_url', models.TextField(blank=True, help_text='URL for the second button', null=True, verbose_name='One To Two Year Last Section Second Button URL')),
                ('one_to_two_year_last_section_third_button_url', models.TextField(blank=True, help_text='URL for the third button', null=True, verbose_name='One To Two Year Last Section Third Button URL')),
                ('career_header_title', models.CharField(blank=True, help_text='Title text that will be shown in the header portion for when the user clicks the Career tab', max_length=255, null=True, verbose_name='Career Header Title')),
                ('career_header_content', models.TextField(blank=True, help_text='Text that will be shown under the header title', null=True, verbose_name='Career Header Content')),
                ('career_first_section_title', models.TextField(blank=True, help_text="Title of the first section of the page. Example 'Create generational transformation'", null=True, verbose_name='Career First Section Title')),
                ('career_first_section_content', wagtail.core.fields.RichTextField(blank=True, help_text='Content under the first section title', null=True, verbose_name='Career First Section Content')),
                ('career_video_thumbnail_alt_text', models.CharField(blank=True, help_text='Alt text for the video thumbnail of the Career page', max_length=255, null=True, verbose_name='Career Video Thumbnail Alt Text')),
                ('career_video_url', models.TextField(blank=True, help_text='URL for the featured video of the page. This needs to be the embed URL of the video or else the video player will not work', null=True, verbose_name='Career Video URL')),
                ('career_start_today_button_url', models.TextField(blank=True, help_text='URL for the start today button of the page', null=True, verbose_name='Career Start Today Button URL')),
                ('career_second_section_title', models.CharField(blank=True, help_text="Title text for the second section of the page. Example 'Career Missionary'", max_length=255, null=True, verbose_name='Career Second Section Title')),
                ('career_second_section_content', wagtail.core.fields.RichTextField(blank=True, help_text='Content for the second section', null=True, verbose_name='Career Second Section Content')),
                ('career_image_section_first_image_alt_text', models.CharField(blank=True, help_text='Alt text for the first image in the image section', max_length=255, null=True, verbose_name='Career Image Section First Image Alt Text')),
                ('career_image_section_first_image_text', models.CharField(blank=True, help_text='Text that will be shown in the first image of the image section', max_length=255, null=True, verbose_name='Career Image Section First Image Text')),
                ('career_image_section_second_image_alt_text', models.CharField(blank=True, help_text='Alt text for the second image in the image section', max_length=255, null=True, verbose_name='Career Image Section Second Image Alt Text')),
                ('career_image_section_second_image_text', models.CharField(blank=True, help_text='Text that will be shown in the second image of the image section', max_length=255, null=True, verbose_name='Career Image Section Second Image Text')),
                ('career_image_section_third_image_alt_text', models.CharField(blank=True, help_text='Alt text for the third image in the image section', max_length=255, null=True, verbose_name='Career Image Section Third Image Alt Text')),
                ('career_image_section_third_image_text', models.CharField(blank=True, help_text='Text that will be shown in the third image of the image section', max_length=255, null=True, verbose_name='Career Image Section Third Image Text')),
                ('career_application_section_title', models.CharField(blank=True, help_text="Title text for the application section of the page. Example 'The Application Process'", max_length=255, null=True, verbose_name='Career Application Section Title')),
                ('career_apply_now_button_url', models.TextField(blank=True, help_text="URL for the 'Apply Now' button", null=True, verbose_name='Career Apply Now Button URL')),
                ('career_qualifications_section_title', models.CharField(blank=True, help_text='Title text for the qualifications section of the page', max_length=255, null=True, verbose_name='Career Qualifications Section Title')),
                ('career_qualifications_image_alt_text', models.CharField(blank=True, help_text='Alt text for the qualifications image', max_length=255, null=True, verbose_name='Career Qualifications Image Alt Text')),
                ('career_qualifications_button_url', models.TextField(blank=True, help_text='URL for the qualifications button', null=True, verbose_name='Career Qualifications Button URL')),
                ('career_last_section_background_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Last Section Background Image', max_length=255, null=True, verbose_name='Career Last Section Background Image Alt Text')),
                ('career_last_section_title', models.CharField(blank=255, help_text='Title text that will be shown in the last section of the page', max_length=255, null=255, verbose_name='Career Last Section Title')),
                ('career_last_section_content', models.TextField(blank=True, help_text='Content text for the last section of the page', null=True, verbose_name='Career Last Section Content')),
                ('career_last_section_button_url', models.TextField(blank=True, help_text='URL for the Last Section button', null=True, verbose_name='Career Last Section Button URL')),
                ('career_image_section_first_image', models.ForeignKey(blank=True, help_text='First image that will be shown for the image section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('career_image_section_second_image', models.ForeignKey(blank=True, help_text='Second image that will be shown for the image section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('career_image_section_third_image', models.ForeignKey(blank=True, help_text='Second image that will be shown for the image section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('career_last_section_background_image', models.ForeignKey(blank=True, help_text='Background image that will be shown for the bottom section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('career_qualifications_image', models.ForeignKey(blank=True, help_text='Image that will be shown for the qualifications section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('career_video_thumbnail', models.ForeignKey(blank=True, help_text='Thumbnail for the video in the Career page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('first_opportunity_image', models.ForeignKey(blank=True, help_text='Image that will be shown for the first opportunity.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('header_image', models.ForeignKey(blank=True, help_text='Image that will be shown in the header portion of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('one_to_two_year_image_section_first_image', models.ForeignKey(blank=True, help_text='First image that will be shown for the image section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('one_to_two_year_image_section_second_image', models.ForeignKey(blank=True, help_text='Second image that will be shown for the image section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('one_to_two_year_image_section_third_image', models.ForeignKey(blank=True, help_text='Second image that will be shown for the image section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('one_to_two_year_last_section_background_image', models.ForeignKey(blank=True, help_text='Background image that will be shown for the bottom section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('one_to_two_year_qualifications_image', models.ForeignKey(blank=True, help_text='Image that will be shown for the qualifications section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('one_to_two_year_video_thumbnail', models.ForeignKey(blank=True, help_text='Thumbnail for the video in the 1-2 Year page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('second_opportunity_image', models.ForeignKey(blank=True, help_text='Image that will be shown for the second opportunity.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('short_term_first_image', models.ForeignKey(blank=True, help_text='First out of three images that will be shown in the page which are above the qualifications section.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('short_term_first_tab_qualifications_image', models.ForeignKey(blank=True, help_text='Image that will be shown for the qualifications section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('short_term_second_image', models.ForeignKey(blank=True, help_text='Second out of three images that will be shown in the page which are above the qualifications section', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('short_term_second_tab_last_section_background_image', models.ForeignKey(blank=True, help_text='Background image that will be shown for the bottom section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('short_term_second_tab_qualifications_image', models.ForeignKey(blank=True, help_text='Image that will be shown for the qualifications section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('short_term_third_image', models.ForeignKey(blank=True, help_text='Third out of three images that will be shown in the page which are above the qualifications section', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('short_term_third_tab_last_section_background_image', models.ForeignKey(blank=True, help_text='Background image that will be shown for the bottom section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('short_term_third_tab_qualifications_image', models.ForeignKey(blank=True, help_text='Image that will be shown for the qualifications section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='OneToTwoYearApplicationProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Title of the application process', max_length=255, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='Description of the application process', null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': '1-2 Year Application Process',
                'verbose_name_plural': '1-2 Year Application Processes',
            },
        ),
        migrations.CreateModel(
            name='OneToTwoYearQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.TextField(blank=True, help_text='Content of the qualification', null=True, verbose_name='Qualification')),
            ],
            options={
                'verbose_name': '1-2 Year Qualification',
                'verbose_name_plural': '1-2 Year Qualifications',
            },
        ),
        migrations.CreateModel(
            name='ShortTermQualificationFirstTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.TextField(blank=True, help_text='Content of the qualification', null=True, verbose_name='Qualification')),
            ],
            options={
                'verbose_name': 'Short Term Qualification First Tab',
                'verbose_name_plural': 'Short Term Qualifications First Tab',
            },
        ),
        migrations.CreateModel(
            name='ShortTermQualificationSecondTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.TextField(blank=True, help_text='Content of the qualification', null=True, verbose_name='Qualification')),
            ],
            options={
                'verbose_name': 'Short Term Qualification Second Tab',
                'verbose_name_plural': 'Short Term Qualifications Second Tab',
            },
        ),
        migrations.CreateModel(
            name='ShortTermQualificationThirdTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.TextField(blank=True, help_text='Content of the qualification', null=True, verbose_name='Qualification')),
            ],
            options={
                'verbose_name': 'Short Term Qualification Third Tab',
                'verbose_name_plural': 'Short Term Qualifications Third Tab',
            },
        ),
        migrations.CreateModel(
            name='OneToTwoYearSectionGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('is_video', models.BooleanField(default=False, help_text='Set this as true if the item in the gallery is a Video', verbose_name='Is Video')),
                ('video_url', models.TextField(blank=True, help_text='URL of the video to be shown. This needs to be the EMBED url of the video or else it will not work properly', null=True, verbose_name='Video URL')),
                ('image_alt_text', models.CharField(blank=True, help_text='Alt text for the image', max_length=255, null=True, verbose_name='Image Alt Text')),
                ('image', models.ForeignKey(blank=True, help_text='Image as part of the gallery. This also serves as the thumbnail if the item of the gallery is a video', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='one_to_two_year_gallery', to='explore_ways_to_serve.ExploreWaysToServe')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CareerSectionGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('is_video', models.BooleanField(default=False, help_text='Set this as true if the item in the gallery is a Video', verbose_name='Is Video')),
                ('video_url', models.TextField(blank=True, help_text='URL of the video to be shown. This needs to be the EMBED url of the video or else it will not work properly', null=True, verbose_name='Video URL')),
                ('image_alt_text', models.CharField(blank=True, help_text='Alt text for the image', max_length=255, null=True, verbose_name='Image Alt Text')),
                ('image', models.ForeignKey(blank=True, help_text='Image as part of the gallery. This also serves as the thumbnail if the item of the gallery is a video', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='career_gallery', to='explore_ways_to_serve.ExploreWaysToServe')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
