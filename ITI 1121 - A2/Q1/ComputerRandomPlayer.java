public class ComputerRandomPlayer extends Utils implements Player{

    public void play(TicTacToeGame game){
        if(game.getGameState() != GameState.PLAYING){
            System.out.println("Game is not currently playable.");
        }else{
            System.out.println("Player 2's turn ");
            int value;
            boolean valid = false;
            while(valid == false){
                value = generator.nextInt(game.lines*game.columns);
                if(value < 0 || value >= (game.lines*game.columns)){
                    valid = false;
                } else if(game.valueAt(value) != CellValue.EMPTY) {
                    valid = false;
                } else {
                    valid = true;
                    game.play(value);
                }
            }
           
            
        }
    }
}