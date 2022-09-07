import axios from "axios"
import { useEffect, useState } from "react";
import { DOMAIN, getInitialData } from "./utils";
import { Inventory } from "./Inventory";

import "./App.css";
import { CoinSlot } from "./CoinSlot";


function App() {
    const [inventory, setInventory] = useState([]);
    const [coinCount, setCoins] = useState(0)
    const [returnedCoinCount, setReturnedCoins] = useState(0)

    useEffect(() => {
        getInitialData().then((data) => {
            const {initial_inventory, initial_coin_count} = data
            setInventory(initial_inventory)
            setCoins(initial_coin_count)
        });
    }, []);

    const insertCoin = async (e) => {
        await axios.put(`${DOMAIN}/coinslot`, {"coin": 1})
                   .then(response => {
                    setCoins(parseInt(response.headers["x-coins"]))
                })
    }

    const returnCoin = async (e) => {
        await axios.delete(`${DOMAIN}/coinslot`)
                   .then(response => {
                    setCoins(parseInt(response.headers["x-coins"]))
                    setReturnedCoins(returnedCoinCount + 1)
                   })
    }

    const purchaseDrink = async (e) => {
        const drinkId = e.target.dataset["id"]
        await axios.put(`${DOMAIN}/inventory/${drinkId}`)
                   .then(response => {
                    // const purchasedInventoryItem = inventory.find(x => x["id"] === parseInt(drinkId))
                    console.log(response.headers["x-inventory-remaining"])
                    setCoins(parseInt(response.headers["x-coins"]))
                    setReturnedCoins(returnedCoinCount + coinCount)
                    setCoins(0)
                   })
    }

    return (
        <div className="App">
            <header className="App-header">
                <p>Hello!</p>
                <Inventory inventory={inventory} purchaseDrink={purchaseDrink}/>
                <CoinSlot coinCount={coinCount} insertCoin={insertCoin} returnCoin={returnCoin} returnedCoinCount={returnedCoinCount}/>
            </header>
        </div>
    );
}

export default App;
