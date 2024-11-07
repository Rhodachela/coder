from db import connection
import mysql.connector

class Product:
    def __init__(self, name, category, stock_quantity, price):
        self.name = name
        self.category = category
        self.stock_quantity = stock_quantity
        self.price = price
    def __str__(self):
        return f"{self.name} ({self.category})"

class InventoryManager:
    def __init__(self):
        self.mydb, self.mycursor = connection()
        if self.mydb is None or self.mycursor is None:
            print("Failed to connect to database")

    def add_product(self, product):
        if self.mydb is None or self.mycursor is None:
            print("Connection failed. Unable to add products")
            return
        sql = "INSERT INTO products (name,category,stock_quantity,price) VALUES(%s,%s,%s,%s)"
        val = (product.name, product.category, product.stock_quantity, product.price)

        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(f"{product.name} added successfully")
        except mysql.connector.Error as err:
            print(f"Failed to add {product.name}: {err}")

    def view_all_products(self):
        if self.mydb is None or self.mycursor is None:
            print("Unable to fetch products. Connection failed")
            return

        self.mycursor.execute("SELECT * FROM products")
        prods = self.mycursor.fetchall()
        if prods:
            for item in prods:
                print(f" Id: {item[0]}, Name: {item[1]}, Category: {item[2]}, Stock_quantity: {item[3]}, Price: {item[4]}")
        else:
            print("No products found in the inventory")
        
    def update_stock(self):
        if self.mydb is None or self.mycursor is None:
            print(f"{product_name} not updated")
            return

        product_name = input("Enter product to update: ")
        new_quantity = input("Enter the new quantity: ")
        self.mycursor.execute("SELECT * FROM products WHERE name = %s", (product_name,))
        item = self.mycursor.fetchone()
        if item:
            sql = "UPDATE products SET stock_quantity = %s WHERE name = %s"
            val = (new_quantity, product_name)

            try:
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print(f"Stock updated for {product_name} to {new_quantity}")
            except mysql.connector.Error as err:
                print(f"Failed to update {product_name}: {err}")
        else:
            print(f"{product_name} not found in the stock")
    
    def delete_product(self):
        if self.mydb is None or self.mycursor is None:
            print("Connection failed. Product not deleted")
            return
        product_name = input("Enter product name to delete: ")
        self.mycursor.execute("SELECT * FROM products WHERE name = %s", (product_name,))
        item = self.mycursor.fetchone()
        if item:
            sql = "DELETE FROM products WHERE name =%s"
            val = (product_name,)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(f"{product_name} deleted succesfully")
        else:
            print(f"Deletion failed. Product doesn't exist in the stock")
    
    def low_stock_alert(self):
        return 