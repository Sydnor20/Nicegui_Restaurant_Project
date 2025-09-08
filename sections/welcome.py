from nicegui import ui

def render():
    with ui.grid(columns=2).classes("w-screen h-screen gap-x-12 items-center justify-between"):
        # The left column text
        with ui.column().classes("gap-4 items-center justify-center"):
             ui.label("Ghanaian Restaurant").classes("text-2xl italic text-red-700")
             ui.label("Welcome").classes("text-6xl font-bold mt-2 mb-6")
             ui.label("Start your day with a smile at Breakfast Arena!....Delicious,fresh breakfast served daily to fuel your morning right.").classes("" \
             "text-xl text-gray-600 max-w-lg")

             ui.link("ABOUT US")
        with ui.column().classes("mt-8 text-black font-semibold no-underline"):
             ui.image("assets/welcome.jpg").classes("w-[500px] h-[500px] shadow-xl rounded-lg")