from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


def page_404(request):
    return render(request, 'page-404.html')


@login_required(login_url='sign-in')
def dashboard_view(request):
    context = {
    }
    return render(request, 'dashboard.html', context)


def sign_in(request):
    return render(request, 'login.html')


def for_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr.status == 1:
                if usr is not None:
                    login(request, usr)
                    return redirect('dashboard')
                else:
                    return redirect('sign-in')
            else:
                return redirect('sign-in')
        else:
            return redirect('sign-in')
    else:
        return redirect('sign-in')


def logout_view(request):
    logout(request)
    return redirect('sign-in')


@login_required(login_url='sign-in')
def reset(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_password = request.POST.get('new-password')
        prove = request.POST.get('confirm-password')
        usr = authenticate(username=user.username, password=password)
        if new_password == prove:
            usr.username = username
            usr.set_password(new_password)
            usr.save()
            return redirect('dashboard')
        return redirect('reset')
    return render(request, 'reset-password.html', {'admin': user})


@login_required(login_url='sign-in')
def staff_view(request):
    return render(request, 'staff.html', {'staff': Staff.objects.all()})


@login_required(login_url='sign-in')
def player_view(request):
    pl = []
    player = Players.objects.all()
    for i in range(1, 100):
        pl.append(i)
    for i in player:
        if i.number in pl:
            pl.remove(i.number)
    context = {
        'player': Players.objects.all(),
        'number': pl
    }
    return render(request, 'players.html', context)


@login_required(login_url='sign-in')
def fc_view(request):
    context = {
        'fc': Fc.objects.filter(status=1),
        'player': Players.objects.all(),
        'staff': Staff.objects.all(),
        'stadium': Stadium.objects.all()
    }
    return render(request, 'andijon.html', context)


@login_required(login_url='sign-in')
def club_view(request):
    return render(request, 'club.html', {'club': Fc.objects.filter(status=2)})


@login_required(login_url='sign-in')
def profile_view(request, pk):
    context = {
        'user': User.objects.get(id=pk)
    }
    return render(request, 'profile.html', context)


@login_required(login_url='sign-in')
def advertiser_view(request):
    return render(request, 'advertiser.html', {'advertiser': Advertiser.objects.all()})


@login_required(login_url='sign-in')
def news_view(request):
    return render(request, 'news.html', {'news': News.objects.all()})


@login_required(login_url='sign-in')
def video_view(request):
    return render(request, 'video.html', {'video': Videos.objects.all()})


@login_required(login_url='sign-in')
def info_view(request):
    return render(request, 'info.html', {'info': Info.objects.all()})


@login_required(login_url='sign-in')
def about_view(request):
    return render(request, 'about.html', {'about': About.objects.all()})


@login_required(login_url='sign-in')
def search(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        player = Players.objects.filter(first_name__icontains=name)
        fc = Fc.objects.filter(name__icontains=name)
        pro = Product.objects.filter(name__icontains=name)
        context = {
            'fc': fc,
            'pro': pro,
            'player': player
        }
    return render(request, 'search.html', context)


@login_required(login_url='sign-in')
def get_pl(request, pk):
    pl = Players.objects.get(id=pk)
    context = {
        'player': pl
    }
    return render(request, 'get-search.html', context)


@login_required(login_url='sign-in')
def get_fc(request, pk):
    context = {
        'fc': Fc.objects.get(id=pk)
    }
    return render(request, 'get-search.html', context)


@login_required(login_url='sign-in')
def get_pro(request, pk):
    context = {
        'pro': Product.objects.get(id=pk)
    }
    return render(request, 'get-search.html', context)


@login_required(login_url='sign-in')
def region_view(request):
    return render(request, 'region.html', {'region': Region.objects.all()})


@login_required(login_url='sign-in')
def preview_view(request):
    context = {
        'fc': Fc.objects.filter(status=1),
        'club': Fc.objects.filter(status=2),
        'preview': Preview.objects.all()
    }
    return render(request, 'preview.html', context)


@login_required(login_url='sign-in')
def squad_view(request):
    fc = Fc.objects.get(status=1)
    context = {
        'preview': Preview.objects.all(),
        'team': fc.players.all(),
        'squad': Squad.objects.all()
    }
    return render(request, 'squad.html', context)


@login_required(login_url='sign-in')
def line_view(request):
    return render(request, 'line.html', {'line': Line.objects.all()})


@login_required(login_url='sign-in')
def subs_view(request):
    context = {
        'squad': Squad.objects.all(),
        'line': Line.objects.all(),
        'subs': Substitute.objects.all()
    }
    return render(request, 'subs.html', context)


@login_required(login_url='sign-in')
def game_view(request):
    context = {
        'line': Line.objects.all(),
        'host': Fc.objects.filter(status=1),
        'guest': Fc.objects.filter(status=2),
        'passes': Passes.objects.all(),
        'subs': Substitute.objects.all(),
        'game': Game.objects.all()
    }
    return render(request, 'game.html', context)


@login_required(login_url='sign-in')
def product_view(request):
    context = {
        'product': Product.objects.all(),
        'size': Size.objects.filter(available=True),
        'image': Images.objects.all()
    }
    return render(request, 'product.html', context)


def add_staff(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        name = request.POST.get('name')
        sur_name = request.POST.get('sur-name')
        date = request.POST.get('date')
        image = request.FILES.get("image")
        Staff.objects.create(
            role=role,
            name=name,
            sur_name=sur_name,
            birth=date,
            image=image,
        )
    return redirect('staff')


def add_player(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sur_name = request.POST.get('sur-name')
        number = request.POST.get('number')
        position = request.POST.get('position')
        option = request.POST.get('option')
        date = request.POST.get('date')
        try:
            if option == 'captain':
                captain = True
                sub_captain = False
            elif option == 'sub_captain':
                captain = False
                sub_captain = True
                pl = Players.objects.filter(sub_captain=True)
                if pl.count() >= 3:
                    p = pl[0]
                    p.sub_captain = False
                    p.save()
            elif option == 'player':
                captain = False
                sub_captain = False
            image = request.FILES.get('image')
            Players.objects.create(
                first_name=name,
                last_name=sur_name,
                number=number,
                position=position,
                captain=captain,
                sub_captain=sub_captain,
                birth=date,
                image=image,
            )
            player = Players.objects.filter(captain=True)
            if player.count() > 1:
                p = player[0]
                p.captain = False
                p.sub_captain = True
                p.save()
        except Exception as err:
            print(f'error : {err}')
    return redirect('player')


def add_passes(request):
    context = {
        'passes': Passes.objects.all(),
    }
    if request.method == 'POST':
        passes = request.POST.get('passes')
        successful = request.POST.get('successful')
        status = request.POST.get('status')
        percent = int(successful) / int(passes) * 100
        Passes.objects.create(all=passes, successful=successful, status=status, percent=round(percent))
        return redirect('add-passes')
    return render(request, 'passes.html', context)


def add_stadium_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        StadiumImage.objects.create(img=image)
        return redirect('add-stadium-image')
    return render(request, 'stadium-image.html', {'image': StadiumImage.objects.all()})


def add_stadium(request):
    context = {
        'stadium': Stadium.objects.all(),
        'image': StadiumImage.objects.all()
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        image = request.POST.getlist('image')
        s = Stadium.objects.create(name=name, capacity=capacity)
        for i in image:
            s.image.add(i)
        return redirect('add-stadium')
    return render(request, 'stadium.html', context)


def add_action(request):
    context = {
        'action': Action.objects.all(),
        'club': Fc.objects.all()
    }
    if request.method == 'POST':
        which = request.POST.get('which')
        who = request.POST.get('who')
        action = request.POST.get('action')
        minute = request.POST.get('minute')
        who = Players.objects.get(last_name__icontains=who)
        if who is not None:
            Stadium.objects.create(which_id=which, who_id=who.id, action=action, minute=minute)
        else:
            Stadium.objects.create(which_id=which, club_who=who, action=action, minute=minute)
        return redirect('add-action')
    return render(request, 'action.html', context)


def add_fc(request):
    if request.method == 'POST':
        player = request.POST.getlist('player')
        staff = request.POST.getlist('staff')
        stadium = request.POST.get('stadium')
        name = request.POST.get('name')
        image = request.FILES.get("logo")
        f = Fc.objects.create(stadium_id=stadium, name=name, logo=image, status=1)
        for i in player:
            f.players.add(i)
        for x in staff:
            f.staff.add(x)
    return redirect('fc')


def add_club(request):
    if request.method == 'POST':
        logo = request.FILES.get('logo')
        name = request.POST.get('name')
        trainer = request.POST.get('trainer')
        Fc.objects.create(logo=logo, name=name, trainer=trainer, status=2)
    return redirect('club')


def add_advertiser(request):
    if request.method == 'POST':
        logo = request.FILES.get('logo')
        url = request.POST.get('url')
        Advertiser.objects.create(logo=logo, url=url)
    return redirect('advertiser')


def add_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('name')
        image = request.FILES.get('image')
        date = request.POST.get('date')
        News.objects.create(title=title, text=text, date=date, image=image)
    return redirect('news')


@login_required(login_url='sign-in')
def stadium_image(request, pk):
    stadium = Stadium.objects.get(id=pk)
    context = {
        'image': stadium.image.all()
    }
    return render(request, 'get-image.html', context)


@login_required(login_url='sign-in')
def product_image(request, pk):
    pro = Product.objects.get(id=pk)
    context = {
        'image': pro.image.all()
    }
    return render(request, 'get-product-image.html', context)


@login_required(login_url='sign-in')
def get_stadium(request, pk):
    fc = Fc.objects.get(id=pk)
    stadium = Stadium.objects.get(id=fc.stadium.id)
    context = {
        'stadium': stadium
    }
    return render(request, 'get-stadium.html', context)


@login_required(login_url='sign-in')
def get_player(request, pk):
    fc = Fc.objects.get(id=pk)
    context = {
        'player': fc.players.all()
    }
    return render(request, 'get-player.html', context)


@login_required(login_url='sign-in')
def get_staff(request, pk):
    fc = Fc.objects.get(id=pk)
    context = {
        'staff': fc.staff.all()
    }
    return render(request, 'get-staff.html', context)


def add_video(request):
    if request.method == 'POST':
        video = request.FILES.get('video')
        bio = request.POST.get('bio')
        date = request.POST.get('date')
        is_top = request.POST.get('is_top')
        if is_top == 'True':
            is_top = True
        elif is_top is None:
            is_top = False
        Videos.objects.create(video=video, description=bio, date=date, is_top=is_top)
    return redirect('video')


def add_info(request):
    if request.method == 'POST':
        insta = request.POST.get('insta')
        telegram = request.POST.get('telegram')
        twitter = request.POST.get('twitter')
        youtube = request.POST.get('youtube')
        facebook = request.POST.get('facebook')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        logo = request.FILES.get('logo')
        Info.objects.create(
            insta=insta,
            telegram=telegram,
            twitter=twitter,
            youtube=youtube,
            facebook=facebook,
            phone=phone,
            email=email,
            bio=bio,
            logo=logo)
    return redirect('info')


def add_about(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        text = request.POST.get('text')
        About.objects.create(title=title, image=image, text=text)
    return redirect('about')


def add_preview(request):
    fc = Fc.objects.get(status=1)
    if request.method == 'POST':
        club = request.POST.get('club')
        guest = request.POST.get('guest')
        date = request.POST.get('date')
        day = request.POST.get('match-day')
        if guest == 1:
            guest = club
            host = fc.id
        elif guest == 2:
            guest = fc.id
            host = club
        Preview.objects.create(guest_id=guest, host_id=host, date=date, day=day)
    return redirect('preview')


def add_squad(request):
    if request.method == 'POST':
        team = request.POST.getlist('team')
        game = request.POST.get('game')
        s = Squad.objects.create(game_id=game)
        for i in team:
            s.squad.add(i)
    return redirect('squad')


@login_required(login_url='sign-in')
def get_squad(request, pk):
    squad = Squad.objects.get(id=pk)
    context = {
        'player': squad.team.all()
    }
    return render(request, 'get-squad.html', context)


@login_required(login_url='sign-in')
def get_preview(request, pk):
    squad = Squad.objects.get(id=pk)
    preview = Preview.objects.get(id=squad.preview.id)
    context = {
        'preview': preview
    }
    return render(request, 'get-preview.html', context)


def add_line(request):
    if request.method == 'POST':
        team = request.POST.getlist('team')
        squad = request.POST.get('squad')
        t = Line.objects.create(squad_list_id=squad)
        for i in team:
            t.team.add(i)
    return redirect('line')


def add_subs(request):
    if request.method == 'POST':
        squad = request.POST.get('squad')
        line = request.POST.get('line')
        minute = request.POST.get("minute")
        seconds = request.POST.get('seconds')
        Substitute.objects.create(squad_id=squad, line_id=line, minute=minute, seconds=seconds)
    return redirect('subs')


def add_game(request):
    context = {
        'game': Game.objects.all(),
        'action': Action.objects.all(),
        'pass': Passes.objects.all(),
        'mvp': Players.objects.all(),
        'subs': Substitute.objects.all()
    }
    if request.method == 'POST':
        line = request.POST.get('line')
        goal = request.POST.get('goal')
        h_goal = request.POST.get('h_goal')
        passion = request.POST.get('passion')
        kross = request.POST.get('kross')
        passes = request.POST.get('passes')
        long = request.POST.get('long')
        helps = request.POST.get('helps')
        subs = request.POST.getlist('subs')
        mvp = request.POST.get('mvp')
        g = Game.objects.create(
            line_id=line,
            guest_goal=goal,
            host_goal=h_goal,
            passion=passion,
            passes_id=passes,
            kross_id=kross,
            long_passes_id=long,
            helps_id=helps,
            mvp_id=mvp
        )
        for i in subs:
            g.subs.add(i)
        return redirect('game')
    return render(request, 'game.html', context)


def add_size(request):
    if request.method == 'POST':
        size = request.POST.get('size')
        available = request.POST.get('available')
        if available is None:
            available = False
        elif available == 'True':
            available = True
        Size.objects.create(size=size, available=available)
        return redirect('add-size')
    return render(request, 'size.html', {'size': Size.objects.all()})


def add_images(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        Images.objects.create(image=image)
        return redirect('add-images')
    return render(request, 'images.html', {'image': Images.objects.all()})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        bonus = request.POST.get('bonus')
        text = request.POST.get('text')
        size = request.POST.getlist('size')
        image = request.POST.getlist('image')
        p = Product.objects.create(name=name, price=price, bonus=bonus, text=text, rating=0)
        for i in size:
            p.size.add(i)
        for x in image:
            p.image.add(x)
    return redirect('product')


def add_wishlist(request):
    if request.method == "POST":
        user = request.POST.get('user')
        product = request.POST.get('product')
        Wishlist.objects.create(user_id=user, product_id=product)
    return redirect('wishlist')


def add_region(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Region.objects.create(name=name)
    return redirect('region')


def update_staff(request, pk):
    staff = Staff.objects.get(id=pk)
    if request.method == 'POST':
        role = request.POST.get('role')
        name = request.POST.get('name')
        sur_name = request.POST.get('sur-name')
        date = request.POST.get('date')
        image = request.FILES.get("image")
        staff.role = role
        staff.name = name
        staff.sur_name = sur_name
        staff.birth = date
        if image is None:
            staff.image = staff.image
        else:
            staff.image = image
        staff.save()
        return redirect('staff')
    return render(request, 'update-staff.html', {'staff': Staff.objects.get(id=pk)})


def update_player(request, pk):
    player = Players.objects.get(id=pk)
    pl = []
    players = Players.objects.all()
    for i in range(1, 100):
        pl.append(i)
    for i in players:
        if i.number in pl:
            pl.remove(i.number)
    if request.method == 'POST':
        name = request.POST.get('name')
        sur_name = request.POST.get('sur-name')
        number = request.POST.get('number')
        position = request.POST.get('position')
        image = request.FILES.get('image')
        option = request.POST.get('option')
        if option == 'captain':
            captain = True
            sub_captain = False
        elif option == 'sub_captain':
            captain = False
            sub_captain = True
        elif option == 'player':
            captain = False
            sub_captain = False
        player.first_name = name
        player.last_name = sur_name
        player.number = number
        player.position = position
        player.captain = captain
        player.sub_captain = sub_captain
        if image is None:
            player.image = player.image
        else:
            player.image = image
        player.save()
        return redirect('player')
    return render(request, 'update-player.html', {'player': Players.objects.get(id=pk), 'number': pl})


def update_passes(request, pk):
    passes = Passes.objects.get(id=pk)
    if request.method == 'POST':
        pass_all = request.POST.get('pass-all')
        pass_success = request.POST.get('pass-success')
        status = request.POST.get('status')
        passes.all = pass_all
        passes.successful = pass_success
        passes.status = status
        return redirect('game')
    return render(request, 'update-passes.html', {'passes': Passes.objects.get(id=pk)})


def update_about(request, pk):
    about = About.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.POST.get('image')
        about.title = title
        about.text = text
        if image is None:
            about.image = image.image
        else:
            about.image = image
        about.save()
        return redirect('about')
    return render(request, 'update-about.html', {'about': About.objects.get(id=pk)})


def update_stadium_image(request, pk):
    image = StadiumImage.objects.get(id=pk)
    if request.method == 'POST':
        images = request.FILES.get('image')
        if image is None:
            image.img = images
        else:
            image.img = images.img
        image.save()
        return redirect('add-stadium-image')
    return render(request, 'update-stadium-images.html', {'image': StadiumImage.objects.get(id=pk)})


def update_stadium(request, pk):
    stadium = Stadium.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        stadium_image = request.POST.getlist('stadium')
        stadium.name = name
        stadium.capacity = capacity
        stadium.image = stadium_image
        stadium.save()
        return redirect('stadium')
    return render(request, 'update-stadium.html', {'stadium': Stadium.objects.get(id=pk)})


def update_fc(request, pk):
    fc = Fc.objects.get(id=pk)
    context = {
        'fc': fc,
        'players': Players.objects.all(),
        'staff': Staff.objects.all(),
        'stadium': Stadium.objects.all()
    }
    if request.method == 'POST':
        player = request.POST.getlist('player')
        staff = request.POST.getlist('staff')
        name = request.POST.getlist('name')
        logo = request.FILES.get('logo')
        stadium = request.POST.get('stadium')
        fc.players = player
        fc.staff = staff
        fc.name = name
        fc.stadium = stadium
        if logo is None:
            fc.logo = fc.logo
        else:
            fc.logo = logo
        fc.save()
        return redirect('fc')
    return render(request, 'update-fc.html', context)


def update_club(request, pk):
    club = Fc.objects.get(id=pk)
    if request.method == 'POST':
        logo = request.FILES.get('logo')
        name = request.POST.get('name')
        trainer = request.POST.get('trainer')
        club.trainer = trainer
        club.name = name
        if logo is None:
            club.logo = club.logo
        else:
            club.logo = logo
        club.save()
        return redirect('club')
    return render(request, 'update-club.html', {'club': Fc.objects.get(id=pk)})


def update_advertiser(request, pk):
    advertiser = Advertiser.objects.get(id=pk)
    if request.method == 'POST':
        logo = request.POST.get('logo')
        url = request.POST.get('url')
        advertiser.url = url
        if logo is None:
            advertiser.logo = advertiser.logo
        else:
            advertiser.logo = logo
        advertiser.save()
        return redirect('advertiser')
    return render(request, 'update-advertiser.html', {'ads': Advertiser.objects.get(id=pk)})


def update_news(request, pk):
    news = News.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.FILES.get('image')
        date = request.POST.get('date')
        news.title = title
        news.text = text
        news.date = date
        if image is None:
            news.image = news.image
        else:
            news.image = image
        news.save()
        return redirect('news')
    return render(request, 'update-news.html', {'news': News.objects.get(id=pk)})


def update_videos(request, pk):
    videos = Videos.objects.get(id=pk)
    if request.method == 'POST':
        video = request.FILES.get('video')
        description = request.POST.get('description')
        date = request.POST.get('date')
        is_top = request.POST.get('is-top')
        videos.description = description
        videos.date = date
        videos.is_top = is_top
        if video is None:
            videos.video = videos.video
        else:
            videos.video = video
        videos.save()
        return redirect('video')
    return render(request, 'update-videos.html', {'video': Videos.objects.get(id=pk)})


def update_info(request, pk):
    info = Info.objects.get(id=pk)
    if request.method == 'POST':
        insta = request.POST.get('insta')
        telegram = request.POST.get('telegram')
        twitter = request.POST.get('twitter')
        youtube = request.POST.get('youtube')
        facebook = request.POST.get('facebook')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        logo = request.FILES.get('logo')
        info.insta = insta
        info.telegram = telegram
        info.twitter = twitter
        info.youtube = youtube
        info.facebook = facebook
        info.phone = phone
        info.email = email
        info.bio = bio
        if logo is None:
            info.logo = info.logo
        else:
            info.logo = logo
        info.save()
        return redirect('info')
    return render(request, 'update-info.html', {'info': Info.objects.get(id=pk)})


def update_region(request, pk):
    region = Region.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        region.name = name
        region.save()
        return redirect('region')
    return render(request, 'update-region.html', {'region': Region.objects.get(id=pk)})


def update_preview(request, pk):
    preview = Preview.objects.get(id=pk)
    if request.method == 'POST':
        guest = request.POST.get('guest')
        guest3 = request.POST.get('guest3')
        host = request.POST.get('host')
        date = request.POST.get('date')
        match_day = request.POST.get('match-day')
        preview.date = date
        if guest3 == '1':
            guest = guest
            host = host
        elif guest3 == '2':
            guest = host
            host = guest

        guest1 = Fc.objects.get(id=guest)
        host1 = Fc.objects.get(id=host)
        preview.guest = guest1
        preview.host = host1
        preview.match_day = match_day
        preview.save()
        return redirect('preview')
    context = {
        'fc': Fc.objects.all(),
        'preview': Preview.objects.get(id=pk)
    }
    return render(request, 'update-preview.html', context)


def update_squad(request, pk):
    squad = Squad.objects.get(id=pk)
    if request.method == 'POST':
        team = request.POST.getlist('team')
        game = request.POST.get('game')
        squad.team = team
        squad.game = game
        squad.save()
        return redirect('squad')
    return render(request, 'update-squad.html', {'squad': Squad.objects.get(id=pk)})


def update_line(request, pk):
    line = Line.objects.get(id=pk)
    if request.method == 'POST':
        team = request.POST.get('title')
        squad = request.POST.get('squad')
        line.team = team
        line.squad = squad
        line.save()
        return redirect('line')
    return render(request, 'update-line.html', {'line': Line.objects.get(id=pk)})


def update_subs(request, pk):
    sub = Substitute.objects.get(id=pk)
    if request.method == 'POST':
        squad = request.POST.get('title')
        line = request.POST.get('text')
        minute = request.POST.get('image')
        sub.squad = squad
        sub.line = line
        sub.minute = minute
        sub.save()
        return redirect('subs')
    return render(request, 'update-subs.html', {'subs': Substitute.objects.get(id=pk)})


def update_action(request, pk):
    action = Action.objects.get(id=pk)
    if request.method == 'POST':
        which = request.POST.get('title')
        who = request.POST.get('text')
        club = request.POST.get('image')
        goal = request.POST.get('image')
        actions = request.POST.get('image')
        minute = request.POST.get('image')
        action.which = which
        action.who = who
        action.club_who = club
        action.goal = goal
        action.action = actions
        action.minute = minute
        action.save()
        return redirect('action')
    return render(request, 'update-action.html', {'action': Action.objects.get(id=pk)})


def update_game(request, pk):
    game = Game.objects.get(id=pk)
    if request.method == 'POST':
        line = request.POST.get('line')
        guest = request.POST.get('guest')
        host = request.POST.get('host')
        passion = request.POST.get('passion')
        kross = request.POST.get('kross')
        passes = request.POST.get('passes')
        long = request.POST.get('long')
        helps = request.POST.get('helps')
        subs = request.POST.get('subs')
        mvp = request.POST.get('mvp')
        game.line = line
        game.guest_action = guest
        game.host_action = host
        game.passion = passion
        game.kross = kross
        game.passes = passes
        game.long_passes = long
        game.helps = helps
        game.subs = subs
        game.mvp = mvp
        game.save()
        return redirect('game')
    return render(request, 'update-game.html', {'game': Game.objects.get(id=pk)})


def update_size(request, pk):
    size = Size.objects.get(id=pk)
    if request.method == 'POST':
        sizes = request.POST.get('size')
        available = request.POST.get('available')
        size.size = sizes
        size.available = available
        size.save()
        return redirect('add-size')
    return render(request, 'update-size.html', {'size': Size.objects.get(id=pk)})


def update_image(request, pk):
    image = Images.objects.get(id=pk)
    if request.method == 'POST':
        images = request.FILES.get('image')
        image.image = images
        image.save()
        return redirect('add-images')
    return render(request, 'update-image.html', {'image': Images.objects.get(id=pk)})


def update_product(request, pk):
    pro = Product.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.POST.getlist('image')
        bonus = request.POST.get('bonus')
        price = request.POST.get('price')
        text = request.POST.get('text')
        size = request.POST.getlist('size')
        rating = request.POST.get('rating')
        pro.name = name
        pro.image = image
        pro.price = price
        pro.text = text
        pro.size = size
        pro.rating = rating
        pro.save()
        return redirect('product')
    return render(request, 'update-product.html', {'pro': Product.objects.get(id=pk)})


def delete_staff(request, pk):
    staff = Staff.objects.get(id=pk)
    staff.delete()
    return redirect('staff')


def delete_player(request, pk):
    player = Players.objects.get(id=pk)
    player.delete()
    return redirect('player')


def delete_passes(request, pk):
    passes = Passes.objects.get(id=pk)
    passes.delete()
    return redirect('add-passes')


def delete_image(request, pk):
    images = StadiumImage.objects.get(id=pk)
    images.delete()
    return redirect('add-stadium-image')


def delete_stadium(request, pk):
    stadium = Stadium.objects.get(id=pk)
    stadium.delete()
    return redirect('add-stadium')


def delete_fc(request, pk):
    fc = Fc.objects.get(id=pk)
    fc.delete()
    return redirect('fc')


def delete_club(request, pk):
    fc = Fc.objects.get(id=pk)
    fc.delete()
    return redirect('club')


def delete_advertiser(request, pk):
    ads = Advertiser.objects.get(id=pk)
    ads.delete()
    return redirect('advertiser')


def delete_news(request, pk):
    news = News.objects.get(id=pk)
    news.delete()
    return redirect('news')


def delete_videos(request, pk):
    video = Videos.objects.get(id=pk)
    video.delete()
    return redirect('video')


def delete_info(request, pk):
    info = Info.objects.get(id=pk)
    info.delete()
    return redirect('info')


def delete_about(request, pk):
    about = About.objects.get(id=pk)
    about.delete()
    return redirect('about')


def delete_region(request, pk):
    region = Region.objects.get(id=pk)
    region.delete()
    return redirect('region')


def delete_preview(request, pk):
    preview = Preview.objects.get(id=pk)
    preview.delete()
    return redirect('preview')


def delete_squad(request, pk):
    squad = Squad.objects.get(id=pk)
    squad.delete()
    return redirect('squad')


def delete_line(request, pk):
    line = Line.objects.get(id=pk)
    line.delete()
    return redirect('line')


def delete_subs(request, pk):
    subs = Substitute.objects.get(id=pk)
    subs.delete()
    return redirect('subs')


def delete_game(request, pk):
    game = Game.objects.get(id=pk)
    game.delete()
    return redirect('game')


def delete_size(request, pk):
    size = Size.objects.get(id=pk)
    size.delete()
    return redirect('add-size')


def delete_product_image(request, pk):
    image = Images.objects.get(id=pk)
    image.delete()
    return redirect('add-images')


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('product')


def delete_wishlist(request, pk):
    wish = Wishlist.objects.get(id=pk)
    wish.delete()
    return redirect('wish')
