from django.shortcuts import render
from django.http import JsonResponse

def chart_list(request):
    return render(request, "chart_list.html")


def chart_bar(request):
    legend = ["尤陆泽", "石头"]

    series_list = [
        {
            'name': '尤陆泽',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
        },
        {
            'name': '石头',
            'type': 'bar',
            'data': [15, 10, 27, 30, 5, 8]
        },
    ]

    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis
        }
    }

    return JsonResponse(result)