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

def sanpham(request, id):
    text = "Không có thông tin về sản phẩm"
    for item in L_sanpham:
        if id == item["id"]:
            text = "ID: {a}<br>Tên sản phẩm: {b}<br>Giá: {c}".format(a = item["id"], b = item["name"], c = item["price"])
    return HttpResponse(text)

def danhsachsanpham0(request):
    text = ""
    for item in L_sanpham:
        text_product = ""
        for product in item['product']:
            text_product += '''<br>
                ID: {a}<br>
                Tên sản phẩm: {b}<br>
                Giá: {c}<br><hr>'''.format(
                    a=product['id'],b=product['name'],c=product['price']
                )
        text += '''ID nhóm: {a}<br>
                    Tên nhóm: {b}<br>
                    Danh sách sản phẩm: {c}<br><hr>'''.format(
                        a=item['id'],b=item['name'],c=text_product
                    )
    return HttpResponse(text)

def danhsachsanpham(request, id):
    ### id group
    ## trả về danh sách sản phẩm của group đó
    text = "Không có thông tin vê nhóm sản phẩm"
    for item in L_sanpham:
        if id == item["id"]:
            text = ""
            for product in item["product"]:
                text += "ID: {a}<br>Tên sản phẩm: {b}<br>Giá: {c}<br><hr>".format(
                    a = product["id"], b = product["name"], c = product["price"])
    return HttpResponse(text)

def sanpham2(request,id_group,id_product):
    ### kiểm tra xem id_product có phải là sản phẩm của id_group hay không
    ### nếu là sản phẩm của id_group thì in tên group và thông tin của sản phẩm ra
    ##### nếu không phải:
    ####### TH1: sản phẩm không tồn tại ở trong bất kỳ group nào
    ######### Không có thông tin vê sản phẩm
    ####### TH2: sản phẩm có tồn tại nhưng thuộc group khác
    ######### In ra ~~> sản phẩm <tên sản phẩm> thuộc group <tên group> có ID group là <id_group>
    return HttpResponse("sanpham có 2 tham số là {a}, {b}".format(
        a=id_group, b=id_product
    ))

def handler404(request, exception):
    return HttpResponse("Bạn đang vào 1 đường dẫn sai")

from django.views.decorators.csrf import csrf_exempt

count = 0

@csrf_exempt
def test_request(request):
    global count
    print("Đường dẫn:",request.path)
    print("Dữ liệu GET:",request.GET)
    if request.method=="GET":
        # ten = request.GET['ten'] if "ten" in request.GET else ""
        ten = request.GET.get("ten")
        return HttpResponse(str(ten) + '''<br>
            <form>
                <input name="ten">
                <input name="tuoi">
                <button type="submit">Submit</button>
            </form>
        ''')
    elif request.method=="POST":
        count += 1
        return HttpResponse("Count đã được tăng")

def search_product(request):
    text = '''
        <form>
            <input name="product" placeholder="Sản phẩm">
            <button type="submit">Submit</button>
        </form>
    '''
    return HttpResponse(text)

@csrf_exempt
def login(request):
    print("Phương thức:",request.method)
    print("Data GET:",request.GET)
    print("Data POST:",request.POST)
    text = ""
    if request.method == "GET":
        text = '''
            <form method="POST">
                <input name="username" placeholder="Username">
                <input type="password" name="password" placeholder="Password">
                <button type="submit">Submit</button>
            </form>
        '''
    elif request.method == "POST":
        if request.POST.get("username") == "hatrang" and request.POST.get("password") == "123":
            return HttpResponse("Bạn đã login thành công")
        text = '''
            Bạn đã nhập sai username hoặc mật khẩu
            <form method="POST">
                <input name="username" placeholder="Username">
                <input type="password" name="password" placeholder="Password">
                <button type="submit">Submit</button>
            </form>
        '''
    return HttpResponse(text)

def add_product(request,id_group):
    ### tạo form để thêm sản phẩm vào group
    ##### form có 3 input: id, tên sản phẩm và giá
    ##### form có method POST
    ####### xử lý form
    ######### xử lý trong POST 
    ######### không có trường nào bị rỗng, id và giá phải là dạng số (sử dụng hàm isnumeric)
    ######### nếu form không đúng định dạng ~~> gen lại form cho người dùng nhập lại
    ######### nếu form đúng định dạng thì thêm sản phẩm mới và trả về trình duyệt tạo sản phẩm thành công
    return HttpResponse()