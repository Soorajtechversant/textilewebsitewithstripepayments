from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse,resolve 
from membership.views import *

class TestHome(SimpleTestCase):
    def test_home(self):
        url = reverse ('products/customer/customer_index')
        self.assertEquals(resolve(url).func.view_class,Customer_index)



class ProductTest(SimpleTestCase):

    def test_reg(self):
        url = reverse ('products/registration/registration')
        self.assertEquals(resolve(url).func.view_class,Registration)


    def test_auth_login(self):
        url = reverse('products/registration/login')
        self.assertEquals(resolve(url).func.view_class,Login)


    def test_owner(self):
        url = reverse('products/productshop_owner/owner_index')
        self.assertEquals(resolve(url).func.view_class,Owner_index)

    def test_add_product(self):
        url = reverse('products/productshop_owner/add_product')
        self.assertEquals(resolve(url).func.view_class,Add_product)

    # def test_bookproduct(self):
    #     url = reverse('products/customer/book_product')
    #     print(response['location'])
    #     self.assertEquals(resolve(url).func.view_class,Book_product)    


    # def test_editprodcuct(self):
    #     url = reverse('products/productshop_owner/edit_product' , args=['id=product_id'])
    #     self.response = self.client.get(url)
    #     self.assertEqual(self.response.status_code, 200)
        # self.assertEquals(resolve(url).func.view_class,Edit_product)

    # def test_detail(self):
    #     url = reverse('detail')
    #     self.assertEquals(resolve(url).func.view_class,productDetailView)


    # def test_Delete_product(self):
    #     url = reverse('products/productshop_owner/Delete_product')
    #     self.assertEquals(resolve(url).func.view_class,Delete_product)



# class PaymentTest(SimpleTestCase):

#     def test_api_checkout_session(self):
#         url = reverse('api_checkout_session')
#         self.assertEquals(resolve(url).func.view_class,create_checkout_session)

#     def test_downgradeiption(self):
#         url = reverse('cancel')
#         self.assertEquals(resolve(url).func.view_class,PaymentFailedView)


#     def test_premium(self):
#         url = reverse('premium')
#         self.assertEquals(resolve(url).func.view_class,premium)

#     def test_auth_settings(self):
#         url = reverse('settings')
#         self.assertEquals(resolve(url).func.view_class,settings)


#     def test_updateaccounts(self):
#         url = reverse('updateaccounts')
#         self.assertEquals(resolve(url).func.view_class,updateaccounts)


#     def test_delete_subscription(self):
#         url = reverse('delete')
#         self.assertEquals(resolve(url).func.view_class,delete)

#     def test_modify(self):
#         url = reverse('modify')
#         self.assertEquals(resolve(url).func.view_class,modify)

#     def test_unpause(self):
#         url = reverse('unpause')
#         self.assertEquals(resolve(url).func.view_class,unpause)


#     def test_success(self):
#         url = reverse('success')
#         self.assertEquals(resolve(url).func.view_class,success)

#     def test_downgrade(self):
#         url = reverse('downgrade')
#         self.assertEquals(resolve(url).func.view_class,downgrade)


    # def test_logout(self):
    #     url = reverse('logout')
    #     self.assertEquals(resolve(url).func,Logout)


