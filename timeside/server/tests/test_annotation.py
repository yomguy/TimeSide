from timeside.server.tests.timeside_test_server import TimeSideTestServer
from timeside.server.models import *

class TestAnnotation(TimeSideTestServer):

    def obj_url(self,obj):
        return '/timeside/api/items/'+str(obj.uuid)+'/'

    def test_create_annotation_track(self):
        item=Item.objects.all()[0]
        user=User.objects.all()[0]
        len_annotation_track=AnnotationTrack.objects.count()
        data={
            "item": self.obj_url(item),
            "title": "test_create_annotation_track",
            "author": '/timeside/api/users/'+str(user.username)+'/',
            "is_public": False,
        }
        annotation_track=self.client.post('/timeside/api/annotation_tracks/',data)
        self.assertEqual(annotation_track.status_code,201)

        data={
            "item": self.obj_url(item),
            "title": "test_create_annotation_track_2",
            "author": '/timeside/api/users/'+str(user.username)+'/',
            "is_public": True,
        }
        annotation_track_2=self.client.post('/timeside/api/annotation_tracks/',data)
        self.assertEqual(annotation_track_2.status_code,201)

        list_annotation_track=self.client.get('/timeside/api/annotation_tracks/')
        self.assertEqual(list_annotation_track.status_code,200)
        self.assertEqual(len(list_annotation_track.data),len_annotation_track+2)

        #test_privacy_of_annotation

        user = User.objects.create(username='usertest')
        self.client.force_authenticate(user)
        list_annotation_track=self.client.get('/timeside/api/annotation_tracks/')
        self.assertEqual(list_annotation_track.status_code,200)
        self.assertEqual(len(list_annotation_track.data),len_annotation_track+1)

        
