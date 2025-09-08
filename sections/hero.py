from nicegui import ui
ui.add_head_html('''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">''')




def render():
    # big container

    with ui.element("div").style("background-image: url(/assets/hero.jpg)").classes(
        "h-screen w-screen flex flex-col no-repeat bg-cover bg-center"
    ):
        # navbar
        with ui.element("nav").classes("flex flex-row justify-between w-full fixed left-0 top-0 px-20 py-10 text-white"
                  ):
            # logo
            ui.label("LOGO")

            # nav links
            navlinks = [
                {"title": "Menu", "path": "/"},
                {"title": "Gallery", "path": "/"},
                {"title": "About", "path": "/"},
                {"title": "Contact", "path": "/"},
                {"title": "Blog", "path": "/"},
            ]

            with ui.row():
                for item in navlinks:
                    ui.link(item["title"], item["path"]).classes(
                        "no-underline uppercase text-white"
                    )

            # socials
            with ui.row():
                ui.html('<i class="fa-brands fa-facebook"></i>').classes("font-bold text-4xl")
                ui.html('<i class="fa-brands fa-square-instagram"></i>').classes("font-bold text-4xl")
                ui.html('<i class="fa-brands fa-square-x-twitter"></i>')
    # Text
        with ui.column().classes("items-center bg-black/50 h-full w-full flex flex-col items-center justify-center"):
            ui.label("Welcome to").classes("text-3xl").style("font-family:dancing script,cursive; color:#fff;")
            ui.label("Breakfast Arena").classes("text-7xl text-white font-bold")
            ui.button("Look Menu", color="White").style("border-radius:2px; width:150px").classes("bg-red")