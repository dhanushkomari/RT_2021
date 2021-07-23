from django.shortcuts import render
from rest_framework import serializers
from .models import Configuration, Standard, Section, Detail, Subject, Topic, Data
from django.contrib.auth.models import User
from .forms import ConfigurationForm
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DataSerializer


# Create your views here.

def home(request):
    return render(request, 'RTApp/home.html')


def StandardView(request):
    s = Standard.objects.all()
    print('s is ', s)
    return render(request, 'RTApp/std.html',{'s':s})

# login Required
def SectionView(request, std_id):
    sec = Section.objects.filter(standard__std_id__iexact = std_id)
    cls = Standard.objects.get(std_id = std_id)

    standard = cls.std_name
    print(standard)
    
    user = request.user
    username = user.username
    userid = user.id
    print(username, userid)

    teacher = User.objects.get(username = username)
    print(teacher)
    section = sec
    detail = Detail.objects.create(standard = standard, teacher = teacher)
    detail.save()

    return render(request, 'RTApp/sec.html', {'sec':sec, 'cls':cls})

def SubjectView(request, sec_id):

    ######  FETCHING THE SECTION ######    
    print(sec_id)
    section = Section.objects.get(sec_id = sec_id)
    print(section)

    #######  FETCHING CLASS   #########
    R = Detail.objects.latest('pk')
    R.section = str(section)
    R.save()
    print(R.teacher, R.standard, R.section)

    ###### FETCHING SUBJECTS RELATED TO CLASS  ############

    standard = R.standard
    subs = Subject.objects.filter(standard__std_name = standard)
    print(subs)

    return render(request, 'RTApp/sub.html', {'subs':subs})

def TopicView(request, sub_id):
    R = Detail.objects.latest('pk')
    subject = Subject.objects.get(sub_id = sub_id)
    print(subject)

    R.subject = str(subject)
    R.save()

    ##########   FETCHING TOPICS RELATED TO SUBJECT   ############
    subject = R.subject
    tops = Topic.objects.filter(subject__sub_name = subject)
    print(tops)   

    return render(request, 'RTApp/top.html',{'tops':tops})



def ConfigurationView(request, topic_id):
    R = Detail.objects.latest('pk')
    topic = Topic.objects.get(topic_id = topic_id)
    print(topic)

    R.topic = str(topic)
    R.save()

    if request.method == "POST":
        form = ConfigurationForm(request.POST)
        if form.is_valid():
            print('form is  valid')
            t1 = request.POST['total_time']
            t2 = request.POST['teaching_time']
            t3 = request.POST['questions_time']
            print(t1,t2,t3)

            RR = Detail.objects.latest('pk')

            RR.total_time = t1
            RR.teaching = t2
            RR.questioning = t3
            RR.save()
            print(RR.total_time, RR.questioning)

            from .models import Data
            D = Data.objects.create(
                                    teacher = RR.teacher,
                                    standard = RR.standard,
                                    section = RR.section,
                                    subject = RR.subject,
                                    topic = RR.topic,
                                    total_time = t1,
                                    teaching = t2,
                                    questioning = t3,
                                )
            return HttpResponse('your details are ready')
    else:
        form = ConfigurationForm

    return render(request, 'RTApp/conf.html', {'form':form})


#######    Creating API   #######


@api_view(['GET'])
def DataView(request):
    data = Data.objects.latest('pk')
    serializers = DataSerializer(data, many = False)
    return Response(serializers.data)


