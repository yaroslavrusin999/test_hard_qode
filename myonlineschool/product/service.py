from django.db.models import Count
from django.utils.timezone import now

from product.models import Product
from student.models import Student, StudyGroup


def distribute_to_study_group(st: Student, pr: Product) -> bool:
    """
    Функция распределяет студента в учебную группу по выбранному продукту.
    Создает новую группу если групп еще нет или все группы заполнены.
    При заполнении всех групп создает новую и распределяет всех учеников равномерно
    в каждую группу.
    """
    product_id = (st.study_groups.
                  select_related('product').
                  filter(product__id=pr.pk).
                  values_list("product_id", flat=True))
    if product_id:
        return False  # Пользователь уже приобрел продукт

    if pr.start_date < now():  # Запись на продукт уже закончилась
        return False

    study_groups = (pr.study_groups.
                    prefetch_related('students').
                    annotate(count_students=Count('students')))
    if len(study_groups) == 0:  # Если ещё нет групп по данному продукту, то создаем новую
        study_group = StudyGroup(title=f'{pr.title}:1')
        study_group.product = pr
        study_group.save()
        study_group.students.add(st)
        study_group.save()
        return True

    # Выбираем группу с наименьшим количеством студентов
    study_group_min_students = min(study_groups, key=lambda g: g.count_students)

    # Если выбранная группа ещё не заполнена, то добавляем пользователя туда
    if study_group_min_students.count_students < pr.max_students:
        study_group_min_students.students.add(st)
        study_group_min_students.save()
        return True

    else:
        # Выбираем всех студентов из учебных групп по данному продукту
        students = []
        for sg in study_groups:
            for s in sg.students.all():
                students.append(s)
        students.append(st)

        # Очищаем связи учебных групп со студентами
        for sg in study_groups:
            sg.students.clear()
            sg.save()

        # Создаем новую учебную группу
        new_study_group = StudyGroup(title=f'{pr.title}:{len(study_groups) + 1}')
        new_study_group.product = pr
        new_study_group.save()
        study_groups = list(study_groups) + [new_study_group]

        # Распределяем студентов равномерно в каждую группу
        i = 0
        for s in students:
            s_g = study_groups[i]
            s_g.students.add(s)
            s_g.save()
            if i < len(study_groups) - 1:
                i += 1
            else:
                i = 0
        return True
