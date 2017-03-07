# -*- coding: utf_8 -*-

import unicodedata
import sys
import csv
import calendar
import time
import subprocess
import os
from os.path import basename,isfile
import string
import random
import ipdb as pdb
import math
import base64
import datetime
import cPickle as pickle
import locale
import codecs

import openerp.addons.decimal_precision as dp
from openerp import models, fields, api, _, http
from openerp.exceptions import Warning, ValidationError
from openerp.modules import get_module_path
from openerp.http import request
from openerp.addons.web.controllers.main import serialize_exception,content_disposition


class medical_record_patient(models.Model):
    _name = 'medical.patient'
    _inherit = 'medical.patient'


    medical_record = fields.Text(string='Medical Record')

medical_record_patient()
