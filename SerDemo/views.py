from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View
from SerDemo import models



# Create your views here.

# book_list = [
#     {
#         'id:1,
#         'title':'xxx',
#     },{}
# ]


class BookView(View):

    def get(self, request):
        book_list = models.Book.objects.values("nid","title", "pub_time", 'publish')  # 获取数据
        book_list = list(book_list)
        ret = []
        for book in book_list:
            publisher_id = book["publish"]
            publisher_obj = models.Publisher.objects.filter(nid=publisher_id).first()
            book["publish"] = {
                "id": publisher_id,
                "title": publisher_obj.title
            }
            ret.append(book)
        # ret = json.dumps(book_list,ensure_ascii=False)
        # return HttpResponse(book_list)
        return JsonResponse(ret, safe=False, json_dumps_params={"ensure_ascii": False})
