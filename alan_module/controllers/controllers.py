 -*- coding: utf-8 -*-
from odoo import http

 class AlanModule(http.Controller):
     @http.route('/alan_module/alan_module/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/alan_module/alan_module/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('alan_module.listing', {
             'root': '/alan_module/alan_module',
             'objects': http.request.env['alan_module.alan_module'].search([]),
         })

     @http.route('/alan_module/alan_module/objects/<model("alan_module.alan_module"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('alan_module.object', {
             'object': obj
         })