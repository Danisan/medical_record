# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Datamatic (<http://www.datamatic.com.uy>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Medical Record',
    'version': '1.0',
    'category': '',
    'description': """
    """,
    'author': 'LFer',
    'maintainer': 'LFer',
    'website': 'https://gitlab.com/LFer',
    'depends': ['base','medical','medical_patient_disease','medical_medication','medical_patient_disease_allergy'],
    'data': [
        'views/medical_record_partient.xml',

    ],
    'installable': True,

}
