# -*- coding: utf-8 -*-

from email.policy import default
from odoo import api,fields,models,_
from odoo.tools.misc import formatLang, get_lang
from datetime import date


class InvoiceAssur(models.Model):
    _inherit = 'account.move'


    @api.depends('partner_id')
    def _compute_num_compte(self):
        self.num_compte =  self.partner_id.num_compte

    ref_dossier             = fields.Char(string = "Numéro de reférence du dossier")
    assured                 = fields.Many2one("res.partner" ,string='Assuré')
    num_compte              = fields.Char(string='Numéro de compte' , compute= _compute_num_compte)
    invoice_date            = fields.Date(string='Date de facturation' , default=fields.Date.context_today)
    # date_assur_end          = fields.Date(related="invoice_line_ids.end_date" , string="Echeance de l'assurance")

    assurance_type = fields.Selection([
        ('maladie', 'assurance maladie'),
        ('auto', 'assurance automobile')
    ], string="Type d'assurance", default ="auto")
    
    # assur = fields.Selection(related='assurance_type', string='assur')
    

#_____________________ contexte d'assurance automobile

    nom_conducteur = fields.Many2one("res.partner" ,string="Conducteur")
    
    zone_tarif = fields.Selection([
        ('a', 'A (Grandes villes)'),
        ('b', 'B (Chefs-lieux de département)'),
        ('c', 'C (Petites villes et villages)')
    ], string='zone tarif', default='a')
    cat_permis = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    ], string='cat. permis', default = 'b' )
    
    modele = fields.Char('Modèle', required=True)
    car_usage  = fields.Selection([
        ('Tourisme', 'Tourisme'),
        ('Personnel', 'Personnel'),
    ], string='Utilisation du véhicule', default = 'Tourisme')
    
    date_acquisition = fields.Date('date_acquisition')
    car_chassis = fields.Char('Numéro de chassis')
    car_category = fields.Selection([
        ('categorie 1', 'CAT 01'),
        ('categorie 2', 'CAT 02'),
        ('categorie 3', 'CAT 03'),
        ('categorie 4', 'CAT 04'),
        ('categorie 5', 'CAT 05'),
        ('categorie 6', 'CAT 06'),
        ('categorie 7', 'CAT 07'),
        ('categorie 8', 'CAT 08'),
        ('categorie 9', 'CAT 09'),
        ('categorie 10', 'CAT 10'),
    ], string='Catégorie', default='categorie 1')
    

    car_power               = fields.Integer(string="Puissance du véhicule")
    car_energie             = fields.Selection([('ess','Essence'),('gas','Gasoil')], 
        string="Energie", default="ess")
    car_brand               = fields.Char(string="Marque du vehicule", required=True)
    car_immatriculation     = fields.Char(string="Immatriculation du véhicule", required=True)
    # car_category            = fields.Char(string="Categorie ")
    car_place_number        = fields.Integer(string="Nombre de place")
    # car_usage               = fields.Char(string= "Utilisation du vehicule")

# ____________________contexte d'assurance maladie

    Nom_client = fields.Char('Nom_client')
    pack = fields.Selection([
        ('individuel', 'Individuel'),
        ('famille', 'Famille'),
        ('groupe', 'Groupe')
    ], string="Pack d'assurance", default = 'individuel')
    
    Nbre_assure = fields.Integer("Nombre d'assures")
    
    Age = fields.Selection([
        ('enfant', '< 18 ans'),
        ('adulte', 'entre 18 et 65 ans'),
        ('vieillard', '> 65 ans')
    ], string='Age des assures')
    
    Nmro_CNI = fields.Char('Numero de CNI du client')
    
    
    
    
class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    assurance_type= fields.Selection(related='move_id.assurance_type')
    
