from nicegui import ui

def discover():
    with ui.element("div").classes("relative w-full h-[70vh] overflow-hidden"):
        ui.image("assets/breakfast-1804457_1280.jpg").classes("absolute inset-0 w-full h-full object-cover filter brightness-50")

        with ui.column().classes("absolute inset-0 flex flex-col items-center justify-center text-white text-center"):
            ui.label("Discover").classes("text-2xl italic text-red")
            ui.label("Breakfast Arena").classes("text-6xl font-bold")