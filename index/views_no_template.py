from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
from index.models import *

# Create your views here.
def index(request):
    context = {
        'foods': Product.objects.all()
    }
    return render(request, 'index/index.html', context)

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

count = 0

def testRequest(request):
    print(request.method)
    return HttpResponse('Test request')

@csrf_exempt
def http_method(request):
    global count
    print('Đường dẫn: ', request.path)
    if request.method == "GET":
        ten = request.GET.get('ten')
        print(ten)
        print(request.GET)
        return HttpResponse('''
            <h1>Input form</h1>
            <form style="padding-top: 12px; display: inline-flex; flex-direction: column; gap: 8px">
                <label for="ten">Ten</label>
                <input id="ten" name="ten"><br>
                <label for="age">Age</label>
                <input id="age" name="age"><br>
                <label for="address">Address</label>
                <input id = "address" name="address">
                <button type="submit">Submit</button>
            </form>
        ''')
    elif request.method == "POST":
        count += 1
        return HttpResponse('Count: ', count)
    print('Phương thức truy cập là: ' + request.method)
    return HttpResponse('Phương thức truy cập là: ' + request.method)

#Điểm yếu: Phải nhập đúng tên tiếng Việt mới tìm được
@csrf_exempt
def search_product(request):
    search = request.GET.get('product')
    text = f'''
        <form method="GET">
            <input value="{search if search != None else ''}" name="product" type="text">
            <button type="submit">Submit</button>
        </form>
    '''
        
    for item in l_sanpham:
        if request.POST.get('product') == item['name']:
            text = '''
                <form method="POST">
                    <input name="product" type="text">
                    <button type="submit">Submit</button>
                </form>
                <h3>Sản phẩm bạn vừa tìm là</h3>
            '''
            for product in item['product']:
                text += '''
                    <ul>
                        <li>{a} - {b}VNĐ</li>
                    </ul>
                '''.format(a=product['name'], b=product['price'])
            return HttpResponse(text)
    text = '''
        <form method="POST">
            <input name="product" type="text">
            <button type="submit">Submit</button>
        </form>
        <h3>Sản phẩm bạn vừa tìm không tồn tại</h3>
    '''
    return HttpResponse(text)

@csrf_exempt
def login(request):
    print("Phương thức: ", request.method)
    print("Data GET: ", request.GET)
    print("Data POST: ", request.POST)
    text = ""
    if request.method == "GET":
        text = '''
            <form method="POST">
                <input name="username" type="text">
                <input name="password" type="password">
                <button type="submit">Submit</button>
            </form>
        '''
    elif request.method == "POST":
        if request.POST.get("username") == "trungtran" and request.POST.get('password') == "123":
            return HttpResponse("Bạn đã login thành công")
        text = '''
        Bạn đã nhập sai username hoặc mật khẩu
            <form method="POST">
                <input name="username" type="text">
                <input name="password" type="password">
                <button type="submit">Submit</button>
            </form>
        '''
    return HttpResponse(text)

@csrf_exempt
def add_product(request, id_group):
    text = ""
    if request.method == "GET":
        text = '''
            <h3>Nhập sản phẩm</h3>
            <form method="POST">
                <label for="id_product">ID-Product</label><br>
                <input name="id_product" type="text" required><br>
                <label for="name_product">Name</label><br>
                <input name="name_product" type="text" required><br>
                <label for="price">Price</label><br>
                <input name="price" type="text" required><br>
                <button type="submit">Submit</button>
            </form>
        '''
    elif request.method == "POST":
        if request.POST.get('id_product').isnumeric() and request.POST.get('price').isnumeric(): 
            for item in l_sanpham:
                if id_group == item['id']:
                    for product in item['product']:
                        if int(request.POST.get('id_product')) == product['id']:
                            return HttpResponse('Bị trùng id - Vui lòng nhập lại')
                    item['product'].append({
                        "id": int(request.POST.get('id_product')),
                        "name": request.POST.get('name_product'),
                        "price": int(request.POST.get('price'))
                    })
                    return HttpResponse("Tạo sản phẩm thành công")
            text = "Group Id bạn nhập không tồn tại"
        else:
            text = '''
            <h3>Id sản phẩm hoặc giá sản phẩm bị nhập sai kiểu. Vui lòng nhập lại</h3>
            <form method="POST">
                <label for="id_product">ID-Product</label><br>
                <input name="id_product" type="text" required><br>
                <label for="name_product">Name</label><br>
                <input name="name_product" type="text" required><br>
                <label for="price">Price</label><br>
                <input name="price" type="text" required><br>
                <button type="submit">Submit</button>
            </form>
        '''

    return HttpResponse(text)

@csrf_exempt
def add_product2(request):
    
    text = ''
    if request.method == "GET":
        text = '''
            <h3>Nhập sản phẩm</h3>
            <form method="POST">
                <label for="name_product">Tên sản phẩm</label><br>
                <input name="name_product" type="text" required><br>
                <label for="price">Giá</label><br>
                <input name="price" type="text" required><br>
                <label for="quantity">Giá</label><br>
                <input name="quantity" type="text" required><br>
                <button type="submit">Submit</button>
            </form>
        '''
    elif request.method == 'POST':
        error = ''
        if len(request.POST.get('name_product')) < 2:
            error += "Tên sản phẩm phải có ít nhất 2 kí tự<br>"
        if not request.POST.get('price').isnumeric() or int(request.POST.get('price')) < 0:
            error += "Giá cần phải là số dương"
        if not request.POST.get('quantity').isnumeric() or int(request.POST.get('quantity')) < 0:
            error += "Quantity cần phải là số dương"
        if len(error) == 0:
            product = Product(name=request.POST.get('name_product'), price=request.POST.get('price'), quantity=request.POST.get('quantity'))
            product.save()
            text = 'Tạo thành công'
        else:
            text = '''
            <h3>Nhập sản phẩm</h3>
            <form method="POST">
                <label for="name_product">Tên sản phẩm</label><br>
                <input name="name_product" type="text" required><br>
                <label for="price">Giá</label><br>
                <input name="price" type="text" required><br>
                <label for="quantity">Giá</label><br>
                <input name="quantity" type="text" required><br>
                <button type="submit">Submit</button>
            </form>
            <p style="color: red">{error}</p>
        '''.format(error=error)
    return HttpResponse(text)

@csrf_exempt
def product(request, id):
    ### trả về thông tin của product tại id đó
    text = ''
    try:
        product = Product.objects.get(id=id)
        text = f'''
                <h3>Sản phầm bạn tìm là:</h3>
                <h4>{product.name}</h4>
                <p>Price: {product.price}</p>
                <p>Quantity: {product.quantity}</p>
                <p>Group: {product.group.name if product.group != None else "Chưa có group"}</p>
                <a href="/edit_product/{id}">Edit</a>
                <a href="/delete_product/{id}">Delete</a>
            '''
    except Product.DoesNotExist:
        text = 'Không tồn tại sản phẩm'
    return HttpResponse(text)

@csrf_exempt
def list_product(request):
    search_name = request.GET.get('name') if request.GET.get('name') != None else ''
    search_quantity = request.GET.get('quantity') if request.GET.get('quantity') != None else ""
    l_product = Product.objects.all()
    if search_name != '':
        l_product = Product.objects.filter(name__icontains=search_name)
    if search_quantity.isnumeric():
        l_product = l_product.filter(quantity__gte=search_quantity)
    text = f'''
        <form>
            <input value="{search_name}" name="name" placeholder="Tên sản phẩm">
            <input value="{search_quantity}" name="quantity" placeholder="Số lượng sản phẩm">
            <button type="submit">Search</button>
        </form>
        <button><a href="/add_group_product2">Add Group</a></button>
        <button><a href="/add_product2">Add Product</a></button>
    '''
    ### access vào DB khi ta sử dụng dữ liệu
    for product in l_product:
        text += f'''
                <h3>Sản phầm bạn tìm là:</h3>
                <h4>{product.name}</h4>
                <p>Price: {product.price}</p>
                <p>Quantity: {product.quantity}</p>
                <p>Group: {product.group.name if product.group != None else "Chưa có group"}</p>
                <button><a href="/edit_product/{product.id}">Edit</a></button>
                <button><a href="/delete_product/{product.id}">Delete</a></button>
            '''

    return HttpResponse(text)

@csrf_exempt
def edit_product(request, id):
    product = Product.objects.get(id=id) 
    group_product = ""
    for gp in GroupProduct.objects.all():
        group_product += f"<option value='{gp.id}'>{gp.name}</option>"
        # "".join([f"<option value='{gp.id}'>{gp.name}</option>"for gp in GroupProduct.objects.all()])
    if request.method == 'GET':
        text = f'''
            <h3>Nhập sản phẩm</h3>
            <form method="POST">
                <label for="name_product">Tên sản phẩm</label><br>
                <input value="{product.name}" name="name_product" type="text" required><br>
                <label for="price">Giá</label><br>
                <input value="{product.price}" name="price" type="text" required><br>
                <label for="quantity">Giá</label><br>
                <input value="{product.quantity}" name="quantity" type="text" required><br>
                <select name="group">
                    <option value="">Không có group</option>
                    {group_product}
                </select>
                <button type="submit">Submit</button>
            </form>
        '''
    elif request.method == 'POST':
        name = request.POST.get('name_product')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        group = request.POST.get('group')
        if group == "": group = None
        product.name = name
        product.price = price
        product.quantity = quantity
        product.group = GroupProduct.objects.get(id=group)
        product.save()
        return redirect(f'/product/{id}')

    return HttpResponse(text)

@csrf_exempt
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/list_product')

@csrf_exempt
def add_group_product2(request):
    text = ''
    if request.method == "GET":
        text = '''
            <h3>Nhập sản phẩm</h3>
            <form method="POST">
                <label for="name">Tên group</label><br>
                <input name="name" type="text" required><br>
                <button type="submit">Submit</button>
            </form>
        '''
        return HttpResponse(text)
    elif request.method == 'POST':
        product = GroupProduct(name=request.POST.get('name'))
        product.save()
        return redirect('/list_product')
    
def list_group(request): 
    l_group = GroupProduct.objects.all()
    text = '<h3>Các group đang có</h3>'
    for gr in l_group:
        # ds_product = Product.objects.filter(group=gr)
        # quantity = ds_product.count()
        ds_product = gr.product_set.all()
        quantity = ds_product.count()
        text += f'''
                <h4>{gr.name}</h4>
                <h5>Số lượng sản phẩm: {quantity}</h5>
                <button><a href="/group/{gr.id}">Edit</a></button>
            '''
    return HttpResponse(text)

def group(request, id):
    text = ''
    try:
        gd = GroupProduct.objects.get(id=id)
        ds_product = gd.product_set.all()
        quantity = len(ds_product)
        
        ds_product = "".join([f'''
                <h4>{product.name}</h4>
                <p>Price: {product.price}</p>
                <p>Quantity: {product.quantity}</p>
            ''' for product in ds_product])

        text = f'''
                <button><a href="/list_product">Back</a></button>
                <h4>{gd.name}</h4>
                <h5>Số lượng sản phẩm: {quantity}</h5>
                <h3>Danh sách sản phẩm</h3>
                {ds_product}
                <a href="/edit_product/{id}">Edit</a>
                <a href="/delete_product/{id}">Delete</a>
            '''
    except Product.DoesNotExist:
        text = 'Không tồn tại sản phẩm'
    return HttpResponse(text)
