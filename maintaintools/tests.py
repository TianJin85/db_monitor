from django.http import HttpResponse
from django.views import View

#
"""文件上传"""


class FileUploadView(View):
    '''
    上传文件接口
    '''

    def post(self, request):
        """
            返回上传的文件地址
        """
        print(self)
        print(request)
        print(request.POST)
        try:
            files = request.FILES.getlist('file', None)  # 文件
            print('1111111111111')
            print(files)
            data = request.POST.get('data', None)  # 携带参数
            print('22222222222')
            print(data)
            # if (data[0] == '' & data == None):
            #     return HttpResponse({"code": 400, "msg": u"上传失败，请选择需要上传的服务器"})

            # from db_monitor import settings
            # if filemkdir not in settings.DATA_FILENAAME or not files:
            #     return HttpResponse({"code":400, "msg":u"上传参数无效"})
            # if filemkdir == 'attachment':
            #     self.IMG_result = self.attachment_uploading(files)
            # else:
            #     self.IMG_result = self.file_upload(files=files,mk=filemkdir)
            # return HttpResponse(self.IMG_result)
            return HttpResponse('999999999999999999999999999')
        except Exception as e:
            print(e)
            return HttpResponse({"code": 400, "msg": u"上传失败"})
# class GetPaerml(View):
# def filepost(self):
#     print(self)
#     print('22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222')
#     print(self.method)
#     file_all=self.request.files.get('file',None)
#     print(file_all)


# if file and allowed_file(file.filename):
#     filename = now + '_' + str(current_user) + '_' + file.filename
#     filename = secure_filename(filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     file_uploaded = True

# print(type(request))
# if self.method == 'POST':
#     print('111112222222222222')
#     myfile = self.FILES.get('File')
#     print(myfile)
#     if myfile is None:
#         print('上传文件失败')
#         return HttpResponse('上传文件失败')
#     else:
#
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         print(myfile)
#         print('2222222222222222222222')
#         print(filename)
#         return HttpResponse('123456')
# return HttpResponse('222222222222222222')
#
# def geifile(request):
#     print(type(request))
#     print('11111111111111111111')
#     # if request.method=='POST':
#     #     File = request.FILES('upload')
#     #     print(File)
#     # filename=None
#     # if request.method == 'POST' and request.FILES.get('file'):
#     #     from django.core.files.storage import FileSystemStorage
#     #     myfile = request.FILES['file']
#     #     fs = FileSystemStorage()
#     #     filename = fs.save(myfile.name, myfile)
#     #     print(filename)
#     if request.method == 'POST':
#         print('111112222222222222')
#         myfile = request.FILES.get('file')
#         print(myfile)
#         if myfile is None:
#             print('上传文件失败')
#             return HttpResponse('上传文件失败')
#         else:
#
#             fs = FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             print(myfile)
#             print('2222222222222222222222')
#             print(filename)
#             return HttpResponse('123456')
#
#     # val = json.loads(request.body)
#
#     # return HttpResponse('123456')
