# -*- coding: utf-8 -*-

from odoo import api,fields,models,_
from odoo.exceptions import UserError
import datetime



class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    start_date  = fields.Date(string= "Date effective" , required = True, default = datetime.datetime.today())
    end_date    = fields.Date(string= "Date d'échéance")
    police      = fields.Char(string="Police")
    risque      = fields.Char(string="Risque")
    accessoire  = fields.Monetary(string="Accessoires")
    dta         = fields.Monetary(string="DTA")
    autres      = fields.Monetary(string="Autres")
    prime_net   = fields.Monetary(string="Prime Net")



    @api.onchange('prime_net',
                  'accessoire')
    def update_price_unit(self):
        self.price_unit = self.prime_net + self.accessoire

    @api.onchange('quantity', 'discount', 'price_unit', 'tax_ids' ,'dta','autres')
    def _onchange_price_subtotal(self):
        self.price_subtotal = self.price_unit + self.dta + self.autres
        for line in self:
            if not line.move_id.is_invoice(include_receipts=True):
                continue

            line.update(line._get_price_total_and_subtotal())
            line.update(line._get_fields_onchange_subtotal(price_subtotal = self.price_subtotal))

    @api.model
    def _get_price_total_and_subtotal_model(self, price_unit, quantity, discount, currency, product, partner, taxes, move_type):
        ''' This method is used to compute 'price_total' & 'price_subtotal'.

        :param price_unit:  The current price unit.
        :param quantity:    The current quantity.
        :param discount:    The current discount.
        :param currency:    The line's currency.
        :param product:     The line's product.
        :param partner:     The line's partner.
        :param taxes:       The applied taxes.
        :param move_type:   The type of the move.
        :return:            A dictionary containing 'price_subtotal' & 'price_total'.
        '''
        res = {}

        # Compute 'price_subtotal'.
        line_discount_price_unit = price_unit * (1 - (discount / 100.0))
        subtotal = quantity * line_discount_price_unit + self.dta + self.autres

        # Compute 'price_total'.
        if taxes:
            force_sign = -1 if move_type in ('out_invoice', 'in_refund', 'out_receipt') else 1
            taxes_res = taxes._origin.with_context(force_sign=force_sign).compute_all(line_discount_price_unit,
                quantity=quantity, currency=currency, product=product, partner=partner, is_refund=move_type in ('out_refund', 'in_refund'))
            res['price_subtotal'] = taxes_res['total_excluded'] + self.dta + self.autres
            res['price_total'] = taxes_res['total_included'] + self.dta + self.autres
        else:
            res['price_total'] = res['price_subtotal'] = subtotal
        #In case of multi currency, round before it's use for computing debit credit
        if currency:
            res = {k: currency.round(v) for k, v in res.items()}
        return res


