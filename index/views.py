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

def danhsachsanpham0(request):
    text = ""
    for item in L_sanpham:
        text_product = ""
        for product in item["product"]:
            text_product += '''
            ID: {a}<br>
            Ten san pham: {b}<br>
            Gia: {c}<br>'''.format(a = product["id"], b=product["name"], c=product["price"])
        text += '''ID nhom: {a}<br>
                Ten nhom: {b}<br>
                Danh sach san pham: <br>{c}<br><hr>'''.format(a = item["id"], b=item["name"], c=text_product)
    return HttpResponse(text)

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

def sanpham2(request,id_group,id_product):
    for group in L_sanpham:
        for product in group['product']:
            if product['id'] == id_product:
                if id_group == group['id']:
                    return HttpResponse(f'''
                    Group: {group['name']}<br>
                    Product id: {product['id']}<br>
                    Product name: {product['name']}<br>
                    Product price: {product['price']}<br>''')
                else:
                    return HttpResponse(f'''
                    Sản phẩm {product['name']} 
                    thuộc group {group['name']} 
                    có id là {group['id']}''')
    return HttpResponse("Không có thông tin về sản phẩm")

def handler404(request,exception):
    return HttpResponse("Ban dang vao 1 duong dan sai")