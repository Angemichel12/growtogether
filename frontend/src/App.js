import { Routes, Route } from "react-router-dom"
import './App.css';
import Home from './components/Home.jsx'
import { Login } from "./components/pages/Login";
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={ <Home/> } />
        <Route path="/login" element={<Login/>}/>
      </Routes>
    </div>
  );
}

export default App;
