
##############################################################################
#
# Copyright (C) 2015 BachacoVE
# Copyright (C) 2017 Empero LLC
# Copyright (C) 2025 Gustavo Lopez
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 
##############################################################################
{
    "name": "Localización Politico Territorial Venezolana: Municipios y Parroquias",
    "version": "18.0.1.0.0",
    "author": "Gustavo Lopez, Empero LLC, BachacoVE",
    "category": "Localization",
    "description":
        """
Localización Venezolana: Municipios y Parroquias
================================================

Basado en información del INE del año 2013, en el trabajo de BachacoVE y en el de Empero LLC, añade los campos de municipio y parroquia a _Contactos_ de
manera que queden disponibles en todos los campos de dirección derivados como _Usuarios_ o _Empresas_.
     """,
    'license': 'LGPL-3',
	'images': ['static/description/icon.png'],
    "depends": ['base', ],
    "data": [
        'security/ir.model.access.csv',
        'data/res.country.state.xml',
        'data/res.country.state.municipality.xml',
        'data/res.country.state.municipality.parish.xml',
        'views/res_company_views.xml',
        'views/l10n_ve_dpt_view.xml',
        'views/res_partner.xml',
    ],
    "installable": True
}
