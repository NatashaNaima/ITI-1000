import java.util.LinkedList;

public class ListOfGamesGenerator {
	

   /**
	* generates all different games for the specified
	* parameters. Each game is recorded only once. 
	* once a game is finished, it is not extended further
	* @param lines
    *  the number of lines in the game
    * @param columns
    *  the number of columns in the game
    * @param sizeWin
    *  the number of cells that must be aligned to win.
    * @return
    * a list of lists of game instances, ordered by levels
  	*/
	public static LinkedList<LinkedList<TicTacToeGame>> generateAllGames(int lines, int columns, int winLength){
    LinkedList<LinkedList<TicTacToeGame>> games = new LinkedList<LinkedList<TicTacToeGame>>(); //master list

		TicTacToeGame game = new TicTacToeGame(lines,columns,winLength);// level zero base game
    LinkedList<TicTacToeGame> level = new LinkedList<TicTacToeGame>(); // storing each board position for a level
    level.add(game);
    games.add(level); // add level zero
    int levels = 0; // count of completed levels
    int size = games.get(0).size();// size of last completed level list  


    for(int j=0;j<size;j++){ // list of lists
      LinkedList<TicTacToeGame> level1 = new LinkedList<TicTacToeGame>();
      for(int h=0;h<games.get(levels).size();h++){
        game = games.get(levels).get(h);
        if(game.getGameState() == GameState.PLAYING && game.getLevel() == levels){
          for(int i=0; i<lines*columns;i++){ // each new play
            TicTacToeGame next = new TicTacToeGame(game,i);
            Boolean duplicate = false;
            for(int k =0; k<level1.size();k++){ // checking for duplicate
              if(next.equals(level1.get(k))){
                duplicate = true;
                break;
              }
              if(next.equals(game)){
                duplicate = true;
                break;
              }
            }
            if(duplicate == false){
              level1.add(next);
            }
          } 
        }
        
      }
      if(level1.size() == 0){
        break;
      }
      
      if(levels >= 1){ //fixes strange bug that I do not understand
        level1.remove(); //I apologize for being bad
      } 
      
      games.add(level1); // adding complete list of boards for level 
      levels +=1;
      size = games.get(levels).size();
    } 
    //System.out.println(games);
    return games;
	}
}