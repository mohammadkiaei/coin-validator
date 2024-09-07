from django.shortcuts import render
import coinaddrvalidator
# import coinaddrng
# from coinaddr.validation import ValidationResult
# from coinaddrvalidator import Currency
# from zope.interface import implementer
# from coinaddr.interfaces import IValidator
# from coinaddr import ValidatorBase
from django.http import HttpResponse

currencies = {'binancecoin', 'bitcoin', 'bitcoin-sv', 'bitcoin-cash', 'boscoin', 'cardano', 'cosmos', 'dashcoin',
              'decred', 'dogecoin', 'eos', 'ethereum', 'ethereum-classic', 'ether-zero', 'groestlcoin', 'horizen',
              'kusama', 'litecoin', 'neocoin', 'ontology', 'polkadot', 'ravencoin', 'ripple', 'stellar', 'tezos',
              'tronix', 'vechain', 'zcash'}

def home(request):
    return render(request, 'home.html', {'currencies': currencies})

def validate(request):
    coinAddress = request.POST.get('coinAddress')
    currency = request.POST.get('currency')
    isValid = coinaddrvalidator.validate(currency, coinAddress)
    isValid = isValid.valid

    return render(request, 'home.html', {'isValid': isValid, 'currencies': currencies})
