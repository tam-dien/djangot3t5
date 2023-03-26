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
        "name": "Bánh",
        "product": [
            {
                "id": 1,
                "name": "Bánh bò",
                "price": "10000"
            },
            {
                "id": 2,
                "name": "Bánh bọt lọc",
                "price": "20000"
            },
            {
                "id": 3,
                "name": "Bánh flan",
                "price": "14000"
            },
        ]
    },
    {
        "id": 2,
        "name": "Bún",
        "product": [
            {
                "id": 4,
                "name": "Phở bò",
                "price": "45000"
            },
            {
                "id": 5,
                "name": "Bún chả",
                "price": "40000"
            }
        ]
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
    return HttpResponse('Không có sản phẩm')

def danhsachsanpham0(request):
    text = ''
    for item in l_sanpham:
        text_product = ""
        for product in item['product']:
            text_product += '''<br>
                ID: {a} <br>
                Tên sản phẩm: {a} <br>
                Giá: {c} <br><hr>
            '''.format(a=product['id'], b=product['name'], c=product['price'])
        text = '''ID nhóm: {a} <br> 
                Tên nhóm: {b} <br>
                Danh sách sản phẩm: {c} <br><hr>
                '''.format(a=item['id'], b=item['name'], c=text_product)
    return HttpResponse(text)

def danhsachsanpham(request, id):
    for item in l_sanpham:
        
        if id == item['id']:
            text = ''
            for i in item['product']:
                text += f'''
                {i["id"]} {i["name"]} {i["price"]}<br>
                '''
            return HttpResponse(text)  
    return HttpResponse('Không có sản phẩm')

def dssanpham(request, id_group, id_product):
    return HttpResponse('san pham co 2 tham so la {a}, {b}'.format(a=id_group, b=id_product))

def findProduct(request, id_group, id_product):
    for item in l_sanpham:
        for product in item['product']:
            for id in range (1, product['id'] + 1):
                if id_product == id and id_group == item['id']:
                    return HttpResponse('''
                                        Group-Name: {a}<br/>
                                        ID: {b}<br/>
                                        Tên sản phẩm: {c}<br/>
                                        Giá sản phẩm: {price}
                                    '''.format(a=item['name'],
                                                b=id,
                                                c=product['name'],
                                                price=product['price']))
                elif id_product == id:
                    return HttpResponse('''
                                            Sản phẩm {a} thuộc group {b}
                                            có ID group là {c}
                                        '''.format(a=product['name'],
                                                    b=item['name'],
                                                    c=item['id']))

    return HttpResponse('Không có sản phẩm này')

