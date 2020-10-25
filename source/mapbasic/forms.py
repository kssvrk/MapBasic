from django.contrib.gis import forms

import floppyforms as gisforms

class OsmPolygonWidget(gisforms.gis.PolygonWidget, gisforms.gis.BaseOsmWidget):
    pass


class UserMapForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=5000, widget=forms.Textarea(
        attrs={'rows': 30,
               'cols': 20,
               'style': 'height: 5em;'}
    ))
    aoi=gisforms.gis.PolygonField(widget=OsmPolygonWidget)
    # aoi = forms.PolygonField(widget=forms.OSMWidget(
    #     attrs={'map_width': 600,
    #            'map_height': 400,
    #            'template_name': 'gis/openlayers-osm.html',
    #            'default_lat': 21.7,
    #            'default_lon': 78,
    #            'default_zoom': 4}
    # ))
    # added_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
