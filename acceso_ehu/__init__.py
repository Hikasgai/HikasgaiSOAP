# -*- coding: utf-8 -*-
"""La librería lib_ehu recoge datos académicos
   de la página web: http://www.ehu.eus/es/.

   Los datos se obtienen a través de la técnica scraping,
   con ayuda de la librería BeautifulSoup.

   BeautifulSoup se pude descargar directamente mediante
   el comando:

        $ pip install beautifulsoup
        $ pip install bs4
        $ pip install html5lib
"""

__author__ = "Alain Barrero (alaininformatica@gmail.com)"
__version__ = "1.0.0"
__copyright__ = "Copyright (c) 2016 Alain Barrero"

__all__ = ['lib_ehu']

from .asginaturasGrado import obtenerAsignaturasGradoInformatica
