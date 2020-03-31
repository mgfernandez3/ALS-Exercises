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


class MainHandler(webapp2.RequestHandler):
    def post(self):
        distancia = str(self.request.get("edDistancia"))
        tiempo = str(self.request.get("edTiempo"))
        consumo = str(self.request.get("edConsumo"))

        if not str.isdigit(distancia) or not str.isdigit(tiempo) or not str.isdigit(consumo) or distancia.strip() == 0 or tiempo.strip() == 0 or consumo.strip() == 0 or float(int(tiempo)) == 0:
            self.response.write("Datos no validos")
        else:
            velocidad = float(int(distancia)) / float(int(tiempo))
            consumo_total = float(int(distancia)) * float(int(consumo))
            self.response.write("Velocidad media: " + str(velocidad) + " km/h<br/>Consumo total: " + str(consumo_total) + " l")


app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
