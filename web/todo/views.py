from django.shortcuts import render, redirect
from redis import Redis


redis = Redis(host='redis', port=6379)


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.models import Product
from todo.serializers import ProductSerializer
from django.views.decorators.csrf import ensure_csrf_cookie


class ProductList(APIView):
    """
    List all snippets, or create a new snippet.
    """
   
    def get(self, request, format=None):                     # 方法名稱是get, 表示是跟host 要資料，注意參數中有個request
        product = Product.objects.all()                     # Snippet的資料庫物件.all() 全部的
        serializer = ProductSerializer(product, many=True)  # 全部的 丟到序列化器
        return Response(serializer.data)                     # 用Response 把序列化器的返回.data 包起丟回去
    # @ensure_csrf_cookie
    def post(self, request, format=None):                    # 方法名稱是post，表示要把資料丟過來，注意參數中有個request
        serializer = ProductSerializer(data=request.data)    # 把丟過來的資料(request.data) 丟到序列化器。
        if serializer.is_valid():                            # 驗證一下，通過就儲存，返回201，不然就丟error，返回400
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):                                # 繼承APIView類，Detail表示會丟出個別資料
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:                                                 # 用一個try包起來 有就返回個別資料，沒有就給404，注意這裡沒有request，因此是給下面的方法叫用的
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):                 # 方法名稱是get，有參數request，先給get_object檢查一下，並且拿出資料庫物件，然後丟進序列化器
        snippet = self.get_object(pk)                        # 最後用Response返回序列化.data
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)
    # @ensure_csrf_cookie
    def put(self, request, pk, format=None):                 # 方法名稱是put,要跟get一樣，最後把資料存進資料庫
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # @ensure_csrf_cookie
    def delete(self, request, pk, format=None):              # 方法名稱是delete，要跟get一樣，最後執行刪除的動作。
        Product = self.get_object(pk)
        Product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)