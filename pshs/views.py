from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Attendance, Assembly, Recurit, Apply
from django.utils import timezone
from .forms import QuestionForm, AssemblyForm, AttendanceForm, RecuritForm
from django.core.mail import EmailMessage
def index(request):
    '''
    pshs 모델 출력
    '''
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pshs/question_list.html', context)

def detail(request, question_id):
    '''
    pshs 내용 출력
    '''
    question = get_object_or_404(Question,id=question_id)
    context = {'question':question}
    return render(request, 'pshs/question_detail.html', context)

def answer_create(request, question_id):
    '''
    pshs 답변 등록
    '''
    question=get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pshs:detail', question_id=question.id)

def question_create(request):
    if request.method =='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pshs:index')

    else:
        form = QuestionForm()
    context = {'form' : form}
    return render(request, 'pshs/question_form.html', context)

def attendance(request):
    attendance_list = Attendance.objects.order_by('lib_room', 'lib_num')
    context = {'attendance_list' : attendance_list}
    return render(request, 'pshs/attendance_list.html', context)

def assembly(request):
    assembly_list = Assembly.objects.order_by('start_time')
    context = {'assembly_list' : assembly_list}
    return render(request, 'pshs/assembly_list.html', context)

def assembly_create(request):
    if request.method =='POST':
        form = AssemblyForm(request.POST)
        if form.is_valid():
            assembly = form.save(commit=False)
            assembly.save()
            return redirect('pshs:assembly')

    else:
        form = AssemblyForm()
    context = {'form' : form}

    return render(request, 'pshs/assembly_form.html', context)

def assembly_detail(request, assembly_id):
    assembly = get_object_or_404(Assembly,id=assembly_id)
    context = {'assembly':assembly}
    return render(request, 'pshs/assembly_detail.html', context)


def allow_email(request, assembly_id):
    assembly = get_object_or_404(Assembly, id=assembly_id)
    address = assembly.email
    email = EmailMessage(
        '집회신청이 완료되었습니다.',  # 이메일 제목
        '안녕하십니까. 귀하의 집회신청이 완료되었습니다. 신청 정보는 홈페이지에서 확인하시길 바랍니다. 끝.',  # 내용
        to=[address],  # 받는 이메일
    )
    email.send()
    return redirect('pshs:assembly_detail', assembly_id = assembly.id)

def disallow_email(request, assembly_id):
    assembly = get_object_or_404(Assembly, id=assembly_id)
    address = assembly.email
    email = EmailMessage(
        '집회신청이 반려되었습니다.',  # 이메일 제목
        '안녕하십니까. 귀하의 집회신청이 반려되었습니다. 죄송합니다. 끝.',  # 내용
        to=[address],  # 받는 이메일
    )
    email.send()
    return redirect('pshs:assembly_detail', assembly_id = assembly.id)

def attendance_create(request):
    if request.method =='POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.check_time = timezone.now()
            attendance.location = '자습실'
            attendance.save()
            return redirect('pshs:attendance')

    else:
        form = AttendanceForm()
    context = {'form' : form}

    return render(request, 'pshs/attendance_form.html', context)

def jasup(request, attendance_id):
    attendance = get_object_or_404(Attendance,pk=attendance_id)
    attendance.location = '자습실'
    attendance.check_time = timezone.now()
    attendance.save()
    return redirect('pshs:attendance')

def classroom(request, attendance_id):
    attendance = get_object_or_404(Attendance,id=attendance_id)
    attendance.location = '수업'
    attendance.check_time = timezone.now()
    attendance.save()
    return redirect('pshs:attendance')

def assemble(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    attendance.location = '집회'
    attendance.check_time = timezone.now()
    attendance.save()
    return redirect('pshs:attendance')

def absent(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    attendance.location = '결석'
    attendance.check_time = timezone.now()
    attendance.save()
    return redirect('pshs:attendance')

def all_jasup(request):
    for i in (Attendance.objects.values_list('id', flat=True)):
        attendance = get_object_or_404(Attendance, id=i)
        attendance.location = '자습실'
        attendance.check_time = timezone.now()
        attendance.save()
    return redirect('pshs:attendance')

def all_classroom(request):
    for i in (Attendance.objects.values_list('id', flat=True)):
        attendance = get_object_or_404(Attendance, id=i)
        attendance.location = '수업'
        attendance.check_time = timezone.now()
        attendance.save()
    return redirect('pshs:attendance')

def all_assemble(request):
    for i in (Attendance.objects.values_list('id', flat=True)):
        attendance = get_object_or_404(Attendance, id=i)
        attendance.location = '집회'
        attendance.check_time = timezone.now()
        attendance.save()
    return redirect('pshs:attendance')

def recurit(request):
    recurit_list = Recurit.objects.order_by('-create_date')
    context = {'recurit_list' : recurit_list}
    return render(request, 'pshs/recurit_list.html', context)



def recurit_create(request):
    if request.method =='POST':
        form = RecuritForm(request.POST)
        if form.is_valid():
            recurit = form.save(commit=False)
            recurit.create_date = timezone.now()
            recurit.save()
            return redirect('pshs:recurit')

    else:
        form = RecuritForm()
    context = {'form' : form}

    return render(request, 'pshs/recurit_form.html', context)

def recurit_detail(request, recurit_id):
    recurit = get_object_or_404(Recurit,id=recurit_id)
    context = {'recurit':recurit}
    return render(request, 'pshs/recurit_detail.html', context)

def apply_create(request, recurit_id):
    recurit=get_object_or_404(Recurit, pk=recurit_id)
    recurit.apply_set.create(content=request.POST.get('content'), create_date=timezone.now())
    contents = request.POST.get('content')
    address = recurit.email
    email = EmailMessage(
        '실험/수행/공구 등 모집 게시판에 새로운 신청이 들어왔습니다. ',  # 이메일 제목
        contents,  # 내용
        to=[address],  # 받는 이메일
    )
    email.send()
    return redirect('pshs:recurit_detail', recurit_id=recurit.id)

def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return redirect('pshs:index')

def delete_assembly(request, assembly_id):
    assembly = get_object_or_404(Assembly, id=assembly_id)
    assembly.delete()
    return redirect('pshs:assembly')

def delete_recurit(request, recurit_id):
    recurit = get_object_or_404(Recurit, id=recurit_id)
    recurit.delete()
    return redirect('pshs:recurit')

def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    attendance.delete()
    return redirect('pshs:attendance')