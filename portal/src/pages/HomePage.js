import * as React from 'react';
import NavBar from '../components/NavBar';


const text_on_image = {
    position: "absolute",
    top: "25%",
    width: "100vw",
    textAlign: "center",
    left: 0, 
    right: 0,
    fontFamily: "Work Sans, sans-serif",
    fontWeight: 600,
    color: "#FFFEFE",
    fontSize: 40,
    margin:0, 
    padding:0
}
export default function HomePage() {
  return (
      <div style={{margin:0, padding:0, position:"relative"}}>
          <NavBar/>
          <img style={{width: "100vw", margin:0, padding:0}} alt="home" src={require('../assets/home.jpg')} />
          <div >
             <h3 style={text_on_image}> Your one-stop solution for patient management</h3>
          </div>
      </div>
  );
}

