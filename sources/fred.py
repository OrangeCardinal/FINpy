import csv
import certifi
import logging
import json
from urllib.parse import urlencode
import urllib3
import tempfile
import zipfile

logger = logging.getLogger(__name__)

class FederalReserveEconomicData(object):
    FRED_FINPY_API_KEY = "d0a92dbe5ee12c742168bd38ad20f9db"  # API Key for this module (can be shared)
    BASE_URL = "https://api.stlouisfed.org/fred/"

    #TODO: change file_type to response_type (DataFrame, xml, json, dict)
    def __init__(self, user_api_key=None):
        self.api_key = self.FRED_FINPY_API_KEY
        if user_api_key:
            self.api_key = user_api_key


    def _get_data(self, url, params):
        """
        Makes the actual request to the FRED API, parses the response as needed, and returns the requested data
        :param url:
        :param params: url GET parameters
        :return:
        """
        encoded_params = urlencode(params)
        url = "{0}{1}?{2}".format(self.BASE_URL, url, encoded_params)
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        response = http.request('GET', url)
        json_data = json.loads(response.data)
        return json_data

    ####################
    ## Core API Calls ##
    ####################
    def category(self, category_id=0, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/category.html
        :param category_id: Category Id (0 is the root category)
        :param file_type:
        :return:
        """
        url = 'category'
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def category_children(self, category_id=0, realtime_start=None, realtime_end=None, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/category_children.html

        :param category_id: Category Id (0 is the root category)
        :param file_type:
        :return:
        """
        url = "category/children"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def category_related(self, category_id=0, realtime_start=None, realtime_end=None, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/category_related.html

        :param category_id: Category Id (0 is the root category)
        :param file_type:
        :return:
        """

        url = "category/related"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)


    def category_series(self, category_id=0, realtime_start=None, realtime_end=None, limit=None, offset=None,
                        order=None, sort_order=None, filter_variable=None, filter_value=None,
                        tag_names=None, exclude_tag_names=None, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/category_related.html

        :param category_id: Category Id (0 is the root category)
        :param file_type:
        :return:
        """
        url = "category/series"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)


    def category_tags(self, category_id=0, realtime_start=None, realtime_end=None, limit=None, offset=None,
                        order=None, sort_order=None, filter_variable=None, filter_value=None,
                        tag_names=None, exclude_tag_names=None, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/category_related.html

        :param category_id: Category Id (0 is the root category)
        :param file_type:
        :return:
        """
        url = "category/tags"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def category_related_tags(self, category_id=0, realtime_start=None, realtime_end=None, limit=None, offset=None,
                        order=None, sort_order=None, filter_variable=None, filter_value=None,
                        tag_names=None, exclude_tag_names=None, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/category_related.html

        :param category_id: Category Id (0 is the root category)
        :param file_type:
        :return:
        """
        url = "category/related_tags"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def releases(self, realtime_start=None, realtime_end=None, limit=None, order=None, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/releases.html
        :return:
        """
        url = "releases"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def releases_date(self, realtime_start=None, realtime_end=None, limit=None, order=None, file_type='json'):
        """

        :return:
        """
        url = "releases/date"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def release(self, release_id, realtime_start=None, realtime_end=None, limit=None, order=None, file_type='json'):
        """

        :return:
        """
        url = "release"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def release_date(self, realtime_start=None, realtime_end=None, limit=None, order=None, file_type='json'):
        """

        :return:
        """
        url = "release/date"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def release_series(self, realtime_start=None, realtime_end=None, limit=None, order=None, file_type='json'):
        """

        :return:
        """
        url = "release/series"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def release_sources(self, realtime_start=None, realtime_end=None, limit=None, order=None, file_type='json'):
        """

        :return:
        """
        url = "release/sources"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def release_tags(self, realtime_start=None, realtime_end=None, limit=None, order=None, file_type='json'):
        """

        :return:
        """
        url = "release/tags"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def release_related_tags(self, realtime_start=None, realtime_end=None, limit=None, order=None, file_type='json'):
        """

        :return:
        """
        url = "release/related_tags"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def release_tables(self, realtime_start=None, realtime_end=None, limit=None, order=None, file_type='json'):
        """

        :return:
        """
        url = "release/tables"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def series(self, series_id:str, realtime_start=None, realtime_end=None, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series.html
        :return:
        """
        url = "series"
        params = {'file_type': file_type, 'api_key': self.api_key, 'series_id':series_id}
        return self._get_data(url, params)

    def series_categories(self, series_id:str, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series_categories.html
        :return:
        """
        url = "sources"
        params = {'file_type': file_type, 'api_key': self.api_key, "series_id":series_id}
        return self._get_data(url, params)

    def series_observations(self, series_id:str, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series_observations.html
        :return:
        """
        url = 'series/observations'
        params = {'file_type':file_type, 'api_key':self.api_key,'series_id':series_id}
        return self._get_data(url, params)

    def series_release(self, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series_release.html
        :param file_type:
        :return:
        """
        url = "series/release"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)


    def series_search(self, search_text:str, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series_search.html
        :param file_type:
        :return:
        """
        url = "series/search"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)



    def series_search_related_tags(self, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series_search_related_tags.html
        :param file_type:
        :return:
        """
        url = "series/search/related_tags"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def series_search_tags(self, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series_search_tags.html
        :param file_type:
        :return:
        """
        url = "series/observations"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def series_tags(self, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series_updates.html
        :param file_type:
        :return:
        """
        url = "series/updates"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def series_updates(self, realtime_start=None, realtime_end=None, limit=None, offset=None, filter_value=None,
                    time_start=None, time_end=None, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series_tags.html
        :param realtime_start:
        :param realtime_end:
        :param limit:
        :param offset:
        :param filter_value:
        :param time_start:
        :param time_end:
        :param file_type:
        :return:
        """
        url = "series/tags"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def series_vintagedates(self, series_id, realtime_start=None, realtime_end=None, limit=None, offset=None,
                            sort_order=None, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/series_tags.html
        :param series_id:
        :param realtime_start:
        :param realtime_end:
        :param limit:
        :param offset:
        :param filter_value:
        :param time_start:
        :param time_end:
        :param file_type:
        :return:
        """
        url = "series/vintagedates"
        params = {'file_type': file_type, 'api_key': self.api_key, 'category_id': category_id}
        return self._get_data(url, params)

    def sources(self, file_type='json'):
        """
        Returns data from the sources FRED API call
        ## References
        https://research.stlouisfed.org/docs/api/fred/sources.html

        :param file_type:
        :return:
        """
        url = "fred/sources"
        params = {'file_type': file_type, 'api_key': self.api_key}
        return self._get_data(url, params)


    def source(self, source_id, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/source.html
        :param source_id:
        :param file_type:
        :return:
        """
        url = "fred/source"
        params = {'file_type': file_type, 'api_key': self.api_key, 'source_id': source_id}
        return self._get_data(url, params)

    def source_releases(self, source_id, file_type='json'):
        """
        https://research.stlouisfed.org/docs/api/fred/source_releases.html
        :return:
        """
        url = "source/releases"
        params = {'file_type': file_type, 'api_key': self.api_key, 'source_id': source_id}
        return self._get_data(url, params)

    ###########################
    ## Convenience Functions ##
    ###########################
    def get_libor_rates(self):
        """

        ==============
        = References =
        ==============
        https://fred.stlouisfed.org/categories/33003/downloaddata/LIBOR_csv_2.zip
        :return libor_rates: LiborRates object containing all parsed data
        """

        # Download the zipfile and store it in a temp file
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        response = http.request('GET',self.LIBOR_CSV_URL)
        temp_zip_filename = tempfile.mktemp()
        temp_zip_file = open(temp_zip_filename, 'wb')
        temp_zip_file.write(response.data)
        temp_zip_file.close()


        # Confirm we have a zipfile as expected
        if zipfile.is_zipfile(temp_zip_filename) == False:
            raise Exception("downloaded file is not a zipfile.")

        zip = zipfile.ZipFile(temp_zip_filename)
        print(zip.namelist())
        #zip.extract()
        #zip.extractall(temp_directory)
        #zip.close()

        #filename = os.listdir(temp_directory)[0]

        #filename = "{0}\{1}".format(temp_directory, os.listdir(temp_directory)[0])
        #print(filename)
        #print(os.path.isfile(filename))
        #print(os.listdir(temp_directory))
        #libor_csv = open(filename)
        #for line in libor_csv:
        #    print(line)
        #with open(filename,'r') as libor_csv:
        #    for line in libor_csv:
        #        print(line)
        #print(request.data)
        #csv_reader = csv.reader(request.data)
        #for line in csv_reader:
        #    print(line)