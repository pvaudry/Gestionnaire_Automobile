import tkinter as tk
from tkinter import *
from PIL import Image


def about_page(master):
    """
    [Description]
    Fonction permettant de générer la page "à propos".

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('1148x786+378+45')
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("A propos")
