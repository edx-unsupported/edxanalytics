"""
Generate dummy data for testing
"""
# import uuid
import random
import string
# import time
import datetime
# from edinsights.core.decorators import view, query, event_handler, memoize_query


def random_date(start, end):
    """
    This function returns a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def generate_random_data(size):
    """
    Generate random data of given size (in pairs of play and pause)
    example tuple:
    (u'juhokim', u'2013-05-31 11:35:50.276888', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"4rpg8Bq6hb4","currentTime":0,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:35:50.275822', 194, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/')
    """
    result = []

    # create random names
    names = []
    for j in range(0, 1500):
        names.append(''.join(random.choice(string.ascii_lowercase) for x in range(6)))

    # TODO: hard-coded
    duration = 171
    date1 = datetime.datetime(2013, 3, 1, 0, 0, 0, 0)
    date2 = datetime.datetime(2013, 6, 30, 0, 0, 0, 0)

    for i in range(0, size):
        username = random.choice(names)
        dt_org = random_date(date1, date2)
        dtcreated = unicode(dt_org.strftime("%Y-%m-%d %H:%M:%S.%f"))
        event_source = u'browser'
        event_type = u'play_video'
        ip_addr = u'127.0.0.1'
        agent = u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'
        event = {}
        event["id"] = "i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x"
        event["code"] = "2deIoNhqDsg"
        #event["currentTime"] = int(random.random() * duration)
        event["currentTime"] = int(random.betavariate(0.1, 10) * duration)
        event["speed"] = random.choice(["0.75", "1.0", "1.25", "1.5"])
        event_string = unicode(event)
        host = u'1.0.0.127.in-addr.arpa'
        time_field = dtcreated
        id_field = 0
        #show this link somewhere in the page
        page = u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'


        # entry = (username, dtcreated, event_source, event_type, ip_addr, agent, event_string, host, time_field, id_field, page)
        entry = {
            'username': username,
            'dtcreated': dtcreated,
            'event_source': event_source,
            'event_type': event_type,
            'ip': ip_addr,
            'agent': agent,
            'event': event_string,
            'host': host,
            'time': time_field,
            'id': id_field,
            'page': page
        }
        result.append(entry)

        # now add a paired tuple
        event_type = u'pause_video'
        new_event = {}
        new_event["id"] = event["id"]
        new_event["code"] = event["code"]
        new_event["speed"] = event["speed"]
        new_duration = int(random.random() * (duration - event["currentTime"]))
        new_event["currentTime"] = event["currentTime"] + new_duration
        new_event_string = unicode(new_event)
        id_field = 0  # uuid.uuid4().int
        new_dt = dt_org + datetime.timedelta(0, new_duration)
        new_time = unicode(new_dt.strftime("%Y-%m-%d %H:%M:%S.%f"))
        # print username, event_type, time_field, new_time, event["currentTime"], new_event["currentTime"]
        #entry = (username, new_time, event_source, event_type, ip_addr, agent, new_event_string, host, new_time, id_field, page)
        entry = {
            'username': username,
            'dtcreated': new_time,
            'event_source': event_source,
            'event_type': event_type,
            'ip': ip_addr,
            'agent': agent,
            'event': new_event_string,
            'host': host,
            'time': new_time,
            'id': id_field,
            'page': page
        }
        result.append(entry)
    return result


def get_hardcoded_data():
    """
    Return small samples of dummay data
    """
    result = [(u'juhokim', u'2013-05-31 11:35:50.276888', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"4rpg8Bq6hb4","currentTime":0,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:35:50.275822', 194, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:35:53.038760', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"4rpg8Bq6hb4","currentTime":1.967,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:35:53.037833', 195, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:35:56.938738', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"4rpg8Bq6hb4","currentTime":1.967,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:35:56.937573', 196, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:35:58.712242', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"4rpg8Bq6hb4","currentTime":3.723,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:35:58.711585', 197, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:43:21.579282', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"4rpg8Bq6hb4","currentTime":20,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:43:21.578603', 198, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:43:25.808996', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"4rpg8Bq6hb4","currentTime":24,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:43:25.808337', 199, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:43:29.770052', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"4rpg8Bq6hb4","currentTime":24,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:43:29.769145', 200, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:43:33.221546', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"4rpg8Bq6hb4","currentTime":27.175,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:43:33.221005', 201, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:43:38.741510', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"q1xkuPsOY6Q","currentTime":"18.117","speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:43:38.740632', 202, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:43:56.356217', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V1_Motivation_for_6_002x","code":"q1xkuPsOY6Q","currentTime":35.585,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:43:56.355444', 203, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:48:18.651950', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":0,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:48:18.651044', 206, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:48:44.467385', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":25.248,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:48:44.466817', 207, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:48:52.519875', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":25.248,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:48:52.519114', 208, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:49:30.311703', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":62.628,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:49:30.310672', 209, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 11:49:55.289938', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":113.814,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 15:49:55.288920', 210, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 12:37:51.041361', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":11,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 16:37:51.040205', 211, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 12:37:53.006115', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":12.246,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 16:37:53.005267', 212, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 12:37:53.753339', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":53,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 16:37:53.752787', 213, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 12:37:55.776533', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":69,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 16:37:55.775983', 214, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 12:46:23.902498', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":69,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 16:46:23.901631', 215, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 12:46:30.202764', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":74.431,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 16:46:30.202105', 216, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 12:46:33.589230', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":102.314,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 16:46:33.588563', 217, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 13:00:16.984349', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"-CWjfl0DKm8","currentTime":0,"speed":"1.50"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 17:00:16.983276', 218, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 13:18:29.418422', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":"0.000","speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 17:18:29.417257', 219, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 13:18:41.588343', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":11.333,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 17:18:41.587056', 220, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 13:18:55.647950', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":70.803,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 17:18:55.646514', 221, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:19:20.677633', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":0,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:19:20.676589', 227, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:19:41.690078', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":20.393,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:19:41.689278', 228, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:20:02.869925', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":20.393,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:20:02.869141', 229, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:20:18.203969', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":35.536,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:20:18.203369', 230, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:20:40.158654', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":99,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:20:40.158046', 231, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:20:42.162036', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":131,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:20:42.161504', 232, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:21:02.759296', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":131,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:21:02.758500', 233, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:21:12.452481', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":140.249,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:21:12.451905', 234, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:21:42.940506', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":24,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:21:42.939378', 235, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:22:03.999339', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":24,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:22:03.998718', 236, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:22:16.539632', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":35.787,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:22:16.538977', 237, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-05-31 17:22:27.426815', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":98.661,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-05-31 21:22:27.426094', 238, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-06-03 11:28:57.614538', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S2V1_Review_KVL_KCL","code":"eLAyO33baQ8","currentTime":0,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-06-03 15:28:57.613530', 248, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Circuit_Analysis_Toolchest/'), (u'juhokim', u'2013-06-03 11:28:58.706628', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S2V1_Review_KVL_KCL","code":"eLAyO33baQ8","currentTime":0.489,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-06-03 15:28:58.706061', 249, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Circuit_Analysis_Toolchest/'), (u'juhokim', u'2013-06-03 12:52:26.716121', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":98.661,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-06-03 16:52:26.715498', 251, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-06-03 12:52:58.384801', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":66,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-06-03 16:52:58.384153', 252, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-06-03 12:54:43.212938', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":170.60500000000002,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-06-03 16:54:43.211874', 253, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-06-03 12:55:57.455615', u'browser', u'play_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":2,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-06-03 16:55:57.454644', 254, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/'), (u'juhokim', u'2013-06-03 12:56:29.562912', u'browser', u'pause_video', u'127.0.0.1', u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4', u'{"id":"i4x-MITx-6_002x-video-S1V2_Administrivia","code":"2deIoNhqDsg","currentTime":33.341,"speed":"1.0"}', u'1.0.0.127.in-addr.arpa', u'2013-06-03 16:56:29.562163', 255, u'http://localhost:8000/courses/MITx/6.002x/2013_Spring/courseware/Week_1/Administrivia_and_Circuit_Elements/')]
    return result
