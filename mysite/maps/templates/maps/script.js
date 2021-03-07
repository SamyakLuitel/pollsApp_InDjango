
  mapboxgl.accessToken = 'pk.eyJ1Ijoic2FteWFrbHVpdGVsIiwiYSI6ImNrbGk4ZW84djJmZ3gydXBjYnlhOG52NXcifQ.pgR5hS5suRaJNuDAjlp9Aw';
  navigator.geolocation.getCurrentPosition(successLocation, errorLocation,{enableHighAccuracy:true})
  
  function successLocation(position){
    console.log(position)
    setupMap([position.coords.longitude,position.coords.latitude])
  }
  
  function errorLocation(position){
      setupMap([85.2560925,27.7089427])
  }
  function setupMap(center){
    const map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v11',
      center : center,
      zoom : 15
  });
  
    const nav = new mapboxgl.NavigationControl();
    map.addControl(nav, 'top-right');
  


var directions = new MapboxDirections({
  accessToken: mapboxgl.accessToken//'YOUR-MAPBOX-ACCESS-TOKEN',
  //unit: 'metric',
  //profile: 'mapbox/cycling'
});


map.addControl(directions, 'top-left');
  
}

