import java.util.Arrays;

// https://open.kattis.com/problems/birthdayboy

public class BirthdayBoy {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

		int dayNumOf27Oct = dateStringToNum("10-27");

		// Reading cases
        int numOfNames = io.getInt();

		int[] dates = new int[numOfNames+1];

		//dates[0] = -1;
		for(int i=0; i<numOfNames; i++) {
			String tull = io.getWord();
			String birthdayString = io.getWord();
			dates[i] = dateStringToNum(birthdayString);
		}
		//System.out.println(Arrays.toString(dates));
		Arrays.sort(dates);
		dates[0] = -(365-dates[dates.length-1]);
		//System.out.println(Arrays.toString(dates));

		int maxDistance = 0;
		int dateOfMaxDist = 0;
		for(int i=0; i<numOfNames; i++) {
			int newDist = dates[i+1]-dates[i];
			//System.out.println(newDist);
			if(newDist > maxDistance) {
				maxDistance = newDist;
				dateOfMaxDist = dates[i+1]-1;
			} else if(newDist == maxDistance) {
				maxDistance = newDist;
				//dateOfMaxDist = Math.min(dateOfMaxDist, dates[i+1]-1);
				int possibleNewDate = dates[i+1]-1;
				if(possibleNewDate > dayNumOf27Oct) {
					if(dateOfMaxDist > dayNumOf27Oct) {
						dateOfMaxDist = Math.min(dateOfMaxDist, possibleNewDate);
					} else {
						dateOfMaxDist = possibleNewDate;
					}
				} else {
					if(dateOfMaxDist > dayNumOf27Oct) {
						dateOfMaxDist = dateOfMaxDist;
					} else {
						dateOfMaxDist = Math.min(dateOfMaxDist, possibleNewDate);
					}
				}
				/*if(dateOfMaxDist<0) {
					dateOfMaxDist = dates[i+1]-1;
				} else {
					dateOfMaxDist = Math.min(dateOfMaxDist, dates[i+1]-1);
				}*/
			}
		}

		System.out.println(dateNumToString(dateOfMaxDist));

		io.close();
	}

	public static int dateStringToNum(String datestring) {
		int[] lengthMonths = {31,28,31,30,31,30,31,31,30,31,30,31};

		String[] parts = datestring.split("-");

		int dateNum = 0;
		for(int mountCounter=1; mountCounter<Integer.parseInt(parts[0]); mountCounter++) {
			dateNum += lengthMonths[mountCounter-1];
		}

		return dateNum+Integer.parseInt(parts[1])-1;
	}

	public static String dateNumToString(int dateNum) {
		int[] lengthMonths = {31,28,31,30,31,30,31,31,30,31,30,31};
		int[] monthsGone = {31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365};

		if(dateNum < 0) {
			dateNum = 365+dateNum;
		}
		//System.out.println(dateNum);

		String month = "";
		int pointer=10;
		while(true) {
			if(dateNum-monthsGone[pointer] >= 0) {
				month = Integer.toString(pointer+2);
				dateNum -= monthsGone[pointer];
				break;
			} else {
				pointer--;
			}
		}

		if(month.length()==1) {
			month = "0"+month;
		}
		String day = Integer.toString(dateNum+1);
		if(day.length()==1) {
			day = "0"+day;
		}
		return month+"-"+day;
	}

}