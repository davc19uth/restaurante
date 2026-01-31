import json
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

# ---------- Pantallas ----------
class InicioScreen(Screen):
    pass


class CategoriasScreen(Screen):
    pass


class ProductosScreen(Screen):
    def mostrar_productos(self, categoria):
        self.ids.contenedor.clear_widgets()

        app = App.get_running_app()
        for producto in app.productos:
            if producto["categoria"] == categoria:
                item = Label(
                    text=f'{producto["nombre"]} - L. {producto["precio"]}',
                    size_hint_y=None,
                    height=40
                )
                self.ids.contenedor.add_widget(item)


# ---------- App Principal ----------
class MenuApp(App):

    def build(self):
        self.title = "Menú del Restaurante"

        # Cargar JSON
        with open("menuPrincipal.json", encoding="utf-8") as f:
            data = json.load(f)
            self.productos = data["productos"]

        sm = ScreenManager()
        sm.add_widget(InicioScreen(name="inicio"))
        sm.add_widget(CategoriasScreen(name="categorias"))
        sm.add_widget(ProductosScreen(name="productos"))

        return sm


if __name__ == "__main__":
    MenuApp().run()