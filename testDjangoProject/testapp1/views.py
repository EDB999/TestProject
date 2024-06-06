from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from testapp1.forms import BookingForm
from testapp1.models import MealMachine, OrderMachine


# Create your views here.

def index_page(request):
    form = BookingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            form = BookingForm()
    return render(request, 'index.html', {'form': form})


def menu_page(request):
    form = BookingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            form = BookingForm()
    meals = MealMachine.objects.all()
    # for meal in meals:
    #     meal.preview_picture = meal.preview_picture.replace(
    #         'C:\\Users\\User\\Desktop\\mealsTP\\project\\meals\\main\\static\\', '')
    return render(request, 'menu.html', {'form': form, 'meals': meals})


# def payment_and_delivery_page(request):
#     return render(request, 'Payment and Delivery.html')


def contacts_page(request):
    form = BookingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            form = BookingForm()
    return render(request, 'contacts.html', {'form': form})


def add_to_payment_and_delivery(request, id):
    payment_and_delivery = request.session.get('payment_and_delivery', {})
    if str(id) in payment_and_delivery:
        payment_and_delivery[str(id)] += 1
    else:
        payment_and_delivery[str(id)] = 1
    request.session['payment_and_delivery'] = payment_and_delivery
    messages.success(request, 'Блюдо добавлено в корзину.')
    return redirect('payment_and_delivery_page')


def remove_from_payment_and_delivery(request, id):
    payment_and_delivery = request.session.get('payment_and_delivery', {})
    action = request.GET.get('action', 'remove')
    if str(id) in payment_and_delivery:
        if action == 'decrease':
            payment_and_delivery[str(id)] -= 1
            if payment_and_delivery[str(id)] == 0:
                del payment_and_delivery[str(id)]
        else:
            del payment_and_delivery[str(id)]
    request.session['payment_and_delivery'] = payment_and_delivery
    messages.success(request, 'Блюдо удален из корзины.')
    return redirect('payment_and_delivery_page')


def payment_and_delivery(request):
    payment_and_delivery = request.session.get('payment_and_delivery', {})
    meals = MealMachine.objects.filter(pk__in=payment_and_delivery.keys())
    print(meals)
    payment_and_delivery_items = []
    total_price = 0
    total_items = 0
    for meal_id, quantity in payment_and_delivery.items():
        meal = MealMachine.objects.get(pk=meal_id)
        price = float(meal.price)
        total_price += price * quantity
        total_items += quantity
        payment_and_delivery_items.append({
            'meal': meal,
            'quantity': quantity,
        })
    total_price += 560
    if request.method == 'POST':
        address = '{}, {}, {}, {}, {}'.format(
            request.POST.get('street_house', ''),
            request.POST.get('flat_office', ''),
            request.POST.get('intercom', ''),
            request.POST.get('entrance', ''),
            request.POST.get('floor', '')
        )

        order = OrderMachine(
            cost=total_price,
            delivery_address=address,
        )
        order.save()  # сохраняем объект в базе данных

        order.content.set(meals)
        order.save()

    return render(request, 'Payment and Delivery.html', {
        'payment_and_delivery_items': payment_and_delivery_items,
        'total_price': total_price,
        'total_items': total_items,
    })
