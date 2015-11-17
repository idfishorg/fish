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
# import simplejson as json
from google.appengine.api import urlfetch
html = """
<form action="identify" method="post">
    <input type="text" style="width:700" name = q>
    <input type="submit" value="identify">
</form>
"""

class IdentifyHandler(webapp2.RequestHandler):
    def post(self):
        url = self.request.get("q")
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            self.response.write("heloo")
        else:
            self.response.write("error")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('q')
        self.response.write('Thank you %s'%name)
        
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler),
    ('/identify', IdentifyHandler)
], debug=True)
