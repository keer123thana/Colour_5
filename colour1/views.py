from django.shortcuts import render
def home(request):
    colourlist=["#ff0000","#00ff00","#0000ff","#ff00ff","#ffff00"]
    return render(request,'colour1/index.html',{'param1':colourlist})
# Create your views here.

#FF0000-red
#00FF00-green
#0000FF-blue
#FFFF00-yellow
#00FFFF-
#FF00FF-purple
#000000-black
#FFFFFF-white