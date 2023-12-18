// Board.js
import React from 'react';
import Square from '../Square/Square';

const Board = ({ squares, onClick, disabled }) => {
  return (
    <div className="board">
      {squares.map((square, index) => (
        <Square
          key={index}
          value={square}
          onClick={() => onClick(index)}
          disabled={disabled}
        />
      ))}
    </div>
  );
};

export default Board;
