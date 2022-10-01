import { useEffect, useState } from "react";
import { fetchOrderData } from "./api";
import DataList from "./components/data-list.component";
import './App.css';

export default function App() {

  const [orderData, setOrderData] = useState({});
  const [error, setError] = useState('');

  useEffect(() => {
  //   console.log("USE EFFECT CALLED");
  //   fetch("http://127.0.0.0:8000/dashboard")
  //   .then(response => response.json())
  //   .then((users) => setOrderData(users))
  //   .catch((error)=>(setError(error)));
  // }, []);
    (async () => {
      try {
        //throw new Error('Oops');
        const orderDataResult = await fetchOrderData();
        console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        setOrderData(orderDataResult);        
      } catch (e) {
        setError(e);
        console.log('This is my error: ', e);
      }
    })();
  }, []);

  return (
    error ? <div> {error.message} </div> :

    <div className="App">
      <h1 className='app-title'>Purrfect Creations Dashboard</h1>
      {console.log("!!!!!",orderData)}
      <DataList expenses={orderData}/>
    </div>
  );
}