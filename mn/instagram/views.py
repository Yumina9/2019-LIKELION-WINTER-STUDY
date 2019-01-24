# shortcuts는 많이 쓰이는 기능을 묶어서 간편하게 해주는 기능 모음집
from django.shortcuts import render
from .forms import PhotoForm
from .models import Photo
# Create your views here.


def image_list(request):
    """
    이곳은 이미지 리스트를 보는 함수입니다.
    """
    # request.method를 통해서 어떠한 요청 메소드가 들어오는지 확인할 수 있다.
    # print(request)  # <WSGIRequest: GET '/instagram/'>
    # print(request.method)  # GET

    if request.method == 'GET':
        form = PhotoForm()

    elif request.method == 'POST':
        # 우리가 작성한 데이터를 기반으로 폼을 생성
        form = PhotoForm(request.POST, request.FILES)
        # 폼이 제대로 생성되었는지 검사
        if form.is_valid():
            photo = form.save(commit=False)  # 즉시 저장하지말고 나중에 저장
            photo.image = request.FILES['image']  # 파일정보는 request.FILES
            # 나머지 정보는 request.POST
            photo.discription = request.POST['discription']
            photo.save()

    return render(request, 'instagram/list.html', {
        'form': form,
        'photo': Photo.objects.all()
    })

# 관리자 페이지
# 이미지 폼 업로드 결과 리스트
