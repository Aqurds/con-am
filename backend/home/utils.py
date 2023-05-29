import os
import requests

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import (
    get_connection,
    send_mail,
    send_mass_mail,
    EmailMultiAlternatives,
)
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def get_upload_path(instance, filename):
    if settings.USE_S3:
        return os.path.join("uploads", instance.__class__.__name__.lower(), filename)

    return os.path.join(instance.__class__.__name__.lower(), filename)


class AGWMAPIService:
    base_url = "https://api.agmd.org/api/v1.2"

    def search(
        self, query: str = "", password: str = "", page_number: int = 1, *args, **kwargs
    ):
        url = (
            f"{self.base_url}/directory/search/{page_number}?text={query}&password={password}"
            if query
            else f"{self.base_url}/directory/search/{page_number}"
        )
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.request("GET", url, json={}, headers=headers)
        return response

    def get_fund_guid(self, missionary_guid):
        url = f"{self.base_url}/directory/missionaryfundguid/{missionary_guid}"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.request("GET", url, json={}, headers=headers)
        return response

    def filter_by_region(self, region: str = "", page_number: int = 1):
        url = (
            f"{self.base_url}/directory/search/{page_number}?region={region}"
            if region
            else f"{self.base_url}/directory/search/{page_number}"
        )
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.request("GET", url, json={}, headers=headers)
        return response

    def filter_by_cam(self, cam, page_number: int = 1):
        url = f"{self.base_url}/directory/search/{page_number}?cam={cam}"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.request("GET", url, json={}, headers=headers)
        return response

    def filter_by_sending_districts(self, district, page_number: int = 1):
        url = f"{self.base_url}/directory/search/{page_number}?sender={district}"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.request("GET", url, json={}, headers=headers)
        return response

    def get_regions(self):
        # To prevent circular import
        from cms.models import Region, MissionaryApi

        response = requests.get("https://api.agmd.org/api/v1.2/directory/regions")
        data = response.json()
        missionary_api = MissionaryApi.objects.first()
        regions_list = []
        regions_update_list = []

        # Loop through the response
        for value in data:
            new_region = Region.objects.filter(region_guid=value["RegionGuid"]).first()
            if new_region is None:
                regions_list.append(
                    Region(
                        missionary_api=missionary_api,
                        name=value["RegionName"],
                        region_guid=value["RegionGuid"],
                    )
                )
            else:
                new_region.name = value["RegionName"]

                regions_update_list.append(new_region)

        if regions_list:
            Region.objects.bulk_create(regions_list)

        if regions_update_list:
            Region.objects.bulk_update(regions_update_list, ["name", "region_guid"])

    def get_cams(self):
        # To prevent circular import
        from cms.models import MissionaryApi, Cam

        response = requests.get("https://api.agmd.org/api/v1.2/directory/cam")
        data = response.json()
        missionary_api = MissionaryApi.objects.first()
        cams_list = []
        cams_update_list = []

        # Loop through the response
        for value in data:
            # Check for api response and skip if text value is All Areas, Countries, and Ministries
            if value["Text"] == "All Areas, Countries, and Ministries":
                continue

            # Filter through the list by using the unique value
            new_cams = Cam.objects.filter(value=value["Value"]).first()
            cam_text = value["Text"]
            # Split cam_text and get all characters after last hyphen
            new_cam_text = cam_text.split("-")[:-1]
            # Strip whitespace from new_cam_text
            remove_whitespace_in_new_cam_text = [
                letter.strip() for letter in new_cam_text
            ]
            # Handle multiple names from cam_text and join them using hyphen
            final_cam_text = " - ".join(remove_whitespace_in_new_cam_text)

            # Split cam_text and get all characters after last hyphen
            cam_type = cam_text.split("-")[-1]
            # Strip all whitespace from cam_type and replace parentheses with empty string
            final_cam_type = cam_type.strip().replace("(", "").replace(")", "")
            # Check if there is no value
            if new_cams is None:
                # Append new value in cams_list
                cams_list.append(
                    Cam(
                        missionary_api=missionary_api,
                        text=final_cam_text,
                        value=value["Value"],
                        type=final_cam_type,
                    )
                )

            else:
                new_cams.text = final_cam_text
                new_cams.type = final_cam_type

                cams_update_list.append(new_cams)

        if cams_list:
            # bulk create the cams list
            Cam.objects.bulk_create(cams_list)

        if cams_update_list:
            Cam.objects.bulk_update(cams_update_list, ["text", "type"])

    def get_sending_districts(self):
        # To prevent circular import
        from cms.models import MissionaryApi, SendingDistrict

        response = requests.get("https://api.agmd.org/api/v1.2/directory/districts")
        data = response.json()
        missionary_api = MissionaryApi.objects.first()
        district_list = []
        district_update_list = []
        # Loop through the response
        for value in data:
            # Filter through the list by finding the unique number value
            new_district = SendingDistrict.objects.filter(
                number=value["Number"]
            ).first()

            #  Check if there's no number
            if new_district is None:
                # Append new number in district_list
                district_list.append(
                    SendingDistrict(
                        missionary_api=missionary_api,
                        name=value["Name"],
                        number=value["Number"],
                    )
                )

            else:
                # update name and append to district update list
                new_district.name = value["Name"]

                district_update_list.append(new_district)

        if district_list:
            # bulk create the district_list
            SendingDistrict.objects.bulk_create(district_list)

        if district_update_list:
            SendingDistrict.objects.bulk_update(
                district_update_list, ["name", "number"]
            )


def send_email_template(is_secure, subject, template, recipients, data={}):
    """
    This function sends an email using a selected template.

    Arguments:
        subject: the subject of the email
        template: the template to be used for the email
        recipient: a list of recipients the email will be sent to
        data: a dictionary to be added as context variables in the email
    """
    context = {
        "current_site": Site.objects.get_current(),
        "protocol": "https" if is_secure else "http",
    }
    context.update(data)

    html_content = render_to_string(template, context)
    text_content = strip_tags(html_content)

    send_mail(
        subject=subject,
        message=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
        fail_silently=False,
        html_message=html_content,
    )


def send_mass_mail(
    request,
    template,
    datatuple,
    fail_silently=False,
    user=None,
    password=None,
    connection=None,
):
    """
    Given a datatuple of (subject, recipient, data), sends each message to each recipient list. Returns the
    number of emails sent.

    Arguments:
        template: the template to be used for the email
        datatuple: (subject, recipient, data) each item is one email
            subject: the subject of the email
            recipient: a list of recipients the email will be sent to
            data: a dictionary to be added as context variables in the email

    If user and password are set, they're used to log in.
    If user is None, the EMAIL_HOST_USER setting is used.
    If password is None, the EMAIL_HOST_PASSWORD setting is used.
    """

    connection = connection or get_connection(
        username=user, password=password, fail_silently=fail_silently
    )
    messages = []
    for subject, recipient, data in datatuple:
        context = {
            "current_site": Site.objects.get_current(),
            "protocol": request.scheme,
        }
        context.update(data)
        html_content = render_to_string(template, context)
        text_content = strip_tags(html_content)
        from_email = settings.DEFAULT_FROM_EMAIL

        message = EmailMultiAlternatives(subject, text_content, from_email, recipient)
        message.attach_alternative(html_content, "text/html")
        messages.append(message)
    return connection.send_messages(messages)


def encrypt_string(code):
    secret = settings.SECRET_KEY
    encoded_list = []

    for i in range(len(code)):
        key_c = secret[i % len(secret)]
        enc_c = chr((ord(code[i]) + ord(key_c)) % 256)
        encoded_list.append(enc_c)

    return encoded_list


def decode_string(code):
    secret = settings.SECRET_KEY
    decoded_list = []

    for i in range(len(code)):
        key_c = secret[i % len(secret)]
        dec_c = chr((256 + ord(code[i]) - ord(key_c)) % 256)
        decoded_list.append(dec_c)

    return decoded_list
