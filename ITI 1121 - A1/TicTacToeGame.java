/**
 * The class <b>TicTacToeGame</b> is the
 * class that implements the Tic Tac Toe Game.
 * It contains the grid and tracks its progress.
 * It automatically maintain the current state of
 * the game as players are making moves.
 *
 * @author Guy-Vincent Jourdan, University of Ottawa
 */
public class TicTacToeGame {

// FINISH THE VARIABLE DECLARATION
   /**
	* The board of the game, stored as a one dimension array.
	*/
	CellValue board[];


   /**
	* level records the number of rounds that have been
	* played so far. 
	*/
	private int level;

   /**
	* gameState records the current state of the game.
	*/
	private GameState gameState;


   /**
	* lines is the number of lines in the grid
	*/
	private int lines;

   /**
	* columns is the number of columns in the grid
	*/
	private int columns;


   /**
	* sizeWin is the number of cell of the same type
	* that must be aligned to win the game
	*/
	private int sizeWin;


   /**
	* default constructor, for a game of 3x3, which must
	* align 3 cells
	*/
	public TicTacToeGame(){
		columns = 3;
		lines = 3;
		sizeWin = 3;
		board = new CellValue [9];
		for(int c = 0; c<9;c++){
			board[c] = CellValue.EMPTY;
		}
		level = 0;
		gameState = GameState.PLAYING;

	}

   /**
	* constructor allowing to specify the number of lines
	* and the number of columns for the game. 3 cells must
	* be aligned.
   	* @param lines
    *  the number of lines in the game
    * @param columns
    *  the number of columns in the game
  	*/
	public TicTacToeGame(int lines, int columns){
		this.lines = lines;
		this.columns = columns;
		sizeWin = 3;
		board = new CellValue [lines*columns];
		for(int c = 0; c<lines*columns;c++){
			board[c] = CellValue.EMPTY;
		}
		level = 0;
		gameState = GameState.PLAYING;
	}

   /**
	* constructor allowing to specify the number of lines
	* and the number of columns for the game, as well as 
	* the number of cells that must be aligned to win.
   	* @param lines
    *  the number of lines in the game
    * @param columns
    *  the number of columns in the game
    * @param sizeWin
    *  the number of cells that must be aligned to win.
  	*/
	public TicTacToeGame(int lines, int columns, int sizeWin){

		this.lines = lines;
		this.columns = columns;
		this.sizeWin = sizeWin;
		board = new CellValue[lines*columns];
		for(int c = 0; c<lines*columns;c++){
			board[c] = CellValue.EMPTY;
		}
		level = 0;
		gameState = GameState.PLAYING;

	}

   /**
	* getter for the variable lines
	* @return
	* 	the value of lines
	*/
	public int getLines(){

		 return lines;

	}

   /**
	* getter for the variable columns
	* @return
	* 	the value of columns
	*/
	public int getColumns(){

		return columns;

	}

   /**
	* getter for the variable level
	* @return
	* 	the value of level
	*/
	public int getLevel(){

		return level;

	}

  	/**
	* getter for the variable sizeWin
	* @return
	* 	the value of sizeWin
	*/
	public int getSizeWin(){

		return sizeWin;

	}

   /**
	* getter for the variable gameState
	* @return
	* 	the value of gameState
	*/
	public GameState getGameState(){

		return gameState; 

	}

   /**
	* returns the cellValue that is expected next,
	* in other word, which played (X or O) should 
	* play next.
	* This method does not modify the state of the
	* game.
	* @return 
    *  the value of the enum CellValue corresponding
    * to the next expected value.
  	*/
	public CellValue nextCellValue(){
		if(level%2 == 0){
			return CellValue.X;
		}
		else{
			return CellValue.O;
		}

	}

   /**
	* returns the value  of the cell at
	* index i.
	* If the index is invalid, an error message is
	* printed out. The behaviour is then unspecified
   	* @param i
    *  the index of the cell in the array board
    * @return 
    *  the value at index i in the variable board.
  	*/
	public CellValue valueAt(int i) {

		if (i >= board.length){
			System.out.println("invalid input");
		}
		return board[i-1];
	}

   /**
	* This method is called when the next move has been
	* decided by the next player. It receives the index
	* of the cell to play as parameter.
	* If the index is invalid, an error message is
	* printed out. The behaviour is then unspecified
	* If the chosen cell is not empty, an error message is
	* printed out. The behaviour is then unspecified
	* If the move is valide, the board is updated, as well
	* as the state of the game.
	* To faciliate testing, is is acceptable to keep playing
	* after a game is already won. If that is the case, the
	* a message should be printed out and the move recorded. 
	* the  winner of the game is the player who won first
   	* @param i
    *  the index of the cell in the array board that has been 
    * selected by the next player
  	*/
	public void play(int i) {


		if(i>=board.length || i< 0){
			System.out.println("Index not on board. Choose another:");

		}
		else if (board[i] != CellValue.EMPTY) {
			System.out.println("Space has been played on already");
		}
		else {
			board[i] = nextCellValue();
			level +=1;
			if(gameState == GameState.PLAYING){
				setGameState(i);
			}
		}

	
	}


   /**
	* A helper method which updates the gameState variable
	* correctly after the cell at index i was just set in
	* the method play(int i)
	* The method assumes that prior to setting the cell
	* at index i, the gameState variable was correctly set.
	* it also assumes that it is only called if the game was
	* not already finished when the cell at index i was played
	* (i.e. the game was playing). Therefore, it only needs to 
	* check if playing at index i has concluded the game, and if
	* set the oucome correctly
	* 
   	* @param i
    *  the index of the cell in the array board that has just 
    * been set
  	*/


	private void setGameState(int i){
		CellValue current = board[i];
		//finding row and column of i
		int row = (i/columns)+1;
		int col = i%columns+1;

		//column win
		boolean colWin = false;
		int j = 0;
		int inARow = 0;
		while(j<lines && colWin == false){
			int index = (columns*j+col)-1;
			if(index<board.length){
				if(board[index] != current){
					inARow = 0;
				}
				else{					
					inARow+=1;
				}
				if(inARow >= sizeWin){
					colWin = true;
				}
			}
			j++;
		}
		
		//row win
		boolean rowWin = false;
		int k = (columns*(row-1));
		inARow = 0;
		while(k <columns*(row) && rowWin==false){
			if(board[k] != current){
				inARow = 0;
			}
			else{
				inARow +=1;
			}
			if(inARow >= sizeWin){
				rowWin = true;
			}
			k++;
		}

		// left to right diagonal win
		inARow = 0;
		boolean rightDiagWin = false;
		i = col - row;
		if(i<0){
			i = (columns*(row-col)+1);
		}
		while(i<board.length && rightDiagWin == false){
			if(board[i] != current){
				inARow = 0;
			}
			else{
				inARow +=1;
			}
			if(inARow>=sizeWin){
				rightDiagWin = true;
			}
			i+=(columns+1);
		}

		//right to left diagonal win b
		inARow = 0;
		boolean leftDiagWin = false;
		i = (row-1)+(col-1);
		int rowCheck = row;
		int colCheck = col;
		while(i<board.length && leftDiagWin == false){
			if(board[i] != current){ // resets counter if alternate player's piece observed in path
				inARow = 0;
			}
			else{
				inARow +=1;
			}
			if(inARow>=sizeWin){ // winning streak obtained
				leftDiagWin = true;
			}

			/*exception case handling: if checking center corner,
			will produce true when false. ends loop for these false cases
			*/
			
			int rowI = (i/columns)+1;
			int colI = i%columns +1;
			if((colI==colCheck) != (rowI == rowCheck)){
				leftDiagWin = false; 
				i = board.length;
			}
			rowCheck = rowI;
			colCheck = colI;


			// next place in diagonal
			i+=(columns-1);
		}

		boolean win = leftDiagWin || rightDiagWin || rowWin || colWin;
		if(win){
			if(current == CellValue.X){
				System.out.println("X has won!");
				gameState = GameState.XWIN;
			}
			if(current == CellValue.O){
				System.out.println("O has won!");
				gameState = GameState.OWIN;
			}
		}

		// draw case
		boolean full = true;
		i = 0;
		while(i<board.length & full == true){
			if(board[i]== CellValue.EMPTY){
				full = false;
			}
			i++;
		}
		if(full == true && !win){
			System.out.println("Game ends in a draw");
			gameState = GameState.DRAW;
		}
	}



   /**
	* Returns a String representation of the game matching
	* the example provided in the assignment's description
	* 
   	* @return
    *  String representation of the game
  	*/

	public String toString(){
		final String NL = System.getProperty("line.separator");
		String grid = "";
		String dash = "";
		for(int i = 0; i<columns; i++){ // creating dash seperators according to board size
			dash+= "----";
		}
		for(int i=0;i<lines;i++){
			//row seperators
			if(i!=0){
				grid += NL;
				grid += dash;
				grid += NL;
			}
			for(int j = 1; j<=columns;j++){ // filling in grid
				if(board[(i*columns+j)-1] == CellValue.X){
					grid+= " X ";
					if(j != columns){
						grid += "|";
					}
				}
				else if(board[(i*columns+j)-1] == CellValue.O){
					grid+=" O ";
					if(j != columns){
						grid += "|";
					}
				}
				else if (board[(i*columns+j)-1] == CellValue.EMPTY){
					grid+="   ";
					if(j != columns){
						grid += "|";
					}
				}
			}
		}
		return grid;
	}

}