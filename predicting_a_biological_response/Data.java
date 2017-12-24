import java.util.*;
import java.io.*;
class Data{
	public static void main(String[] args){

	}
	public static void readFile(){
		BufferedReader reader = new BufferedReader(new FileReader('train.csv'));
		String line = null;
		Scanner scanner = null;
		int index = 0;
		int id = 1;
		ArrayList<String> on = new ArrayList<String();
		while((line = reader.readLine()) != null){
			Record r = new Record();
			scanner = new Scanner(line);
			scanner.useDelimiter(",");
			while(scanner.hasNext()){
				String data = scanner.next();
				if(index == 0){
					r.setId(id);
					r.setOn(Integer.parseInt(data) == 1? true: false);
				}
				index ++;
			}
		}
	}
}