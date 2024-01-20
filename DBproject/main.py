# Libraries and modules used
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
import typing
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextBrowser, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt, QDateTime, QDate, QDate
import sys
import pyodbc


server = "DESKTOP-51E978F\SSMSRS0001"
database = "BookMySalon2" # Name of database
use_windows_authentication = True # Set to True to use Windows Authentication

# database connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        loadUi('Welcome.ui', self)
        # load welcome file
        
        # function called according to the button clicked
        self.Cliwnt.clicked.connect(self.clientDashboard)
        self.Employee.clicked.connect(self.employeeDashboard)

    def clientDashboard(self):
        # hide previous window
        self.hide() 
        # call to load client dashboard window
        self.client_dashboard_window = ClientDashboardWindow()
        self.client_dashboard_window.show()

    def employeeDashboard(self):
        self.hide()
        # Add functionality for the employee dashboard here
        self.Employee_dashboard_window = EmployeeDashboardWindow()
        self.Employee_dashboard_window.show()
        

class ClientDashboardWindow(QMainWindow):
    def __init__(self):
        super(ClientDashboardWindow, self).__init__()
        loadUi('ClientDashboard.ui', self)

        self.createAcc.clicked.connect(self.CreateAcc)
        self.login.clicked.connect(self.LoginScreen)


    def CreateAcc(self):
        self.hide()
        self.CreateAcc_window = CreateAccWindow()
        self.CreateAcc_window.show()

    def LoginScreen(self):
        self.hide()
        self.LoginScreenwindow = LoginScreenWindow()
        self.LoginScreenwindow.show()

class LoginScreenWindow(QMainWindow):
    def __init__(self):
        super(LoginScreenWindow, self).__init__()
        loadUi('ClientLogin.ui', self)
        
        self.login.clicked.connect(self.checkInfo)
        self.back.clicked.connect(self.goBack)
        
    def goBack(self):
        self.hide()
        self.goBacktoWelcome_window = MyMainWindow()
        self.goBacktoWelcome_window.show()

    def checkInfo(self):
        username = self.username.text()
        password = self.password.text()
        if not username or not password:
            if not username:
                warning = QMessageBox()
                warning.setText("Please enter a username.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            elif not password:
                warning = QMessageBox()
                warning.setText("Please enter a password.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            
            return
        else:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                sql_query = "SELECT UserName, Password FROM Account WHERE UserName = ? AND Password = ?"
                cursor.execute(sql_query, (username, password))
                
                result = cursor.fetchone()
                if result is None:
                    warning = QMessageBox()
                    # warning.setWindowTitle("Confirmation Box")
                    warning.setText("Incorrect password or username. Try again!")
                    warning.setIcon(QMessageBox.Icon.Warning)
                    warning.addButton(QMessageBox.StandardButton.Ok)
                    warning.exec()
                else:
                    warning = QMessageBox()
                    # warning.setWindowTitle("Confirmation Box")
                    warning.setText("Account login successful. You can now book an appointment!")
                    warning.setIcon(QMessageBox.Icon.Information)
                    warning.addButton(QMessageBox.StandardButton.Ok)
                    warning.exec()
                    self.bookAppp(username)
        
    def bookAppp(self, username):
        self.hide()
        self.bookAppOrView_window = BookApporViewWindow(username)
        self.bookAppOrView_window.show()

class CreateAccWindow(QMainWindow):
    def __init__(self):
        super(CreateAccWindow, self).__init__()
        loadUi('CreateAcc.ui', self)
        
        self.Confirm.clicked.connect(self.check_text)
        self.Back.clicked.connect(self.backtomain)

    def get_username(self, username):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query_username = """select username from account where username = ?"""
        cursor.execute(sql_query_username, (username))
        result_username = cursor.fetchone()
        connection.commit()
        connection.close()
        return result_username
    
    def get_email(self, email):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query_email = """select email from customer where email = ?"""
        cursor.execute(sql_query_email, (email))
        
        result_email = cursor.fetchone()
        connection.commit()
        connection.close()
        return result_email

        
    def check_text(self):
        name = self.name.text()
        contactNo = self.contactNo.text()
        email = self.email.text()
        dob = self.dateEdit.date()
        username = self.Username.text()
        password = self.password.text()
        gender = self.comboBox.currentText()
        city = self.city.text()
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        usernames = self.get_username(username)
        emails = self.get_email(email)
        
        # if  name==' ' or contactNo==' ' or email==' ' or username==' ' or password==' ' or dob>QDate.currentDate():
        if not name or not contactNo or not email or not username or not password or dob>QDate.currentDate():
        # Check if the text contains any numbers
            if not name:
                warning = QMessageBox()
                warning.setText("Please write your name.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            
            elif not contactNo:
                warning = QMessageBox()
                warning.setText("Please provide your contact number.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            elif not email:
                warning = QMessageBox()
                warning.setText("Please provide your email.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            
            elif not username:
                warning = QMessageBox()
                warning.setText("Please provide a username.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
                
            elif not password:
                warning = QMessageBox()
                warning.setText("Please provide a password.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            
            elif not city:
                warning = QMessageBox()
                warning.setText("Please enter your city.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            elif dob>QDate.currentDate():
                warning = QMessageBox()
                warning.setText("Please enter the correct date of birth.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

        else:
            if len(contactNo)>6 or len(contactNo)<6:
                warning = QMessageBox()
                warning.setText("Contact number should have 6 digits.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            elif not any(char.isdigit() for char in username):
                warning = QMessageBox()
                warning.setText("Username requires at least one number.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            elif not any(char.isdigit() for char in password):
                warning = QMessageBox()
                warning.setText("Password requires at least one special character.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            elif usernames is not None:
                warning = QMessageBox()
                warning.setText("Username already exists, choose a different username.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            elif emails is not None:
                warning = QMessageBox()
                warning.setText("Account already exists for this email, try again.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
            else:
                sql_query = """INSERT INTO CUSTOMER
                ([Name], [Contact_number], [Email])
            VALUES (?, ?, ?)"""
                cursor.execute(sql_query, (name, contactNo, email))
                connection.commit()
                connection.close()
                self.add_loginInfo(email, username, password)

    def add_loginInfo(self, email, username, password):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query2 = "select customerID from customer WHERE email = ?;"
        cursor.execute(sql_query2, (email))
        result = cursor.fetchone()
        sql_query = """INSERT INTO Account
    ([UserName], [Password], [customerID])
        VALUES (?, ?, ?)"""
        cursor.execute(sql_query, (username, password, result[0]))
        connection.commit()
        confirmation = QMessageBox()
        confirmation.setText("Your account has been created, you can login now.")
        confirmation.setIcon(QMessageBox.Icon.Information)
        confirmation.addButton(QMessageBox.StandardButton.Ok)
        confirmation.exec()
        self.redirectLogin()
        connection.close()
        
            
    def backtomain(self):
        self.hide()

    def redirectLogin(self):
        self.hide()
        self.LoginScreenwindow = LoginScreenWindow()
        self.LoginScreenwindow.show()
       

class BookApporViewWindow(QMainWindow):
    def __init__(self, username):
        super(BookApporViewWindow, self).__init__()
        loadUi('BookOrView.ui', self)
        self.username = username
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "select customerID from account WHERE username = ?;"
        cursor.execute(sql_query, (username))
        result = cursor.fetchone()
        customerID = result[0]
        connection.commit()
        connection.close()
        self.bookAppt.clicked.connect(lambda: self.bookApp(username, customerID))
        self.viewAppt.clicked.connect(lambda: self.viewApp(username, customerID))


    def bookApp(self, username, customerID):
        self.hide()
        self.bookApp_window = BookApptWindow(username, customerID)
        self.bookApp_window.show()

    def viewApp(self, username, customerID):
        self.hide()
        self.viewApp_window = ViewApptWindow(username, customerID)
        self.viewApp_window.show()

class EmployeeDashboardWindow(QMainWindow):
    def __init__(self):
        super(EmployeeDashboardWindow, self).__init__()
        loadUi('EmporManager.ui', self)
        self.emplogin.clicked.connect(self.showEmpLoginWindow)

    def showEmpLoginWindow(self):
        self.hide()
        self.emp_login_window = EmpLoginWindow()
        self.emp_login_window.show()

        
class EmpLoginWindow(QMainWindow):
    def __init__(self):
        super(EmpLoginWindow, self).__init__()
        loadUi('EmpLogin.ui', self)

        self.pushButton.clicked.connect(self.checkLogin)

        self.pushButton_2.clicked.connect(self.goBack)

    def checkLogin(self):
        name = self.lineEdit.text()
        employee_id = (self.lineEdit_2.text())
        salon_id = (self.lineEdit_4.text())
        if not name or not employee_id or not salon_id:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please fill in all fields.')
            return
        # if name == ' ' or employee_id == ' ' or salon_id == ' ':
        #     if name == ' ':
        #         warning = QMessageBox()
        #         warning.setText("Please enter your name.")
        #         warning.setIcon(QMessageBox.Icon.Warning)
        #         warning.addButton(QMessageBox.StandardButton.Ok)
        #         warning.exec()
        #     elif employee_id == ' ':
        #         warning = QMessageBox()
        #         warning.setText("Please enter your ID.")
        #         warning.setIcon(QMessageBox.Icon.Warning)
        #         warning.addButton(QMessageBox.StandardButton.Ok)
        #         warning.exec()
        #     elif salon_id == ' ':
        #         warning = QMessageBox()
        #         warning.setText("Please enter your salon ID.")
        #         warning.setIcon(QMessageBox.Icon.Warning)
        #         warning.addButton(QMessageBox.StandardButton.Ok)
        #         warning.exec()
        else:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            sql_query = "SELECT Name, EmployeeID, SalonID FROM Employee WHERE Name = ? AND EmployeeID = ? AND SalonID = ?"
            cursor.execute(sql_query, (name, int(employee_id,), int(salon_id,)))

            result = cursor.fetchone()
            if result is None:
                warning = QMessageBox()
                warning.setText("No such employee found. Try again.")
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()

            else:
                warning = QMessageBox()
                warning.setText("Employee login successful. You can now proceed!")
                warning.setIcon(QMessageBox.Icon.Information)
                warning.addButton(QMessageBox.StandardButton.Ok)
                warning.exec()
                connection.close()
                # Redirect to manager dashboard
                self.redirectToManagerDashboard(int(employee_id), int(salon_id))        

    def redirectToManagerDashboard(self, employee_id, salon_id):
        self.manager_dashboard_window = managerDashboardWindow(employee_id, salon_id)
        self.manager_dashboard_window.show()
        self.hide()

    def goBack(self):
        self.hide()
        self.employee_dashboard_window = EmployeeDashboardWindow()
        self.employee_dashboard_window.show()

class managerDashboardWindow(QMainWindow):
    def __init__(self, employee_id, salon_id):
        super(managerDashboardWindow, self).__init__()
        loadUi('ManagerDashboard.ui', self)
        self.inventory.clicked.connect(lambda: self.inventoryWindow(employee_id, salon_id))
        self.update.clicked.connect(lambda: self.updateService(employee_id, salon_id))
        self.monthlyRep.clicked.connect(lambda: self.monthlyReport(employee_id, salon_id))

    def inventoryWindow(self, employee_id, salon_id):
        self.inventory_window = InventoryWindow(employee_id, salon_id)
        self.inventory_window.show()

    def updateService(self, employee_id, salon_id):
        self.updateServices_window = UpdateServicesWindow(employee_id, salon_id)
        self.updateServices_window.show()

    def monthlyReport(self, employee_id, salon_id):
        self.monthlyReport_window = MonthlyReportWindow(employee_id, salon_id)
        self.monthlyReport_window.show()
            
class InventoryWindow(QMainWindow):
    def __init__(self, employee_id, salon_id):
        super(InventoryWindow, self).__init__()
        loadUi('Inventory.ui', self)

        # Autofill Manager ID, Salon ID
        self.lineEdit.setText(str(employee_id))
        self.lineEdit_2.setText(str(salon_id))
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        
        # Connect search button
        self.pushButton_5.clicked.connect(lambda: self.searchInventory(salon_id))

    def searchInventory(self, salon_id):
        product_id = int(self.lineEdit_3.text())
        product_name = self.lineEdit_4.text()

        # Access Inventory table for the specified ProductID
        self.populateInventoryData(product_id, salon_id)
        self.pushButton_6.clicked.connect(lambda: self.orderProd(product_id, salon_id))

    def orderProd(self, product_id, salon_id):
        suppRow = self.tableWidget.currentRow()
        suppID = int(self.tableWidget.item(suppRow, 2).text())
        prodName = (self.tableWidget.item(suppRow, 1).text())
        self.orderProd_window = OrderProdWindow(product_id, salon_id, suppID, prodName)
        self.orderProd_window.show()

    def populateInventoryData(self,product_id,salon_id):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = """
            SELECT i.ProductID, p.Product_name, s.SupplierID, i.QuantityLeft
            FROM Inventory AS i
            JOIN Product p on p.productID = i.ProductID
            JOIN Suppliers AS s ON i.ProductID = s.ProductID
            WHERE i.SalonID = ? AND i.ProductID = ?
        """

        cursor.execute(sql_query, (salon_id, product_id))

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def clearTable(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        
class OrderProdWindow(QMainWindow):
    def __init__(self, product_id, salon_id, suppID, prodName):
        super(OrderProdWindow, self).__init__()
        loadUi('ReOrder.ui', self)

         # Autofill Salon ID
        self.salonid.setText(str(salon_id))
        self.salonid.setDisabled(True)
        self.product_id.setText(str(product_id))
        self.product_id.setDisabled(True)
        self.supplier_id.setText(str(suppID))
        self.supplier_id.setDisabled(True)
        self.prodname.setText(str(prodName))
        self.prodname.setDisabled(True)
        
        # Connect order button
        self.pushButton_6.clicked.connect(lambda: self.placeOrder(salon_id, product_id, suppID))

    def placeOrder(self, salon_id, product_id, suppID):
        try:
            quantity_ordered = int(self.quantity.text())

            # Insert values into the Order table
            self.insertOrder(salon_id, product_id, suppID, quantity_ordered)
            self.updateInventory(salon_id, product_id, suppID, quantity_ordered)
            # Show confirmation message
            self.showConfirmation()

            # Close the window after successful order
            self.close()
        except ValueError:
            # Show warning for invalid input
            self.showWarning("Invalid input. Please enter integer values for Product ID, Supplier ID, and Quantity.")

    def updateInventory(self, salon_id, product_id, suppID, quantity_ordered):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Assuming Order table has columns OrderID, SalonID, ProductID, SupplierID, QuantityOrdered
        sql_query = """
            UPDATE Inventory
SET QuantityLeft = QuantityLeft + ?
WHERE SalonID = ? AND ProductID = ?
        """

        cursor.execute(sql_query, (quantity_ordered,salon_id, product_id))
        connection.commit()
        connection.close()

    def insertOrder(self, salon_id, product_id, supplier_id, quantity_ordered):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Assuming Order table has columns OrderID, SalonID, ProductID, SupplierID, QuantityOrdered
        sql_query = """
            INSERT INTO Orders (SalonID, ProductID, SupplierID, QuantOrdered)
            VALUES (?, ?, ?, ?)
        """

        cursor.execute(sql_query, (salon_id, product_id, supplier_id, quantity_ordered))
        connection.commit()
        connection.close()

    def showConfirmation(self):
        QMessageBox.information(self, 'Order Placed', 'Order placed successfully!')

    def showWarning(self, message):
        QMessageBox.warning(self, 'Warning', message)

class UpdateServicesWindow(QMainWindow):
    def __init__(self, employee_id, salon_id):
        super(UpdateServicesWindow, self).__init__()
        loadUi('AddDeleteServices (1).ui', self)

        self.populateServices_table(salon_id)
        self.add.clicked.connect(lambda: self.addService(salon_id))
        self.delete_2.clicked.connect(lambda: self.deleteService(salon_id))
        self.Ok.clicked.connect(lambda: self.hide())

    def populateServices_table(self, salon_id):
        self.service.setRowCount(0)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select s.servicesID, s.duration, s.name, s.description, s.price from services as s join salon_serv ss on ss.servicesID = s.servicesID where ss.salonID = ?"
        # SQL query to fetch services data
        cursor.execute(sql_query, (salon_id))

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.service.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.service.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.service.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def addService(self, salon_id):
        # Get input values from line edits
        service_name = self.service_2.text()
        price = float(self.price.text())  # Assuming price is a float
        description = self.desc.text()
        duration = int(self.dur.text())  # Assuming duration is an integer
        product_needed = int(self.products.text())

        # Insert into Services table
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_insert_service = """
            INSERT INTO Services (Name, Description, Price, Duration, ProductID)
            VALUES (?, ?, ?, ?, ?)
        """

        cursor.execute(sql_insert_service, (service_name, description, price, duration, product_needed))
        connection.commit()

        # Get the newly inserted ServicesID
        cursor.execute("SELECT @@IDENTITY")
        services_id = cursor.fetchone()[0]

        # Insert into Salon_Serv table
        sql_insert_salon_serv = """
            INSERT INTO Salon_Serv (ServicesID, SalonID)
            VALUES (?, ?)
        """

        cursor.execute(sql_insert_salon_serv, (services_id, salon_id))
        connection.commit()

        connection.close()

        # Display confirmation message
        confirm = QMessageBox()
        confirm.setText("New service has been added.")
        confirm.setIcon(QMessageBox.Icon.Information)
        confirm.addButton(QMessageBox.StandardButton.Ok)
        confirm.exec()

        # Refresh the services table
        self.populateServices_table(salon_id)


    def deleteService(self, salon_id):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        servRow = self.service.currentRow()
        servID = int(self.service.item(servRow, 0).text())
        sql_query = "delete from Salon_Serv where servicesID = ?"
        #SQL query to delete service from salon_Serv table where the servicesID is being referenced
        cursor.execute(sql_query, (servID))
        connection.commit()
        
        #SQL query to delete service from Services table
        cursor.execute("DELETE FROM Services WHERE servicesID = ?", (servID,))
        connection.commit()
        
        # message box for confirmation
        confirm = QMessageBox()
        confirm.setText("This service has been deleted.")
        confirm.setIcon(QMessageBox.Icon.Information)
        confirm.addButton(QMessageBox.StandardButton.Ok)
        confirm.exec()
        self.service.removeRow(servRow)
        connection.close()



class MonthlyReportWindow(QMainWindow):
    def __init__(self,employee_id, salon_id ):
        super(MonthlyReportWindow, self).__init__()
        loadUi('MonthlyReport2.ui', self)

        # Autofill fields
        self.lineEdit_2.setText(str(salon_id))
        self.lineEdit_3.setText(self.getSalonName(salon_id))
        self.lineEdit_9.setText(QDate.currentDate().toString("MMMM"))
        self.lineEdit_10.setText(str(QDate.currentDate().year()))
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)

        # Populate other details
        self.monthRep.clicked.connect(lambda: self.populateDetails(salon_id))

        # Connect buttons
        self.Confirm.clicked.connect(self.confirm)
        self.Confirm_2.clicked.connect(self.goBack)

    def getSalonName(self, salon_id):
        
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_query = "SELECT name FROM Salons WHERE SalonID = ?"
        cursor.execute(sql_query, salon_id)
        result = cursor.fetchone()

        connection.close()

        if result:
            return result[0]
        else:
            return ""

    def populateDetails(self, salon_id):
        month = self.lineEdit_9.text()
        month_mapping = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

        # Convert month name to numeric value
        month_numeric = month_mapping.get(month, 1) 
        year = int(self.lineEdit_10.text())

        # Total No. Of Appointments
        total_appointments = self.getTotalAppointments(salon_id, month_numeric, year)
        self.lineEdit_4.setText(str(total_appointments))

        # Total Profit
        total_profit = self.getTotalProfit(salon_id, month_numeric, year)
        self.lineEdit_5.setText(str(total_profit))

        # Average Rating
        average_rating = self.getAverageRating(salon_id, month_numeric, year)
        self.lineEdit_6.setText(str(average_rating))
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        self.lineEdit_6.setDisabled(True)
        
    def getTotalAppointments(self, salon_id, month, year):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "SELECT COUNT(*) FROM Appointment WHERE salonID = ? AND MONTH(date) = ? AND YEAR(date) = YEAR(GETDATE())"
        cursor.execute(sql_query, (salon_id, month))
        result = cursor.fetchone()[0]
        connection.close()
        return result
    
    def getTotalProfit(self, salon_id, month, year):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = """
            SELECT SUM(s.Price)
            FROM Appointment AS a
            JOIN Services AS s ON a.ServicesID = s.ServicesID
            WHERE a.salonID = ? AND MONTH(a.date) = ? AND YEAR(a.date) = YEAR(GETDATE())
        """
        cursor.execute(sql_query, (salon_id, month))
        result = cursor.fetchone()[0]
        connection.close()
        return result if result else 0
    
    def getAverageRating(self, salon_id, month, year):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_query = """
    SELECT AVG(Rating)
    FROM SalonRating
    WHERE salonID = ? AND MONTH(CONVERT(date, [month] + ' 1 ' + CAST([year] AS VARCHAR(4)))) = ?
    AND YEAR(CONVERT(date, [month] + ' 1 ' + CAST([year] AS VARCHAR(4)))) = YEAR(GETDATE())
"""

        cursor.execute(sql_query, (salon_id, month))
        result = cursor.fetchone()[0]
        connection.close()
        return result if result else 0
    
    def confirm(self):
        QMessageBox.information(self, "Confirmation", "Monthly report details confirmed!")
        self.goBack()

    def goBack(self):
        self.hide()

class BookApptWindow(QMainWindow):
    def __init__(self, username, customerID):
        super(BookApptWindow, self).__init__()
        loadUi('BookAppointment.ui', self)

        self.findSalons.clicked.connect(lambda: self.populate_salonList_table())
        self.salonList.itemSelectionChanged.connect( self.getSelectedSalon)
        self.book.clicked.connect(lambda: self.bookConfirm(username,customerID))
        self.Cancel.clicked.connect(lambda: self.cancel(username))

    def cancel(self, username):
        self.hide()
        self.bookAppOrView_window = BookApporViewWindow(username)
        self.bookAppOrView_window.show()

    def onRadioButtonToggled(self):
        # Determine which radio button is selected
        if self.COD.isChecked():
            payMeth = "Cash"
        elif self.credit.isChecked():
            payMeth = "Credit Card"
        elif self.debit.isChecked():
           payMeth = "Debit Card"
        return payMeth

    def bookConfirm(self, username, customerID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        stylistRow = self.stylist.currentRow()
        serviceRow = self.serviceList.currentRow()
        salonRow = self.salonList.currentRow()
        datee = self.stylist.item(stylistRow, 3).text()
        timee = self.stylist.item(stylistRow, 4).text()
        payMeth = self.onRadioButtonToggled()
    
        print(datee, timee)
        servicesID = int(self.serviceList.item(serviceRow, 0).text())
        employeeID = int(self.stylist.item(stylistRow, 1).text())
        salonID = int(self.salonList.item(salonRow, 0).text())
        print(customerID, datee, timee, servicesID, employeeID, salonID)

        self.bookConfirm_window = bookingConfirm(username,customerID, salonID, servicesID, employeeID, payMeth, datee, timee)
        self.bookConfirm_window.show()
        
    def populate_salonList_table(self):
        city = self.city.text()
        if city == " ":
            confirm = QMessageBox()
            confirm.setText("Please enter your city.")
            confirm.setIcon(QMessageBox.Icon.Information)
            confirm.addButton(QMessageBox.StandardButton.Ok)
            confirm.exec()
        else:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            sql_query = "Select s.salonID, s.name, sr.rating, s.plotno, s.streetno, s.city from salons s join salonrating sr on s.salonID = sr.salonID and city = ? "
            # Write SQL query to fetch salons data
            cursor.execute(sql_query, (city))

            # Fetch all rows and populate the table
            for row_index, row_data in enumerate(cursor.fetchall()):
                self.salonList.insertRow(row_index)
                for col_index, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    self.salonList.setItem(row_index, col_index, item)
            
            connection.close()

            # Adjust the column widths for better display
            header = self.salonList.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
            header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
    
    def getSelectedSalon(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        # self.salonList.setRowCount(0)
        self.serviceList.setRowCount(0)
        self.stylist.setRowCount(0)
        salonRow = self.salonList.currentRow()
        salonID = int(self.salonList.item(salonRow, 0).text())
        self.populate_services_table(salonID)
        self.populate_stylist_table(salonID)
        

    def populate_services_table(self, salonID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select s.servicesID, s.name, s.description, s.price, s.duration from services as s join salon_serv as ss on ss.servicesID = s.servicesID and ss.salonID = ?"
        # SQL query to fetch services data
        cursor.execute(sql_query, (salonID))

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.serviceList.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.serviceList.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.serviceList.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def populate_stylist_table(self, salonID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select e.name, e.employeeID, e.Specialty, s.date, s.time from employee as e, availability as s where s.employeeID = e.employeeID and e.specialty != 'Manager' and e.salonID = ?"
        #SQL query to fetch stylists and their availability
        cursor.execute(sql_query, (salonID))

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.stylist.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.stylist.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.stylist.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

class bookingConfirm(QMainWindow):
    def __init__(self, username, customerID, salonID, servicesID, employeeID, payMeth, datee, timee):
        super(bookingConfirm, self).__init__()
        loadUi('BookConfirmation.ui', self)

        self.setCustName(customerID)
        self.setSalonName(salonID)
        self.setServiceName(servicesID)
        self.setVals(datee, timee, payMeth)
        totalAmt = self.getTotAMT(servicesID)

        # setting all fields to disabled so that there arent inconsistencies in data retrieval
        self.name.setDisabled(True)
        self.salonName.setDisabled(True) 
        self.service.setDisabled(True) 
        self.date.setDisabled(True)
        self.time.setDisabled(True)
        self.charges.setDisabled(True)   
        self.paymeth.setDisabled(True)   
        
        self.confirm.clicked.connect(lambda: self.insertApp(customerID, datee,
                           timee, servicesID, employeeID, salonID, payMeth, totalAmt, username))
        self.back.clicked.connect(lambda: self.backToBook(username, customerID))

    def backToBook(self, username, customerID):
        self.hide()
        self.bookApp_window = BookApptWindow(username, customerID)
        self.bookApp_window.show()

    def setVals(self, datee, timee, payMeth):
        self.date.setText(datee)
        self.time.setText(timee)
        self.paymeth.setText(payMeth)

    def setCustName(self, customerID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select name from customer where customerID = ?"
        #SQL query to fetch customers data
        cursor.execute(sql_query, (customerID))
        result = cursor.fetchone()
        self.name.setText(result[0])

    def setSalonName(self, salonID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select name from salons where salonID = ?"
        #Write SQL query to fetch salon name
        cursor.execute(sql_query, (salonID))
        result = cursor.fetchone()
        self.salonName.setText(result[0])

    def setServiceName(self, servicesID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select name from Services where servicesID = ?"
        #SQL query to fetch service name 
        cursor.execute(sql_query, (servicesID))
        result = cursor.fetchone()
        self.service.setText(result[0])

    def getTotAMT(self, servicesID):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select price from services where servicesID = ?"
        #SQL query to fetch service price
        cursor.execute(sql_query, (servicesID))
        result = cursor.fetchone()
        self.charges.setText(str(result[0]))
        return result[0]
    
    def insertApp(self, customerID, datee,timee, servicesID, employeeID, salonID, payMeth, totalAmt, username):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = """INSERT INTO Appointment
    ([customerID], [date], [time], [servicesID], [employeeID], [salonID])
    VALUES (?, ?, ?, ?, ?, ?)"""

        cursor.execute(sql_query, (customerID, datee,
                           timee, servicesID, employeeID, salonID))
        connection.commit()
        connection.close()
        self.getAppt(employeeID, customerID, salonID, servicesID, payMeth, totalAmt, username)
        
    
    def getAppt(self, employeeID, customerID, salonID, servicesID, payMeth, totalAmt, username):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select apptID from appointment where employeeID = ? and customerID = ? and salonID = ? and servicesID = ?"
        # SQL query to fetch AppointmentID
        cursor.execute(sql_query, (employeeID, customerID, salonID, servicesID))
        result = cursor.fetchone()
        apptID = result[0]
        self.insertReceipt(apptID, customerID, salonID, servicesID, payMeth, totalAmt, employeeID, username)
        # inserting receipt

    def insertReceipt(self, apptID, customerID, salonID, servicesID, payMeth, totalAmt, employeeID, username):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_query =  """INSERT INTO Receipt
    ([apptID], [customerID], [PayMethod], [TotalAmt])
    VALUES (?, ?, ?, ?)"""

        cursor.execute(sql_query, (apptID, customerID,
                           payMeth, totalAmt))
        connection.commit()
        connection.close()
        
        confirm = QMessageBox()
        confirm.setText("Your appointment has been booked!")
        confirm.setIcon(QMessageBox.Icon.Information)
        confirm.addButton(QMessageBox.StandardButton.Ok)
        confirm.exec()
        self.viewAppt(username, customerID)
        
    def viewAppt(self, username, customerID):
        self.viewAppt_Window = ViewApptWindow(username, customerID)
        self.viewAppt_Window.show()


class ViewApptWindow(QMainWindow):
    def __init__(self, username, customerID):
        super(ViewApptWindow, self).__init__()
        loadUi('ViewAppt.ui', self)

        self.populate_AppList_table(customerID)
        self.cancel.clicked.connect(lambda: self.cancelApp())
        self.cancel_2.clicked.connect(lambda: self.backToDash(username))

    def populate_AppList_table(self, customerID):
        print("populate function")
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        sql_query = "Select a.apptID, a.customerID, a.employeeID, a.date, a.time, a.servicesID, a.salonID from appointment as a where a.customerID = ?"
        #SQL query to fetch appointment data
        cursor.execute(sql_query, customerID)

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.appointment.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.appointment.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.appointment.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def backToDash(self, username):
        self.hide()
        self.bookAppOrView_window = BookApporViewWindow(username)
        self.bookAppOrView_window.show()


    def backtoApp(self, username, customerID):
        self.hide()
        self.bookApp_window = BookApptWindow(username, customerID)
        self.bookApp_window.show()

    def cancelApp(self):
        print("cancel function")
        appRow = self.appointment.currentRow()
        appID = int(self.appointment.item(appRow, 0).text())
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Receipt WHERE apptID = ?", (appID,))
        connection.commit()
        sql_query = "delete from appointment where apptID = ?"
        #SQL query to delete appointment from the main table appointment and where it is being referenced i.e reciept
        cursor.execute(sql_query, (appID))
        connection.commit()
        
        # message box for confirmation
        confirm = QMessageBox()
        confirm.setText("Your appointment has been cancelled.")
        confirm.setIcon(QMessageBox.Icon.Information)
        confirm.addButton(QMessageBox.StandardButton.Ok)
        confirm.exec()
        self.appointment.removeRow(appRow)
        connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    app.exec()

