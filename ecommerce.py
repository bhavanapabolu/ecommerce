import csv
orders={}
products={}
def add_products():
   pid=input("Enter Product ID:")
   if pid in products:
      print("Product Already Exists")
   else:
      name=input("Enter Product Name:")
      price=float(input("Enter Price:"))
      stock=int(input("Enter Stock Quantity:"))
      products[pid]={"name":name,"price":price,"stock":stock}
      print("Products Added Successfully")
def view_products():
  if not products:
      print("No Products Available")
  else:
      print("Available Products:")
      for pid,details in products.items():
          print(f"ID:{pid},Name:{details['name']},Price:{details['price']},Stock:{details['stock']}")
def place_order():
   pid =input("Enter product Id to buy:")
   if pid in products:
     quantity=int(input("Enter Quantity:"))
     if 0<quantity<=products[pid]["stock"]:
        cname=input("Enter your Name:")
        total=quantity*products[pid]["price"]
        products[pid]["stock"]-=quantity
        if cname not in orders:
           orders[cname]=[]
        orders[cname].append({
        "product":products[pid]["name"],
        "qty":quantity,
        "total":total
         })
        print(f"Order Placed! Total:{total}")
     else:
        print("Insufficient Stock or Invalid Quantity")
   else:
     print("Product Not Found")
def view_orders():
   if not orders:
      print("No  orders placed")
   else:
      for cname,orders_list in orders.items():
         print(f"\n Orders for {cname}:")
      for order in orders_list:
         print(f"-{order['product']}x{order['qty']}={order['total']}")
def export_orders_to_csv():
   filename="orders.csv"
   file=open(filename,mode='w',newline='')
   writer=csv.writer(file)
   writer.writerow(["Customer Name","ProductName","Quantity","Total Amount"])
   for cname,orders_list in orders.items():
      for order in orders_list:
        writer.writerow([cname,order["product"],order["qty"],order["total"]])
def menu():
  while True:
    print("\n E-commerece Application")
    print("1.Add Products")
    print("2.View Products")
    print("3.place order")
    print("4.View Orders")
    print("5.Export Orders to CSV")
    print("6.Exit")
    choice=input("Choose an option(1-6):")
    if choice=="1":
       add_products()
    elif choice=="2":
       view_products()
    elif choice=="3":
       place_order() 
    elif choice=="4":
       view_orders()
    elif choice=="5":
       export_orders_to_csv()
    elif choice=="6":
       print("Thank You For Using The Application")
       break
menu()
