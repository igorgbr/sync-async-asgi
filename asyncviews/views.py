import time
import asyncio
import httpx
from django.http import HttpResponse

# from django.http import JsonResponse


# def api(request):
#     time.sleep(1)
#     payload = {"message": "Hello, world!"}

#     if "task_id" in request.GET:
#         payload["task_id"] = request.GET["task_id"]
#     return JsonResponse(payload)


# make async call
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")
        print(r)


# make sync call
def http_call_sync():
    for num in range(1, 6):
        time.sleep(1)
        print(num)

    r = httpx.get("https://httpbin.org/get")
    print(r)


# make async view
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP Response")


# make sync call
def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP Response")
