import React, { useState, useEffect } from 'react';
import Board from './Components/Board/Board';
import './App.css';

const App = () => {
  const [boardSize, setBoardSize] = useState(6);
  const [squares, setSquares] = useState(Array(boardSize * boardSize).fill(null));
  const [currentPlayer, setCurrentPlayer] = useState('X');
  const [winner, setWinner] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/calcul", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        return response.json(); // Return the promise
      })
      .then((data) => {
        console.log(data);
        const initialBoardSize = data.boardSize || 3; // Adjust the default value as needed
        setBoardSize((_prev) => initialBoardSize);
        console.log(boardSize)
        setSquares(Array(boardSize * boardSize).fill(null));
        console.log(squares)
      })
      .catch((error) => {
        console.error("Error fetching initial data:", error);
      });
  }, []);
  
  //Faire ca du coté serv
  const handleSquareClick = (index) => {
    setCurrentPlayer(currentPlayer === 'X' ? 'O' : 'X');
    setSquares((prevSquares) => {
      const newSquares = [...prevSquares];
      newSquares[index] = currentPlayer;
      console.log(newSquares)
      return newSquares;
    });
  };

  return (
    <div className="app">
      <h1>Tic Tac Toe</h1>
      {winner ? (
        <p>Player {winner} wins!</p>
      ) : (
        <p>Current player: {currentPlayer}</p>
      )}
      <Board squares={squares} onClick={handleSquareClick} />
    </div>
  );
};

export default App;