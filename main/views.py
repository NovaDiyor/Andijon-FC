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
    return render(request, 'andijon.html', {'fc': Fc.objects.all()})


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
def region_view(request):
    return render(request, 'region.html', {'region': Region.objects.all()})


@login_required(login_url='sign-in')
def preview_view(request):
    return render(request, 'preview.html', {'preview': Preview.objects.all()})


@login_required(login_url='sign-in')
def squad_view(request):
    return render(request, 'squad.html', {'squad': Squad.objects.all()})


@login_required(login_url='sign-in')
def line_view(request):
    return render(request, 'line.html', {'line': Line.objects.all()})


@login_required(login_url='sign-in')
def subs_view(request):
    return render(request, 'subs.html', {'subs': Substitute.objects.all()})


@login_required(login_url='sign-in')
def game_view(request):
    return render(request, 'game.html', {'game': Game.objects.all()})


@login_required(login_url='sign-in')
def product_view(request):
    return render(request, 'product.html', {'product': Product.objects.all()})


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
            if player.count() > 2:
                p = player[0]
                p.captain = False
                p.save()
        except Exception as err:
            print(f'error : {err}')
    return redirect('player')


def add_passes(request):
    if request.method == 'POST':
        passes = request.POST.get('passes')
        successful = request.POST.get('successful')
        Passes.objects.create(all=passes, successful=successful)
    return redirect('game')


def add_long(request):
    if request.method == 'POST':
        passes = request.POST.get('passes')
        successful = request.POST.get('successful')
        Long.objects.create(all=passes, successful=successful)
    return redirect('game')


def add_helps(request):
    if request.method == 'POST':
        passes = request.POST.get('passes')
        successful = request.POST.get('successful')
        Helps.objects.create(all=passes, successful=successful)
    return redirect('game')


def add_kross(request):
    if request.method == 'POST':
        passes = request.POST.get('passes')
        successful = request.POST.get('successful')
        Kross.objects.create(all=passes, successful=successful)
    return redirect('game')


def add_stadium_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        Players.objects.create(image=image)
    return redirect('stadium-image')


def add_stadium(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        image = request.FILES.getlist('image')
        s = Staff.objects.create(name=name, capacity=capacity)
        for i in image:
            s.image.add(i)
    return redirect('stadium')


def add_fc(request):
    if request.method == 'POST':
        player = request.POST.getlist('player')
        staff = request.POST.getlist('staff')
        stadium = request.POST.get('stadium')
        name = request.POST.get('name')
        image = request.FILES.get("image")
        f = Fc.objects.create(stadium_id=stadium, name=name, logo=image)
        for i in player:
            f.players.add(i)
        for x in staff:
            f.staff.add(x)
    return redirect('fc')


def add_club(request):
    if request.method == 'POST':
        logo = request.POST.get('logo')
        name = request.POST.get('name')
        trainer = request.POST.get('trainer')
        Fc.objects.create(logo=logo, name=name, trainer=trainer)
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
    if request.method == 'POST':
        guest = request.POST.get('guest')
        host = request.POST.get('host')
        date = request.POST.get('date')
        day = request.POST.get('match-day')
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


def add_size(request):
    if request.method == 'POST':
        size = request.POST.get('size')
        available = request.POST.get('available')
        Size.objects.create(size=size, available=available)
    return redirect('size')


def add_images(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        Images.objects.create(image=image)
    return redirect('images')


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        bonus = request.POST.get('bonus')
        text = request.POST.get('text')
        size = request.POST.getlist('size')
        rating = request.POST.get('rating')
        image = request.POST.getlist('image')
        p = Product.objects.create(name=name, price=price, bonus=bonus, text=text, rating=rating)
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
    return render(request, 'update-player.html', {'player': Players.objects.get(id=pk)})


def update_passes(request, pk):
    game = Game.objects.get(id=pk)
    passes = game.passes
    long = game.long
    helps = game.helps
    kross = game.kross
    context = {
        'pass': passes,
        'long': long,
        'help': helps,
        'kross': kross,
    }
    if request.method == 'POST':
        pass_all = request.POST.get('pass-all')
        long_all = request.POST.get('long-all')
        help_all = request.POST.get('helps-all')
        kross_all = request.POST.get('kross-all')
        pass_success = request.POST.get('pass-success')
        long_success = request.POST.get('long-success')
        help_success = request.POST.get('help-success')
        kross_success = request.POST.get('kross-success')
        passes.all = pass_all
        long.all = long_all
        helps.all = help_all
        kross.all = kross_all
        passes.successful = pass_success
        long.successful = long_success
        helps.successful = help_success
        kross.successful = kross_success
        return redirect('game')
    return render(request, 'update-passes.html', context)


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
        return redirect('stadium')
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
        host = request.POST.get('host')
        date = request.POST.get('date')
        match_day = request.POST.get('match-day')
        preview.guest = guest
        preview.host = host
        preview.date = date
        preview.match_day = match_day
        preview.save()
        return redirect('preview')
    return render(request, 'update-preview.html', {'preview': Preview.objects.get(id=pk)})


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
        return redirect('size')
    return render(request, 'update-size.html', {'size': Size.objects.get(id=pk)})


def update_image(request, pk):
    image = Images.objects.get(id=pk)
    if request.method == 'POST':
        images = request.FILES.get('image')
        image.image = images
        image.save()
        return redirect('product')
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
    return redirect('passes')


def delete_long(request, pk):
    long = Long.objects.get(id=pk)
    long.delete()
    return redirect('long-passes')


def delete_helps(request, pk):
    helps = Helps.objects.get(id=pk)
    helps.delete()
    return redirect('helps')


def delete_kross(request, pk):
    kross = Kross.objects.get(id=pk)
    kross.delete()
    return redirect('kross')


def delete_image(request, pk):
    images = StadiumImage.objects.get(id=pk)
    images.delete()
    return redirect('stadium-image')


def delete_stadium(request, pk):
    stadium = Stadium.objects.get(id=pk)
    stadium.delete()
    return redirect('stadium')


def delete_fc(request, pk):
    fc = Fc.objects.get(id=pk)
    fc.delete()
    return redirect('fc')


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
    return redirect('size')


def delete_product_image(request, pk):
    image = Images.objects.get(id=pk)
    image.delete()
    return redirect('product-image')


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('product')


def delete_wishlist(request, pk):
    wish = Wishlist.objects.get(id=pk)
    wish.delete()
    return redirect('wish')
