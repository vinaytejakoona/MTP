
def LF_Desc_Regex_AirPollution(c):
    words = ["air","pollution","dust|smoke|burn"]
    pattern = 'air.*pollution|pollution|dust'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 1
    return 0

def LF_Desc_Regex_AutorickshawsandTaxis(c):
    words = ["autorickshaws","taxis","taxi","auto","autorickshaw"]
    pattern = 'autorickshaws|taxis|taxi|auto|autorickshaw'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 2
    return 0

def LF_Desc_Regex_BMTCDriverorConductor(c):
    words = ["bmtc","driver","conductor","rude","behaviour"]
    pattern = 'bmtc.*driver|bmtc.*conductor|bus.*driver|bus.*conductor'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 3
    return 0

def LF_Desc_Regex_BMTCNeednewBusRoute(c):
    words = ["bmtc","need","new","bus","route","frequency"]
    pattern = 'bus.*route'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 4
    return 0

def LF_Desc_Regex_BMTCOthers(c):
    words = ["bmtc"]
    pattern = 'bmtc'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 5
    return 0

def LF_Desc_Regex_BadRoads(c):
    words = ["bad","roads","road"]
    pattern = 'bad.*road|road.*bad'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 6
    return 0

def LF_Desc_Regex_BrokenStormWaterDrains(c):
    words = ["broken","storm","water","drains","overflow","drainage"]
    pattern = '(broken|damage).*(drain)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 7
    return 0

def LF_Desc_Regex_Cattle(c):
    words = ["cattle","cows","buffaloes","goats","cow"]
    pattern = '(cattle|cows|buffaloes|goats)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 8
    return 0

def LF_Desc_Regex_ClearingofBlockageofUnderGroundDrainagePipelinesandReplacementofDamagedorMissingManholeCover(c):
    words = ["clearing","blockage","under","ground","drainage","pipelines","replacement","damaged","missing","manhole","cover"]
    pattern = 'clearing|blockage|under|ground|drainage|pipelines|replacement|damaged|missing|manhole|cover'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 9
    return 0

def LF_Desc_Regex_DesiltingLakes(c):
    words = ["desilting","lakes","lake"]
    pattern = 'lake'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 10
    return 0

def LF_Desc_Regex_Diseases(c):
    words = ["diseases","malaria","dengue","cholera","fever","disease","hospital","epidemic"]
    pattern = 'diseases|malaria|dengue|cholera'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 11
    return 0

def LF_Desc_Regex_Electricity(c):
    words = ["electricity","power","current","power cut"]
    pattern = 'electricity|power|current|power.*cut'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 12
    return 0

def LF_Desc_Regex_FloodingofRoadsandFootpaths(c):
    words = ["flooding","roads","footpaths","water","flood","floods"]
    pattern = '((water|flood|flow).*(roads|footpaths))|((roads|footpaths).*(water|flood|flow))'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 13
    return 0

def LF_Desc_Regex_Footpaths(c):
    words = ["footpaths","footpath"]
    pattern = 'footpath'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 14
    return 0

def LF_Desc_Regex_Garbage(c):
    words = ["garbage","waste","plastic","dirt"]
    pattern = 'garbage|waste|plastic|dirt'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 15
    return 0

def LF_Desc_Regex_GovernmentLandEncroachment(c):
    words = ["government","land","encroachment","occupy","illegal"]
    pattern = '(government.*land).*(encroach|occupy|illegal)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 16
    return 0

def LF_Desc_Regex_HawkersandVendors(c):
    words = ["hawkers","vendors"]
    pattern = '(hawkers|vendors)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 17
    return 0

def LF_Desc_Regex_Hoardings(c):
    words = ["hoardings","advertise"]
    pattern = '(hoardings|advertisements)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 18
    return 0

def LF_Desc_Regex_IllegalpostersandHoardings(c):
    words = ["illegal","posters","hoardings","banner","ads ","advertise"]
    pattern = 'posters|hoardings|banner|ads|advertise'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 19
    return 0

def LF_Desc_Regex_LakesOthers(c):
    words = ["lakes","lake"]
    pattern = 'lake'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 20
    return 0

def LF_Desc_Regex_MaintenanceofRoadsandFootpathsOthers(c):
    words = ["maintenance","roads","footpaths"]
    pattern = '(maintenance).*(roads|footpaths)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 21
    return 0

def LF_Desc_Regex_Manholes(c):
    words = ["manholes","manhole","man hole"]
    pattern = '(manholes|manhole|man hole)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 22
    return 0

def LF_Desc_Regex_Mosquitos(c):
    words = ["mosquitos","mosquito","mosquitoe","mosquitoes","dengue","malaria"]
    pattern = 'mosquito|mosquitoe|mosquitoes|dengue|malaria'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 23
    return 0

def LF_Desc_Regex_NeedNewStreetlights(c):
    words = ["need","new","streetlights","streetlight","light","new streetlight"]
    pattern = '(need|no|new).*(streetlight|light)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 24
    return 0

def LF_Desc_Regex_NeedNewToilets(c):
    words = ["need","new","toilets","toilet","urinal","urinate"]
    pattern = 'toilets|toilet|urinal|urinate'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 25
    return 0

def LF_Desc_Regex_NewBusShelters(c):
    words = ["new","bus","shelters","shelter"]
    pattern = 'bus.*shelter|shelter.*bus'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 26
    return 0

def LF_Desc_Regex_NoSewageDrains(c):
    words = ["sewage","drains","drainage"]
    pattern = 'drain'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 27
    return 0

def LF_Desc_Regex_NoisePollution(c):
    words = ["noise","pollution","siren","speakers","speakers","loud"]
    pattern = 'noise|noise.*pollution|siren|speakers|speakers|loud'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 28
    return 0

def LF_Desc_Regex_Others(c):
    words = ["others"]
    pattern = 'others'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 29
    return 0

def LF_Desc_Regex_OverflowofStormWaterDrains(c):
    words = ["overflow","storm","water","drains","pipes"]
    pattern = 'overflow.*(drains|pipes)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 30
    return 0

def LF_Desc_Regex_ParkingViolations(c):
    words = ["parking","violations","parked","parker"]
    pattern = 'parking|parked|parker'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 31
    return 0

def LF_Desc_Regex_Parksandplaygrounds(c):
    words = ["parks","playgrounds","park","play","playground"]
    pattern = '(parks|playgrounds|park|play|playground)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 32
    return 0

def LF_Desc_Regex_Potholes(c):
    words = ["potholes","holes","pothole"]
    pattern = '(pot hole|holes|pothole)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 33
    return 0

def LF_Desc_Regex_PublicNuisance(c):
    words = ["public","nuisance"]
    pattern = '(public.*nuisance|nuisance)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 34
    return 0

def LF_Desc_Regex_Repairofstreetlights(c):
    words = ["repair","streetlights","streetlight","light","broken","damaged"]
    pattern = '((light).*(repair|broke|damage))|((repair|broke|damage).*(light))'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 35
    return 0

def LF_Desc_Regex_SewageandStormWaterDrainsOthers(c):
    words = ["sewage","storm","water","drains","drainage"]
    pattern = '(sewage|storm|water|drains|drainage)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 36
    return 0

def LF_Desc_Regex_StrayDogs(c):
    words = ["stray","dogs","dog"]
    pattern = '(stray|dogs|dog)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 37
    return 0

def LF_Desc_Regex_Traffic(c):
    words = ["traffic","vehicles"]
    pattern = '(traffic|vehicles)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 38
    return 0

def LF_Desc_Regex_TreesParksandPlaygroundsOthers(c):
    words = ["trees","parks","playgrounds","tree"]
    pattern = '(trees|parks|playgrounds|tree)'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 39
    return 0

def LF_Desc_Regex_UnauthorizedConstruction(c):
    words = ["unauthorized","construction","encroach","building","built"]
    pattern = 'encroachbuildingbuilt'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 40
    return 0

def LF_Desc_Regex_WaterLeakage(c):
    words = ["water","leakage"]
    pattern = 'water.*leak|leak.*water'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 41
    return 0

def LF_Desc_Regex_WaterSupply(c):
    words = ["water","supply"]
    pattern = 'water.*supply|supply.*water'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 42
    return 0
