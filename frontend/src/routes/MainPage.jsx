import { useEffect, useState } from 'react';
import { Link, useNavigate } from "react-router-dom";
import Footer from '../components/Footer';

import MapComponent from '../components/MapComponent';



function MainPage() {



  const containerStyle = {
    textAlign: 'center',
    fontFamily: 'Arial, sans-serif',
  };

  const [showProfile, setShowProfile] = useState(true);
  const [showIssue, setShowIssue] = useState(false);

  const toggleProfile = () => {
    setShowProfile(true);
    setShowIssue(false); // Close the Issue component when opening the Profile component
  };

  const toggleIssue = () => {
    setShowIssue(true);
    setShowProfile(false); // Close the Profile component when opening the Issue component
  };

  return (
    <div style={containerStyle}>
      <div className="main-page">
      <MapComponent/>
      </div>
      <Footer />
    </div>
  );
}

export default MainPage;
