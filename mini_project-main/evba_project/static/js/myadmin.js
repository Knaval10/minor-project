
let unseen;
let notifications;

function set_hover(){
    let url = `http://${window.location.host}${window.location.pathname}`;
    const links = document.querySelectorAll('.link');

    url = url.split('/');
    if(url.length>5){
        url = `${url[0]}//${url[2]}/${url[3]}/${url[4]}/`;
    }
    else{
        url = `${url[0]}//${url[2]}/${url[3]}/`;
    }
    
    // console.log(links);
    for(let link of links){
        // console.log(url,link.href)
        if(link.href === url){
            
            link.style['background-color'] = "#b6adaddc";
            link.style['color'] = "rgb(249, 253, 253)";
        }
        
        
        
    }

}
window.onload = set_hover();

const url = `ws://${window.location.host}/ws/staff/notifications/`;

const ws = new WebSocket(url);

ws.onopen = event=>{
    console.log("connecting .......");
}
ws.onmessage = event=>{
    console.log("receiving .......");
    const data = JSON.parse(event.data);
    console.log(data);
    unseen +=1
    notifications = [data,...notifications];
  
    set_notifications();
    
}
ws.onerror = event=>{
    console.log("error ...");
}
ws.onclose = event=>{
    console.log("closing");
}


const notification_btn = document.getElementById('notification_btn');
notification_btn.addEventListener('click',e=>{
    const url = `http://${window.location.host}/myadmin/watch_notifications/`;
    fetch(url).then(resp=>resp.json()).then(json_data=>{
       
        if (json_data.status){
            document.getElementById('unseen').innerText = '';
            unseen = 0;

        }
    })
})


const set_notifications = ()=>{
    let notification_div = document.getElementById('notification_content');
    notification_div.innerText = '';

    const not_seen = document.getElementById('unseen');
    if(unseen){
        not_seen.innerText = unseen;
    }
    
    let url;
    for(let notification of notifications){
    
        if(notification.notification.driver_id){
            url = `http://${window.location.host}/myadmin/driver_mngt/update/${notification.notification.driver_id}/`;
        }
        else{
            url = `http://${window.location.host}/myadmin/mechanic_mngt/update/${notification.notification.mechanic_id}/`;
        }    
        const a = `<a href="${url}" class="list-group-item list-group-item-action p-1"><small>${notification.notification.message}</small></a>
                    `;
        notification_div.innerHTML +=a;
    }
  
}

function load_notifications(){
    const url = `http://${window.location.host}/myadmin/fetch_notifications/`;
    // console.log(notification)
    fetch(url).then(resp=>resp.json()).then(json_data=>{
        // console.log(json_data);
        notifications = json_data.data;
        unseen = json_data.not_seen;
      
        set_notifications();
    })
}

window.onload = load_notifications()