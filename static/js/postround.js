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
//normalization of longitudes in case the markers are across the International Date Line,
//which causes a bug that makes the polyline go around the whole map instead of taking the shorter path
userlng=lnguser;
anslng=lngans;
if(Math.abs(userlng-anslng)>180){
    if(anslng<userlng)
        anslng+=360;
    else
        userlng+=360;
}

usercoor=[latuser,userlng];
anscoor=[latans,anslng];
usermarker=L.marker(usercoor,{icon:usericon,riseOnHover:true}).addTo(map);
ansmarker=L.marker(anscoor,{icon:ansicon,riseOnHover:true}).addTo(map);
conLine=L.polyline([usercoor,anscoor],{color:'#9709d3',dashArray:'10,10'}).addTo(map);
var bounds=conLine.getBounds();
map.fitBounds(bounds);
usermarker.bindPopup("Your Guess");
ansmarker.bindPopup("Correct Location");
