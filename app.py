import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Sonic Guard",
    layout="wide"
)

# Title section
st.markdown(
    """
    <h1 style='text-align:center;'>Sonic Guard</h1>
    <p style='text-align:center; color:gray;'>
    Noise Monitoring & Prediction System
    </p>
    """,
    unsafe_allow_html=True
)

# Card-style container using Streamlit
with st.container():
    st.subheader("Noise Monitoring Map")

    # Google Maps HTML embedded
    map_html = """
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          #map {
            height: 400px;
            width: 100%;
            border-radius: 10px;
          }
        </style>
      </head>

      <body>
        <div id="map"></div>

        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDxxxxxxxxxxxxxxxxxxx&callback=initMap" async defer></script>

        <script>
          function initMap() {
            var center = {lat: 13.0827, lng: 80.2707};

            var map = new google.maps.Map(document.getElementById('map'), {
              zoom: 13,
              center: center
            });

            var noiseData = [
              {lat: 13.0827, lng: 80.2707, db: 85},
              {lat: 13.0600, lng: 80.2500, db: 65},
              {lat: 13.1000, lng: 80.2900, db: 45}
            ];

            function getIcon(db) {
              if (db > 80)
                return "http://maps.google.com/mapfiles/ms/icons/red-dot.png";
              if (db > 60)
                return "http://maps.google.com/mapfiles/ms/icons/orange-dot.png";
              return "http://maps.google.com/mapfiles/ms/icons/green-dot.png";
            }

            noiseData.forEach(function(data) {
              new google.maps.Marker({
                position: {lat: data.lat, lng: data.lng},
                map: map,
                icon: getIcon(data.db),
                title: "Noise Level: " + data.db + " dB"
              });
            });
          }
        </script>
      </body>
    </html>
    """

    components.html(map_html, height=450)
