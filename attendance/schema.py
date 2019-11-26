import graphene
from graphene_django import DjangoObjectType
from .models import Attendance


class AttendanceType(DjangoObjectType):
    class Meta:
        model = Attendance


class Query(graphene.ObjectType):
    attendance = graphene.List(AttendanceType)

    def resolve_classes(self, info, **kwargs):
        return Attendance.objects.all()


class CreateAttendance(graphene.Mutation):
    id = graphene.Int()
    isPresent = graphene.Boolean()
    childName = graphene.String()

    class Arguments:
        isPresent = graphene.Boolean()
        childName = graphene.String()

    def mutate(self, info, isPresent, childName):
        newAttendance = Attendance(isPresent=isPresent, childName=childName)
        newAttendance.save()

        return CreateAttendance(
            id=newAttendance.id,
            isPresent=newAttendance.isPresent,
            childName=newAttendance.childName
        )


class Mutation(graphene.ObjectType):
    create_attendance = CreateAttendance.Field()
