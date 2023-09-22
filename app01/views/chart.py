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


def chart_pie(request):
    data_list = [
        {"value": 1048, "name": 'Search Engine'},
        {"value": 735, "name": 'Direct'},
        {"value": 580, "name": 'Email'},
        {"value": 484, "name": 'Union Ads'},
        {"value": 300, "name": 'Video Ads'}
    ]

    result = {
        "status": True,
        "data": data_list
    }

    return JsonResponse(result)


def chart_line(request):
    legend = ['Email', 'Union Ads', 'Video Ads', 'Direct', 'Search Engine']

    series_list = [
        {
            'name': 'Email',
            'type': 'line',
            'stack': 'Total',
            'data': [120, 132, 101, 134, 90, 230, 210]
        },
        {
            'name': 'Union Ads',
            'type': 'line',
            'stack': 'Total',
            'data': [220, 182, 191, 234, 290, 330, 310]
        },
        {
            'name': 'Video Ads',
            'type': 'line',
            'stack': 'Total',
            'data': [150, 232, 201, 154, 190, 330, 410]
        },
        {
            'name': 'Direct',
            'type': 'line',
            'stack': 'Total',
            'data': [320, 332, 301, 334, 390, 330, 320]
        },
        {
            'name': 'Search Engine',
            'type': 'line',
            'stack': 'Total',
            'data': [820, 932, 901, 934, 1290, 1330, 1320]
        },
    ]

    x_axis = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis
        }
    }

    return JsonResponse(result)


def highcharts(request):
    return render(request, "highcharts.html")
