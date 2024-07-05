import { useState } from 'react';
import Footer from '../components/Footer';
import MapComponent from '../components/MapComponent';
import { Link, useNavigate } from "react-router-dom";
import { IoIosArrowBack } from "react-icons/io";


function MainPage() {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchLocation, setSearchLocation] = useState(null);

  const handleSearch = (e) => {
    e.preventDefault();
    const [lat, lon] = searchQuery.split(',').map(Number);
    if (!isNaN(lat) && !isNaN(lon)) {
      setSearchLocation({ lat, lon });
    }
  };

  const containerStyle = {
    textAlign: 'center',
    fontFamily: 'Arial, sans-serif',
  };

  return (
    <div style={containerStyle}>
    <Link to="/"><IoIosArrowBack className ='arrow' size={100}/></Link>

      <div className='main-page'>

        <div className='side-menu'>
          <form onSubmit={handleSearch}>
          <h2>Search By Coordinates</h2>
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Enter coordinates (lat, lon)"
              />
              <br/>
            <button type="submit">Search</button>
          </form>
        </div>
        <div className='side-menu1'>
            <MapComponent searchLocation={searchLocation} />
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default MainPage;
