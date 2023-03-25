from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("đây là hàm index ở app 1")

def hi(request):
    return HttpResponse("đây là hàm hi ở app 1")

L_sanpham = [
    {
        "id":1,
        "name":"Bánh bò",
        "price":"10000",
    },
    {
        "id":2,
        "name":"Bún chả",
        "price":"35000",
    },
    {
        "id":3,
        "name":"Bánh mì chảo",
        "price":"40000",
    },
]

L_sanpham2 = [
    {
        "id":1,
        "name":"Bánh",
        "product":[
            {
                "id":1,
                "name":"Bánh bò",
                "price":"10000",
            },
            {
                "id":2,
                "name":"Bánh bột lọc",
                "price":"10000",
            },
        ]
    },
    {
        "id":2,
        "name":"Bún",
        "product":[
            {
                "id":3,
                "name":"Bún chả",
                "price":"35000",
            },
            {
                "id":4,
                "name":"Bún riêu",
                "price":"40000",
            },
        ]
    },
]

def sanpham(request, id):
    text = "Không có thông tin về sản phẩm"
    
    for item in L_sanpham:
        if id == item["id"]:
            text = "ID: {a}<br>Tên sản phẩm: {b}<br>Giá: {c}".format(a = item["id"], b = item["name"], c = item["price"])

    return HttpResponse(text)

def danhsachsanpham(request,id):
    # id gr
    # trả về sp của gr

    text = "Không có thông tin về danh mục"

    for category in L_sanpham2:
        if id == category["id"]:
            lst = []
            for item in category["product"]:
                lst.append("ID: {a}<br>Tên sản phẩm: {b}<br>Giá: {c}<br>".format(a = item["id"], b = item["name"], c = item["price"]))
                a = len(lst)
    return HttpResponse(lst)