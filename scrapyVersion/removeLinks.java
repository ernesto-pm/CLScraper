import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class removeLinks{
  public static void main(String[] args) {
    BufferedReader br = null;

  		try {

  			String sCurrentLine;

  			br = new BufferedReader(new FileReader("holi.txt"));

  			while ((sCurrentLine = br.readLine()) != null) {
          //print all of the links in one line with [] for python for allowed domains
          //System.out.print("[\""+sCurrentLine+"\"]+");

          //int count = StringUtils.countMatches(sCurrentLine, "//");
          int count = sCurrentLine.length() - sCurrentLine.replace(".org", "").length();
          //System.out.println(count);

          if(count==4){
            System.out.println(sCurrentLine);
          }
          //print all of the links for start_urls
          //System.out.print("[\""+sCurrentLine+"search/cpg?query=web+site %7C+website+%7C+wordpress&is_paid=yes\"]+");
  			}

  		} catch (IOException e) {
  			e.printStackTrace();
  		} finally {
  			try {
  				if (br != null)br.close();
  			} catch (IOException ex) {
  				ex.printStackTrace();
  			}
  		}

  	}
}
