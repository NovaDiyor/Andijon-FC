from django.shortcuts import redirect
from main.models import *
from rest_framework import authentication, permissions
from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics


@api_view(['POST'])
def Register(request):
    try:
        username = request.data['username']
        password = request.data['password']
        country = request.data['country']
        users = User.objects.create_user(username=username, password=password, country=country )
        token = Token.objects.create(user=users)
        data = {
            'username': username,
            'user_id': users.id,
            'token': token.key,
        }
        return Response(data)

    except Exception as err:
        return Response({'error': f'{err}'})



@api_view(['POST'])
def login(request):
    try:
        username = request.data['username']
        password = request.data['password']
        try:
            usrs = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            if user is not None:
                status = 200
                token, created = Token.objects.get_or_create(user=user)
                data = {
                    'username': username,
                    'user_id': usrs.id,
                    'token': token.key,
                }
            else:
                status = 403
                message = 'Username yoki parol xato!'
                data = {
                    'status': status,
                    'message': message,
                }
        except User.DoesNotExist:
            status = 404
            message = 'Bunday foydalanuvchi mavjud emas!'
            data = {
                'status': status,
                'message': message,
            }
        return Response(data)
    except Exception as er:
        return Response({"error": f'{er}'})


# club
@api_view(['GET'])
def Clubs(request):
    context = {
        'club': FcSerializer(Fc.objects.all(), many=True).data,
    }
    return Response(context)

# news
@api_view(['GET'])
def New(request):
    new = News.objects.all().order_by('-date')
    context = {
        'news': NewsSerializer(new, many=True).data,
        'vidoe': VideosSerializer(Videos.objects.all().order_by('-id')[0:3], many=True).data,
        'videos': VideosSerializer(Videos.objects.all().order_by('-id')[0:6], many=True).data,
        'logo': AdvertiserSerializer(Advertiser.objects.all(),many=True).data,
        'info': InfoSerializer(Info.objects.last()).data,
    }
    return Response(context)

# media
@api_view(['GET'])
def Media(request):
    context = {
        'mashhur': VideosSerializer(Videos.objects.filter(is_top=1), many=True).data,
        'logo': AdvertiserSerializer(Advertiser.objects.all(), many=True).data,
        'info': InfoSerializer(Info.objects.last()).data,
    }
    return Response(context)

@api_view(['GET'])
def Shop(request):
    context = {
        'shop': ProductSerializer(Product.objects.all(), many=True).data,
        'logo': AdvertiserSerializer(Advertiser.objects.all(), many=True).data,
        'info': InfoSerializer(Info.objects.last()).data,
    }
    return Response(context)

@api_view(['GET'])
def Academy(request):
    context = {
        'about': AcademySerializer(About.objects.last()).data,
        'academy': AcademySerializer(About.objects.all().order_by('-id')[0:5], many=True).data,
        'logo': AdvertiserSerializer(Advertiser.objects.all(),many=True).data,
        'info': InfoSerializer(Info.objects.last()).data,
    }
    return Response(context)
# single-shop
@api_view(['GET'])
def Singleshop(request, pk):
    context = {
        'singleshop': ProductSerializer(Product.objects.get(id=pk)).data,
        'shop': ProductSerializer(Product.objects.filter(rating=5).order_by('-id')[0:4], many=True).data,
        'logo': AdvertiserSerializer(Advertiser.objects.all(), many=True).data,
        'info': InfoSerializer(Info.objects.last()).data,
    }
    return Response(context)


@api_view(['GET'])
def Singlenews(request, pk):
    context = {
        'singlenews': NewsSerializer(News.objects.get(id=pk)).data,
        'shop': NewsSerializer(News.objects.all().order_by('-id')[0:4], many=True).data,
        'logo': AdvertiserSerializer(Advertiser.objects.all(), many=True).data,
        'info': InfoSerializer(Info.objects.last()).data,
    }
    return Response(context)

# single_video
@api_view(['GET'])
def Singlevideo(request, pk):
    context = {
        'singlevideo': VideosSerializer(Videos.objects.get(id=pk)).data,
        'video': VideosSerializer(Videos.objects.filter(is_top=True).order_by('-id')[0:4], many=True).data,
        'logo': AdvertiserSerializer(Advertiser.objects.all(), many=True).data,
        'info': InfoSerializer(Info.objects.last()).data,
    }
    return Response(context)

# wishlist
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def WishlistAdd(request, pk):
    user = request.user
    product = request.POST.get('product')
    Wishlist.objects.create(user=user, product_id=product)

    return Response('ok')



# order item create
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def OrderItemCreate(request, pk):
    product = Product.objects.get(id=pk)
    quantity = request.POST.get('quantity')
    OrderItem.objects.create(product=product, quantity=quantity)
    return Response('ok')

# order create
@api_view(['POST'])
def OrderCreate(request):
    order = request.POST.getlist('order')
    user = request.user
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    phone_number = request.POST.get('phone_number')
    address = request.POST.get('address')
    postal_code = request.POST.get('postal_code')
    email = request.POST.get('email')
    region = request.POST.get('region')
    city = request.POST.get('city')
    create = Order.objects.create(user=user, name=name, surname=surname, phone_number=phone_number, address=address,
                         postal_code=postal_code, email=email, region_id=region, city=city)

    for i in order:
        create.order_item.add(OrderItem.objects.get(id=i))

    return Response('Siz Sotib oldingiz adminlar siz bilan bog`lanadi')

# game
@api_view(['GET'])
def game_view(request):
    context = {
        'game': GameSerializer(Game.objects.all(),many=True).data,
    }
    return Response(context)
# game andijon chart
@api_view(['GET'])
def game_chart(request):
    point = 0
    won = 0
    equality = 0
    defeat = 0
    top = 0
    fail = 0
    ballratio = 0
    game = Game.objects.all()
    for i in game:
        if i.guest_goal > i.host_goal:
            point += 1
            won += 1
            top += i.guest_goal
            fail += i.host_goal
            ballratio += 3
        elif i.guest_goal == i.host_goal:
            point += 1
            equality += 1
            top += i.guest_goal
            fail += i.host_goal
            ballratio += 1
        elif i.guest_goal < i.host_goal:
            point += 1
            defeat += 1
            top += i.guest_goal
            fail += i.host_goal
        context = {
            'game': point,
            'won': won,
            'draw': equality,
            'defeat': defeat,
            'score': top,
            'conceded': fail,
            'point': ballratio,
        }
    return Response(context)



