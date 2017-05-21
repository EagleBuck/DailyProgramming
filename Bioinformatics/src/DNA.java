import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Created 2017-05-17
 */
public class DNA {

    public static void main(String[] args) {
        System.out.println("This program will create the parallel to a string of DNA inputs\nA pairs with T, G pairs with C");
        while(true) {
            Scanner reader = new Scanner(System.in);
            System.out.println("Enter a string of A T G C");
            String inString = reader.nextLine();
            inString = inString.toLowerCase();
            inString = inString.replace(" ", "");

            flip(inString);
        }
    }

    public static String flip(String inString){
        String[] inList = inString.split("");
        String[] outList = new String[inList.length];
        for (int i = 0; i < inString.length(); i++) {
            switch (inList[i]) {
                case ("a"):
                    outList[i] = "t";
                    break;
                case ("t"):
                    outList[i] = "a";
                    break;
                case ("g"):
                    outList[i] = "c";
                    break;
                case ("c"):
                    outList[i] = "g";
                    break;
            }
        }
        String outString = String.join("", outList);
        System.out.println(outString);
        return outString;
    }



    //a-t g-c

    //get user input
    //check user input is just atgc
    //created parallel string
    //give parallel string

}
