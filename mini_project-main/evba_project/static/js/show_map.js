let lat = 26.820629631172608;
let lon = 87.2906443710893;
var map = L.map('map').setView([lat,lon], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);




let address = document.getElementById("id_address");
let lat_input = document.getElementById("id_latitude");
let lon_input = document.getElementById("id_longitude");
const search = document.getElementById("id_search");
var marker = L.marker([lat, lon]).addTo(map);
if(lat_input.value && lon_input.value){

    const i_lat = parseFloat(lat_input.value);
    const i_lng = parseFloat(lon_input.value);
    map.flyTo([i_lat,i_lng],15);
    const latlng = {'lat':i_lat,'lng':i_lng}
    marker.setLatLng(latlng);
    setTimeout(()=>{
        getAddress(i_lat,i_lng);
    },1000);
}
marker.bindPopup("Dharan Clock Tower").openPopup();

search.addEventListener('change',e=>{

    if(e.target.value){
        const url = `https://nominatim.openstreetmap.org/?addressdetails=1&q=${e.target.value}&format=json&limit=1`;
        fetch(url).then(resp=>resp.json()).then(json_resp=>{
            console.log(json_resp);
            if(json_resp){
                // console.log(json_resp[0])
                const data = json_resp[0];
                map.flyTo([data.lat, data.lon],15);
                const latlng = {'lat':data.lat,'lng':data.lon}
                marker.bindPopup(data.display_name).openPopup();
          
                marker.setLatLng(latlng);
            }
        })
    }
})

map.on('click',e=>{
    marker.setLatLng(e.latlng)
    lat_input.value = e.latlng.lat;
    lon_input.value = e.latlng.lng;
    const url = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${e.latlng.lat}&lon=${e.latlng.lng}`;

    fetch(url).then(resp=>resp.json()).then(json_data=>{
        const addr_obj = json_data.address;
        
        let full_address ='';
        if(addr_obj.amenity !==undefined){
      
            full_address+=addr_obj.amenity+' ';
        }
        if(addr_obj.road !==undefined){

            full_address +=addr_obj.road+' ';
        }
        // const full_address = `${amenity} ${road} ${addr_obj.city}`;
        full_address +=addr_obj.city;
        address.value = full_address;
        marker.bindPopup(full_address).openPopup();
        search.value = full_address;



    })

})

const getAddress = (lat,lng)=>{
    const url = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}`;

    fetch(url).then(resp=>resp.json()).then(json_data=>{
        const addr_obj = json_data.address;
        
        let full_address ='';
        if(addr_obj.amenity !==undefined){
      
            full_address+=addr_obj.amenity+' ';
        }
        if(addr_obj.road !==undefined){

            full_address +=addr_obj.road+' ';
        }
        // const full_address = `${amenity} ${road} ${addr_obj.city}`;
        full_address +=addr_obj.city;
        address.value = full_address;
        marker.bindPopup(full_address).openPopup();
        search.value = full_address;



    })
}