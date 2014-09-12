#! /usr/bin/env python
# encoding: utf-8

import requests

class AuthenticationMixinBase(object):
    """Provide core logic to the authentication mixins."""

    def call_grant(self, path, data):
        """Perform the calls to the grant endpoints.

        These endpoints handle the echange to get the information from the API.
        """
        assert self.app_info[0] is not None and self.app_info[1] is not None

        resp = requests.post(self.API_ROOT + path,
            auth=self.app_info,
            data=data)

        return resp.status_code, resp.headers, resp.json()