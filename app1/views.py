from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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

    text = "Không có thông tin về sản phẩm"

    for category in L_sanpham2:
        if id == category["id"]:
            text = ""
            for item in category["product"]:
                text += "ID: {a}<br>Tên sản phẩm: {b}<br>Giá: {c}<br><hr>".format(a = item["id"], b = item["name"], c = item["product"])

    return HttpResponse(text)

def sanpham2(request, group, id):
    text = "Không có thông tin về sản phẩm"

    for item in L_sanpham2:
        for i in item["product"]:
            if id == i["id"]:
                if group == item["id"]:
                    text = "Group: {d}<br>ID: {a}<br>Tên sản phẩm: {b}<br>Giá: {c}".format(a = i["id"], b = i["name"], c = i["price"], d = item["name"])
                else:
                    text = "Sản phẩm {b} thuộc nhóm {c} có ID là {a}<br>".format(a = i["id"], b = i["name"], c = item["name"])

    return HttpResponse(text)

count = 0

def test_request(request):
    global count
    print("Phương thức truy cập: ", request.method)
    print("Đường dẫn: ", request.path)
    print("Dữ liệu GET: ", request.GET)
    if request.method == "GET":
        ten = request.GET.get("ten")
        return HttpResponse(str(ten) + '''<br>
            <form>
                <input name = "ten">
                <input name = "tuoi">
                <button type = "submit">Submit</button>
            </form>
        ''')
    elif request.method == "POST":
        count += 1
        return HttpResponse("Phương thức truy cập: " + request.method + "<br>Count đã được nâng")
    
def timsp(request):
    ten = request.GET.get("ten")
    if ten == "":
        return HttpResponse(str(ten) + '''<br>
            <form>
                <input name = "ten" placeholder = "Sản phẩm">
                <button type = "submit">Submit</button>
            </form>
        ''')
    else:
        for item in L_sanpham2:
            for i in item:
                if ten == i:
                    return HttpResponse("")

@csrf_exempt           
def login(request):
    print("Phương thức truy cập: ", request.method)
    print("Data GET: ", request.GET)
    print("Data POST: ", request.POST)
    text = ""
    if request.method == "GET":
        text = '''    
            <form method = "POST">
                <input name = "username" placeholder="Username">
                <input type = "password" name = "password" placeholder = "Password">
                <button type = "submit">Submit</button>
            </form>
        '''
    elif request.method == "POST":
        if request.POST.get("username") == "lanphuong" and request.POST.get("password") == "huhu":
            return HttpResponse("Bạn đã đăng nhập thành công!")
        text = ''' 
            Bạn đã nhập sai username hoặc password<br>   
            <form method = "POST">
                <input name = "username" placeholder="Username">
                <input type = "password" name = "password" placeholder = "Password">
                <button type = "submit">Submit</button>
            </form>
        '''
    return HttpResponse(text)

@csrf_exempt
def add_product(request, group):
    text = ""
    if request.method == "GET":
        text = '''    
            <form method = "POST">
                <input type = "number" name = "id" placeholder="ID sản phẩm">
                <input name = "name" placeholder = "Tên sản phẩm">
                <input type = "number" name = "price" placeholder = "Giá sản phẩm">
                <button type = "submit">Submit</button>
            </form>
        '''
    elif request.method == "POST":
        if request.POST.get("id") != "" and request.POST.get("name") != "" and request.POST.get("price") != "":
            for item in L_sanpham2:
                for i in item["product"]:
                    if id == i["id"]:
                        return HttpResponse("ID đã tồn tại. Hãy nhập ID khác." + '''    
            <form method = "POST">
                <input type = "number" name = "id" placeholder="ID sản phẩm">
                <input name = "name" placeholder = "Tên sản phẩm">
                <input type = "number" name = "price" placeholder = "Giá sản phẩm">
                <button type = "submit">Submit</button>
            </form>
        ''')

            a = request.POST.get("id") 
            b = request.POST.get("name") 
            c = request.POST.get("price")
            for item in L_sanpham2:
                if group == item["id"]:
                    item["product"].append({
                        "id": a,
                        "name": b,
                        "price": c
                    })
            return HttpResponse("Bạn đã thêm sản phẩm {b} có ID là {a} và giá là {c} vào danh mục {d}.".format(a = a, b = b, c = c, d = item["name"]))
        text = "Vui lòng nhập đủ cả 3 trường dữ liệu!" + '''    
            <form method = "POST">
                <input type = "number" name = "id" placeholder="ID sản phẩm">
                <input name = "name" placeholder = "Tên sản phẩm">
                <input type = "number" name = "price" placeholder = "Giá sản phẩm">
                <button type = "submit">Submit</button>
            </form>
        '''
    return HttpResponse(text)