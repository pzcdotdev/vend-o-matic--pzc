import { InventoryItem } from "./InventoryItem";

export const Inventory = ({inventory, purchaseDrink}) => {
  return <div>
      {inventory.map(inventoryItem => <InventoryItem inventoryItem={inventoryItem} key={inventoryItem.id} purchaseDrink={purchaseDrink}/>)}
  </div>
};