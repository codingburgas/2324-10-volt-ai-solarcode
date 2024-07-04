import React, { useRef, useEffect } from 'react'; 
import NavBar from '../components/NavBar';
import Footer from '../components/Footer'
import { Link, Navigate } from "react-router-dom"
import 'react-lazy-load-image-component/src/effects/blur.css'; // Import the desired effect
import iPhonePhoto from "../assets/iPhone-13-Pro-Front.png"
import MacPhoto from "../assets/Mac Studio.png"
import { IoIosArrowDown } from "react-icons/io";



function HomePage() {
  const section1Ref = useRef(null);
  const section2Ref = useRef(null);
  const section3Ref = useRef(null);



  const handleClick_section1 = () => {
    if (section1Ref.current) {
      section1Ref.current.scrollIntoView({ behavior: 'smooth' });
    }
  };
  const handleClick_section2 = () => {
    if (section2Ref.current) {
      section2Ref.current.scrollIntoView({ behavior: 'smooth' });
    }
  };
  const handleClick_section3 = () => {
    if (section3Ref.current) {
      section3Ref.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const containerStyle = {
    textAlign: 'center',
    fontFamily: 'Arial, sans-serif',
    overflow: 'hidden'
  };
  
  return (
    <div style={containerStyle}>
      <NavBar handleClick={handleClick_section1} handleClick1={handleClick_section2} handleClick2={handleClick_section3}/>

      <div>
        <div className='content-banner'>
          <div className='content-banner2'>

            <div className='content-banner1'>
              <h1>Complete Solution for Your Solar Panel Needs!</h1>
              <h3>Complete Solution for Your Solar Panel Needs!Complete Solution for Your Solar Panel Needs!Complete Solution for Your Solar Panel Needs!Complete Solution for Your Solar Panel Needs!Complete Solution for Your Solar Panel Needs!</h3>
            </div>

            <div className='content-banner1'>
                <Link to="/main"><button type="button">Try Now</button></Link>
            </div>

            <div className='content-banner1'>
              <Link to="/"><IoIosArrowDown  className='arrow-down' size={90}  onClick={handleClick_section1}/></Link>
            </div>
        </div>
      </div>


      
            <img src={iPhonePhoto} alt="My Image" className='iphone'/>
            <img src={MacPhoto} alt="My Image" className='mac'/>
      <section className="section-2" ref={section1Ref} id="section-2">
        <div className="section__title">
          <h4>Features</h4>
          <h1>What does <span id='specialEffect'>SolarCoders</span> offer?</h1>
          <br></br>
          <hr></hr>
        </div>              
        <div className="section-content2">
          <br></br>
          <ul>
            <li id="special"><b>Interactive Mapping Interface:</b> Our user-friendly interactive map allows you to effortlessly navigate and explore potential solar panel installation sites. Zoom in and out, pan across different areas, and click on specific locations to get detailed information about their solar potential.</li>           
            <li><b>Solar Potential Analysis</b> Harness the power of advanced algorithms and satellite data to evaluate the solar potential of any location. Our tool provides detailed insights into sunlight exposure, average solar radiation, and seasonal variations to help you make informed decisions. </li>
            <li><b>Customizable Layers</b> Tailor your map view with customizable layers that include terrain, building footprints, vegetation cover, and more. Visualize how different factors impact the suitability of a location for solar panel installation. </li>
            <li><b>Resource Hub:</b> Access and share study materials and notes. </li>
            <li><b>Weather Data Integration </b> Access real-time and historical weather data to understand how local climate conditions affect solar energy production. Our tool integrates information on cloud cover, temperature, and precipitation to give you a comprehensive overview. </li>
          </ul>
        </div>



      </section>
      
      <section className="section-3" ref={section2Ref}>
        <div className="section__title">
          <h4>ABOUT</h4>
          <h1>About Our Team</h1>
          <br></br>
          <hr></hr>
        </div>
        <div className='section__3content'>
          <p>
          Welcome to Solar Coders, your premier destination for discovering optimal locations for solar panel installations. Our mission is to empower individuals, businesses, and communities to harness the power of solar energy, contributing to a sustainable and energy-efficient future. Here’s what makes us the trusted leader in solar mapping solutions:
          </p>
          <br></br>
          <h2>Our Mission</h2>
          <p>
          Welcome to our Solar Panel Mapping Tool, your premier destination for discovering optimal locations for solar panel installations. Our mission is to empower individuals, businesses, and communities to harness the power of solar energy, contributing to a sustainable and energy-efficient future. Here’s what makes us the trusted leader in solar mapping solutions:
          </p>
        </div>
      </section>
      
      <section className="section-1" ref={section3Ref} id="section-1">
        <div className="section__title">
          <h4>Team</h4>
          <h1>Members of the Team </h1>
          <br></br>
          <hr></hr>
        </div>
        <div className="section-content1">

        </div>
      </section>
      
      <Footer />  
    </div>
    </div>
  )
}

export default HomePage;
