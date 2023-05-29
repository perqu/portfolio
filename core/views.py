from django.shortcuts import render
from django.db.models import Count
from .models import Project


def index(request):
    projects = Project.objects.order_by("-rating")

    # Tworzenie listy technologii, rozdzielonych przecinkiem
    technologies_list = [
        tech.strip().lower()
        for project in projects
        for tech in project.technologies.split(",")
    ]

    # Zliczenie wystąpień każdej technologii
    technologies_counts = {}
    for technology in technologies_list:
        technologies_counts[technology] = technologies_counts.get(technology, 0) + 1

    # Sortowanie technologii malejąco po liczbie wystąpień
    sorted_technologies = sorted(
        technologies_counts.items(), key=lambda x: x[1], reverse=True
    )
    sorted_technologies = [
        tech[0] + "[" + str(tech[1]) + "]" for tech in sorted_technologies
    ]
    amount = 3
    return render(
        request,
        "core/index.html",
        {
            "projects": zip(projects[:amount], list(range(1, 1 + amount))),
            "technologies": sorted_technologies,
        },
    )
