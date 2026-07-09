var map = L.map("map").setView([20, 0], 1)
var userMarker=L.icon({
    iconUrl: '/static/markers/marker-icon-violet.png',
    shadowUrl: '/static/markers/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; OpenStreetMap &copy; CARTO',
    maxZoom: 19
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
