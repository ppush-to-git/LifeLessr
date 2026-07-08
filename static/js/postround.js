var map = L.map('map').setView([28.613,77.209],13)
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
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
conLine=L.polyline([usercoor,anscoor],{color:'#9709d3',dashArray:'10,10'}).addTo(map);
var bounds=conLine.getBounds();
map.fitBounds(bounds);
usermarker.bindPopup("Your Guess");
ansmarker.bindPopup("Correct Location");