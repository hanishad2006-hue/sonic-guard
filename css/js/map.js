function initMap() {

  // Center location
  const centerLocation = { lat: 13.0827, lng: 80.2707 };

  // Create map
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: centerLocation
  });

  // Noise data
  const noiseData = [
    { lat: 13.0827, lng: 80.2707, db: 85 },
    { lat: 13.0600, lng: 80.2500, db: 70 },
    { lat: 13.1000, lng: 80.2900, db: 50 }
  ];

  // Marker color logic
  function markerColor(db) {
    if (db > 80) return "http://maps.google.com/mapfiles/ms/icons/red-dot.png";
    if (db > 60) return "http://maps.google.com/mapfiles/ms/icons/orange-dot.png";
    return "http://maps.google.com/mapfiles/ms/icons/green-dot.png";
  }

  // Add markers
  noiseData.forEach(data => {
    new google.maps.Marker({
      position: { lat: data.lat, lng: data.lng },
      map: map,
      icon: markerColor(data.db),
      title: `Noise Level: ${data.db} dB`
    });
  });
}
