from django.shortcuts import render, render_to_response 
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap

# Create your views here.
def index(request):
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]
    
    plot = figure(title = 'Line Graph', x_axis_label = 'X-Axis', y_axis_label = 'Y-Axis', plot_width = 400, plot_height = 400)
    
    plot.line(x, y, line_width = 2)
    
    script, div = components(plot)
    
    return render_to_response('index.html', {'script' : script , 'div' : div} )
    #return HttpResponse(plot.line)
    
