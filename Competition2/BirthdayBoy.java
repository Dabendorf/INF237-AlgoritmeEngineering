// https://open.kattis.com/problems/birthdayboy

import java.util.Arrays;

/**
 * There is a group of people with different birthdays.
 * We would like to find the date which has the biggest time having passed since the last birthday
 * If two dates have the same time passed, choose the day with shortest time passed since 27 October
 * 
 * Solution: Write conversion methods date<->dayNumOfTheYear.
 * Convert the dates to dayNumOfTheYear and sort them.
 * Add the last birthday a second time as the first birthday with index 365-day
 * 
 * Find the minimum span between two neighbouring dates and output it converted back to date
 * If two have same distance, output date nearest to 27 October
 */
public class BirthdayBoy {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

		int dayNumOf27Oct = dateStringToNum("10-27");

		// Reading cases
        int numOfNames = io.getInt();

		int[] dates = new int[numOfNames+1];

		// Read birthdays
		for(int i=0; i<numOfNames; i++) {
			io.getWord();
			String birthdayString = io.getWord();
			dates[i] = dateStringToNum(birthdayString);
		}
		
		Arrays.sort(dates);
		dates[0] = -(365-dates[dates.length-1]);

		// Calculate distance between two neighbouring days
		int maxDistance = 0;
		int dateOfMaxDist = 0;
		for(int i=0; i<numOfNames; i++) {
			int newDist = dates[i+1]-dates[i];
			if(newDist > maxDistance) {
				maxDistance = newDist;
				dateOfMaxDist = dates[i+1]-1;
			} else if(newDist == maxDistance) {
				maxDistance = newDist;
				int possibleNewDate = dates[i+1]-1;

				// Special case for two days with same distance
				if(possibleNewDate > dayNumOf27Oct) {
					if(dateOfMaxDist > dayNumOf27Oct) {
						dateOfMaxDist = Math.min(dateOfMaxDist, possibleNewDate);
					} else {
						dateOfMaxDist = possibleNewDate;
					}
				} else {
					if(dateOfMaxDist > dayNumOf27Oct) {
						dateOfMaxDist = dateOfMaxDist + 0;
					} else {
						dateOfMaxDist = Math.min(dateOfMaxDist, possibleNewDate);
					}
				}
			}
		}

		System.out.println(dateNumToString(dateOfMaxDist));

		io.close();
	}

	/**
	 * Converts date into dayNum between 0 and 364 (ignoring leap years)
	 * @param datestring mm-dd
	 * @return Number between 0 and 364
	 */
	public static int dateStringToNum(String datestring) {
		int[] lengthMonths = {31,28,31,30,31,30,31,31,30,31,30,31};

		String[] parts = datestring.split("-");

		int dateNum = 0;
		for(int mountCounter=1; mountCounter<Integer.parseInt(parts[0]); mountCounter++) {
			dateNum += lengthMonths[mountCounter-1];
		}

		return dateNum+Integer.parseInt(parts[1])-1;
	}

	/**
	 * Converts dayOfTheYear back to day format
	 * @param dateNum Number between 0 and 364
	 * @return mm-dd
	 */
	public static String dateNumToString(int dateNum) {
		int[] monthsGone = {31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365};

		if(dateNum < 0) {
			dateNum = 365+dateNum;
		}

		// Looping backwards through monthsGone array to determine the month
		String month = "";
		int pointer=10;
		while(true) {
			if(dateNum-monthsGone[pointer] >= 0) {
				month = Integer.toString(pointer+2);
				dateNum -= monthsGone[pointer];
				break;
			} else {
				pointer--;
				if(pointer<0) {
					month = "01";
					break;
				}
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