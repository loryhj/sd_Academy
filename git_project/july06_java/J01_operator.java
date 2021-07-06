package com.sd.jul06.sooup;

import java.util.Scanner;

// insa라는 변수에 20살 이상이면 안녕하세요, 아니면 안녕
public class J01_operator {
	public static void main(String[] args) {
		Scanner k = new Scanner(System.in);
		System.out.print("나이: ");
		int age = k.nextInt();
		
		// P : and, or, not
		// J : &&, ||, !
		double height = 180;
		
		
		// 키가 150이상이고, 나이가 90이상이면 true
		System.out.println((age >= 90) && (height >=150));
		
		// System.out.println(10 < age < 20 );
		System.out.println((age < 20) && (age > 10));

		// 3항연산
		String insa = (age >= 20) ? "안녕하세요" : "안녕";
		System.out.println(insa);
		

		
		
		
		
		
		
		
		System.out.println("asd");
	}
}

// numpy, pandas, matplotlib, seaborn, nltk, konlpy, opencv, scikit-learn

