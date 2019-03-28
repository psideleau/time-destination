

#Author: Alhussain Darbi
###################################


#I could not get a result because I do not have database to hold the values which are pulled from the API


import googlemaps
from googlemaps import convert


_ROADS_BASE_URL = "https://roads.googleapis.com"


def snap_to_roads(client, path, interpolate=False):  #Snaps a path to the most likely roads travelled
   

    params = {"path": convert.location_list(path)}

    if interpolate:
        params["interpolate"] = "true"

    return client._request("/v1/snapToRoads", params,
                       base_url=_ROADS_BASE_URL,
                       accepts_clientid=False,
                       extract_body=_roads_extract).get("snappedPoints", [])

def nearest_roads(client, points): #Find the closest road segments for each point

    params = {"points": convert.location_list(points)}

    return client._request("/v1/nearestRoads", params,
                       base_url=_ROADS_BASE_URL,
                       accepts_clientid=False,
                       extract_body=_roads_extract).get("snappedPoints", [])

###Hamdan Helped me with speed_limits function###
def speed_limits(client, place_ids): #Returns the posted speed limit (in km/h) for given road segments

    params = [("placeId", place_id) for place_id in convert.as_list(place_ids)]

    return client._request("/v1/speedLimits", params,
                       base_url=_ROADS_BASE_URL,
                       accepts_clientid=False,
                       extract_body=_roads_extract).get("speedLimits", [])


def snapped_speed_limits(client, path):
    

    params = {"path": convert.location_list(path)}

    return client._request("/v1/speedLimits", params,
                       base_url=_ROADS_BASE_URL,
                       accepts_clientid=False,
                       extract_body=_roads_extract)


def _roads_extract(resp): #Extracts a result from a Roads API HTTP response

    try:
        j = resp.json()
    except:
        if resp.status_code != 200:
            raise googlemaps.exceptions.HTTPError(resp.status_code)

        raise googlemaps.exceptions.ApiError("UNKNOWN_ERROR",
                                             "Received a malformed response.")

    if "error" in j:
        error = j["error"]
        status = error["status"]

        if status == "RESOURCE_EXHAUSTED":
            raise googlemaps.exceptions._OverQueryLimit(status,
                                                        error.get("message"))

        raise googlemaps.exceptions.ApiError(status, error.get("message"))

    if resp.status_code != 200:
        raise googlemaps.exceptions.HTTPError(resp.status_code)

    return j




#new class for destinations A and B
from googlemaps import convert


def directions(client, origin, destination,
               mode=None, waypoints=None, alternatives=False, avoid=None,
               language=None, units=None, region=None, departure_time=None,
               arrival_time=None, optimize_waypoints=False, transit_mode=None,
               transit_routing_preference=None, traffic_model=None):
    

    params = {
        "origin": convert.latlng(origin),
        "destination": convert.latlng(destination)
    }

    if mode:
        
        if mode not in ["driving", "walking", "bicycling", "transit"]:
            raise ValueError("Invalid travel mode.")
        params["mode"] = mode

    if waypoints:
        waypoints = convert.location_list(waypoints)
        if optimize_waypoints:
            waypoints = "optimize:true|" + waypoints
        params["waypoints"] = waypoints

    if alternatives:
        params["alternatives"] = "true"

    if avoid:
        params["avoid"] = convert.join_list("|", avoid)

    if language:
        params["language"] = language

    if units:
        params["units"] = units

    if region:
        params["region"] = region

    if departure_time:
        params["departure_time"] = convert.time(departure_time)

    if arrival_time:
        params["arrival_time"] = convert.time(arrival_time)

    if departure_time and arrival_time:
        raise ValueError("Should not specify both departure_time and"
                         "arrival_time.")

    if transit_mode:
        params["transit_mode"] = convert.join_list("|", transit_mode)

    if transit_routing_preference:
        params["transit_routing_preference"] = transit_routing_preference

    if traffic_model:
        params["traffic_model"] = traffic_model

    return client._request("/maps/api/directions/json", params).get("routes", [])


#New class to calculat destination from A to B
from googlemaps import convert
from googlemaps.convert import as_list


def distance_matrix(client, origins, destinations,
                    mode=None, language=None, avoid=None, units=None,
                    departure_time=None, arrival_time=None, transit_mode=None,
                    transit_routing_preference=None, traffic_model=None, region=None):
    

    params = {
        "origins": convert.location_list(origins),
        "destinations": convert.location_list(destinations)
    }

    if mode:
        # NOTE(broady): the mode parameter is not validated by the Maps API
        # server. Check here to prevent silent failures.
        if mode not in ["driving", "walking", "bicycling", "transit"]:
            raise ValueError("Invalid travel mode.")
        params["mode"] = mode

    if language:
        params["language"] = language

    if avoid:
        if avoid not in ["tolls", "highways", "ferries"]:
            raise ValueError("Invalid route restriction.")
        params["avoid"] = avoid

    if units:
        params["units"] = units

    if departure_time:
        params["departure_time"] = convert.time(departure_time)

    if arrival_time:
        params["arrival_time"] = convert.time(arrival_time)

    if departure_time and arrival_time:
        raise ValueError("Should not specify both departure_time and"
                         "arrival_time.")

    if transit_mode:
        params["transit_mode"] = convert.join_list("|", transit_mode)

    if transit_routing_preference:
        params["transit_routing_preference"] = transit_routing_preference

    if traffic_model:
        params["traffic_model"] = traffic_model

    if region:
        params["region"] = region

    return client._request("/maps/api/distancematrix/json", params)
