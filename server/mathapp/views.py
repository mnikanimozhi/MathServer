from django.shortcuts import render

def calculate_gst(request):

    tax = None
    total = None

    if request.method == "POST":

        amount = float(request.POST.get("amount"))
        gst = float(request.POST.get("gst"))

        tax = (amount * gst) / 100

        total = amount + tax

        print("Amount:", amount)
        print("GST:", gst)
        print("GST Amount:", tax)
        print("Total:", total)

    return render(
        request,
        "mathapp/math.html",
        {
            "tax": tax,
            "total": total
        }
    )