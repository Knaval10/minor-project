let s_lat = 26.812152279090817;
let s_lng = 87.2850183216681;
let d_lat;
let d_lng;
let global_data;
let myModal;
let routingControl;
let map=null;

let timeInterval;

function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(setLocation);
    }

  }


const waiting_time = ()=>{
    let time=100;
    timeInterval=setTimeout(()=>{
                console.log("time out");
                change_last_mechanic_status(false);
                send_again_help_request();
            },time*1000);
}

const show_btn = document.getElementById("show_btn");
show_btn.addEventListener("click",e=>{
    showModel();
})

const setLocation = (position)=>{
    s_lat = position.coords.latitude;
    s_lng = position.coords.longitude;
    console.log(s_lat,s_lng);
}

const showModel = ()=>{
	myModal =  new bootstrap.Modal(document.getElementById('myModal'), {
				  keyboard: false
					});
 
    
    myModal.show();
    
	
}
const helpForm = document.getElementById('helpForm');

helpForm.addEventListener('submit',e=>{
    
    e.preventDefault();
    const modal_footer = document.getElementById('modal_footer');
    modal_footer.innerHTML = `<span class="text-info">sending....</span><div class="spinner-border text-primary" role="status">
  </div>`;
    let problem_desc = e.target.problem_desc.value;
    let service_id = e.target.service.value;
    let data = new FormData();
    
    var input = document.querySelector('input[type="file"]')
    data.append('vehicle_image',input.files[0]);
    data.append('problem_desc',problem_desc);
    data.append('service_id',service_id);
  
    data.append('lat',s_lat);
    data.append('lon',s_lng);
    global_data = data;
    
    const params = {
        'method':'POST',
       
        body:data
    }
    const url = `http://${window.location.host}/tracker/driver/send_help/`;
    fetch(url,params).then(resp=>resp.json()).then(json_data=>{
        if(json_data.status){
            
            waiting_time();
            
            e.target.service.value = "";
            e.target.problem_desc.value = "";
            e.target.vehicle_image.value = "";
            myModal.hide();
            show_mechanics(json_data.data)


        }
        modal_footer.innerHTML = `<button type="submit" class="btn btn-primary">Send</button>`;
   
    })

});

const show_mechanics = (data)=>{
    const mechanic_table = document.getElementById('mechanic_table');
    const sno = mechanic_table.rows.length;
    const tr = `<tr>
                    <th scope="row">${sno}</th>
                    <td>${data.name}</td>
                    <td>${data.distance.toFixed(2)}</td>
                    <td>
                        <span class="badge bg-info">sending ...</span>
                    </td>
                </tr>`;
    mechanic_table.innerHTML +=tr;


}


const change_last_mechanic_status = (accept_status)=>{
    const mechanic_table = document.getElementById('mechanic_table');
    // console.log(mechanic_table.rows)
    const tr = mechanic_table.rows[mechanic_table.rows.length-1];
    if(accept_status){
        tr.cells[tr.cells.length - 1].innerHTML = `<span class="badge bg-success">accept</span>`;
    }
    else{
        tr.cells[tr.cells.length - 1].innerHTML = `<span class="badge bg-warning">cancel</span>`;
    }
    

}


const url = `ws://${window.location.host}/ws/driver/notifications/`;
const ws = new WebSocket(url);
ws.onopen = event=>{
    console.log("connecting .......");
}
ws.onmessage = event=>{
    console.log("receiving .......");

    const data = JSON.parse(event.data);
    change_last_mechanic_status(data.accept);
    console.log(data);
    if(data.accept === false){
        send_again_help_request();
        clearTimeout(timeInterval);
       }
    else{
        d_lat = data.m_lat;
        d_lng = data.m_lng;
        document.getElementById("map_container").innerHTML = `<button type="button" onClick="enlarge()" id="map_ctrl_btn">view</button>`;
        document.getElementById("map_container").innerHTML += `<div id="map" style="height:650px;">`;
        setTimeout(()=>{
            show_map();
        showRouting();
    },2000);
        clearTimeout(timeInterval);
        
    }
}
ws.onerror = event=>{
    console.log("error ...");
}
ws.onclose = event=>{
    console.log("closing");
}

const send_again_help_request = ()=>{
    // console.log("again send");
    const params = {
        'method':'POST',
        
        body:global_data
    }
    const url = `http://${window.location.host}/tracker/driver/send_help_again/`;
    fetch(url,params).then(resp=>resp.json()).then(json_data=>{
        if(json_data.status){
            show_mechanics(json_data.data);
            waiting_time();

        }
    })
}

const show_map = ()=>{
    console.log(map);
    if(map){
        map == null;
    }
    map = L.map('map').setView([s_lat, s_lng],13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);

}

const showRouting = ()=>{
    if (routingControl != null) {
            map.removeControl(routingControl);
            routingControl = null;
        }
          routingControl = L.Routing.control({
          waypoints: [
              L.latLng(s_lat,s_lng),
              L.latLng(d_lat,d_lng),
             
            
            
          ],
          routeWhileDragging: false,
          urlParameters: {
        vehicle: 'car'
    }

        }).addTo(map);
   showMarkerAddress();
        
   // routingControl.getRouter().options.urlParameters.vehicle = 'foot';
   // routingControl.route();
      }
    const showMarkerAddress = ()=>{
      const dest_marker = L.marker([d_lat,d_lng]).addTo(map);
      const source_marker = L.marker([s_lat,s_lng]).addTo(map);
      setAddress('Source',source_marker,s_lat,s_lng);
      setAddress('Destination',dest_marker,d_lat,d_lng);
      
      

    }
    const setAddress = (source_or_dest,marker,lat,lng)=>{
        console.log(source_or_dest)
      const url = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}`;
      fetch(url).then(resp=>resp.json()).then(json_resp=>{
  
        let full_address = '';
        // console.log(json)
        if(json_resp.address.amenity){
          full_address += json_resp.address.amenity+' ';
        }
        if(json_resp.address.road){
          full_address +=json_resp.address.road;
        }
        full_address +=json_resp.address.city;
        marker.bindPopup(`<span>${source_or_dest}</span><br><span>${full_address}</span>`,{closeOnClick: false, autoClose: false}).openPopup();

        
      })

    }

    const resize_map = ()=>{
        let map_div = document.getElementById('map_container');
        map_div.style.transform = "scale(1)";
        map_div.style.transition = "transform 0.25s ease";
        let map_ctrl_btn = document.getElementById("map_ctrl_btn");
        map_div.style.width ="";
        map_div.style['translate'] = "0 0";

        map_ctrl_btn.setAttribute("onClick","enlarge()");
        map_ctrl_btn.innerHTML = "view full";
    }

    const enlarge = ()=>{
        console.log("hello world");
        // Set image size to 1.5 times original
        let map_div = document.getElementById('map_container');
       
        map_div.style.height = "650px";
        map_div.style.width = "1000px";
        // map_div.innerHTML = `<button type="button">Resize</button>`
        let map_ctrl_btn = document.getElementById("map_ctrl_btn");
        map_ctrl_btn.innerHTML ="resize";
        map_ctrl_btn.setAttribute("onClick","resize_map()");
        map_div.style['translate'] = "-400px 0";
        map_div.style.transform = "scale(1.5)";

        // Animation effect 
        map_div.style.transition = "transform 0.25s ease";

    }