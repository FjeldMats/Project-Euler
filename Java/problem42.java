import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class problem42 {

	public static void main(String[] args) {
		
		String Filnavn = "words.txt";
		ArrayList<String> words = new ArrayList<String>();
		
		
		try (BufferedReader br = new BufferedReader(new FileReader(Filnavn))) {

			String sCurrentLine;

			while ((sCurrentLine = br.readLine()) != null) {
				//System.out.println(sCurrentLine);
				words.add(sCurrentLine);
			}

		} catch (IOException e) {
			e.printStackTrace();
		}
		
		List<String> wordsList = Arrays.asList(words.get(0).split(","));
		//System.out.println(wordScore(wordsList.get(2)));
		
		int count = 0;
		for(int i=0;i<wordsList.size();i++) {
			if( isTriangleNum(wordScore(wordsList.get(i)))){
				count++;
			}
		}
		
		System.out.println("Number of Triangle words: "+count);
	}
	
	public static int wordScore(String word) {
		int Score = 0;
		List<String> letters = Arrays.asList(word.split(""));
		
		ArrayList<Character> alph = new ArrayList<Character>();
		
		for (char c = 'A'; c <= 'Z'; c++) {
		    alph.add(c);
		}
		
		for(int i = 0; i < letters.size(); i++) {
			for(int j = 0; j<alph.size(); j++){
				String letter = letters.get(i);
				if(letter.charAt(0) == alph.get(j)) {
					//System.out.println(letter + "  + "+ (j+1));
					Score += j+1;
					break;
				}
			}
		}
		//System.out.println(word);
		return Score;
	}
	
	public static boolean isTriangleNum(int num) {
		
		ArrayList<Integer> triangleNums = new ArrayList<Integer>();
		
		for(int n=1;n<=1000;n++) {
			triangleNums.add((int) (n*(n+1)/2));
		}
		for(int i=0;i<=triangleNums.size();i++) {
			if(triangleNums.get(i)> num) {
				return false;
			}
			if(triangleNums.get(i) == num) {
				return true;
			}
		}
		return false;
	}
}
