from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from apps.payments.models import Payment

@login_required
def make_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id, user=request.user)

    if request.method == 'POST':
        payment.status = 'success'
        payment.save()
        return render(request, 'payments/payment_success.html', {'payment': payment})

    return render(request, 'payments/make_payment.html', {'payment': payment})
