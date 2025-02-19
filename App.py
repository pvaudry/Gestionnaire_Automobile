#!/bin/python3 -*- coding: utf-8 -*-
"""
@Author : Jessy JOSE -- Pierre VAUDRY -- Enora GUILLAUME -- Luc VIERNE
IPSA Aero2 - Prim1
Release date: 07/04/2021


[other information]
Licence: MIT
Version: GUI_v6.0 / DataTool_v1.8


[Description]

    Ce projet a pour but de permettre la gestion d'un parc automonile


[Class]

    ToolBar() -- ToolBar class generate a great toolbar at the top of main screen app
    MainApp() -- main class to make first page and instance all functions


[Other variable]:

    Many other constants and variable may be defined;
    these may be used in calls

"""

# --------- Import module section --------- #

import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image, ImageTk

import lib.DataTool as DT

# --------- Import module page section --------- #

import lib.WelcomePage as WP
import lib.HelpPage as HP
import lib.AjoutVehiPage as AVP
import lib.AnnulPage as AnP
import lib.FinLocPage as FP
import lib.ReservPage as RP
import lib.SupClientPage as SCP
import lib.SupVehiPage as SVP
import lib.ClientPage as CP
import lib.easter_egg as ee
import lib.ExpImp_Data as EIData
import lib.ModifBddPage as MBP
import lib.grille_tarifaire as gt
import lib.grille_client as gc
import lib.grille_vehicule as gv
import lib.grille_reservation as gr
import lib.ModifClientPage as MCP
import lib.ModifTarifPage as MTP
import lib.ModifVehiculePage as MVP



# --------- Class and process --------- #

class ToolBar:
    """
    [summary]
    ToolBar class make a simple toolbar to dispatch functionalities
    
    [Methode]
    __init__
    top_menu
    quit_app
    """    

    def __init__(self, master):
        """
        [summary]
        initiate class

        Args:
            master (class): tkinter parent page of main app
        """        
        self.root = master
        self.top_menu()

    def top_menu(self):
        """
        [summary]
        generate toolbar on the screen
        """        
        
        menubar = Menu(self.root)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(
            label="Modifier BDD [Grille tarifaire/Grille client/Grille vehicule]",
            command=lambda: MBP.modif_bdd_page(self.root))
        menu1.add_separator()
        menu1.add_command(
            label="Importer base de donnée [Not_Finished]", command=0)
        menu1.add_command(
            label="Exporter base de donnée Client",
            command=lambda: EIData.export_page("client"))
        menu1.add_command(
            label="Exporter base de donnée Véhicule",
            command=lambda: EIData.export_page("vehicule"))
        menu1.add_command(
            label="Exporter base de donnée Grille tarification",
            command=lambda: EIData.export_page("tarif"))
        menu1.add_separator()
        menu1.add_command(label="Sauvegarder", command=self.sauvegarde)
        menu1.add_command(label="Quitter & Sauvegarder", command=self.quit_app)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Grille Tariffaires",
                          command=lambda: gt.run(self.root))
        menu2.add_command(label="Grille Véhicules",
                          command=lambda: gv.run(self.root))
        menu2.add_command(label="Grille Clients",
                          command=lambda: gc.run(self.root))
        menu2.add_command(label="Réservation actuelle",
                          command=lambda: gr.run(self.root))
        
        menubar.add_cascade(label="Informations", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="Bienvenue",
                          command=lambda: WP.welcome_page(self.root))
        menu3.add_command(label="A propos",
                          command=lambda: messagebox.showinfo(title="A propos !",
                                                              message=WP.msgBoxAbout))
        menu3.add_command(label="? Aide ?",
                          command=lambda: HP.welcome_page(self.root))
        menubar.add_cascade(label="Aide", menu=menu3)

        self.root.config(menu=menubar)
        
    def sauvegarde(self):
        DT.enregistrer_json(DT.dfc, "./data/clients.json")
        DT.enregistrer_json(DT.dft, "./data/tarifs.json")
        DT.enregistrer_json(DT.dfv, "./data/vehicules.json")
        

    def quit_app(self):
        """
        [summary]
        a simple function to stop and save programme
        """        
        
        MessageBox = """
        Voulez-vous quittez l'application ?
        """
        resp = messagebox.askokcancel(
            title="Quitter Lock'Auto", message=MessageBox)
        if resp:
            DT.enregistrer_json(DT.dfc, "./data/clients.json")
            DT.enregistrer_json(DT.dft, "./data/tarifs.json")
            DT.enregistrer_json(DT.dfv, "./data/vehicules.json")
            self.root.destroy()
        else:
            pass

class MainApp:
    """
    [description]
    MainApp is the class for generating,
    load and instantiate the base of the management program.
    This class contains the graphical base.
    
    [Methode]
    __init__
    widgets
    admin
    """

    def __init__(self):
        """
        [summary]
        initiate class
        """        

        # Generate the main page with sitting
        self.root = tk.Tk()
        self.root.wm_attributes('-transparentcolor', 'red')
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.title("Gestionnaire Automobile - Lock'Auto")
        self.screen = str(self.w)+"x"+str(self.h)
        print(self.screen)
        self.root.geometry(self.screen)
        self.root.resizable(True, True)
        
        self.root.wm_state(newstate="zoomed")

        # Fullscreen mode
        #self.root.attributes('-fullscreen', 0)


        # Menu : 
        ToolBar(self.root)

        # Background image
        self.image = PhotoImage(file='./images/ABF8686-bewerkt.gif')
        self.canvas = Canvas(self.root, width=self.w, height=self.h)
        self.canvas.place(rely=0.0, relx=0.0, relwidth=1, relheight=1)
        self.canvas.create_image(0, 0, image=self.image, anchor=NW, )

        self.root.iconbitmap('./images/icon.ico')
        self.widgets()

        self.root.mainloop()

    def widgets(self):
        """
        [description]
        Function containing all the elements of the main page of the program.
        This function gathers all the buttons and interaction objects.

        :return:
        """

        # Banner 
        self.banner = tk.Frame(self.root, bg="#0d0d0d")
        self.banner.place(relx=0.001, rely=0.01,
                          relwidth=0.25, relheight=0.988)
        
        # Button of main functionnalities 
        tk.Button(self.banner, text='CLIENT',
            command=lambda: CP.client_page(self.root),
                bg="lightgrey").place(relx=0.3,
                    rely=0.2, relheight=0.05, relwidth=0.4)
        tk.Button(self.banner, text='RESERVATION',
                  command=lambda: RP.reserv_page(self.root),
                  bg="lightgrey").place(relx=0.3, rely=0.3,
                  relheight=0.05, relwidth=0.4)
        tk.Button(self.banner, text='TERMINER Location',
                                    command=lambda: FP.fin_loc_page(self.root), 
                                    bg="lightgrey").place(
                                        relx=0.3, rely=0.4, relheight=0.05,
                                        relwidth=0.4)
                                
                      
        def pointeur(event):
            """[summary]

            Args:
                event ([type]): [description]
            """            
            
            if event:
                x,y = event.x,event.y
                ee.easter_egg_page(x, y, self.root)
                  
        self.egg = tk.Label(self.root, bg="#0d0d0d")
        self.egg.place(relx=0.1, rely=0.80, relheight=0.05, relwidth=0.15)
        self.egg.bind("<Button-1>", pointeur)
        
        # Button ton select the following page to make an action                            
        self.admin = tk.Button(self.banner, text='ADMIN',
        command=self.admin, bg="lightgrey").place(relx=0.3, rely=0.55,
        relheight=0.05, relwidth=0.4)

        self.listeAdmin = ["Selectionner une action", "Ajout Véhicule",
                           "Modification Vehicule","Suppression Véhicule",
                           "Modification Client", "Suppression Client",
                           "Annulation d'une location", "Modification Tarif"]
        self.listeCombo1 = Combobox(
            self.banner, height=200, width=27, values=self.listeAdmin)
        self.listeCombo1.current(0)
        self.listeCombo1.place(
            relx=0.3, rely=0.6, relheight=0.05, relwidth=0.4)
        self.listeCombo1.bind("<<ComboboxSelected>>", self.admin)

    def admin(self):  # pylint: disable=E0202
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        # Get the selected item
        self.select = self.listeCombo1.get()
        print("Vous avez sélectionné : '", self.select, "'")

        if self.select == "Ajout Véhicule":
            AVP.ajout_vehi_page(self.root)
        elif self.select == "Suppression Véhicule":
            SVP.sup_vehi_page(self.root)
        elif self.select == "Suppression Client":
            SCP.sup_client_page(self.root)
        elif self.select == "Annulation d'une location":
            AnP.annul_page(self.root)
        elif self.select == "Modification Vehicule":
            MVP.modif_vehicule_page(self.root)
        elif self.select == "Modification Client":
            MCP.modif_client_page(self.root)
        elif self.select == "Modification Tarif":
            MTP.modif_tarif_page(self.root)


# ------ Run & Start server program ------ #


if __name__ == '__main__':
    print(__doc__)

    # Run the program
    app = MainApp()
