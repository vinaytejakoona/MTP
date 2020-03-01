
def LF_KeyWord_AirPollution(c):
    words = ["air","pollution","dust|smoke|burn"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 1
    return 0

def LF_KeyWord_AutorickshawsandTaxis(c):
    words = ["autorickshaws","taxis","taxi","auto","autorickshaw"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 2
    return 0

def LF_KeyWord_BMTCDriverorConductor(c):
    words = ["bmtc","driver","conductor","rude","behaviour"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 3
    return 0

def LF_KeyWord_BMTCNeednewBusRoute(c):
    words = ["bmtc","need","new","bus","route","frequency"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 4
    return 0

def LF_KeyWord_BMTCOthers(c):
    words = ["bmtc"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 5
    return 0

def LF_KeyWord_BadRoads(c):
    words = ["bad","roads","road"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 6
    return 0

def LF_KeyWord_BrokenStormWaterDrains(c):
    words = ["broken","storm","water","drains","overflow","drainage"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 7
    return 0

def LF_KeyWord_Cattle(c):
    words = ["cattle","cows","buffaloes","goats","cow"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 8
    return 0

def LF_KeyWord_ClearingofBlockageofUnderGroundDrainagePipelinesandReplacementofDamagedorMissingManholeCover(c):
    words = ["clearing","blockage","under","ground","drainage","pipelines","replacement","damaged","missing","manhole","cover"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 9
    return 0

def LF_KeyWord_DesiltingLakes(c):
    words = ["desilting","lakes","lake"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 10
    return 0

def LF_KeyWord_Diseases(c):
    words = ["diseases","malaria","dengue","cholera","fever","disease","hospital","epidemic"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 11
    return 0

def LF_KeyWord_Electricity(c):
    words = ["electricity","power","current","power cut"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 12
    return 0

def LF_KeyWord_FloodingofRoadsandFootpaths(c):
    words = ["flooding","roads","footpaths","water","flood","floods"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 13
    return 0

def LF_KeyWord_Footpaths(c):
    words = ["footpaths","footpath"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 14
    return 0

def LF_KeyWord_Garbage(c):
    words = ["garbage","waste","plastic","dirt"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 15
    return 0

def LF_KeyWord_GovernmentLandEncroachment(c):
    words = ["government","land","encroachment","occupy","illegal"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 16
    return 0

def LF_KeyWord_HawkersandVendors(c):
    words = ["hawkers","vendors"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 17
    return 0

def LF_KeyWord_Hoardings(c):
    words = ["hoardings","advertise"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 18
    return 0

def LF_KeyWord_IllegalpostersandHoardings(c):
    words = ["illegal","posters","hoardings","banner","ads ","advertise"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 19
    return 0

def LF_KeyWord_LakesOthers(c):
    words = ["lakes","lake"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 20
    return 0

def LF_KeyWord_MaintenanceofRoadsandFootpathsOthers(c):
    words = ["maintenance","roads","footpaths"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 21
    return 0

def LF_KeyWord_Manholes(c):
    words = ["manholes","manhole","man hole"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 22
    return 0

def LF_KeyWord_Mosquitos(c):
    words = ["mosquitos","mosquito","mosquitoe","mosquitoes","dengue","malaria"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 23
    return 0

def LF_KeyWord_NeedNewStreetlights(c):
    words = ["need","new","streetlights","streetlight","light","new streetlight"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 24
    return 0

def LF_KeyWord_NeedNewToilets(c):
    words = ["need","new","toilets","toilet","urinal","urinate"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 25
    return 0

def LF_KeyWord_NewBusShelters(c):
    words = ["new","bus","shelters","shelter"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 26
    return 0

def LF_KeyWord_NoSewageDrains(c):
    words = ["sewage","drains","drainage"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 27
    return 0

def LF_KeyWord_NoisePollution(c):
    words = ["noise","pollution","siren","speakers","speakers","loud"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 28
    return 0

def LF_KeyWord_Others(c):
    words = ["others"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 29
    return 0

def LF_KeyWord_OverflowofStormWaterDrains(c):
    words = ["overflow","storm","water","drains","pipes"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 30
    return 0

def LF_KeyWord_ParkingViolations(c):
    words = ["parking","violations","parked","parker"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 31
    return 0

def LF_KeyWord_Parksandplaygrounds(c):
    words = ["parks","playgrounds","park","play","playground"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 32
    return 0

def LF_KeyWord_Potholes(c):
    words = ["potholes","holes","pothole"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 33
    return 0

def LF_KeyWord_PublicNuisance(c):
    words = ["public","nuisance"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 34
    return 0

def LF_KeyWord_Repairofstreetlights(c):
    words = ["repair","streetlights","streetlight","light","broken","damaged"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 35
    return 0

def LF_KeyWord_SewageandStormWaterDrainsOthers(c):
    words = ["sewage","storm","water","drains","drainage"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 36
    return 0

def LF_KeyWord_StrayDogs(c):
    words = ["stray","dogs","dog"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 37
    return 0

def LF_KeyWord_Traffic(c):
    words = ["traffic","vehicles"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 38
    return 0

def LF_KeyWord_TreesParksandPlaygroundsOthers(c):
    words = ["trees","parks","playgrounds","tree"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 39
    return 0

def LF_KeyWord_UnauthorizedConstruction(c):
    words = ["unauthorized","construction","encroach","building","built"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 40
    return 0

def LF_KeyWord_WaterLeakage(c):
    words = ["water","leakage"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 41
    return 0

def LF_KeyWord_WaterSupply(c):
    words = ["water","supply"]
    if(len(set(c['complaint_text']).intersection(words))>0):
            return 42
    return 0
