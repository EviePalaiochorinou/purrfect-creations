import { useEffect, useState } from "react";
import { fetchOrderData } from "./api";
import DataList from "./components/data-list.component";
import './App.css';

const App = () => {

  const [orderData, setOrderData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    (async () => {
      try {
        //throw new Error('Oops');
        const orderDataResult = await fetchOrderData();
        setOrderData(orderDataResult);        
      } catch (e) {
        setError(e);
        console.log('This is my error: ', e);
      }
    })();
  }, []);

  if (!orderData) {return <div>Dashboard Loading...</div>}
  
  return (
    error ? <div> {error.message} </div> :

    <div className="App">
      <h1 className='app-title'>Purrfect Creations Dashboard</h1>
      <DataList orderData={orderData}/>
    </div>
  );
}

export default App;