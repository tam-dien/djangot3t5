from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    # now = datetime.datetime.now()
    # ## now là dạng datetime ~~> string với cái kiểu format ngày/tháng/năm giờ:phút:giây
    # ### strftime = string from time
    # now_str = now.strftime("%d/%m/%Y %H:%M:%S")
    a = 2
    bcc = ""
    for i in range(1,10):
        b = a*i
        bcc += "2 x " + str(i) + " = " + str(b) + "<br/>"
    return HttpResponse(bcc)

def xulytime(request):
    a = datetime.datetime(day=21,month=3,year=2023,hour=21,minute=15)
    b = datetime.datetime(day=21,month=3,year=2023,hour=21,minute=30)
    ### hiển thị lên trình duyệt:
    ##### Giờ A: a ~~> ngày/tháng/năm giờ:phút:giây
    ##### Giờ B: b ~~> ngày/tháng/năm giờ:phút:giây
    ##### Nếu giờ hiện tại đang nằm trong khoảng từ a đến b thì in ra dòng chữ "Đang trong giờ từ A đến B"
    ##### ngược lại: in ra dòng chữ "Đang không trong giờ từ A đến B"
    now = datetime.datetime.now()
    result = "Đang trong giờ từ A đến B" if a < now < b else "Đang không trong giờ từ A đến B"
    return HttpResponse('''
        {a}<br/>
        {b}<br/>
        {result}
    '''.format(a=a.strftime("%d/%m/%Y %H:%M:%S"),
               b=b.strftime("%d/%m/%Y %H:%M:%S"),
               result=result))

def link1(request):
    return HttpResponse("<a href='/link2'>Sang link 2</a>")

def link2(request):
    return HttpResponse("<a href='/link1'>Sang link 1</a>")

L_sanpham = [
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
        "id":1,
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

def sanpham(request,id):
    for i in L_sanpham:
        for j in i["product"]:
            if id == j["id"]:
                return HttpResponse(f'''
                ID : {id}<br>
                Name: {j["name"]}<br>
                Price: {j["price"]}
            ''')
    return HttpResponse("San pham khong ton tai")

def danhsachsanpham(request, id):
    for i in L_sanpham:
        if id == i["id"]:
            chuoi = ""
            for item in i["product"]:
                chuoi += f'''
                {item["id"]} {item["name"]} {item["price"]}<br>
                '''
            return HttpResponse(chuoi)
    return HttpResponse("Khong co id group")