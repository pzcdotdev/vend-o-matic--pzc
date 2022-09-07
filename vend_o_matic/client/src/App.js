import axios from "axios"
import { useEffect, useState } from "react";
import { DOMAIN, getInitialData } from "./utils";
import { Inventory } from "./Inventory";

import "./App.css";
import { CoinSlot } from "./CoinSlot";


function App() {
    const [{inventory, coin_count}, setData] = useState({"inventory": [],"coin_count": 0});

    useEffect(() => {
        getInitialData().then((data) => {
            const {initial_inventory, initial_coin_count} = data
            setData({
                "inventory": initial_inventory,
                "coin_count": initial_coin_count
            });
        });
    }, []);

    const insertCoin = async (e) => {
        await axios.put(`${DOMAIN}/coinslot`, {"coin": 1})
                   .then(res => console.log(res))
    }


    return (
        <div className="App">
            <header className="App-header">
                <p>Hello!</p>
                <Inventory inventory={inventory} />
                <CoinSlot coin_count={coin_count} insertCoin={insertCoin}/>
            </header>
        </div>
    );
}

export default App;
