import React, { useState, useRef, useEffect } from "react";
import "./App.css";
import BarChartWithImages from "./D3components";

function App() {
  const myData = [
    { name: "Boston Bruins", value: -9.81, imageUrl: "" },
    { name: "Buffalo Sabres", value: 4.35, imageUrl: "" },
    { name: "Detroit Red Wings", value: -6.72, imageUrl: "" },
    { name: "Florida Panthers", value: -6.3, imageUrl: "" },
    { name: "Montreal Canadiens", value: -4.8, imageUrl: "" },
    { name: "Ottawa Senators", value: -8.5, imageUrl: "" },
    { name: "Tampa Bay Lightning", value: -4.1, imageUrl: "" },
    { name: "Toronto Maple Leafs", value: -5.3, imageUrl: "" },
    { name: "Carolina Hurricanes", value: 2.4, imageUrl: "" },
    { name: "Columbus Blue Jackets", value: -5.7, imageUrl: "" },
    { name: "New Jersey Devils", value: -9.9, imageUrl: "" },
    { name: "New York Islanders", value: 1.84, imageUrl: "" },
    { name: "New York Rangers", value: 1.79, imageUrl: "" },
    { name: "Philadelphia Flyers", value: 6.6, imageUrl: "" },
    { name: "Pittsburgh Penguins", value: -9.81, imageUrl: "" },
    { name: "Washington Capitals", value: -7.62, imageUrl: "" },
    { name: "Chicago Blackhawks", value: 5.23, imageUrl: "" },
    { name: "Colorado Avalanche", value: -1.67, imageUrl: "" },
    { name: "Dallas Stars", value: 2.64, imageUrl: "" },
    { name: "Minnesota Wild", value: 8.5, imageUrl: "" },
    { name: "Nashville Predators", value: 5.05, imageUrl: "" },
    { name: "St. Louis Blues", value: -1.55, imageUrl: "" },
    { name: "Winnipeg Jets", value: -9.34, imageUrl: "" },
    { name: "Anaheim Ducks", value: 7.96, imageUrl: "" },
    { name: "Arizona Coyotes", value: 3.4, imageUrl: "" },
    { name: "Calgary Flames", value: -7.24, imageUrl: "" },
    { name: "Edmonton Oilers", value: 4.9, imageUrl: "" },
    { name: "Los Angeles Kings", value: -8.96, imageUrl: "" },
    { name: "San Jose Sharks", value: -2.91, imageUrl: "" },
    { name: "Seattle Kraken", value: 1.3, imageUrl: "" },
    { name: "Vancouver Canucks", value: 6.84, imageUrl: "" },
    { name: "Vegas Golden Knights", value: 6.77, imageUrl: "" },
  ];

  // Sorting all the elements of data from lowest to highest
  function insertionSort(arr) {
    let n = arr.length;
    for (let i = 1; i < n; i++) {
      let current = arr[i];

      let j = i - 1;
      while (j > -1 && current.value < arr[j].value) {
        arr[j + 1] = arr[j];
        j--;
      }
      arr[j + 1] = current;
    }
    return arr;
  }

  const sorted_data = insertionSort(myData);
  // console.log(sorted_data);

  return (
    <div className="App">
      <BarChartWithImages data={myData} />
    </div>
  );
}

export default App;
