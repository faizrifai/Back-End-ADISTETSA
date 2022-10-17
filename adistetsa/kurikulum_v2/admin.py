from calendar import HTMLCalendar
from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import KalenderPendidikanForm
from .models import KalenderPendidikan


class CustomCalendar(HTMLCalendar):
    def __init__(self, events=None):
        super().__init__()
        self.events = events

    def formatday(self, day, weekday, events):
        """
        Return a day as a table cell.
        """

        event = events.filter(
            TANGGAL_MULAI__day__lte=day, TANGGAL_BERAKHIR__day__gte=day
        )

        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        elif event:
            events_html = event[0].get_url(day)
            events_color = event[0].WARNA

            return '<td class="%s" style="background-color: %s;">%s</td>' % (
                self.cssclasses[weekday],
                events_color,
                events_html,
            )
        else:
            return '<td class="%s">%d</td>' % (self.cssclasses[weekday], day)

    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = "".join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return "<tr>%s</tr>" % s

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """

        events = KalenderPendidikan.objects.filter(TANGGAL_MULAI__month=themonth)

        v = []
        a = v.append
        a(
            '<table border="0" cellpadding="0" cellspacing="0" class="%s">'
            % (self.cssclass_month)
        )
        a("\n")
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a("\n")
        a(self.formatweekheader())
        a("\n")
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, events))
            a("\n")
        a("</table>")
        a("\n")
        return "".join(v)


# Register your models here.
class KalenderPendidikanAdmin(admin.ModelAdmin):
    change_list_template = "admin/kurikulum/kalender_pendidikan_change_list.html"
    form = KalenderPendidikanForm
    list_display = ["TANGGAL_MULAI", "TANGGAL_BERAKHIR", "KEGIATAN"]

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        cal = CustomCalendar()
        html_calendar = cal.formatmonth(2022, 9, withyear=True)
        extra_context["calendar"] = mark_safe(html_calendar)

        events = KalenderPendidikan.objects.filter(TANGGAL_MULAI__month=9).order_by(
            "TANGGAL_MULAI"
        )
        events_html = ""
        space = "&nbsp;" * 10

        for event in events:
            if not event.TANGGAL_MULAI == event.TANGGAL_BERAKHIR:
                events_html += (
                    '<div style="font-size: 12px; margin-top: 10px;"><span style="background-color: %s; color: %s;">%s</span> %d - %d : %s</div>'
                    % (
                        event.WARNA,
                        event.WARNA,
                        space,
                        event.TANGGAL_MULAI.day,
                        event.TANGGAL_BERAKHIR.day,
                        event.KEGIATAN,
                    )
                )
            else:
                events_html += (
                    '<div style="font-size: 12px; margin-top: 10px;"><span style="background-color: %s; color: %s;">%s</span> %d : %s</div>'
                    % (
                        event.WARNA,
                        event.WARNA,
                        space,
                        event.TANGGAL_MULAI.day,
                        event.KEGIATAN,
                    )
                )

        extra_context["event"] = mark_safe(events_html)

        return super().changelist_view(request, extra_context)


admin.site.register(KalenderPendidikan, KalenderPendidikanAdmin)
