import base64

from django.conf import settings
from django.shortcuts import redirect, render

from home.utils import AGWMAPIService, encrypt_string
from find_a_missionary.models import FindAMissionaryPage
from individual_missionaries.models import IndividualMissionaryIndexPage

from django.http import HttpResponse

agwm_service = AGWMAPIService()


def redirect_to_missionary_page(request, account_number, last_name):
    code = f"{account_number}"
    enc = []
    response = agwm_service.search(query=account_number)
    is_sensitive_search = response.json().get("IsSensitiveSearch")

    # encrypt code
    enc = encrypt_string(code)

    encrypted_string = base64.urlsafe_b64encode("".join(enc).encode()).decode()

    return redirect(
        f"{IndividualMissionaryIndexPage.objects.first().url}?code={encrypted_string}&last_name={last_name}&is_sensitive_search={is_sensitive_search}",
    )


def redirect_to_find_a_missionary_page_filter_by_region(request, region):

    return redirect(
        f"{FindAMissionaryPage.objects.first().url}?region={region}",
    )


def redirect_to_find_a_missionary_page_filter_by_cam(request, cam):
    # Filter by countries, areas, and ministries
    return redirect(
        f"{FindAMissionaryPage.objects.first().url}?cam={cam}",
    )


def redirect_to_find_a_missionary_page_filter_by_sending_districts(request, district):
    # Filter by sending districts
    return redirect(
        f"{FindAMissionaryPage.objects.first().url}?sender={district}",
    )


def search_missionary(request, initial_argument):
    query = request.POST.get("query", "")
    password = request.POST.get("password", "")
    enc = []
    encrypted_string = ""

    if not password:
        response = agwm_service.search(query=query)
    else:
        # Encrypt password
        enc = encrypt_string(password)
        encrypted_string = base64.urlsafe_b64encode("".join(enc).encode()).decode()
        response = agwm_service.search(query=initial_argument, password=password)

    results = response.json().get("Results")
    is_sensitive_search = response.json().get("IsSensitiveSearch")

    # Check if missionary is flagged as safe search
    if is_sensitive_search and not results:
        context = {"query": query if query else initial_argument, "flag": query}
        return render(request, "partials/confirm_page.html", context)

    else:
        response = HttpResponse()
        # Safe search
        if is_sensitive_search and results:
            response[
                "HX-Redirect"
            ] = f"{FindAMissionaryPage.objects.first().url}?query={initial_argument}&code={encrypted_string}"
        # Normal search
        else:
            response[
                "HX-Redirect"
            ] = f"{FindAMissionaryPage.objects.first().url}?query={query}&code={initial_argument}"
        return response
