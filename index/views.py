from django.shortcuts import render
from django.http import HttpResponse
import datetime
from index.models import Product

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
def sanpham(request,id):
    chuoi=""
    for i in L_sanpham:
        if id == i["id"]:
          chuoi = " thong tin" + str(i["id"])+str(i["name"]) + str(i["price"])
          return HttpResponse("San pham co:"+ chuoi)

    return HttpResponse("hihi")
L_sanpham2= [
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

def danhsachsanpham(request,id):
    chuoi2=""
    for item in L_sanpham2:
        if id == item["id"]:
            for product in item["product"]:
                    chuoi2 = " thong tin" + str(product["id"])+str(product["name"]) + str(product["price"])
                    return HttpResponse("San pham co:"+ chuoi2)

    return HttpResponse("San pham co:"+ chuoi2)

def sanpham2(request, id_group, id_product):
     
     for group in L_sanpham2:
            if id_group ==group["id"]:
                for product in group["product"]:
                        if id_product == product["id"]:
                             return HttpResponse("sanpham có 2 tham số là {a}, {b}".format( a=id_group, b=id_product))
                        elif id_product != product["id"]: 
                            for group in L_sanpham2:
                                 for product in group["product"]:
                                        if id_product == product["id"]:
                                            return HttpResponse("sanpham có 2 tham số là {a}, {b}".format( a=group["id"], b=id_product))

    
     return HttpResponse("no group")
from django.views.decorators.csrf import csrf_exempt

count =0 
@csrf_exempt
def test_request(request):
    global count
    print("Đường dẫn", request.path)
    print("Dữ liệu GET:", request.GET)
    if request.method =="GET":
        ten =request.GET.get("ten")
        tuoi= request.GET.get("tuoi")
        return HttpResponse (str(ten) + str(tuoi)+ '''<br>
            <form>
                <input name = "ten">
                <input name = " tuoi">
                <button type = "submit">Submit</button>
            </form>
            ''' )
    elif request.method =="POST":
        count +=1
        return HttpResponse("Count up")

def searchproduct(request):
    
    text='''
        <form >
            <input name = "product" placeholder = "sanpham">
            <button type ="submit">Submit</button>
        </form>
    '''
    if request.method =="GET":
        tensp =request.GET.get("tensp")
        for group in L_sanpham2:
            for item in group:
                 if tensp== group["name"]:
                      
                      return HttpResponse (+str(tensp) + str(text))
                      
    return HttpResponse(text)
@csrf_exempt
def login(request):
    #  text=""
    text = '''
            <form method = "POST">
                <input name ="username" placeholder = "Username">
                <input type ="password" name="password" placeholder ="Password">
                <button type ="submit">Submit</button>
            </form>
    '''
   
    if request.method =="POST":
        name=request.POST.get("username")
        pw= request.POST.get("password")
        if name =="ngocquynh" and pw=="123":
            return HttpResponse (str(name) + str(pw) + str(text))
    return HttpResponse(text)
@csrf_exempt
def add_product(request):

    text = '''
            <form method = "POST">
                <input name="price" placeholder = "price" >
                <input name="product" placeholder ="product">
                <input name="quantity" placeholder ="quantity">
                <button type ="submit">Submit</button>
            </form>
    '''
    if request.method =="POST":
            gia =request.POST.get("price")
            sp =request.POST.get("product")
            sl =request.POST.get("quantity")
                 
            if (gia.isnumeric() == True) and(sp != None):
                product=Product(name=sp,price=gia,quantity=sl)
                product.save()
    return HttpResponse (text)
def queryproduct(request,id):
    text = '''
            <form>
                <button type ="submit">Edit</button>
                <button type ="submit">Delete</button>
            </form>
    '''


    product=Product.objects.get(id=id)

    return HttpResponse(text+"<br>"+product.name+"<br>"+str(product.price)+"<br>"+str(product.quantity))


