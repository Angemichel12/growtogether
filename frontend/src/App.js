import { Routes, Route } from "react-router-dom"
import './App.css';
import Home from './components/Home.jsx'
import Login from "./pages/Login";
import Umubyeyidash from "./pages/Umubyeyidash";
import UmuMessage from "./pages/UmuMessage";
import UmuSchedule from "./pages/UmuSchedule";
import HealthLogin from "./pages/HealthLogin";
import HealthHome from "./pages/HealthHome";
import HealthRegist from "./pages/HealthRegist";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={ <Home/> } />
        <Route path="/login" element={<Login/>}/>
        <Route path="/umubyeyidash" element={<Umubyeyidash/>}/>
        <Route path="/umuMessage" element={<UmuMessage/>}/>
        <Route path="/umuSchedule" element={<UmuSchedule/>}/>
        <Route path="/healthlogin" element={<HealthLogin/>}/>
        <Route path="/healthhome" element={<HealthHome/>}/>
        <Route path="/healthregist" element={<HealthRegist/>}/>
      </Routes>
    </div>
  );
}

export default App;
