import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class problem54 {

	public static void main(String[] args) {
		
		String Filnavn = "p054_poker.txt";
		ArrayList<String> rounds = new ArrayList<String>();
		
		
		try (BufferedReader br = new BufferedReader(new FileReader(Filnavn))) {

			String sCurrentLine;

			while ((sCurrentLine = br.readLine()) != null) {
				//System.out.println(sCurrentLine);
				rounds.add(sCurrentLine);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		ArrayList<ArrayList<String>> players = splitToPlayer(rounds.get(0));
		
		System.out.println(players.get(1));
		System.out.println(evalValue(players.get(1)));
	}
	
	public static int evalValue(ArrayList<String> cards) {
		String[] value = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
		//ArrayList<String> cards = (ArrayList<String>) Arrays.asList(hand.split(" "));
		
		int sum = 0;
		
		for (int i = 0; i < cards.size(); i++) {
			for (int j = 0; j < value.length; j++) {
				System.out.println((String) cards.get(i).substring(0,1) + " = " + value[j]);
				if((String) cards.get(i).substring(0,1) == value[j]) {
					sum += j+1;
					break;
				}
			}
		}
		return sum;	
	}
	
	public static ArrayList<ArrayList<String>> splitToPlayer(String hand){
		ArrayList<ArrayList<String>> p = new ArrayList<ArrayList<String>>();
		int ind = 0;
		List<String> cards = Arrays.asList(hand.split(" "));
		ArrayList<String> p1 = new ArrayList<String>();
		ArrayList<String> p2 = new ArrayList<String>();
		
		for (String card: cards) {
			if(ind <  5) {
				p1.add(card);
			}else {
				p2.add(card);
			}
			ind++;
		}
		
		p.add(p1);
		p.add(p2);
		
		return p;
	}

}
