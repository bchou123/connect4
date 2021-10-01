public class Main {
  public static void main(String args[]) {
    String playerName1 = "Lisa";
    String playerName2 = "AI";
    ConnectFour game = new ConnectFour(playerName1, playerName2);

    while (game.getStatus() == ConnectFour.Status.PLAYING) {
      ConnectFour.Player currentPlayer = game.getCurrentPlayer();

      if (currentPlayer.name == "AI") {
        // do ranodm stuff
      }
      
      System.out.println("The current player is "+currentPlayer.getName()); //prints "The current player is Lisa"

      game.makeMove(column);
      int[][] board = game.getBoard(); //prints board after dropping checker into first column
      System.out.println(game.getStatus());  //prints PLAYING

      if (game.getStatus() == PLAYER_1_WIN)
      System.out.println"
    }
  }
}

=======
PLAYING
=======