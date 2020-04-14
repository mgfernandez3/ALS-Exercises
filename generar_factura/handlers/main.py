#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from datetime import datetime


class MainHandler(webapp2.RequestHandler):
    def post(self):
        valores = self.request.POST.items()

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = dict()

        for i in valores:
            if i[1]:
                valores_plantilla[i[0]] = i[1]
            else:
                self.response.write("Datos no validos")

        valores_plantilla["fecha"] = datetime.utcnow()

        self.response.write(jinja.render_template("factura.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/factura', MainHandler)
], debug=True)
