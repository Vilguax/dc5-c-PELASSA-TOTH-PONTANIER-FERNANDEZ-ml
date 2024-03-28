import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Canvas, Tk, Checkbutton, Button, Label, OptionMenu, StringVar
from tkinter import IntVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

dataset = pd.read_csv("dataset.csv", parse_dates=['Date'])
dataset.set_index('Date', inplace=True)

for column in dataset.columns[1:]:
    dataset[column] = (dataset[column] - dataset[column].iloc[0]) / dataset[column].iloc[0] * 100

techcomm = ["ZOOM 19-21", "TESLA 19-21", "SHOPIFY 19-21", "NVIDIA 19-21", "NETFLIX 19-21", "MICROSOFT 19-21", "META 19-21", "APPLE 19-21", "AMAZON 19-21", "ALPHABET 19-21"]
techinfo = ["SQUARE 19-21", "SALESFORCE 19-21", "ORACLE 19-21", "INTEL 19-21", "CISCO SYSTEMS 19-21"]
santepharma = ["PFIZER 19-21", "MODERNA 19-21", "JOHNSON&JOHNSON 19-21", "GILEAD SCIENCES 19-21", "ASTRAZENECA 19-21"]
industrans = ["UAL 19-21", "GENERAL MOTORS 19-21", "FEDEX 19-21", "CATERPILLAR 19-21", "BOEING 19-21"]
finimmo = ["ZILLOW GROUP 19-21", "VISA 19-21", "JPMORGAN CHASE & CO 19-21", "GOLDMAN SACHS GROUP 19-21", "AMERICAN EXPRESS COMPANY 19-21"]
enemat = ["NUCOR 19-21", "EXXON MOBIL 19-21", "DUKE ENERGY 19-21", "CHEVRON 19-21", "BARRICK GOLD 19-21"]
divers = ["WALT DISNEY 19-21", "IBM 19-21", "HONEYWELL 19-21", "AT&T 19-21", "3M COMPANY 19-21"]
consobase = ["WALMART 19-21", "PROTECTER & GABLE 19-21", "PELOTON 19-21", "NIKE 19-21", "COCA COLA 19-21"]
consocycl = ["THE HOME DEPOT 19-21", "STARBUCKS 19-21", "MCDONALD 19-21", "LOWE 19-21", "BOOKING 19-21"]

time_options = {
    "Original": None,
    "Mensuel": 'M',
    "Bimestriel": '2M',
    "Trimestriel": '3M'
}

def draw_plot(selected_companies, resample_period):
    frequency = time_options[resample_period]
    
    if frequency:
        resampled_dataset = dataset.resample(frequency).mean()
    else:
        resampled_dataset = dataset
    
    fig = Figure(figsize=(14, 7))
    ax = fig.add_subplot(111)
    for company in selected_companies:
        if selected_companies[company].get() == 1:
            ax.plot(resampled_dataset.index, resampled_dataset[company], label=company)
    ax.legend()
    ax.set_title("Evolution des actions du secteur Energie/Matériaux")
    ax.set_xlabel("Date")
    ax.set_ylabel("Pourcentage d'augmentation")
    ax.grid()

    for widget in root.winfo_children():
        if isinstance(widget, Canvas):
            widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

def on_show_button_click():
    draw_plot(check_vars, time_var.get())

root = Tk()
root.title("Sélection des entreprises et plage de temps")

check_vars = {}
for company in techcomm:
    check_var = IntVar(value=1)
    Checkbutton(root, text=company, variable=check_var).pack()
    check_vars[company] = check_var

time_var = StringVar(root)
time_var.set("Original")
OptionMenu(root, time_var, *time_options.keys()).pack()

Button(root, text="Afficher le graphique", command=on_show_button_click).pack()

root.mainloop()