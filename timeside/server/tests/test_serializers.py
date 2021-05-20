from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from timeside.server.tests.timeside_test_server import TimeSideTestServer
from timeside.server.serializers import *
from timeside.server.models import Item
from django.contrib.sites.models import Site



class TestSerializers(APITestCase):

    def setUp(self):
        TimeSideTestServer.setUp(self)
        self.client.login(username='admin', password='admin')
        self.sweep_32000=Item.objects.get(title="sweep_32000")
        current_domain = Site.objects.get_current().domain

    def test_item_playable_serializer(self):
        ips=ItemPlayableSerializer()
        current_site = Site.objects.get_current()
        self.assertEqual("https://"+current_site.domain+"/timeside/player/#item/"+str(self.sweep_32000.uuid)+'/',ips.get_player_url(self.sweep_32000))

    def test_item_list_serializer(self):
        ils=ItemListSerializer(
            context={'model': self.sweep_32000})
        print(ils.data)
        print(ils.get_url(self.sweep_32000))
        
    def test_audio_url_serializer(self):
        aus=AudioUrlSerializer()
        print(aus.to_representation(self.sweep_32000))