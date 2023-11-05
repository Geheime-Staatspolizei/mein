from flask import Flask
from flask import request
from classes.Token import Token
from classes.Schemas.ProductRecord import ProductRecord
from classes.Schemas.UserRecord import UserRecord
from classes.Schemas.UserGet import UserGet
from classes.INITDB import INITDB
from classes.Roles import ADMIN_ROLE
from classes.Roles import USER_ROLE
from classes.Roles import ROOT_ROLE
from  classes.FIRSEVERROOT import FIRSTEVERROOT

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"

@app.route("/INITIAL_ROOT_ROLE", methods=["POST"])
def initialrootrole(): 
    email = request.json['email']
    FIRSTEVERROOT(email)
    return "Sucssesfuly created root role"

@app.route("/INIT")
def init():
    INITDB()
    return "DB Initialized"

@app.route("/createuser", methods=["POST"])
def createuser(): 
    email = request.json['email']
    tel = request.json['tel']
    name = request.json['name']
    password = request.json['password']
    token = UserRecord().setRole(
        USER_ROLE
        ).setName(
            name
            ).setEmail(
                email
                ).setPassword(
                    password
                    ).setTelephoneNumber(
                        tel
                        ).commit().getToken()
    return {
        "token": token,
    }

@app.route("/gettoken", methods=['POST'])
def gettoken(): 
    by = request.json['by']
    password = request.json['password']
    if by == "email":
        email = request.json['email']
        data = UserGet().byEmail(email).data()
        token = UserRecord().setRole(data[0][4]).setPassword(password).setEmail(email).getToken()
    if by == "phone":
        phone = request.json['phone']
        data = UserGet().byPhone(phone).data()
        token = UserRecord().setRole(data[0][4]).setPassword(password).setTelephoneNumber(phone).getToken()
    if(data[0][0] == password):
        return token
    return {
        "msg": "Wrong password"
    }

@app.route("/add-product/", methods=['POST'])
def addproduct():
    token = request.headers.get('authorization')
    title = request.json['title']
    des = request.json['description']
    price = request.json['price']
    imageUrl = request.json['image']
    timestamp = 0
    ProductRecord().verify(token).roles([ROOT_ROLE, ADMIN_ROLE]).setTitle(
        title
        ).setDescription(
            des
            ).setPrice(
                price
                ).setImageUrl(
                    imageUrl
                    ).setTimestamp(
                        timestamp
                        ).commit()
    return {
        "msg": "Product created successfuly"
    }

@app.route("/paginate-products/")
def paginateproducts(username):
    return f"<p>Hello, World! {username}</p>"

@app.route("/make-order/", methods=['POST'])
def makeorder():
    return f"<p>Create order</p>"

@app.route("/order-done/<order_id>")
def orderdone():
    return f"<p>Hello, World</p>"

@app.route("/pay/<order_id>")  
def pay(order_id):
    return """
    Место для оплаты
    """