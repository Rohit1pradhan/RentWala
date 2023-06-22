import io
from random import randint

from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import user, reset, activations, varify_mail, AddHouse
from api.serializers import userserializer, resetserializer, activationserializer, varifyserializer, addhouseserializer


# Create your views here.



def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'registration.html')

def varify(request):
    tdata=request
    serializer=varifyserializer(data=tdata)
    if serializer.is_valid():
        serializer.save()
        print("check mail")
        return HttpResponse("otp sand")
    return Response(serializer.errors)


@method_decorator(csrf_exempt,name='dispatch')
class registeration(APIView):
    def post(self,request):
        pdata=request.data
        mail = pdata.get('email_id')
        try:
            odata = user.objects.get(email_id=mail)
        except user.DoesNotExist:
            odata = None
        if odata == None:
            serializer = userserializer(data=pdata)
            if serializer.is_valid():
                serializer.save()
            data=user.objects.get(email_id=mail)
            id=data.id
            st='off'
            send={'user_id':id,'activation':st}
            activation=activationserializer(data=send)
            if activation.is_valid( raise_exception=True):
                activation.save()
            OTP=rendom()
            print(odata)
            send_mail(
                "Registration Varification",
                f"your otp is {OTP} plese dont shere it with anyone",
                "2018pcemerohit58@poornima.org",
                ['"'+mail+'"'],
                fail_silently=False,
            )
            data=user.objects.get(email_id=mail)
            id=data.id
            sendData={"user_id":id,"verify_otp":OTP}
            v=varify(sendData)
            print("mail send")
            userID=id
            print(userID)
            return render(request,'verify.html')

        if odata != None:
            result = {"msg": 'you are alrady a user'}
            return JsonResponse(result, content_type='application/json')

    def get(self,request):
        OTP=request.GET.get('otp')
        print(OTP)
        try:
            olddata=varify_mail.objects.get(verify_otp=OTP)
            print(olddata)
            x=0
        except varify_mail.DoesNotExist:
            olddata=None
        if olddata is not None:
            x=1
            return render(request,'home.html',{'register':x})
        print(olddata)
        return HttpResponse("incorect OTP")




def login(request):
    mail=request.GET.get('email')
    password=request.GET.get('password')
    try:
        odata=user.objects.get(email_id=mail)
    except user.DoesNotExist:
        odata=None
    if odata!=None:
        userdata=user.objects.get(email_id=mail)
        pas=userdata.password
        if pas==password:
            name=userdata.name
            id=userdata.id
            activation=activations.objects.get(user_id=id)
            data=activation.activation
            if data.lower()=='on':
                x=1
            else:
                x=0
            return render(request,'login.html',{'name':name,'data':x,'id':id})
        else:
            result = {"msg": "password is incorect"}
            return render(request,'home.html',{'data':1})
    result = {"msg": "You are not a register user plese first register yourself"}
    return render(request,'home.html',{'value':1})


def rendom():
    otp=0
    for i in range(1,7):
        otp=otp*10+randint(0,9)
    return otp

# @csrf_exempt
# def forgetpassword(request):
#     data=request.body
#     scream=io.BytesIO(data)
#     pdata=JSONParser().parse(scream)
#     mail=pdata.get('email_id')
#     try:
#         odata=user.objects.get(email_id=mail)
#     except user.DoesNotExist:
#         odata=None
#     if odata!=None:
#         password=pdata.get('password')
#         pas=odata.password
#         id=odata.id
#         if pas!=password:
#             try:
#                 olddata=reset.objects.get(user_id=id)
#             except reset.DoesNotExist:
#                 olddata=None
#             if olddata==None:
#                 x=rendom()
#                 data1={"user_id":id,"OTP":x}
#                 serializer=resetserializer(data=data1)
#                 if serializer.is_valid():
#                     serializer.save()
#                     result={"OTP":x}
#                     return JsonResponse(result,content_type='application/json')
#             olddata.delete()
#             x = rendom()
#             data1 = {"user_id": id, "OTP": x}
#             serializer = resetserializer(data=data1)
#             if serializer.is_valid():
#                 serializer.save()
#                 result = {"OTP": x}
#                 return JsonResponse(result, content_type='application/json')
#
#         else:
#             return HttpResponse('password is currect')
#     return HttpResponse("not found data regarding to this mail id plese check mail id again")


def forpassword(request):
    return render(request,'forgatPassword.html')
@method_decorator(csrf_exempt,name='dispatch')
class ForgetPassword(APIView):
    def post(self,request):
        data=request.data
        mail=data.get('mail')
        try:
            odata=user.objects.get(email_id=mail)
        except user.DoesNotExist:
            odata=None
        if odata==None:
            return HttpResponse('not a registerd user')
        id=odata.id
        try:
            rdata=reset.objects.get(user_id=id)
        except reset.DoesNotExist:
            rdata=None
        print(rdata)
        if rdata!=None:
            rdata.delete()
        else:
            print('ok')
        x = rendom()
        data1 = {"user_id": id, "OTP": x}
        serializer = resetserializer(data=data1)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        send_mail(
            "Reset Password",
            f"your otp is {x} plese dont shere it with anyone",
            "2018pcemerohit58@poornima.org",
            ['"' + mail + '"'],
            fail_silently=False,
        )
        return render(request,'ResetPassword.html',{'id':id})

# @csrf_exempt
# def resetpassword(request):
#     data=request.body
#     stream=io.BytesIO(data)
#     pdata=JSONParser().parse(stream)
#     otp=pdata.get('OTP')
#     id=pdata.get('user_id')
#     print(id)
#     password=pdata.get('password')
#     userdata=user.objects.get(id=id)
#     print(userdata)
#     odata=reset.objects.get(user_id=id)
#     print(odata)
#     potp=odata.OTP
#     if int(potp)==int(otp):
#         # result={"password":password}
#         # print(result)
#         serializer=userserializer(userdata,data=pdata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse("password change successfully")
#         return Response(serializer.errors)
#     return HttpResponse("incorrect otp")


class ResetPassword(APIView):
    def post(self,request):
        data=request.data
        print(data.get('otp'))
        print(data.get('password'))
        print(data.get('id'))
        id=data.get('id')
        password=data.get('password')

        odata=reset.objects.get(user_id=id)
        potp=odata.OTP
        x=1
        if int(potp)!=int(data.get('otp')):
            x=0
            print(x)
            return render(request,'ResetPassword.html',{'otp':x,'id':id})
        userdata = user.objects.get(id=id)
        result = {"password": password}
        serializer = userserializer(userdata, data=result, partial=True)
        z=0
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            z=1
            return render(request,'home.html',{'reset':z})
        return HttpResponse('ok')
class actavation(APIView):
    def post(self,request):
        id=int(request.data.get('user_id'))
        odata=activations.objects.get(user_id=id)
        status=odata.activation
        if status.lower()=='off':
            x='on'
        else:
            x='off'
        data={'activation':x}
        serializer=activationserializer(odata, data=data ,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        data1=user.objects.get(id=id)
        name=data1.name
        if x=='on':
            id1=1
        else:
            id1=0
        print(id1)
        return render(request,'login.html',{'name':name,'data':id1,'id':id})
    def get(self,request):
        odata=activations.objects.filter(activation='on')
        l=[]
        print(odata)
        for i in odata:
            l1=[]
            id=i.user_id
            data=user.objects.get(id=id)
            l1.append(data.name)
            l1.append(data.email_id)
            l1.append(data.mobile_number)
            l1.append(data.city)
            l.append(l1)
        return render(request,'FindTenant.html',{'len':len(odata),'data':l})


def searchfortanent(request):
    data=activations.objects.all()
    l=[]
    for i in data:
        x=i.activation
        if str(x).upper()=="On".upper():
            d={}
            id=i.user_id
            olddata=user.objects.get(id=id)
            d["name"]=olddata.name
            d["number"]=olddata.mobile_number
            d["current_city"]=i.current_city
            l.append(d)
    return HttpResponse(l)

def allusers(request):
    data=user.objects.all()
    l=[]
    for i in data:
        serializer = userserializer(i)
        jdata = JSONRenderer().render(serializer.data)
        l.append(jdata)
    return HttpResponse(l)


def addproparty(request):
    return render(request,'houses.html')

@method_decorator(csrf_exempt,name='dispatch')
class addhouse(APIView):
    def post(self,request):
        serializer=addhouseserializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'data save'})
        return HttpResponse('Error in serializer validations')

    def get(self,request):
        data=AddHouse.objects.all()
        l = []
        for i in data:
            l1=[]
            serializer = addhouseserializer(i)
            l1.append(serializer.data['owner_name'])
            l1.append(serializer.data['owner_contect_number'])
            l1.append(serializer.data['house_type'])
            l1.append(serializer.data['rent'])
            l1.append(serializer.data['house_facing'])
            l1.append(serializer.data['area'])
            l1.append(serializer.data['conditions'])
            l1.append(serializer.data['Facilities'])
            l1.append(serializer.data['city'])
            l1.append(serializer.data['picture1'])
            l1.append(serializer.data['picture2'])
            l1.append(serializer.data['picture3'])

            l.append(l1)
        print(type(l))

        return render(request,'Rent Houses.html',{'data':l,'length':len(l)})



# class demo(APIView):
#     def get(self,request):
#         return render(request,'forgatPassword.html')
# class demo1(APIView):
#     def get(self,request):
#         return render(request,'ResetPassword.html')












