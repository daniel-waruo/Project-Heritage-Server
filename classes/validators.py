from django.core.exceptions import ValidationError


def validate_age(value, maximum_age=11, minimum_age=3):
    if value <= minimum_age:
        raise ValidationError(
            '(value) is less than minimum ph age {min}',
            params={'value': value, 'min': minimum_age},
        )
    elif value >= maximum_age:
        raise ValidationError(
            '(value) is above the maximum  ph age of {max}',
            params={'value': value, 'max': maximum_age},
        )


def validate_minimun(min_value):
    # import to avoid circular import
    from .models import PhClass
    # for ph_class in ph_classes
    for ph_class in PhClass.objects.all():
        # if the minimum value within the range of the ph class raise an error
        if ph_class.min_value >= min_value and min_value <= ph_class.max_value:
            raise ValidationError(
                'Invalid Min Value ({}).Minimum Value Range clashing with range ({} - {}).'.format(
                    min_value,
                    ph_class.min_value,
                    ph_class.max_value
                ),
            )


def validate_maximum(max_value):
    # import to avoid circular import
    from .models import PhClass
    # for ph_class in ph_classes
    for ph_class in PhClass.objects.all():
        # if the maximum value within the range of ph classes raise an error
        if ph_class.max_value >= max_value and max_value <= ph_class.min_value:
            raise ValidationError(
                'Invalid Max Value ({}).Maximum Value Range clashing with range ({} - {}).'.format(
                    max_value,
                    ph_class.min_value,
                    ph_class.max_value
                ),
            )
