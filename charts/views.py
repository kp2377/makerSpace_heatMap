from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from fusioncharts import FusionCharts
from fusioncharts import FusionTable
from fusioncharts import TimeSeries


# Loading Data and schema from a Static JSON String url
# The `chart` method is defined to load chart data from an JSON string.
import json

def index(request):
    return HttpResponse("<h2>This is kartikey purohit in Charts</h2>")

# The `chart` method is defined to load chart data from an JSON string.
def charts(request):
    d = open('./charts/data.json').read()
    s = open('./charts/schema.json').read()
    data = json.loads(d)
    schema = json.loads(s)

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
    fcChart = FusionCharts("timeseries", "ex1", 1400, 900, "chart-1", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return  render(request, 'charts/charts.html', {'output' : fcChart.render()})