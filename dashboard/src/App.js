import { useState, useEffect } from 'react';
import { fetchOrderData } from "./api";
import './App.css';

export default function App() {

  const [orderData, setOrderData] = useState([]);
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
        // return error && <div> {error.message} </div>
      }
    })();
  }, []);

  return (
    error ? <div> {error.message} </div> :
    
    <div className="App">
      <h1 className='app-title'>Monsters Rolodex</h1>
    </div>
  );
}
