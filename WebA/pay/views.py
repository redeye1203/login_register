from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

# Create your views here.


class LoginView(View):

    def post(self,request):

        # 取到表單中提交上來的參數
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not all([username, password]):
            print('參數錯誤')
        else:
            print(username, password)
            if username == 'redeye' and password == '1234':
                # 狀態保持，設置用戶名到cookie中表示登入成功
                response = redirect(reverse('transfer'))
                response.set_cookie('username', username)
                return response
            else:
                print('密碼錯誤')
        return render(request,'login.html')
    def get(self,request):
        return render(request,'login.html')

class TransferView(View):

    def post(self,request):
        # 從cookie中取到用戶名
        username = request.COOKIES.get('username', None)
        # 如果沒有取道，代表沒有登入
        if not username:
            return redirect(reverse('index'))

        to_account = request.POST.get("to_account")
        money = request.POST.get("money")

        print('假裝執行轉帳操作，將當前登入用戶的前轉帳到指定帳戶')
        return HttpResponse('轉帳 %s 元到 %s 成功' % (money, to_account))

    def get(self, request):
        #生成一個隨機碼
        from django.middleware.csrf import get_token
        csrf_token=get_token(request)
        response = render(request, 'transfer.html')

        return response
