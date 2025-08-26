from django.http import JsonResponse

def faq(request):
    faqs = [
        {"question": "How to track my order?", "answer": "Go to Profile > Orders > Track Order."},
        {"question": "How to apply a coupon?", "answer": "Go to Cart and enter your coupon code."}
    ]
    return JsonResponse({'faqs': faqs})
