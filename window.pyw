import datetime
import main
import weather_static
import weather_obj
try:
    # for Python2
    import Tkinter as Tk
except ImportError:
    # for Python3
    import tkinter as Tk

session = main.Main()


class DevOps:
    @staticmethod
    def output_cities_list():
        if session.save["settings"]["dev"]:
            for item in session.save["cities"]:
                print(item["name"])
                print(item["country"])
        else:
            print("No dev")

    @staticmethod
    def output_cities_obj():
        if session.save["settings"]["dev"]:
            for item in session.cities_obj:
                print(item.name)
                print(item.country_code)
        else:
            print("No dev")
# Developer options


root = Tk.Tk()
root.config(width=300, height=500, padx=5, pady=5)
list_mng = Tk.Frame(root, padx=2)
list_mng.grid(column=0)
weather_text = Tk.Text(root)
weather_text.config(width=25, height=12)
weather_text.grid(row=0, column=1)


def add_city_window_event():
    add_city_window = Tk.Tk()
    add_city_window.title("Add a new city")
    add_city_window.attributes("-topmost", True)

    add_city_textbox = Tk.Label(add_city_window, text="Add a new city to the list")
    add_city_textbox.grid(row=0, columnspan=2)

    add_city_name_label = Tk.Label(add_city_window, text="City Name")
    add_city_name_label.grid(row=1)
    add_city_name_entry = Tk.Entry(add_city_window)
    add_city_name_entry.grid(row=1, column=1)
    add_city_code_label = Tk.Label(add_city_window, text="Country Code")
    add_city_code_label.grid(row=2)
    add_city_code_entry = Tk.Entry(add_city_window)
    add_city_code_entry.grid(row=2, column=1)

    def add_city_event():
        name = add_city_name_entry.get()
        code = add_city_code_entry.get()
        if code == "":
            code = session.save["settings"]["default_country"]
        session.add_city(name, code)
        root.attributes("-topmost", True)
        cities_listbox_update()
        add_city_window.destroy()

    def add_city_abort_event():
        add_city_window.destroy()

    add_city_button = Tk.Button(add_city_window, text="Confirm", command=add_city_event)
    add_city_button.grid(row=3)
    add_city_abort_button = Tk.Button(add_city_window, text="Abort", command=add_city_abort_event)
    add_city_abort_button.grid(row=3, column=1)
    # Add city event and window


if not session.save["cities"]:
    add_city_window_event()

cities_listbox = Tk.Listbox(list_mng)


def cities_listbox_update():
    cities_listbox.delete(0, cities_listbox.size())
    i = 0
    for item in session.cities_obj:
        cities_listbox.insert(i, item.name + ", " + item.country_code)
        i += 1
    cities_listbox.activate(1)


cities_listbox_update()
cities_listbox.grid(row=0, columnspan=3, padx=2, pady=2)


def query_weather():
    try:
        index = cities_listbox.curselection()[0]
    except IndexError:
        index = 0

    city = session.cities_obj[index]
    weather_text.delete("1.0", Tk.END)
    weather_text.insert("1.0", weather_static.build_weather(weather_obj.Weather(city, session.save["settings"]["dev"])))

# TODO fix timezones


query_city_button = Tk.Button(list_mng, command=query_weather, text="Get weather")
query_city_button.grid(row=1)

add_city_window_button = Tk.Button(list_mng, command=add_city_window_event, text=" + ")
add_city_window_button.grid(row=1, column=1)


def remove_city_event():
    index = cities_listbox.curselection()[0]
    session.remove_city(index)
    cities_listbox_update()


dev_var = Tk.BooleanVar()


def save_event():
    session.save["settings"]["dev"] = dev_var.get()
    session.save_event()


remove_city_button = Tk.Button(list_mng, command=remove_city_event, text=" - ")
remove_city_button.grid(row=1, column=2, ipadx=2)

save_button = Tk.Button(list_mng, command=save_event, text="Save & Quit")
save_button.grid(row=2, columnspan=2)


dev_button = Tk.Checkbutton(list_mng, text="dev_ops", variable=dev_var, onvalue=True, offvalue=False)
if session.save["settings"]["dev"]:
    dev_button.toggle()
dev_button.grid(row=3)

root.mainloop()
