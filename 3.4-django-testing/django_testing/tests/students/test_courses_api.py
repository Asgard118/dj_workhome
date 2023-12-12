import pytest
from students.models import Course, Student
from rest_framework.test import APIClient
from model_bakery import baker

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory):
    #Arrange
    course = course_factory(name='python', id=1)
    url = f'/courses/{course.id}/'
    #Act
    response = client.get(url)
    #Assert
    assert response.status_code == 200
    assert response.data['name'] == 'python'
@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    course = course_factory(_quantity=4)
    url = '/courses/'

    response = client.get(url)

    assert len(response.data) == 4
@pytest.mark.django_db
def test_get_course_id_filter(client, course_factory):
    course1 = course_factory(name='Java', id=1)
    course2 = course_factory(name='c#', id=2)
    course3 = course_factory(name='python', id=3)

    filter_id = course2.id
    url = f'/courses/?id={filter_id}'

    response = client.get(url)

    assert len(response.data) == 1 #проверка того что фильтр вернул только 1 курс
    assert response.data[0]['name'] == 'c#'
@pytest.mark.django_db
def test_get_course_name_filter(client, course_factory):
    course1 = course_factory(name='Java', id=1)
    course2 = course_factory(name='c#', id=2)
    course3 = course_factory(name='python', id=3)

    filter_name = 'python'
    url = f'/courses/?name={filter_name}'

    response = client.get(url)

    assert len(response.data) == 1 #проверка того что фильтр вернул только 1 курс
    assert response.data[0]['name'] == 'python'
@pytest.mark.django_db
def test_create_course(client):
    data = {
        'name': 'python',
        'id': '1',
    }

    url = '/courses/'

    response = client.post(url, data, format='json')

    assert response.status_code == 201
@pytest.mark.django_db
def test_get_update_course(client, course_factory):
    course = course_factory(name='python')
    data = {
        'name': 'python-fullstack',
    }

    url = f'/courses/{course.id}/'

    response = client.patch(url, data, format='json', follow=True)
    print(response.content)

    course.refresh_from_db()


    assert course.name == 'python-fullstack'

@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(name='python')

    url = f'/courses/{course.id}/'

    response = client.delete(url)

    assert response.status_code == 204
