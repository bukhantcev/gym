from lib2to3.fixes.fix_input import context

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import length

from .forms import UpragForm
from .models import Upragneniya, Trenirovka, TrenirovkaGroup, Groups
from .calendar_fill import fill_cal
from datetime import datetime

def main(request):

    context = {

    }
    return render(request, 'main/welkom.html', context=context)





def calendar_view(request):

    # ---------CALENDAR
    context = {
        'fill_cal': fill_cal()['date_list'],
        'months': fill_cal()['month_list'],
        'years': fill_cal()['year_list'],
        'current_year': fill_cal()['current_year'],
        'current_month': fill_cal()['current_month'],
        'today': datetime.today(),


    }

    if 'monthSwitch' in request.GET:
        context = {
            'fill_cal': fill_cal(month=int(request.GET["monthSwitch"]), year=int(request.GET["yearSwitch"]))['date_list'],
            'months': fill_cal(month=int(request.GET["monthSwitch"]))['month_list'],
            'years': fill_cal(year=int(request.GET["yearSwitch"]))['year_list'],
            'current_year': fill_cal(year=int(request.GET["yearSwitch"]))['current_year'],
            'current_month': fill_cal(month=int(request.GET["monthSwitch"]))['current_month'],
            'today': datetime.today(),


        }

    trenya = TrenirovkaGroup.objects.all()
    context['trenya'] = trenya
    # ---------CALENDAR-CLOSE
    # ------------ADD TREN
    if request.method == 'POST':
        if 'addTren' in request.POST:
            try:
                TrenirovkaGroup.objects.get(date=request.POST.get('addTren'))
            except:


                try:

                    latest = str(TrenirovkaGroup.objects.latest('date').group)
                    if TrenirovkaGroup.objects.latest('date').date < datetime.strptime(request.POST.get('addTren'), '%Y-%m-%d').date():
                        if latest == "Грудь и трицепс":
                            group = Groups.objects.get(name="Ноги и плечи")
                        elif latest == "Ноги и плечи":
                            group = Groups.objects.get(name="Спина и бицепс")
                        elif latest == "Спина и бицепс":
                            group = Groups.objects.get(name="Грудь и трицепс")
                        else:
                            group = Groups.objects.get(name="Грудь и трицепс")
                    else:
                        if latest == "Грудь и трицепс":
                            group = Groups.objects.get(name="Спина и бицепс")
                        elif latest == "Спина и бицепс":
                            group = Groups.objects.get(name="Ноги и плечи")
                        elif latest == "Ноги и плечи":
                            group = Groups.objects.get(name="Грудь и трицепс")
                        else:
                            group = Groups.objects.get(name="Грудь и трицепс")

                except:
                    group = Groups.objects.get(name="Грудь и трицепс")
                new_tren = TrenirovkaGroup(group=group, date=request.POST.get('addTren'))
                new_tren.save()
                list_tren = Trenirovka.objects.order_by('-date').filter(group=group)


                try:
                    list_last1 = Trenirovka.objects.order_by('-date').filter(date=list_tren[0].date)
                    try:
                        list_last = []
                        list_last.append(list_last1[1])
                        list_last.append(list_last1[0])
                        for i in list_last1[2:]:
                            list_last.append(i)
                    except:
                        list_last = list_last1





                    for upr in list_last:
                        new_upr = upr
                        new_upr.pk = None
                        new_upr.date = request.POST.get('addTren')
                        if upr.status == '1':
                            if upr.level != '3':
                                new_upr.level = str(int(upr.level) + 1)
                                new_upr.amount1 = upr.amount1 + 1
                                new_upr.amount2 = upr.amount2 - 1
                                new_upr.povtor2 = upr.povtor2 - 1

                            else:
                                new_upr.level = '0'
                                new_upr.max_weight = str(int(upr.max_weight) + 5)
                        new_upr.status = '0'
                        new_upr.save()
                except:
                    pass
            # ------------ADD TREN-CLOSE

    if request.method == 'POST':
        if 'delTren' in request.POST:
            try:
                trens = TrenirovkaGroup.objects.filter(date=request.POST.get('delTren'))
                for tren in trens:
                    tren.delete()
                trens1 = Trenirovka.objects.filter(date=request.POST.get('delTren'))
                for tren in trens1:
                    tren.delete()
            except:
                pass


    return render(request, 'main/calendar.html', context=context)



def uprs(request):

    context = {

            }
    try:
        context['uprs'] = Upragneniya.objects.filter(group=Groups.objects.get(name=request.GET['group']))
        context['date'] = request.GET['addUpr']
    except:
        pass
    trens = Trenirovka.objects.all()
    context['trens'] = trens
    if request.GET:
        if 'addUpr' in request.GET:
            trenirovka = Trenirovka.objects.filter(date=request.GET['addUpr'])
            context['group'] = TrenirovkaGroup.objects.get(date=request.GET['addUpr'])
            context['group_choice'] = Groups.objects.all()
            context['date'] = request.GET['addUpr']
            context['trenirovka'] = trenirovka
        if 'uprs' in request.GET:
            print(request.GET)
            context['uprs'] = Upragneniya.objects.filter(group=Groups.objects.get(name=request.GET['uprs']))
            context['date'] = request.GET['date']
            change_group = TrenirovkaGroup.objects.get(id=request.GET['id'])
            change_group.group = Groups.objects.get(name=request.GET['uprs'])
            change_group.save()
            return render(request, 'main/uprslist.html', context)
        if 'newUpr' in request.GET:

            try:
                last_tren = Trenirovka.objects.order_by('-date').filter(name=Upragneniya.objects.get(name=request.GET['newUpr']))[0]
                newUpr = last_tren
                newUpr.pk = None
                newUpr.date = request.GET['date']
                if last_tren.status == '1':
                    if last_tren.level != '3':
                        newUpr.level = str(int(last_tren.level) + 1)
                        newUpr.amount1 = last_tren.amount1 + 1
                        newUpr.amount2 = last_tren.amount2 - 1
                        newUpr.povtor2 = last_tren.povtor2 - 1
                    else:
                        newUpr.level = '0'
                        newUpr.max_weight = str(int(last_tren.max_weight) + 5)
                newUpr.status = '0'
                newUpr.save()
            except:
                newUpr = Trenirovka(name=Upragneniya.objects.get(name=request.GET['newUpr']), date=request.GET['date'], group=Upragneniya.objects.get(name=request.GET['newUpr']).group)
                newUpr.save()



            return render(request, 'main/uprslist.html', context)
        if 'status' in request.GET:
            change_tren = Trenirovka.objects.get(id=request.GET['id'])
            change_tren.status = request.GET['status']
            change_tren.save()
            return render(request, 'main/uprslist.html', context)
        if 'DeleteUpr' in request.GET:
            delete_upr = Trenirovka.objects.get(id=request.GET['DeleteUpr'])
            delete_upr.delete()
            return render(request, 'main/uprslist.html', context)
        if 'maxWeight' in request.GET:
            if str(request.GET['maxWeight']).isdigit():
                change_weight = Trenirovka.objects.get(id=request.GET['id'])
                change_weight.max_weight = request.GET['maxWeight']
                change_weight.save()
                return render(request, 'main/uprslist.html', context)
            else:
                return HttpResponse('nodigit', content_type='text/html')


    return render(request, 'main/uprs.html', context)