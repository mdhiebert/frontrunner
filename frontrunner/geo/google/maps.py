import requests

class StaticMap:
    '''
        Wrapper for Google's static map API
    '''

    BASE_REQUEST = 'https://maps.googleapis.com/maps/api/staticmap?'

    def __init__(self, api_key) -> None:
        self._api_key = api_key

    def get_map(self, center, zoom, size, scale=None, format=None, maptype=None, language=None, region=None, hide_overlay=True):
        '''
            More information here: https://developers.google.com/maps/documentation/maps-static/start

            Parameters
            ----------
            center :: str : (required if markers not present) defines the center of the map, equidistant from all edges of the map. This parameter takes a location as either a comma-separated {latitude,longitude} pair (e.g. "40.714728,-73.998672") or a string address (e.g. "city hall, new york, ny") identifying a unique location on the face of the earth. For more information, see Locations below.

            zoom :: str : (required if markers not present) defines the zoom level of the map, which determines the magnification level of the map. This parameter takes a numerical value corresponding to the zoom level of the region desired. For more information, see zoom levels below.

            size :: str : (required) defines the rectangular dimensions of the map image. This parameter takes a string of the form {horizontal_value}x{vertical_value}. For example, 500x400 defines a map 500 pixels wide by 400 pixels high. Maps smaller than 180 pixels in width will display a reduced-size Google logo. This parameter is affected by the scale parameter, described below; the final output size is the product of the size and scale values.

            scale :: int or str : (optional) affects the number of pixels that are returned. scale=2 returns twice as many pixels as scale=1 while retaining the same coverage area and level of detail (i.e. the contents of the map don't change). This is useful when developing for high-resolution displays. The default value is 1. Accepted values are 1 and 2. See Scale Values for more information.

            format :: str : (optional) defines the format of the resulting image. By default, the Maps Static API creates PNG images. There are several possible formats including GIF, JPEG and PNG types. Which format you use depends on how you intend to present the image. JPEG typically provides greater compression, while GIF and PNG provide greater detail. For more information, see Image Formats.

            maptype :: str : (optional) one of either {roadmap, satellite, terrain, hybrid}. default is roadmap

            language :: str : (optional) the language of this map, default is english

            region :: str : (optional) the regional perspective from which to view this map. default is USA

            hide_overlay :: bool : (optional) whether or not to hide the default overlay graphics provided by google maps API

        '''

        args = {
            'center': center,
            'zoom': zoom,
            'size': size,
            'scale': scale,
            'format': format,
            'maptype': maptype,
            'language': language,
            'region': region,

            # TODO styling

            'key': self._api_key
        }

        if hide_overlay:
            args['style'] = 'feature:poi|element:labels|visibility:off&style=feature:road|visibility:off'
            args['style'] += '&style=feature:road|visibility:off&style=feature:landscape|visibility:off&style=feature:road|visibility:off'

        argstring = self._aggregate_args(args)

        res = requests.get(f'{self.BASE_REQUEST}{argstring}')

        return res.content


    def _aggregate_args(self, args: dict):
        arglist = [f'{key}={val}' for key,val in args.items() if val is not None]
        return '&'.join(arglist)

        

    

    