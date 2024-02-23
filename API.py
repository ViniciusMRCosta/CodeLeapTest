from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden
from django.views import View
import requests


BASE_URL = "https://dev.codeleap.co.uk/careers/"

def create_post(request):
    data = request

    try:
        response = requests.post(BASE_URL, json=data)
        response.raise_for_status()

        return JsonResponse({"id": response.json()["id"]}, status=200)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            return HttpResponseBadRequest(e.response.text)
        elif e.response.status_code == 403:
            return HttpResponseForbidden(e.response.text)
        else:
            return HttpResponseBadRequest("Erro ao criar post")
    except Exception as e:
        return HttpResponseBadRequest("Erro ao criar post")

def get_posts():
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        posts = response.json()
        return JsonResponse({"results": posts}, status=200)
    else:
        return HttpResponseBadRequest("Erro ao obter posts")

def update_post(request, item_id):
    data = request.data

    try:
        response = requests.patch(f"{BASE_URL}{item_id}/", json=data)
        response.raise_for_status()

        return JsonResponse({"success": True}, status=200)
    except requests.exceptions.HTTPError as e: 
        if e.response.status_code == 400:
            return HttpResponseBadRequest(e.response.text)
        elif e.response.status_code == 403:
            return HttpResponseForbidden(e.response.text)
        elif e.response.status_code == 404:
            return HttpResponseNotFound("Post não encontrado")
        else:
            return HttpResponseBadRequest("Erro ao atualizar post")
    except Exception as e:
        return HttpResponseBadRequest("Erro ao atualizar post")

def delete_post(request, item_id):
    response = requests.delete(f"{BASE_URL}{item_id}/")

    if response.status_code == 204:
        return JsonResponse({"success": True}, status=200)
    elif response.status_code == 404:
        return HttpResponseNotFound("Post não encontrado")
    else:
        return HttpResponseBadRequest("Erro ao excluir post")
