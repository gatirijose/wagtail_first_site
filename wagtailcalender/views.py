import calendar
from django.shortcuts import render
from django.utils import timezone


def index(request):
    current_year = timezone.now().year
    calendar_html = calendar.HTMLCalendar().formatyear(current_year)
    current_date = timezone.now().date

    return render(request, 'wagtailcalendar/index.html', {
        'current_year': current_year,
        'calendar_html': calendar_html,
        'current_date': current_date,
    })
def month(request):
    current_year = timezone.now().year
    current_month = timezone.now().month
    calender_html = calendar.HTMLCalendar().formatmonth(current_year, current_month)
    return render(request, 'wagtailcalendar/index.html', {
        'current_year': current_year,
        'calender_html': calender_html
    })