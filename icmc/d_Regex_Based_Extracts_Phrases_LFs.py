
def LF_Extract_Phrase_Regex_AirPollution(c):
   
    pattern = 'wood or garbage burnt|lot of dust due to speeding buses'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 1
    return 0

def LF_Extract_Phrase_Regex_BMTCDriverorConductor(c):
   
    pattern = 'rude behavious'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 3
    return 0

def LF_Extract_Phrase_Regex_BMTCNeednewBusRoute(c):
   
    pattern = 'increase frequency of buses'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 4
    return 0

def LF_Extract_Phrase_Regex_BMTCOthers(c):
   
    pattern = 'need more bmtc buses|buses at regular intervals|traffic jams|buses speeding lot|no buses|extra buses,no proper timing,|increase in bus service|need more buses'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 5
    return 0

def LF_Extract_Phrase_Regex_BadRoads(c):
   
    pattern = 'worst road|ups and downs on roads|mud road,cant walk,bike stuck|no asphalted road|holes in road|road damaged|build new lane|road broken,road repair|sewage cleaning|dangerous road due to potholes and unscientific humps|construct road|road destroyed|road in bad state|no road|road repair|widening footpaths|slip over the road|road bad|road dug|road condition poor|road bad to commute|very bad roads|made tar road|need good roads|road not asphalted|pot holes|roads worse|road going down|road has been dug|deep potholes|misusing permits|roads not proper|no tar road|road in bad shape|roads are not asphalted|road never repaired|deep craters,humps,potholes|road not usable|potholes|unscientific road humps|bad road|unpainted speed bumps (effectively invisible)|road digged|widen the road|no tarred roads|road bumpy and muddy|bad road service conditions,full of potholes,repair these roads|mud road|road in bad condition|road not good|troad bot tareed or asphalted|road in pathetic state|multiple potholes and uneven small bumps.'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 6
    return 0

def LF_Extract_Phrase_Regex_BrokenStormWaterDrains(c):
   
    pattern = 'no drainage lane|no proper drainage system|drainage left open|storm water drain filled with garbage'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 7
    return 0

def LF_Extract_Phrase_Regex_ClearingofBlockageofUnderGroundDrainagePipelinesandReplacementofDamagedorMissingManholeCover(c):
   
    pattern = 'connect tank to drainage line|sewage pipies narrow|sewage drain blocked'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 9
    return 0

def LF_Extract_Phrase_Regex_DesiltingLakes(c):
   
    pattern = 'clean lajke'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 10
    return 0

def LF_Extract_Phrase_Regex_Diseases(c):
   
    pattern = 'waste dumped|garbage dumped|garbage|garbage dump|dead cat at residential place'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 11
    return 0

def LF_Extract_Phrase_Regex_Electricity(c):
   
    pattern = 'frequent power cut|electric fixture protuding on road|power cut|transformer bursts|streetlight not working|street  light not working|complete power cut|street light is not there|powert outages|power supply'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 12
    return 0

def LF_Extract_Phrase_Regex_FloodingofRoadsandFootpaths(c):
   
    pattern = 'not aintained road|sanitary water from manhole|many potholes|footpath|roads badly designed|no road maintainance|no proper roads and footpath ,not able to walk on street'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 13
    return 0

def LF_Extract_Phrase_Regex_Footpaths(c):
   
    pattern = 'overflowing drains|footpath bad|provide footover bridge|footpath enroached|driving on footpath|footpath unusable|plight to see footpath|footpath|garbage|drainage open|footpath driving|no footpath'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 14
    return 0

def LF_Extract_Phrase_Regex_Garbage(c):
   
    pattern = 'no garbage collection|lot of garbage on road|pipe line has become garbage house|garbage segregation|garbage being dumped|garbage|throw garabge,not use van facility|garbage dump|garbage point|garbage piled|dump yard|garbage cleaning|garbage piled,clear garbage|garabge dumped|garbage ,dumpyard|garbage dumped|no proper way to dispose garbage|garbage pick upon payment|home for bad smell|garbage not colelcted|garbage collection is not good|buring of garbage|garbage mini truck once in week|liier in parking side|garbage dumping|drainage waste not cleared|uncleared garbages|garbage auto irregular|dumping,garbage collecting vechicles not coming,bad smell|dustbin|no garbage collection,garbage segregation|garbage autorikshaw not for week|garabage|no garbage bin|permanent garbage pile which stinks nonstop|place clan|garbage burning|no place to throw garbage|dumping garbage|garbage dumping|potholes|garbage dump|dump of garbage|dumped garbage|no garbage collection|lot of garbage|dumping zone|regular burning of garbage|garbage pilling|need dustbin|garbage collector  is not coming,people are dumping garbage|garabager dumping|garabge collection|no garbage vehicle|no dustbin|irregular garbage collection|garbage set obn fire'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 15
    return 0

def LF_Extract_Phrase_Regex_HawkersandVendors(c):
   
    pattern = 'footpath enroached|stores on footpath'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 17
    return 0

def LF_Extract_Phrase_Regex_IllegalpostersandHoardings(c):
   
    pattern = 'posters on trees|unauthorized no parking board'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 19
    return 0

def LF_Extract_Phrase_Regex_LakesOthers(c):
   
    pattern = 'lake in bad state|lake polluted|lake in bad condition'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 20
    return 0

def LF_Extract_Phrase_Regex_MaintenanceofRoadsandFootpathsOthers(c):
   
    pattern = 'install a road divider'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 21
    return 0

def LF_Extract_Phrase_Regex_Manholes(c):
   
    pattern = 'road full of manholes|open manhole'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 22
    return 0

def LF_Extract_Phrase_Regex_Mosquitos(c):
   
    pattern = 'mosquitoes'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 23
    return 0

def LF_Extract_Phrase_Regex_NeedNewStreetlights(c):
   
    pattern = 'lights gone off|install new streelight|streetlight went off|no proper streetlight|damaged street light not fixed'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 24
    return 0

def LF_Extract_Phrase_Regex_NewBusShelters(c):
   
    pattern = 'private bus operators are creating havoc near bus shelters|no enough buses|no bus shelter|create new bus stop|more number of buses|provide bus shelters'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 26
    return 0

def LF_Extract_Phrase_Regex_NoSewageDrains(c):
   
    pattern = 'no sewage lines|sewage problem|sewage water causing smell|sewage water block|sopen drain clogged with garbage|blockage in street,low levelling of pipe|cleaning sewage waste|drainage overflow|flooded road|damaging the roads'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 27
    return 0

def LF_Extract_Phrase_Regex_NoisePollution(c):
   
    pattern = 'dog barks'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 28
    return 0

def LF_Extract_Phrase_Regex_Others(c):
   
    pattern = 'bribery|no utlity center|enroachment of ffotpath|drainage problems|footpath unusable|grant a new bus route|no sign board'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 29
    return 0

def LF_Extract_Phrase_Regex_OverflowofStormWaterDrains(c):
   
    pattern = 'poor drainage system|sewage/storm water drain overflow'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 30
    return 0

def LF_Extract_Phrase_Regex_ParkingViolations(c):
   
    pattern = 'commuting nightmare|no parking zone|car parked on footpath'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 31
    return 0

def LF_Extract_Phrase_Regex_Parksandplaygrounds(c):
   
    pattern = 'plan a park|tree collapse'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 32
    return 0

def LF_Extract_Phrase_Regex_Potholes(c):
   
    pattern = 'road is bad|huge and deep potholes|road worse|roads worst|filled with potholes|water logging|full of dust and patholes|strecth in bad condition|terrible condition of road|potholes|ridden with potholes|road repair|new tar road|road bad|full of potholes|tar road|unwalkable|potholes,road uneven|potholes in road,roads slanted|deep path hole|rioad to be repaired|whole road is there to break our back,potholes|lot many potholes|road potholes|dangeropus pothole|potholes|bad road,potholes|drain water overflowing|potholes filled with water and mud|land become dumpyard|bad road|dangerous potholes|big crater|road full ogf potholes|pathetic conditon|full of pot hole|bad road conditions|dangerous pothole|unusable road|roads to be tarred|asphalting road'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 33
    return 0

def LF_Extract_Phrase_Regex_PublicNuisance(c):
   
    pattern = 'public yelling on terrace|bar in residential area|nuisance by house construction'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 34
    return 0

def LF_Extract_Phrase_Regex_Repairofstreetlights(c):
   
    pattern = 'streetlight fuse|not working strelights|no streetlight|the streetlight has not installed|non functional|repair existing street lights|street light not working|street light not working,area dark|streelights not working|street lights not working|street light is not working|street lights are always on..|strretlight not working|not functioning,install more street light|no proper streetlight|not working'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 35
    return 0

def LF_Extract_Phrase_Regex_SewageandStormWaterDrainsOthers(c):
   
    pattern = 'manhole overflowing'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 36
    return 0

def LF_Extract_Phrase_Regex_StrayDogs(c):
   
    pattern = 'dogs bark|strret dogs|aggressive dogs|diseased dogs|dogs|stray dogs|sterlize stray dogs|dogs menance|dogs in night|dog menance|dogs are scaring publics|street dog bites|straydogs|issue with street dogs and street lights|dogs running on vehicles|illegal hoarding|dogs murmering|stary dogs|dog injured|stray dogs|stray dog attack|stray dog|street dogs|steralization program for stray  dogs|get rid of stary dogs'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 37
    return 0

def LF_Extract_Phrase_Regex_Traffic(c):
   
    pattern = 'no sign board,no police to stop traffic|obstructing traffic|traffic jam is increasing|road blocked|no helmet|one way regulation traffic|the bus will either breakdown or their will be no ac,|lack of road infrastructure|loud vehicles|garbage piled|traffic is too high need|huge traffic|install height barrier|traffic rules|one way road|traffic|parked on footpath|road bad|more taffic & lack of bus facility|stop line,pedestrain crossing|no traffic controller|more traffic|severe traffic|congestion at junction blocked by vechicles|road not tarred|road side selling|install road humps /speed breakers|heavy traffic|underground pass subway|driving rashly|onw way rule violated|riding on footpath|heavy raffic|road repair and footpath widening|helmetless|road not wide enough|lake polluted|footpath driving|sky walk required|police violating traffic rules|traffic|no helemt|parking on footpath|traffic jams|defective number plate|signal timings|no traffic police|wrong parking|parking on road causing traffic jams|traffic signals,zebra crossings at junctions|one way board|road widening,reach on time'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 38
    return 0

def LF_Extract_Phrase_Regex_TreesParksandPlaygroundsOthers(c):
   
    pattern = 'no public park and plackground'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 39
    return 0

def LF_Extract_Phrase_Regex_WaterLeakage(c):
   
    pattern = 'water leakage|water provided in nights'
    if(re.search(pattern,c['complaint_description'],flags=re.I)):
            return 41
    return 0
