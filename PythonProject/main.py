import flet as ft
from datetime import datetime, timedelta


def main(page: ft.Page):
    page.title = "NetSchool"
    page.bgcolor = "#F2F3F7"
    page.padding = 0
    page.theme_mode = "light"

    # Настройки дат
    today = datetime(2026, 5, 18)
    current_week_monday = today - timedelta(days=today.weekday())
    page.current_offset = -2
    page.current_screen = "schedule"
    page.current_tab = "periods"

    # Данные расписания
    schedule_data = {
        "Понедельник": ["Биология", "Разговоры о важном", "Литература", "Алгебра", "История", "Музыка",
                        "Английский язык"],
        "Вторник": ["Литература", "Основы фин. грамотности", "Русский язык", "Химия", "Обществознание", "Геометрия",
                    "География"],
        "Среда": ["Химия", "Алгебра", "Русский язык", "Физкультура", "Физика", "История", "Английский язык"],
        "Четверг": ["Вероятность и статистика", "Россия - мои горизонты", "Русский язык", "Труд", "Информатика",
                    "Английский язык"],
        "Пятница": ["Геометрия", "Физкультура", "Физика", "География", "Инфографика", "Биология", "Алгебра"]
    }

    # Текущие оценки за дни
    grades_data = {
        "2026-05-04": {"Английский язык": "4"},
        "2026-05-05": {"Русский язык": "4", "География": "3"},
        "2026-05-06": {"Физика": "4"},
        "2026-05-12": {"Геометрия": "2"},
        "2026-05-13": {"Русский язык": "4", "Физика": "4", "Английский язык": "2"},
        "2026-05-14": {"Труд": "4", "ОБЖ": "5"}
    }

    months_ru = ["Мая", "Мая", "Мая", "Мая", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября",
                 "Декабря"]

    schedule_container = ft.Column(spacing=10, scroll="auto", expand=True)
    results_container = ft.Column(spacing=0, scroll="auto", expand=True)
    content_area = ft.Container(content=schedule_container, expand=True)

    week_label = ft.Text("", color="white", size=18, weight="bold")
    week_dates_label = ft.Text("", color="#90A4AE", size=14)

    def build_day_card(day_name, day_date):
        current_lessons = schedule_data.get(day_name, [])
        date_str = f"{day_date.day} {months_ru[day_date.month - 1]}"
        date_key = day_date.strftime("%Y-%m-%d")

        day_grades = grades_data.get(date_key, {})
        lesson_items = ft.Column(spacing=0, visible=False)

        grades_row = ft.Row(spacing=4, alignment=ft.MainAxisAlignment.END)
        for lesson_name, grade_val in day_grades.items():
            grades_row.controls.append(
                ft.Container(
                    content=ft.Row(
                        [ft.Text(grade_val, color="#333333", size=13, weight="bold")],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    width=28, height=24, bgcolor="#F0F2F5", border_radius=4
                )
            )

        time_str = "12:25 - 18:10"
        if day_name in ["Понедельник", "Четверг", "Пятница"]:
            time_str = "13:10 - 19:00"

        for name in current_lessons:
            lesson_items.controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Text(name, size=16, color="#4F5A66", expand=True),
                        ft.Text("›", color="#B0BEC5", size=22)
                    ]),
                    padding=8
                )
            )

        def toggle_click(e):
            lesson_items.visible = not lesson_items.visible
            arrow_text.value = "Свернуть ▴" if lesson_items.visible else f"{len(current_lessons)} уроков ▾"
            page.update()

        arrow_text = ft.Text(f"{len(current_lessons)} уроков ▾", color="#4F5A66", size=15, weight="bold")

        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([
                        ft.Text(day_name, size=19, weight="w500", color="#656D78"),
                        ft.Text(date_str, size=12, color="#AAB2BD")
                    ], spacing=2),ft.Text(time_str, size=13, color="#AAB2BD"),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=8),
                ft.Row([
                    ft.GestureDetector(content=ft.Container(content=arrow_text, padding=2), on_tap=toggle_click),
                    ft.Container(content=grades_row, expand=True)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                lesson_items,
            ]),
            bgcolor="white", padding=14, border_radius=10, margin=12
        )

    def build_results_screen():
        # Четвертные оценки
        final_grades = {
            "Алгебра": ["4", "4", "4", "4"],
            "Английский язык": ["4", "4", "4", "4"],
            "Биология": ["4", "4", "4", "4"],
            "Вероятность и статистика": ["4", "4", "4", "4"],
            "География": ["4", "4", "4", "4"],
            "Геометрия": ["4", "4", "4", "4"],
            "Инфографика": ["н/оц", "н/оц", "н/оц", "н/оц"],
            "Информатика": ["5", "5", "5", "5"],
            "История": ["4", "4", "4", "5"],
            "Литература": ["5", "5", "5", "5"],
            "Музыка": ["5", "5", "5", "5"],
            "Обществознание": ["5", "5", "5", "5"],
            "Основы безопасности и защиты Родины": ["5", "5", "5", "5"],
            "Основы финансовой грамотности": ["5", "5", "5", "5"],
            "Русский язык": ["4", "4", "4", "4"],
            "Труд": ["5", "5", "5", "5"],
            "Физика": ["4", "3", "4", "4"],
            "Физкультура": ["5", "5", "5", "5"],
            "Химия": ["4", "4", "4", "4"]
        }

        # Годовые оценки
        yearly_grades = {
            "Алгебра": "4", "Английский язык": "4", "Биология": "4",
            "Вероятность и статистика": "4", "География": "4", "Геометрия": "4",
            "Инфографика": "н/оц", "Информатика": "4", "История": "5",
            "Литература": "5", "Музыка": "5", "Обществознание": "5",
            "Основы безопасности и защиты Родины": "5", "Основы финансовой грамотности": "5",
            "Русский язык": "4", "Труд": "5", "Физика": "4", "Физкультура": "5", "Химия": "4"
        }

        results_container.controls.clear()
        is_periods = page.current_tab == "periods"

        tabs_row = ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Text("Итоги периодов", color="white" if is_periods else "#90A4AE", weight="bold", size=14),
                    bgcolor="#2B5B99" if is_periods else "#1F4373",
                    padding=10,
                    border_radius=5,
                    on_click=lambda _: change_results_tab("periods")
                ),
                ft.Container(
                    content=ft.Text("Итоги года", color="#90A4AE" if is_periods else "white", weight="bold", size=14),
                    bgcolor="#1F4373" if is_periods else "#2B5B99",
                    padding=10,
                    border_radius=5,
                    on_click=lambda _: change_results_tab("year")
                )
            ], spacing=2, alignment=ft.MainAxisAlignment.START),
            bgcolor="#2B5B99",
            padding=10
        )
        results_container.controls.append(tabs_row)

        if is_periods:
            table_header = ft.Container(
                content=ft.Row([
                    ft.Text("Четверти", size=14, color="#78909C", expand=2),
                    ft.Text("1/4", size=14, color="#78909C", width=45, text_align=ft.TextAlign.CENTER),
                    ft.Text("2/4", size=14, color="#78909C", width=45, text_align=ft.TextAlign.CENTER),
                    ft.Text("3/4", size=14, color="#78909C", width=45, text_align=ft.TextAlign.CENTER),
                    ft.Text("4/4", size=14, color="#78909C", width=45, text_align=ft.TextAlign.CENTER),
                ]),
                bgcolor="#EBF0F5", padding=10
            )
            results_container.controls.append(table_header)

            for idx, (subject, info) in enumerate(final_grades.items()):
                bg = "#FFFFFF" if idx % 2 == 0 else "#F8FAFC"
                row_item = ft.Container(
                    content=ft.Row([
                        ft.Text(subject, size=15, color="#2C3E50", weight="w500", expand=2),
                        ft.Text(info[0], size=15, color="#2C3E50", width=45, text_align=ft.TextAlign.CENTER),
                        ft.Text(info[1], size=15, color="#2C3E50", width=45, text_align=ft.TextAlign.CENTER),
                        ft.Text(info[2], size=15, color="#2C3E50", width=45, text_align=ft.TextAlign.CENTER),
                        ft.Text(info[3], size=15, color="#2C3E50", weight="bold", width=45, text_align=ft.TextAlign.CENTER),
                    ]),
                    bgcolor=bg, padding=12
                )
                results_container.controls.append(row_item)
        else:
            table_header = ft.Container(
                content=ft.Row([
                    ft.Text("Предмет", size=14, color="#78909C", expand=2),
                    ft.Text("Год", size=14, color="#78909C", width=60, text_align=ft.TextAlign.CENTER),
                ]),
                bgcolor="#EBF0F5", padding=10
            )
            results_container.controls.append(table_header)

            for idx, (subject, grade) in enumerate(yearly_grades.items()):
                bg = "#FFFFFF" if idx % 2 == 0 else "#F8FAFC"
                row_item = ft.Container(
                    content=ft.Row([
                        ft.Text(subject, size=15, color="#2C3E50", weight="w500", expand=2),
                        ft.Text(grade, size=15, color="#2C3E50", weight="bold", width=60, text_align=ft.TextAlign.CENTER),
                    ]),
                    bgcolor=bg, padding=12
                )
                results_container.controls.append(row_item)

        results_container.controls.append(ft.Container(height=60))

    def change_results_tab(tab_name):
        page.current_tab = tab_name
        build_results_screen()
        page.update()

    def refresh_all():
        if page.current_screen == "schedule":
            target_monday = current_week_monday + timedelta(weeks=page.current_offset)
            target_sunday = target_monday + timedelta(days=6)

            if page.current_offset == 0:
                week_label.value = "Текущая неделя"
            elif page.current_offset == -1:
                week_label.value = "Прошлая неделя"
            elif page.current_offset == -2:
                week_label.value = "Предыдущая неделя"
            else:
                week_label.value = "Архив расписания"

            month_start = months_ru[target_monday.month - 1]
            month_end = months_ru[target_sunday.month - 1]

            if month_start == month_end:
                week_dates_label.value = f"{target_monday.day} - {target_sunday.day} {month_start}"
            else:
                week_dates_label.value = f"{target_monday.day} {month_start} - {target_sunday.day} {month_end}"

            header_calendar_row.visible = True
            header_title.value = "Мария"

            schedule_container.controls.clear()
            schedule_container.controls.append(ft.Container(height=4))

            days_list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
            for i, day_name in enumerate(days_list):
                day_date = target_monday + timedelta(days=i)
                schedule_container.controls.append(build_day_card(day_name, day_date))

            schedule_container.controls.append(ft.Container(height=80))
            content_area.content = schedule_container
        else:
            header_calendar_row.visible = False
            header_title.value = "Итоги"
            build_results_screen()
            content_area.content = results_container

        page.update()

    def move_week(delta):
        page.current_offset += delta
        refresh_all()

    def navigate_to(screen_name):
        page.current_screen = screen_name
        for item in nav_row.controls:
            item.content.controls[1].color = "#4CAF50" if item.data == screen_name else "grey"
        refresh_all()

    header_title = ft.Text("Мария", color="white", size=20, weight="bold", expand=True, text_align=ft.TextAlign.CENTER)
    header_calendar_row = ft.Row([
        ft.GestureDetector(content=ft.Text(" ❮ ", color="white", size=22), on_tap=lambda _: move_week(-1)),
        ft.Column([
            week_label, week_dates_label
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
        ft.GestureDetector(content=ft.Text(" ❯ ", color="white", size=22), on_tap=lambda _: move_week(1)),
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=60)

    header = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Text(" ☰ ", color="white", size=24),
                header_title,
                ft.Text(" 🔔 ", color="white", size=24),
            ]),
            ft.Container(height=5),
            header_calendar_row
        ]),
        bgcolor="#2B5B99", padding=15
    )

    def build_nav_item(icon, text, screen_name, is_active=False):
        return ft.GestureDetector(
            data=screen_name,
            on_tap=lambda e: navigate_to(e.control.data),
            content=ft.Column([
                ft.Text(icon, size=22),
                ft.Text(text, size=10, color="#4CAF50" if is_active else "grey")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )

    nav_row = ft.Row([
        build_nav_item("🕒", "День", "day"),
        build_nav_item("📅", "Расписание", "schedule", is_active=True),
        build_nav_item("🏠", "Д/З", "homework"),
        build_nav_item("📖", "Итоги", "results"),
        build_nav_item("📢", "Сообщения", "messages"),
    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

    bottom_nav = ft.Container(content=nav_row, bgcolor="white", height=70)

    page.add(header, content_area, bottom_nav)
    page.update()
    refresh_all()

ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)