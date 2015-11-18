#--------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# 
# Code generated by Microsoft (R) AutoRest Code Generator 0.13.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
#--------------------------------------------------------------------------

from msrest.serialization import Model

class Product(Model):

    _required = []

    _attribute_map = {
        'display_names':{'key':'display_names', 'type':'[str]'},
        'capacity':{'key':'capacity', 'type':'int'},
        'image':{'key':'image', 'type':'str'},
    }

    def __init__(self, *args, **kwargs):

        self.display_names = []
        self.capacity = None
        self.image = None
