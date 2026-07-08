var map = L.map('map').setView([28.613,77.209],13)
var userMarker=L.icon({
    iconUrl: '/static/markers/marker-icon-violet.png',
    shadowUrl: '/static/markers/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
let marker=null;
function onMapClick(e){
    if (marker===null){
        marker=L.marker(e.latlng,{icon:userMarker,riseOnHover:true}).addTo(map);
    }
    else{
        marker.setLatLng(e.latlng)
    }
    document.getElementById('lat').value=e.latlng.lat;
    document.getElementById('lng').value=e.latlng.lng;
}
map.on("click",onMapClick)
