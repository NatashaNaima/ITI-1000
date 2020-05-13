

public class TicTacToe extends Utils{

   /**
     * <b>main</b> of the application. Creates the instance of  GameController 
     * and starts the game. If two parameters line  and column
     * are passed, they are used. 
     * Otherwise, a default value is used. Defaults values are also
     * used if the paramters are too small (less than 2).
     * 
     * @param args
     *            command line parameters
     */
     public static void main(String[] args) {

        StudentInfo.display();

        TicTacToeGame game;
        int lines = 3;
        int columns = 3;
        int win = 3;

   
        try{
            if (args.length >= 2) {
                lines = Integer.parseInt(args[0]);
                if(lines<2){
                    System.out.println("Invalid argument, using default...");
                    lines = 3;
                }
                columns = Integer.parseInt(args[1]);
                if(columns<2){
                    System.out.println("Invalid argument, using default...");
                    columns = 3;
                }
            }
            if (args.length >= 3){
                win = Integer.parseInt(args[2]);
                if(win<2){
                    System.out.println("Invalid argument, using default...");
                    win = 3;
                }
            } 
            if (args.length > 3){
                System.out.println("Too many arguments. Only the first 3 are used.");
            } 

        } catch(NumberFormatException e){
            System.out.println("Invalid argument, using default...");
            lines   = 3;
            columns  = 3;
            win = 3;
        }

        game = new TicTacToeGame(lines, columns,win);
        
        Player[] players = new Player[2];
        int random = generator.nextInt(2);
        HumanPlayer user = new HumanPlayer();
        ComputerRandomPlayer rando = new ComputerRandomPlayer();
        players[random] = user;
        if(random == 0){
            players[1] = rando;
        }else{
            players[0] = rando;
        }
        while(game.getGameState() == GameState.PLAYING){
            Player p1 = players[0];
            Player p2 = players[1];
            if(game.nextCellValue() == CellValue.X){
                p1.play(game);
            }
            else if(game.nextCellValue() == CellValue.O){
                p2.play(game);
            }
        }
        if(game.getGameState() != GameState.PLAYING){
            System.out.println("The game is over!");
            System.out.println(game);
            System.out.println("Result: " + game.getGameState());
        }

    }

}