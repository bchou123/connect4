import java.util.*;

/**
 * A Connect 4 game interface. Connect 4 is a two-player game where each player tries to
 * make a straight line (vertical, horizontal, or diagonal) of four of their
 * colored checkers by dropping their checkers into a 6 x 7 grid.
 * The ConnectFourGame interface provides methods for client to set two players, make move(choose a column to drop a checker every round),
 * get current player, get the game status and get a deep copy of the board.
 * Example:
 * <pre>
 *         String playerName1 = "Lisa";
 *         String playerName2 = "Luna";
 *         ConnectFour game = new ConnectFour(playerName1, playerName2);
 *
 *         ConnectFour.Player currentPlayer = game.getCurrentPlayer();
 *         System.out.println("The current player is "+currentPlayer.getName()); //prints "The current player is Lisa"
 *         int column = 1;
 *         game.makeMove(column);
 *         int[][] board = game.getBoard(); //prints board after dropping checker into first column
 *         System.out.println(game.getStatus());  //prints PLAYING
 * </pre>
 * @author  Disha Das
 * @author  Yiqin Han
 *
 */
public class ConnectFour{
    /**
     * Inner class that defines player in this game and records his name and winning status.
     */
    public class Player{

        private String name;
        private boolean is_winner;

        public Player(String name){
            this.name = name;
            is_winner = false;
        }

        /**
         * Get the name of the player.
         * @return name in String.
         */
        public String getName(){
            return name;
        }

        /**
         * Get the winning status of the player.
         * @return winning status in bool. True represents win, and false otherwise.
         */
        public boolean isWinner(){
            return is_winner;
        }
    }
    /**
     * Game status. A game starts from PLAYING until any player wins this game(PLAYER_1_WINS or PLAYER_2_WINS),
     * or DRAW(all columns are full without anyone winning)
     */
    public enum Status {
        /**
         * Represents player 1 wins the game.
         */
        PLAYER_1_WINS,
        /**
         * Represents player 2 wins the game.
         */
        PLAYER_2_WINS,
        /**
         * Represents that the game is still playing.
         */
        PLAYING,
        /**
         * Represents a draw.
         */
        DRAW
    }

    private Player player1;
    private Player player2;
    private Player nextMove;
    private Player[] players;
    private Status status;

    private int player_id;
    /**
     * Record the next position for each column.
     */
    HashMap<Integer,Integer> nextPositions = new HashMap<Integer, Integer>();
    /**
     * 6 * 7 game board recording every user's move.
     */
    private int[][] board = new int[6][7];

    /**
     * Constructor for initializing players and game status.
     * @param playerName1, player 1's name
     * @param playerName2, player 2's name
     */
    public ConnectFour(String playerName1, String playerName2){
        players = new Player[2];
       
       
        for(int i=0;i<7;i++){
            nextPositions.put(i,5);
        }

        status = Status.PLAYING;
        this.setPlayers(playerName1,playerName2);
    }


    /**
     * Allow a player to drop a checker into a specified column. Check if there is a winner after the player make a move and switch to another player.
     * @param column into which the player drop a checker, integer, [1, 7] inclusive.
     * @throws IllegalArgumentException when
     * 1.the column is full
     * 2.the column specified is out of range.
     */

    public void makeMove(int column){
        int col = column - 1;

        if(col < 0 || col > board[0].length){
            throw new IllegalArgumentException("Column is out of range. please enter column from 1 to 7");
        }
        int row = nextPositions.get(col);

        if(row < 0){
            throw new IllegalArgumentException("Column is full. Please choose another column");
        }

        board[row][col] = player_id;

        nextPositions.put(col,row-1);


        if(checkWinner()){
            if(player_id == 1){
                status = Status.PLAYER_1_WINS;
                player1.is_winner = true;
            }
            else{
                status = Status.PLAYER_2_WINS;
                player2.is_winner = true;
            }
        }

        else{
            checkDraw();
        }

        // System.out.println("Current: "+player_id+" "+nextMove.name);
        player_id = (player_id) %2 + 1;
        // System.out.println("next player: "+player_id);
        nextMove = players[player_id - 1];
        // System.out.println(nextMove.name);
    }

    /**
     * Set the players of current game.
     * @param playerName1 the name of the player 1
     * @param playerName2 the name of the player 2
     */
    private void setPlayers(String playerName1, String playerName2){
        Player p1 = new Player(playerName1);
        Player p2 = new Player(playerName2);
        this.player1 = p1;
        this.player2 = p2;
        players[0] = player1;
        players[1] = player2;
        //randomly first player instead of assigning #1
        player_id = 1;
        this.nextMove = p1;
    }

    /**
     * Get current game status.
     * @return Status, an enum represents the game status
     */

    public Status getStatus(){
        return status;
    }


    /**
     * Get the board array.
     * @return a deep copy of the board array
     */

    public int[][] getBoard() {
        int[][] newBoard = new int[6][7];
        for (int i = 0; i < board.length; ++i) {
            for (int j = 0; j < board[0].length; ++j) {
                newBoard[i][j] = board[i][j];
            }
        }
        return newBoard;
    }

    /**
     * Get current player (whose move it is).
     * @return Player object.
     */

    public Player getCurrentPlayer(){
        return nextMove;
    }

    /**
     * Check if any player win in horizontal, vertical, diagonal direction.
     * @return true if there is winner.
     */
    private boolean checkWinner(){
        return checkHorizontal() || checkVertical() || checkDiagonalDown() || checkDiagonalUp();
    }

    /**
     * Check if any player win in horizontal direction.
     * @return true if there is winner.
     */
    private boolean checkHorizontal(){
        System.out.println("checking horizontal");
        int counter = 0;
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                if(board[i][j] == player_id){
                    counter++;
                    if(counter == 4){
                        return true;
                    }
                }else{
                    counter = 0;
                }
            }
        }

        return false;
    }


    /**
     * Check if there is a draw.
     * @return true if the board is full without a winner.
     */
    private boolean checkDraw(){
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                if(board[i][j] == 0){
                    return false;
                }
            }
        }

        return true;
    }


    /**
     * Check if any player win in vertical direction.
     * @return true if there is winner.
     */
    private boolean checkVertical(){
        System.out.println("checking vertical");

        int counter = 0;
        for(int j=0;j<board[0].length;j++){
            for(int i=0;i<board.length;i++){
            
                if(board[i][j] == player_id){
                    counter++;
                    if(counter == 4){
                        return true;
                    }
                }else{
                    counter = 0;
                }
            }
        }

        return false;
    }

    /**
     * Check if any player win in diagonal up direction.
     * @return true if there is winner.
     */
    private boolean checkDiagonalUp(){
        System.out.println("checking diagonal up");

        for(int i=0;i<board.length - 3;i++){
            for(int j=0;j<board[0].length - 3;j++){
                if(board[i][j] == player_id && board[i+1][j+1] == player_id && board[i+2][j+2] == player_id && board[i+3][j+3]==player_id){
                    return true;
                }
            }
        }

        return false;
    }

    /**
     * Check if any player win in diagonal down direction.
     * @return true if there is winner.
     */
    private boolean checkDiagonalDown(){
        System.out.println("checking diagonal down");

        for(int i=0;i<board.length - 3;i++){
            for(int j=3;j<board[0].length;j++){
                if(board[i][j] == player_id && board[i+1][j-1] == player_id && board[i+2][j-2] == player_id && board[i+3][j-3]==player_id){
                    return true;
                }
            }
        }

        return false;
    }
    
}
