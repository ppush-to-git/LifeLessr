var map = L.map('map').setView([28.613,77.209],13)
L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; OpenStreetMap &copy; CARTO',
    maxZoom:19
}).addTo(map);
var usericon=L.icon({
    iconUrl: '/static/markers/marker-icon-violet.png',
    shadowUrl: '/static/markers/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var ansicon=L.icon({
    iconUrl: '/static/markers/marker-icon-green.png',
    shadowUrl: '/static/markers/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
usercoor=[latuser,lnguser];
anscoor=[latans,lngans];
usermarker=L.marker(usercoor,{icon:usericon,riseOnHover:true}).addTo(map);
ansmarker=L.marker(anscoor,{icon:ansicon,riseOnHover:true}).addTo(map);
//normalising longitudes if it crosses International Date Line;eventually causing a bug that makes the polyline go all around the world even if the points are adjacent.
anslng=lngans;
userlng=lnguser;
if(Math.abs(userlng-anslng)>180){
    if(userlng<anslng)
        userlng+=360
    else
        anslng+=360
}
cooruser=[latuser,userlng];
coorans=[latans,anslng];
conLine=L.polyline([cooruser,coorans],{color:'#9709d3',dashArray:'10,10'}).addTo(map);
var bounds=conLine.getBounds();
map.fitBounds(bounds);
usermarker.bindPopup("Your Guess");
ansmarker.bindPopup("Correct Location");