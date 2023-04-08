from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from index.models import Product

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

count = 0
@csrf_exempt
def testrequest(request):
    global count
    print(request.method)
    print(request.GET)
    if request.method == "GET":
        ten = request.GET['ten'] if 'ten' in request.GET else ""
        # ten = request.GET.get("ten")
        return HttpResponse('''
        <form>
            <input name="ten">
            <input name="tuoi">
            <button type="submit">Submit</button>
        </form>
        ''')
    elif request.method == "POST":
        count += 1
        return HttpResponse("count da duoc tang")

def searchproduct(request):
    search = request.GET['product'].lower() if 'product' in request.GET else ""
    text = f'''
    <form>
        <input value="{search if search!=None else ""}"name='product' placeholder='san pham'>
        <button type='submit'>Submit</button>
    </form>
    '''
    if 'product' in request.GET:
        # search = request.GET['product'].lower() 
        for group in L_sanpham:
            for product in group['product']:
                if search in product['name'].lower():
                    text += f'''
                        {product['id']} {product['name']} {product['price']}<br>
                    '''
    return HttpResponse(text)

@csrf_exempt
def login(request):
    if request.method == "GET":
        return HttpResponse('''
        <form method='POST'>
            <input name='username' placeholder='username'>
            <input type='password' name='password'>
            <button type='submit'>Submit</button>
        </form>
        ''')
    elif request.method == "POST":
        if request.POST['username'] == 'hatrang' and request.POST['password'] == '123':
            return HttpResponse("Login thanh cong")
        return HttpResponse('''
        Sai username hoac password!
        <form method='POST'>
            <input name='username' placeholder='username'>
            <input type='password' name='password'>
            <button type='submit'>Submit</button>
        </form>
        ''')

@csrf_exempt
def addproduct(request):
    if request.method == "GET":
        text = '''
            <form method="POST">
                <input name="product" placeholder="Tên sản phẩm">
                <input name="price" placeholder="Giá">
                <input name="quantity" placeholder="Số lượng">
                <button type="submit">Submit</button>
            </form>
        '''
    elif request.method == "POST":
        error = ""
        if len(request.POST.get("product")) < 2:
            error += "Tên sản phẩm phải có ít nhất 2 ký tự<br>"
        if not request.POST.get("price").isnumeric() or int(request.POST.get("price")) < 0:
            error += "Giá cần phải là số dương<br>"
        if not request.POST.get("quantity").isnumeric() or int(request.POST.get("quantity")) < 0:
            error += "Số lượng cần phải là số dương<br>"

        if len(error) == 0:
            product = Product(name=request.POST.get("product"),price=request.POST.get("price"), quantity=request.POST.get("quantity"))
            product.save()
            return redirect("/listproduct/")
        else:
            text = f'''
            <form method="POST">
                <input name="product" placeholder="Tên sản phẩm" value="{request.POST.get("product")}">
                <input name="price" placeholder="Giá" value="{request.POST.get("price")}">
                <input name="quantity" placeholder="Số lượng" value="{request.POST.get("quantity")}">
                <button type="submit">Submit</button>
            </form>
            <p style="color:red">{error}</p>
            '''
    return HttpResponse(text)

@csrf_exempt
def product(requets,idproduct):
    try:
        product = Product.objects.get(id=idproduct) 
        text = f'''
        <button><a href='/listproduct/'>Quay lại</a></button>
        <ul>
            <li>Tên sản phẩm:{product.name}</li>
            <li>Gía sản phảm: {product.price}</li>
            <li>Số lượng: {product.quantity}</li>
        </ul>
        <button><a href='/editproduct/{idproduct}/'>Chỉnh sửa</a></button>
        <button><a href='/deleteproduct/{idproduct}/'>Xóa</a></button>
        '''
    except Product.DoesNotExist:
        text = "ID không tồn tại"
    return HttpResponse(text)

@csrf_exempt
def editproduct(request,id):
    product = Product.objects.get(id=id)
    if request.method == "GET":
        return HttpResponse (f'''
        <form method="POST">
            <input name="name" placeholder="Tên sản phẩm" value="{product.name}">
            <input name="price" placeholder="Giá" value="{product.price}">
            <input name="quantity" placeholder="Giá" value="{product.quantity}">
            <button type="submit">Lưu</button>
        </form>
        ''')
    elif request.method == "POST":
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.save()
        return redirect(f"/product/{id}")

@csrf_exempt
def deleteproduct(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/listproduct/")

@csrf_exempt
def list_product(request):
    print(request.GET)
    print("quantity1:",request.GET.get("quantity"))
    search_name = request.GET.get("name") if request.GET.get("name") != None else ""
    search_quantity = request.GET.get("quantity") if request.GET.get("quantity") != None else ""
    print("quantity2:",request.GET.get("quantity"))
    if search_name == "" and search_quantity == "":
        l_product = Product.objects.all()
    elif search_quantity == "":
        l_product = Product.objects.filter(name__icontains=search_name)
    else:
        l_product = Product.objects.filter(name__icontains=search_name, quantity__gte=search_quantity)
    print("quantiy:",search_quantity)
    text = f'''
    <form>
        <input value="{search_name}" name="name" placeholder="Tên sản phẩm"><br>
        <input value="{search_quantity}" name="quantity" placeholder="Số lượng sản phẩm"><br>
        <button><a href='/addproduct/'>Thêm sản phẩm</a></button>
    </form>
    '''

    for product in l_product:
        text += f'''
        <ul>
            <li>Tên sản phẩm:{product.name}</li>
            <li>Gía sản phảm: {product.price}</li>
            <li>Số lượng: {product.quantity}</li>
            <li><button><a href='/product/{product.id}'>Chi tiết</a></button></li>
        </ul>
        '''

    return HttpResponse(text)