from django import forms
from pshs.models import Question, Assembly, Attendance, Recurit


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',
        }
class AssemblyForm(forms.ModelForm):
    class Meta:
        model = Assembly
        fields = ['name', 'email', 'content', 'start_time', 'end_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '이름',
            'email': '이메일',
            'content': '내용',
            'start_time':'시작시간',
            'end_time': '종료시간',

        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['name', 'lib_room', 'lib_num', 'class_num']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lib_room': forms.NumberInput(attrs={'class': 'form-control'}),
            'lib_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'class_num': forms.NumberInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'name': '이름',
            'lib_room': '자습실 호실',
            'lib_num': '자습실 번호',
            'class_num':'학반번호',

        }

class RecuritForm(forms.ModelForm):
    class Meta:
        model = Recurit
        fields = ['name', 'email', 'content', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '이름',
            'email': '이메일',
            'content': '내용',
            'subject':'제목',
        }