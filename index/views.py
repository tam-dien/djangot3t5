from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from index.models import Product
from django.db import models

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

@csrf_exempt 
def add_product(request):
    if request.method == "GET":
        text = '''    
            <form method = "POST">
                <input name="product" placeholder="Tên sản phẩm">
                <input name="price" placeholder="Giá sản phẩm">
                <input name="quantity" placeholder="Số lượng sản phẩm">
                <button type="submit">Submit</button>
            </form>
        '''

    elif request.method == "POST":
        name = request.POST.get("product")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")

        
        error = ""
        if len(name) < 2:
            error += "Tên sản phẩm phải có ít nhất 2 ký tự. <br>"
        if not price.isnumeric() or int(price) < 0:
            error += "Giá cần phải là số dương. <br>"
        if not quantity.isnumeric() or int(price) < 0:
            error += "Số lượng cần phải là số dương. <br>"   
        
        if len(error) == 0:
            product = Product(name=name, price=price, quantity=quantity)
            product.save()
            return redirect("/list_product")
            #text = "Đã thêm sản phẩm {a} có giá {b} và số lượng {c} vào bảng.".format(a=name, b=price, c=quantity)
        else:
            text = f'''    
                <form method = "POST">
                    <input name="product" placeholder="Tên sản phẩm" value='{name}'>
                    <input name="price" placeholder="Giá sản phẩm" value='{price}'>
                    <input name="quantity" placeholder="Số lượng sản phẩm" value='{quantity}'>
                    <button type="submit">Submit</button>
                </form>

                <p style='color:red'>{error}</p>
            '''
    return HttpResponse(text)

@csrf_exempt 
def product(request, id):
    # trả thông tin sản phẩm tại id đó
    # có 2 nút là Xóa và Edit
    try:
        product = Product.objects.get(id=id) #filter trả về list sp. Còn get trả về 1 sp
        text = f'''
            Thông tin sản phẩm:<br>
            <ul>
                <li>Tên: {product.name}</li>
                <li>Giá: {product.price}</li>
                <li>Số lượng: {product.quantity}</li>
            </ul>
            <button><a href="/list_product/">Bach</a></button>
            <button><a href="/delete_product/{id}">Delete</a></button>
            <button><a href="/edit_product/{id}">Edit</a></button>
        '''
    
    except Product.DoesNotExist:
        text = 'Sản phẩm không tồn tại.'

    return HttpResponse(text)

@csrf_exempt
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "GET":
        text = f'''    
            <form method = "POST">
                <input value="{product.name}" name="product" placeholder="Tên sản phẩm">
                <input value="{product.price}" name="price" placeholder="Giá sản phẩm">
                <input value="{product.quantity}" name="quantity" placeholder="Số lượng sản phẩm">
                <button type="submit">Submit</button>
            </form>
        '''

    if request.method == "POST":
        name = request.POST.get("product")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        product.name = name
        product.price = price
        product.quantity = quantity
        product.save()
        return redirect(f"/product/{id}")

    return HttpResponse(text)

@csrf_exempt  
def delete_product(request, id):
    return HttpResponse()

@csrf_exempt
def list_product(request):
    search_name = request.GET.get("name") if request.GET.get("name") != None else ""
    search_quantity = request.GET.get("quantity") if request.GET.get("quantity") != None else ""
    
    if search_name == "" and search_quantity == "":
        L_product = Product.objects.all()
    elif search_name != "" and search_quantity == "":
        L_product = Product.objects.filter(name__icontains=search_name)
    elif search_name == "" and search_quantity != "":
        L_product = Product.objects.filter(quantity=search_quantity)
    else:
        L_product = Product.objects.filter(name__icontains=search_name, quantity=search_quantity)

    text = f'''
        <form>
            <input value='{search_name}' name="name" placeholder="Tên sản phẩm">
            <input value='{search_quantity}' name="quantity" placeholder="Số lượng sản phẩm">
            <button type="submit">Submit</button>
        </form>
    '''

    for product in L_product:
        text += f'''
            <ul>
                <li>Tên: {product.name}</li>
                <li>Giá: {product.price}</li>
                <li>Số lượng: {product.quantity}</li>
                <li><button><a href="/product/{product.id}">Edit</a></button></li>
            </ul>
        '''

    return HttpResponse(text)