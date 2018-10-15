from django.db import models

# Create your models here.


# - 학교
# 	- 학교명
# - 학생
# 	- 소속 학교 (MTO)
# 	- 학생 이름
# 	- 친한 친구 목록 (MTM)
# 		- 대칭적관계로 구현
class School(models.Model):
    name = models.CharField('학교명', max_length=60)

    def __str__(self):
        return self.name



class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField('학생 이름', max_length=50)
    


    def __str__(self):
        return self.name