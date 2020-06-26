from django.db import models

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICES = (
    (GENDER_MALE, 'male'),
    (GENDER_FEMALE, 'female')
)


STATUS_PENDING = 'pending'
STATUS_ACCEPTED = 'accepted'
STATUS_REJECTED = 'rejected'
STATUS_CHOICES = (
    (STATUS_PENDING, 'pending'),
    (STATUS_REJECTED, 'rejected'),
    (STATUS_ACCEPTED, 'accepted')
)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100,
                              choices=GENDER_CHOICES, default=GENDER_MALE)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    expected_salary = models.IntegerField()
    will_relocate = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.mobile)

    def cand_will_relocate(self):
        if self.will_relocate:
            return 'Yes'
        else:
            return 'No'

    def is_engaged(self):
        status_engaged = [
            STATUS_PENDING,
            STATUS_ACCEPTED
        ]
        jobs = CandidateJobMap.objects.filter(
            candidate=self, status__in=status_engaged).all()
        if len(jobs) == 0:
            return 'No'
        else:
            return "Yes"


class CandidateJobMap(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=STATUS_PENDING)
    feedback = models.TextField(blank=True, null=True)

    def age(self):
        return self.candidate.age

    def gender(self):
        return self.candidate.gender

    def city(self):
        return self.candidate.city

    def __str__(self):
        return "{} - {} - {}".format(self.candidate.name, self.job.position_name, self.status)

    class Meta:
        verbose_name_plural = "Review Candidates"
