from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from index.models import *
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
    ### tạo form để thêm sản phẩm vào group
    ##### form có 3 input: id, tên sản phẩm và giá
    ##### form có method POST
    ####### xử lý form
    ######### xử lý trong POST 
    ######### không có trường nào bị rỗng, id và giá phải là dạng số (sử dụng hàm isnumeric)
    ######### nếu form không đúng định dạng ~~> gen lại form cho người dùng nhập lại
    ######### nếu form đúng định dạng thì thêm sản phẩm mới và trả về trình duyệt tạo sản phẩm thành công
    # product = Product(name="Bún bò",price="35000")
    # product.save()
    if request.method == "GET":
        text = '''
            <form method="POST">
                <input name="product" placeholder="Tên sản phẩm">
                <input name="price" placeholder="Giá">
                <input name="quantity" placeholder="Số lutợng">
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
            product = Product(name=request.POST.get("product"),price=request.POST.get("price"),quantity=request.POST.get("quantity"))
            product.save()
            return redirect("/list_product")
        else:
            text = f'''
            <form method="POST">
                <input name="product" placeholder="Tên sản phẩm" value="{request.POST.get("product")}">
                <input name="price" placeholder="Giá" value="{request.POST.get("price")}">
                <button type="submit">Submit</button>
            </form>
            <p style="color:red">{error}</p>
        '''
    return HttpResponse(text)

@csrf_exempt
def product(request,id):
    ### trả về thông tin của product tại id đó
    try:
        product = Product.objects.get(id=id)
        text = f'''
            <button><a href="/list_product">Back</a></button>
            <ul>
                <li>Tên sản phẩm: {product.name}</li>
                <li>Giá: {product.price}</li>
                <li>Số lượng: {product.quantity}</li>
                <li>Nhóm: {product.group.name if product.group != None else "Chưa có group"}</li>
            </ul>
            <button><a href="/edit_product/{id}">Edit</a></button>
            <button><a href="/delete_product/{id}">Delete</a></button>
        '''
    except Product.DoesNotExist:
        text = "Không tồn tại sản phẩm"
    return HttpResponse(text)

@csrf_exempt
def edit_product(request,id):
    product = Product.objects.get(id=id)
    group_product = ""
    for gp in GroupProduct.objects.all():
        group_product += f"<option value='{gp.id}'>{gp.name}</option>"
    # "".join([f"<option value='{gp.id}'>{gp.name}</option>" for gp in GroupProduct.objects.all()])
    if request.method == "GET":
        text = f'''
            <form method="POST">
                <input value="{product.name}" name="product" placeholder="Tên sản phẩm">
                <input value="{product.price}" name="price" placeholder="Giá">
                <input value="{product.quantity}" name="quantity" placeholder="Số lutợng">
                <select name="group">
                    <option value="">Không có group</option>
                    {group_product}
                </select>
                <button type="submit">Submit</button>
            </form>
        '''
    elif request.method == "POST":
        name = request.POST.get("product")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        group = request.POST.get("group")
        if group == "": group = None
        product.name = name
        product.price = price
        product.quantity = quantity
        gr = GroupProduct.objects.get(id=group)
        ## dòng 287 lấy group product từ id có đc tư form
        ## giả sử e chọn id tư form là 2
        ## ~~> gr của e sẽ là đối tượng Phở
        product.group = gr
        ### product.group là 1 foreign key
        ### product.group ~~> là 1 đối tượng productGroup
        product.save()
        return redirect(f"/product/{id}")
    return HttpResponse(text)

def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/list_product")

@csrf_exempt
def add_group_product(request):
    if request.method == "GET":
        text = '''
            <form method="POST">
                <input name="name" placeholder="Tên group">
                <button type="submit">Submit</button>
            </form>
        '''
        return HttpResponse(text)
    elif request.method == "POST":
        product = GroupProduct(name=request.POST.get("name"))
        product.save()
        return redirect("/list_product")
       
@csrf_exempt
def list_product(request): 
    search_name = request.GET.get("name") if request.GET.get("name") != None else ""
    search_quantity = request.GET.get("quantity") if request.GET.get("quantity") != None else ""
    L_product = Product.objects.all()
    if search_name != "":
        L_product = L_product.filter(name__icontains=search_name)
    if search_quantity.isnumeric():
        L_product = L_product.filter(quantity__gte=search_quantity)
    ### khi nào django thực thi câu lệnh SQL
    ### thực thi cậu lệnh SQL có nghĩa la access database
    text = f'''
        <form>
            <input value="{search_name}" name="name" placeholder="Tên sản phẩm">
            <input value="{search_quantity}" name="quantity" placeholder="Số lượng sản phẩm">
            <button type="submit">Search</button>
        </form>
        <button><a href="/add_group_product">Add Group</a></button>
        <button><a href="/add_product">Add</a></button>
    '''
    ### access vào database khi ta sử dụng dữ liệu
    for product in L_product:
        text += f'''
            <ul>
                <li>Tên sản phẩm: {product.name}</li>
                <li>Giá: {product.price}</li>
                <li>Số lượng: {product.quantity}</li>
                <li>Nhóm: {product.group.name if product.group != None else "Chưa có group"}</li>
                <li><button><a href="/product/{product.id}">View</a></button></li>
            </ul>
        '''
    return HttpResponse(text)

def list_group(request):
    # show danh sách gr như list product
    # gồm tên gr thôi
    search_name = request.GET.get("name") if request.GET.get("name") != None else ""
    L_group = GroupProduct.objects.all()
    if search_name != "":
        L_group = L_group.filter(name__icontains=search_name)
    text = f'''
        <form>
            <input value="{search_name}" name="name" placeholder="Tên nhóm">
        </form>
    '''
    for group in L_group:
        text += f'''
            <ul>
                <li>Tên nhóm: {group.name}</li>
            </ul>
        '''
        # <li><button><a href="/group/{group.id}">View group</a></button></li>
    return HttpResponse(text)

def group(request, id):
    ### trả về thông tin của group tại id đó
    try:
        group = GroupProduct.objects.get(id=id)
        text = f'''
            <button><a href="/list_group">Back to list group</a></button>
            <ul>
                <li>Tên sản phẩm: {group.name}</li>
                <li>ID: {product.id}</li>
            </ul>
            <button><a href="/edit_group/{id}">Edit</a></button>
            <button><a href="/delete_group/{id}">Delete</a></button>
        '''
    except GroupProduct.DoesNotExist:
        text = "Không tồn tại nhóm"
    return HttpResponse(text)