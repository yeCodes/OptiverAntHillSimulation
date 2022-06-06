import java.util.Random;
//Random ran = new Random();
//int x = ran.nextInt(6) + 5;

//System.out.println(x);

class anthill{  
	
	public static int oneIteration(){
		//System.out.println("Hello Java");  
         
        Random ran = new Random();
		int x; //= ran.nextInt(4) + 1;
		//System.out.println(x);
		
		int x_pos = 0;
		int y_pos = 0;
		
		boolean foodFound = false;
		
		//int[] antPosition = {0.0};
		int i = 0;
		//for (int i = 0; i <10; i++){
		while(i < 1e5 && foodFound == false){ 
			x = ran.nextInt(4) + 1;
			//System.out.println(x);
			
			if(x ==1){
				//System.out.println("north");
				y_pos += 10;

			}
			else if(x==2){
				//System.out.println("east");
				x_pos += 10;
			}
			else if(x==3){
				//System.out.println("south");
				y_pos += -10;
			}
			else{
				//System.out.println("west");
				x_pos += -10;
			}
			i +=1;
			//check boundary
			if(x_pos + y_pos >= 10){
				foodFound = true;
				//System.out.println("found. i = "+ i);
				return i;
			}
			
		}
		return -1;
	}
	
	public static double multipleSims(int numSims){
		
		long cumulativeTime = 0;
		int noTimesFoodFound = 0;
		double avgTimeFindFood = 0;
		int result;
		
		for(int i =0; i<numSims; i++){
			 result = oneIteration();
			 if(result > 0){
				cumulativeTime += result;
				noTimesFoodFound += 1;
			 }
			 else{
			 
			 }
		}
		
		System.out.println("cumulative time taken " + cumulativeTime);
		System.out.println("no times food found " + noTimesFoodFound);
		avgTimeFindFood = (double)cumulativeTime/ (double) noTimesFoodFound;
		
		return avgTimeFindFood;
	}
	
	
	public static void main(String args[]){  
		
		double answer;
		//answer = multipleSims(100000); //7996.5938 turns. 793270072 cum time, no times 99201
		//answer = multipleSims(1000000);	// overflow error corrected. 7851 turns.  found food 991831 times. cum time taken 77870346460
		//answer = multipleSims(10000000); // run start 2102. end: 2148. 7937.06 at 1cm step per iteration. Re-run for 10cm steps per iteration
		//System.out.println("avg time find food is " + answer + " turns");
		
		//re-run with 10cm per interval
		//answer = multipleSims(100000);	// getting around 210-251
		//answer = multipleSims(1000000); // got 750 or so
		//answer = multipleSims(10000000); // 252.56. 219174141 food found 9,974,473. 251.856 - tot 2512165559. found 9,974,601 timres
		answer = multipleSims(100000000); 	// got 251.745. Cumu time take - 2,511,059,693. No times food found 99,747,975!!  Runtime ~15mins
		System.out.println("avg time find food is " + answer + " turns");
	}  
}  
