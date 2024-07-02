from django.shortcuts import render
from.models import Choices, Questions , UserAnswers
# Create your views here.



def homePage(request):
    return render(request,'home.html')


def quizPage(request):
    if request.method == "POST":
        sorular = Questions.objects.all()

        toplam_puan = 0 

        username = request.POST.get('username', 'Anonimm')  

        for soru in sorular:
            secilen_cevap_id = request.POST.get(f"question_{soru.id}")

            if secilen_cevap_id:
                try:
                    secilen_cevap = Choices.objects.get(id = int(secilen_cevap_id))
                    #  kullanıcı cevabını kayıt edelim
                    toplam_puan += secilen_cevap.points

                except Choices.DoesNotExist:
                    pass

        UserAnswers.objects.create(
                    username = username,
                    total_score = toplam_puan
                )
            
        print(toplam_puan)

        sorular = Questions.objects.all()
        secenekler = Choices.objects.all()
        context = {
            'sorular': sorular,
            'secenekler': secenekler,
            'toplam_puan': toplam_puan  # Yeni context değişkeni: toplam_puan
        }
        return render(request,"quiz.html",context)


    else:
        sorular = Questions.objects.all()
        secenekler = Choices.objects.all()

        context = {
            'sorular':sorular,
            'secenekler':secenekler
        }
   
        return render(request,'quiz.html',context)