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

l_sanpham = [
    {
        "id": 1,
        "name": "Bánh bò",
        "price": "10000"
    },
    {
        "id": 2,
        "name": "Coca",
        "price": "20000"
    },
    {
        "id": 3,
        "name": "Bánh flan",
        "price": "14000"
    },
    {
        "id": 4,
        "name": "Phở bò",
        "price": "45000"
    },
]

def sanpham(request, id): 
    
    for item in l_sanpham:
        if id == item['id']:
            return HttpResponse('''
                ID: {a}<br/>
                Tên sản phẩm: {b}<br/>
                Giá sản phẩm: {price}
            '''.format(a=item['id'],
                        b=item['name'],
                        price=item['price']))
        # elif id != item['id']:
        #     
    return HttpResponse('Không có sản phẩm')
