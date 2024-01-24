from django.shortcuts import render, redirect
from cnnClassifier.pipeline.prediction import PredictionPipeline
from django.core.files.storage import FileSystemStorage
media = 'media'
import os 

# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['upload']:
        f = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(f.name,f)
        file_url = fss.url(file)
        pred_img = os.path.join(media, file)
        pred = PredictionPipeline(pred_img)
        result = pred.predict()

        context = {
            'file_url':file_url,
            'result':result,
            'pred_img':pred_img

        }
        return render(request, 'index.html', context)
        
    return render(request, 'index.html')