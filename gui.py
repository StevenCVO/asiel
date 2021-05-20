import PySimpleGUI as gui
from db.datamanager_sqlite import DataManagerSQLite
from models.dier import Dier
from models.asiel import Asiel
from datetime import datetime

dm = DataManagerSQLite()

asielen = dm.get_asielen()

layout = [
    [gui.Text("ASIELEN", font="32")],
    [
        gui.Listbox(asielen, key="-ASIELEN-", size=(20, 5), enable_events=True),
        gui.Listbox([], key="-DIEREN-", size=(20, 5), enable_events=True)
    ],
    [gui.Text("Naam:", size=(20, 1)), gui.Text("", k="-DIER_NAAM-", size=(20, 1))],
    [gui.Text("Soort:", size=(20, 1)), gui.Text("", k="-DIER_SOORT-", size=(20, 1))],
    [gui.Text("Geslacht:", size=(20, 1)), gui.Text("", k="-DIER_GESLACHT-", size=(20, 1))],
    [gui.Text("Datum opname:", size=(20, 1)), gui.Text("", k="-DIER_OPNAME-", size=(20, 1))],
    [gui.HorizontalSeparator()],
    [gui.Text("Dier verwelkomen in asiel")],
    [gui.Text("Naam:", size=(20, 1)), gui.Input(key="-INVOER_NAAM-", size=(20, 1))],
    [gui.Text("Soort:", size=(20, 1)), gui.Combo(values=Dier.SOORTEN, key="-INVOER_SOORT-", size=(18, 1), readonly=True)],
    [gui.Text("Geslacht:", size=(20, 1)), gui.Combo(values=["Mannelijk", "Vrouwelijk"], key="-INVOER_GESLACHT-", size=(18, 1), readonly=True)],
    [gui.Button("Verwelkomen", key="-VERWELKOMEN-")]
]

window = gui.Window("Asielapplicatie", layout, size=(400, 400), element_justification="c")

while True:
    event, values = window.read()

    if event == gui.WIN_CLOSED:
        break
    if event == "-ASIELEN-":
        asiel = values["-ASIELEN-"][0]
        window["-DIEREN-"].update(values=sorted(asiel.dieren, key=lambda x: x.naam))
    if event == "-DIEREN-":
        dier = values["-DIEREN-"][0]
        window["-DIER_NAAM-"].update(value=dier.naam)
        window["-DIER_SOORT-"].update(value=dier.soort.capitalize())
        window["-DIER_GESLACHT-"].update(value="Mannelijk" if dier.geslacht == "m" else "Vrouwelijk")
        datum = datetime.strptime(dier.opname_datum, "%Y-%m-%d")
        window["-DIER_OPNAME-"].update(value=datum.strftime("%d-%m-%Y"))
    if event == "-VERWELKOMEN-":
        if not values["-ASIELEN-"]:
            continue

        naam = values["-INVOER_NAAM-"]
        soort = values["-INVOER_SOORT-"]
        geslacht = values["-INVOER_GESLACHT-"][0].lower()
        asiel = values["-ASIELEN-"][0]
        dier = Dier(naam, soort, geslacht, asiel_id=asiel.id)
        dm.insert_dier(dier)
        asiel.dieren.append(dier)
        window["-DIEREN-"].update(values=sorted(asiel.dieren, key=lambda x: x.naam))
        window["-INVOER_NAAM-"].update("")
        window["-INVOER_SOORT-"].update(set_to_index=0)
        window["-INVOER_GESLACHT-"].update(set_to_index=0)
        window["-INVOER_NAAM-"].set_focus()
