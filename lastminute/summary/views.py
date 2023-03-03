from django.http import HttpResponse, JsonResponse
from .models import Lecture, Feature
from datetime import datetime
from . import helper

OOP = """
Object Oriented Programming, or OOP for short, is a programming paradigm that is centered around the concept of objects. These objects are instances of classes, which are essentially blueprints for creating objects with certain properties and behaviors.
One of the key features of OOP is encapsulation, which involves bundling data and methods that manipulate that data into a single entity, known as a class. This encapsulation helps to create a cleaner, more organized codebase by hiding implementation details and preventing external access to sensitive data. Additionally, it allows for the creation of reusable code, as classes can be instantiated multiple times throughout a program.
Another important aspect of OOP is inheritance. Inheritance involves creating new classes based on existing classes, known as parent classes. The new classes, known as child classes, inherit the properties and methods of the parent class and can also add new properties and methods of their own. This allows for the creation of more specialized classes that can reuse code from their parent classes, making it easier to write and maintain code.
Polymorphism is another important concept in OOP. Polymorphism refers to the ability of objects to take on multiple forms, depending on the context in which they are used. This can be achieved through the use of interfaces, which define a set of methods that must be implemented by any class that implements the interface. This allows for more flexible and modular code, as different objects can be used interchangeably as long as they implement the same interface.
Abstraction is another key principle of OOP. Abstraction involves focusing on the essential features of an object while hiding unnecessary details. This allows for more flexible and adaptable code, as the implementation details of an object can be changed without affecting the overall functionality of the program.
One of the main benefits of OOP is its ability to promote code reuse and modularity. By encapsulating data and methods into classes, and allowing for inheritance and polymorphism, code can be written in a more modular and reusable way. This can lead to faster development times, easier maintenance, and fewer bugs in the codebase.
However, OOP is not without its drawbacks. One potential issue with OOP is the potential for classes to become too complex and difficult to maintain. Additionally, the use of inheritance can sometimes lead to overly complex and convoluted class hierarchies.
Despite these potential drawbacks, OOP remains a popular and widely used programming paradigm, especially in larger and more complex software projects. Its focus on modularity, encapsulation, and reuse can lead to more maintainable and scalable code, making it a valuable tool for many developers."""

OS_CN = """
Good morning everyone, today we will be discussing Operating Systems and Computer Networks. Before we begin, let's define what an Operating System (OS) is. An OS is a software program that manages computer hardware and software resources and provides common services for computer programs. It acts as a communication bridge between the computer hardware and software applications.
The primary goal of an Operating System is to make it easier for users to interact with the computer hardware and software by providing a user-friendly interface, multitasking capabilities, and efficient use of resources. In addition, Operating Systems also provide services such as file management, memory management, and security.
I wanted to remind you that the first assignment is due this Monday. It focuses on implementing semaphores and mutexes in a real-world scenario. This assignment will help you solidify your understanding of these synchronization tools and give you practical experience in their usage. Be sure to submit your completed assignment by the deadline posted.
Let's now move on to computer networks. A computer network is a group of computers that are connected together and can communicate with each other. Computer networks allow computers to share resources such as printers, scanners, and files. They also enable users to access the internet and other network resources.
One of the key components of computer networks is the transmission medium. This is the physical medium used to transmit data between computers. Common transmission mediums include copper wires, fiber optics, and wireless signals.
Another important component of computer networks is the network protocol. Network protocols are a set of rules that govern communication between computers on a network. Examples of network protocols include TCP/IP, HTTP, and FTP.
Now, let's talk about the relationship between Operating Systems and computer networks. Operating Systems provide network support by offering networking protocols and services. These protocols and services enable computers to communicate with each other and share resources. Operating Systems also offer network management tools such as network configuration utilities and monitoring tools.
Lastly, I want to remind that office hours are available every Tuesday and Thursday from 1pm to 2 pm. If you're struggling with semaphores, mutexes, or any other course material, this is a great opportunity to get some one-on-one help. I'm here to support you and help you succeed in this course
"""


def create_dummy_objects():
    lecture1 = Lecture(Name='Operating Systems', date=datetime.now(), professor='Dr. Phunksuk Wangdu', transcript=OS_CN,
                       thumbnail='os.png', hidden=False)
    lecture2 = Lecture(Name='Computer Networks', date=datetime.now(), professor='Dr. Itachi Uchiha', transcript=OS_CN,
                       thumbnail='os.png', hidden=True)
    lecture3 = Lecture(Name='OOP', date=datetime.now(), professor='Dr. Minato Namikaze', transcript=OOP,
                       thumbnail='os.png', hidden=True)
    lecture3.save()
    lecture2.save()
    lecture1.save()


def index(_):
    create_dummy_objects()
    lectures = Lecture.objects.values()
    return JsonResponse(list(lectures), safe=False)


def lecture(request):
    id_ = request.GET['id']
    lecture_object = Lecture.objects.get(id=id_)
    if not Feature.objects.filter(id=id_).exists():
        lecture_ = lecture_object.transcript
        summary = helper.generate_summary(lecture_).summary
        outline = helper.generate_outline(lecture_)
        quiz = helper.generate_quiz(outline)
        announcements = helper.generate_announcements(lecture_, 2)
        announcements = ''.join([ele['metadata']['text'] for ele in announcements['matches']])
        feature1 = Feature(id=id_, summary=summary, outline=outline, quiz=quiz, announcements=announcements)
        feature1.save()
    else:
        feature = Feature.objects.get(id=id_)
        summary, outline, quiz, announcements = feature.summary, feature.outline, feature.quiz, feature.announcements.split(
            '\n')
        lecture_ = lecture_object.transcript
    response = {
        "summary": helper.remove_empty_strings(list(map(lambda x: f'{x}.' if x else '', summary.split('.')))),
        "outline": helper.remove_empty_strings(outline.split(',')),
        "announcements": helper.remove_empty_strings(announcements),
        "quiz": helper.remove_empty_strings(quiz.split('\n')),
        "transcript": helper.remove_empty_strings(lecture_.split('\n'))}

    response = JsonResponse(response)
    return response


def semantic_search(request):
    query = request.POST['query']
    result = helper.semantic_search(query, 3)
    response = {
        "results": result
    }
    return JsonResponse(response)
