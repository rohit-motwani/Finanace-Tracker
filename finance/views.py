from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from .models import Transaction
from .forms import TransactionForm
from django.contrib import messages

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'finance/dashboard.html', {'transactions': transactions})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'finance/add_transaction.html', {'form': form})

@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'finance/edit_transaction.html', {'form': form})

@login_required
def report(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'finance/report.html', {'transactions': transactions})

@login_required
def monthly_report(request):
    user = request.user
    monthly_report = Transaction.objects.filter(user=user).values('date__year', 'date__month').annotate(
        total_income=Sum('amount', filter=Q(transaction_type='IN')),
        total_expense=Sum('amount', filter=Q(transaction_type='EX'))
    ).order_by('date__year', 'date__month')

    context = {
        'monthly_report': monthly_report,
    }
    return render(request, 'finance/monthly_report.html', context)

@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Transaction deleted successfully.')
        return redirect('dashboard')
    return render(request, 'finance/delete_transaction.html', {'transaction': transaction})
