import { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, LayersControl, LayerGroup, useMap } from 'react-leaflet';
import MarkerClusterGroup from "react-leaflet-cluster";
import "../components/MapComponentStyle.css";
import "leaflet/dist/leaflet.css";

const { BaseLayer, Overlay } = LayersControl;

const markers = [
  {
    geocode: [52.5200, 13.4050],
    popUp: "Power Consumption (GWh): 553.2"
  },
  {
    geocode: [48.8567, 2.3522],
    popUp: "Power Consumption (GWh): 450.8"
  },
  {
    geocode: [51.5074, -0.1278],
    popUp: "Power Consumption (GWh): 343.4"
  },
  {
    geocode: [41.8719, 12.4964],
    popUp: "Power Consumption (GWh): 320.5"
  },
  {
    geocode: [40.4168, -3.7038],
    popUp: "Power Consumption (GWh): 293.1"
  },
  {
    geocode: [52.2374, 21.0113],
    popUp: "Power Consumption (GWh): 242.9"
  },
  {
    geocode: [55.7558, 37.6173],
    popUp: "Power Consumption (GWh): 235.6"
  },
  {
    geocode: [41.0082, 28.9744],
    popUp: "Power Consumption (GWh): 224.1"
  },
  {
    geocode: [52.3702, 4.8952],
    popUp: "Power Consumption (GWh): 214.5"
  },
  {
    geocode: [50.8503, 4.3517],
    popUp: "Power Consumption (GWh): 204.2"
  },
  {
    geocode: [37.9833, 23.7333],
    popUp: "Power Consumption (GWh): 195.6"
  },
  {
    geocode: [48.2083, 16.3739],
    popUp: "Power Consumption (GWh): 184.5"
  },
  {
    geocode: [50.0757, 14.4375],
    popUp: "Power Consumption (GWh): 176.2"
  },
  {
    geocode: [47.4979, 19.0402],
    popUp: "Power Consumption (GWh): 168.1"
  },
  {
    geocode: [59.3297, 18.0681],
    popUp: "Power Consumption (GWh): 165.9"
  },
  {
    geocode: [55.6757, 12.5686],
    popUp: "Power Consumption (GWh): 159.5"
  },
  {
    geocode: [59.9139, 10.7514],
    popUp: "Power Consumption (GWh): 155.2"
  },
  {
    geocode: [47.3667,8.5333],
    popUp: "Power Consumption (GWh): 149.8"
  },
  {
    geocode: [38.7237,-9.1358],
    popUp: "Power Consumption (GWh): 144.9"
  },
  {
    geocode: [53.3498,-6.2603],
    popUp: "Power Consumption (GWh): 139.6"
  },
  {
    geocode: [42.6953,23.3225],
    popUp: "Power Consumption (GWh): 136"
  },
  {
    geocode: [48.1576,17],
    popUp: "Power Consumption (GWh): 133"
  },
  {
    geocode: [45.8067,16],
    popUp: "Power Consumption (GWh): 129"
  },
  {
    geocode: [46.1919,14.5576],
    popUp: "Power Consumption (GWh): 124"
  },
  {
    geocode: [59.4377,24.6975],
    popUp: "Power Consumption (GWh): 124"
  },
  {
    geocode: [46.1919,14.5576],
    popUp: "Power Consumption (GWh): 119"
  },
  {
    geocode: [54.6805,25.2804],
    popUp: "Power Consumption (GWh): 114"
  },
  {
    geocode: [56.9667,24.1065],
    popUp: "Power Consumption (GWh): 109"
  },
  {
    geocode: [49.6113,6],
    popUp: "Power Consumption (GWh): 103"
  },
  {
    geocode: [60.1697,24.9377],
    popUp: "Power Consumption (GWh): 99"
  },
  {
    geocode: [35.1667,33.3656],
    popUp: "Power Consumption (GWh): 96"
  },
  {
    geocode: [35.9067,14.5147],
    popUp: "Power Consumption (GWh): 93"
  },
  {
    geocode: [64.0818,21.9485],
    popUp: "Power Consumption (GWh): 88"
  },


];

function RecenterMap({ searchLocation }) {
  const map = useMap();

  useEffect(() => {
    if (searchLocation) {
      map.setView([searchLocation.lat, searchLocation.lon], 5);
    }
  }, [searchLocation, map]);

  return null;
}

function MapComponent({ searchLocation }) {
  return (
    <MapContainer center={[48.8566, 2.3522]} zoom={5} className="leaflet-container">
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
      </MarkerClusterGroup>
      {searchLocation && <RecenterMap searchLocation={searchLocation} />}
    </MapContainer>
  );
}

export default MapComponent;
