import { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, LayersControl, LayerGroup, useMap } from 'react-leaflet';
import MarkerClusterGroup from "react-leaflet-cluster";
import "../components/MapComponentStyle.css";
import "leaflet/dist/leaflet.css";

const { BaseLayer, Overlay } = LayersControl;

const markers = [
  {
    geocode: [48.86, 2.3522],
    popUp: "Hello, I am pop up 1"
  },
  {
    geocode: [48.85, 2.3522],
    popUp: "Hello, I am pop up 2"
  },
  {
    geocode: [48.855, 2.34],
    popUp: "Hello, I am pop up 3"
  },
  {
    geocode: [52.52, 13.40],
    popUp: "Hello, I am pop up 1"
  },
  {
    geocode: [48.85, 2.3522],
    popUp: "Hello, I am pop up 2"
  },
  {
    geocode: [51.5074, -0.12],
    popUp: "Hello, I am pop up 3"
  },
  {
    geocode: [41.8719, 12.49],
    popUp: "Hello, I am pop up 1"
  },
  {
    geocode: [40.4168, -3.70],
    popUp: "Hello, I am pop up 2"
  },
  {
    geocode: [52.2374, 21.01],
    popUp: "Hello, I am pop up 3"
  },
  {
    geocode: [55.7558, 37.61],
    popUp: "Hello, I am pop up 1"
  },
  {
    geocode: [41.0082, 28.97],
    popUp: "Hello, I am pop up 2"
  },
  {
    geocode: [52.3702, 4.895],
    popUp: "Hello, I am pop up 3"
  }
];

function RecenterMap({ searchLocation }) {
  const map = useMap();

  useEffect(() => {
    if (searchLocation) {
      map.setView([searchLocation.lat, searchLocation.lon], 13);
    }
  }, [searchLocation, map]);

  return null;
}

function MapComponent({ searchLocation }) {
  return (
    <MapContainer center={[48.8566, 2.3522]} zoom={13} className="leaflet-container">
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <MarkerClusterGroup>
        {markers.map((marker, index) => (
          <Marker key={index} position={marker.geocode}>
            <Popup>{marker.popUp}</Popup>
          </Marker>
        ))}
        <Overlay checked name="Parks">
          <LayerGroup>
            <Marker position={[39.75, -105.09]}>
              <Popup>This is Crown Hill Park.</Popup>
            </Marker>
            <Marker position={[39.68, -105.00]}>
              <Popup>This is Ruby Hill Park.</Popup>
            </Marker>
          </LayerGroup>
        </Overlay>
      </MarkerClusterGroup>
      {searchLocation && <RecenterMap searchLocation={searchLocation} />}
    </MapContainer>
  );
}

export default MapComponent;
