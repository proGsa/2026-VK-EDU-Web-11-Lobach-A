from django.shortcuts import render
from django.http import HttpResponse
from .paginator import paginate 

def ask_view(request):
    ask_data = {
        'question': 'Как построить луна-парк?',
        'explaination': 'Планирую небольшой луна-парк. С чего начать? Какие документы нужны и какие аттракционы лучше выбрать для старта?'
    }
    return render(request, 'questions/ask.html', {'ask': ask_data})

def index_view(request):
    questions_list = []
    for i in range(1, 31):
        questions_list.append({
            'id': i,
            'title': f'Вопрос #{i}: Как работает Django?',
            'text': f'Текст вопроса #{i}. Помогите разобраться с этим моментом в Django.',
            'rating': (i * 17) % 100,  # случайный рейтинг от 0 до 99
            'answers_count': i % 15,
            'created_at': f'{i} часов назад',
            'tags': ['django', 'python'] if i % 2 == 0 else ['python', 'web']
        })
    
    # Сортировка
    sort_by = request.GET.get('sort', 'rating')
    if sort_by == 'date':
        questions_list.sort(key=lambda x: x['created_at'], reverse=True)
    else:  # rating по умолчанию
        questions_list.sort(key=lambda x: x['rating'], reverse=True)
    
    page_obj = paginate(questions_list, request, per_page=20)
    
    return render(request, 'questions/index.html', {
        'questions': page_obj,
        'sort': sort_by
    })
    return render(request, 'questions/index.html')

def question_view(request, question_id):
    question_data = {
        'id': question_id,
        'title': 'Как работает Django ORM?',
        'text': 'Пытаюсь разобраться, как правильно использовать ORM в Django. Особенно интересует работа с select_related и prefetch_related, а также оптимизация запросов. Приведите примеры.',
        'rating': 123,
        'created_at': '10 минут назад',
        'tags': ['django', 'python'],
        'author': 'proGsa2026',
        'author_avatar': 'img/avatar1.png'
    }
    
    # Список ответов (заглушка)
    answers_list = [
        {
            'id': 1,
            'text': '<b>select_related</b> используется для связей "один-к-одному" и "многие-к-одному". Он делает SQL JOIN и вытаскивает данные одним запросом.',
            'code': "posts = Post.objects.select_related('author')\nfor post in posts:\n    print(post.author.username)",
            'rating': 56,
            'created_at': '9 минут назад',
            'author': 'user123',
            'author_avatar': 'img/avatar4.jpg',
            'is_correct': False
        },
        {
            'id': 2,
            'text': '<b>prefetch_related</b> используется для "многие-ко-многим" и обратных связей. Он делает несколько запросов, но потом объединяет их в Python.',
            'code': "authors = Author.objects.prefetch_related('posts')\nfor author in authors:\n    for post in author.posts.all():\n        print(post.title)",
            'rating': 34,
            'created_at': '7 минут назад',
            'author': 'dev_expert',
            'author_avatar': 'img/avatar5.jpg',
            'is_correct': False
        },
        {
            'id': 3,
            'text': 'Общее правило:',
            'code': None,
            'rating': 78,
            'created_at': '3 минуты назад',
            'author': 'django_guru',
            'author_avatar': 'img/avatar6.jpeg',
            'is_correct': True,
            'list_items': [
                '<b>select_related</b> → когда нужен JOIN (ForeignKey, OneToOne)',
                '<b>prefetch_related</b> → когда список объектов (ManyToMany, reverse FK)'
            ]
        }
    ]
    
    page_obj = paginate(questions_list, request, per_page=5)
    
    if request.method == 'POST':
        pass
    
    return render(request, 'questions/question.html', {
        'question': question_data,
        'answers': page_obj,
        'total_answers': len(answers_list)
    })

def tag_view(request, tag_name):
    questions_list = []
    for i in range(1, 25): 
        questions_list.append({
            'id': i,
            'title': f'Вопрос про {tag_name} #{i}',
            'text': f'Текст вопроса #{i} о теге {tag_name}. Здесь может быть описание проблемы или вопроса пользователя.',
            'rating': (i * 7) % 100,
            'answers_count': i % 15,
            'tags': [tag_name, 'python' if i % 2 == 0 else 'django', 'backend'],
            'created_at': f'{i} часов назад'
        })
    page_obj = paginate(questions_list, request, per_page=20)

    return render(request, 'questions/tag.html', {'tag': {'tag': tag_name}, 'questions': page_obj,})

def hot_view(request):
    questions_list = []
    for i in range(1, 31):
        questions_list.append({
            'id': i,
            'title': f'Горячий вопрос #{i}',
            'text': f'Текст вопроса #{i}',
            'rating': (i * 23) % 100 + 50,  # высокий рейтинг
            'answers_count': i % 15,
            'created_at': f'{i} часов назад',
            'tags': ['django', 'python'] if i % 2 == 0 else ['python', 'web']
        })
    
    questions_list.sort(key=lambda x: x['rating'], reverse=True)  # ← главное отличие
    
    page_obj = paginate(questions_list, request, per_page=20)
    
    return render(request, 'questions/hot.html', {'questions': page_obj})