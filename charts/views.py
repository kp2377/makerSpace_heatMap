from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse


# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from fusioncharts import FusionCharts
from fusioncharts import FusionTable
from fusioncharts import TimeSeries

from django.views.decorators.csrf import csrf_exempt


# Loading Data and schema from a Static JSON String url
# The `chart` method is defined to load chart data from an JSON string.
import json as JSON
import datetime

def index(request):
    return HttpResponse("<h2>This is kartikey purohit in Charts</h2>")

# The `chart` method is defined to load chart data from an JSON string.
def charts(request):
    d = open('./charts/data.json').read()
    s = open('./charts/schema.json').read()
    data = JSON.loads(d)
    schema = JSON.loads(s)

    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute("caption", """{
                                        text: 'People Counter'
                                        }""")

    timeSeries.AddAttribute("subcaption", """{
                                    text: 'People'
                                    }""")

    timeSeries.AddAttribute("yAxis", """[{
                                            plot: {
                                            value: 'Number Of People',
                                            type: 'line'
                                            },
                                            format: {
                                            prefix: 'Nos.'
                                            },
                                            title: 'Counter'
                                        }]""")

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 1650, 1000, "chart-1", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return  render(request, 'charts/charts.html', {'output' : fcChart.render()})


@csrf_exempt
def tfuck(request):
    x = request.body
    my_json = x.decode('utf8')
    temp = JSON.loads(my_json)
    ret = temp["Time"]
    entry = [[ret, 32]]
    #new_entry = JSON.loads(entry)
    d = open('./charts/data.json').read()
    old_data = JSON.loads(d)
    throw = old_data + entry


    with open('./charts/data.json', mode='w+') as feedsjson:
        feedsjson.write(JSON.dumps(throw))
        feedsjson.close()
    return HttpResponse(ret)


@csrf_exempt
def json(request):
    x = request.body
    my_json = x.decode('utf8')
    temp = JSON.loads(my_json)
    ret = temp["Time"]
    tet = int(temp["count"])
    entry = [[ret, tet]]
    #new_entry = JSON.loads(entry)
    d = open('./charts/data.json').read()
    old_data = JSON.loads(d)
    throw = old_data + entry


    with open('./charts/data.json', mode='w+') as feedsjson:
        feedsjson.write(JSON.dumps(throw))
        feedsjson.close()
    return HttpResponse(ret)