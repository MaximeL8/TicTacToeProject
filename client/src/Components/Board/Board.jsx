import React from 'react';
import Square from '../Square/Square';

const Board = ({ squares, onClick, style }) => {
  return (
    <div style={style}>
      {squares.map((square, index) => (
        <Square
          key={index}
          value={square}
          onClick={() => onClick(index)}
          
        />
      ))}
    </div>
  );
};

export default Board;
