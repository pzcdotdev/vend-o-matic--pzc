import { useEffect, useState } from "react";
import { getInitialData } from "./utils";
import { Inventory } from "./Inventory";

import "./App.css";

function App() {
    const [{initial_inventory, initial_coin_count}, setInitialData] = useState({"initial_inventory": [],"initial_coin_count": 1});

    useEffect(() => {
        getInitialData().then((data) => {
            console.log(data)
            const {initial_inventory, initial_coin_count} = data
            console.log(initial_coin_count)
            setInitialData({"initial_inventory": initial_inventory,
                            "initial_coin_count": initial_coin_count
                            });
        });
    }, []);


    return (
        <div className="App">
            <header className="App-header">
                <p>Hello!</p>
                <div className="">here {initial_coin_count}</div>
            </header>
        </div>
    );
}

export default App;