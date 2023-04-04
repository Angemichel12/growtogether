import { Routes, Route } from "react-router-dom"
import './App.css';
import Home from './components/Home.jsx'
import Login from "./pages/Login";
import Umubyeyidash from "./pages/Umubyeyidash";
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={ <Home/> } />
        <Route path="/login" element={<Login/>}/>
        <Route path="/umubyeyidash" element={<Umubyeyidash/>}/>
      </Routes>
    </div>
  );
}

export default App;
