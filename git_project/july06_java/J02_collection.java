package com.sd.jul06.sooup;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

// 멀티쓰레드 : 동시에 작업 여러개
// Go
public class J02_collection {
	public static void main(String[] args) {
		//배열 - 크기조절불가
		int[] a = {123, 345, 45, 214};
		System.out.println(a[0]);
		a[3] =100;
		System.out.println(a[3]);
				
		//list 계열
		ArrayList<Integer> b = new ArrayList<>();
		b.add(10);
		b.add(10);
		b.add(20);
		
		System.out.println(b.get(0));
		System.out.println(b);
		
		// set 계열
		HashSet<Integer> c = new HashSet<>();
		c.add(10);
		c.add(10);
		c.add(20);
		System.out.println(c.size());
		System.out.println(c);
		
		// map계열
		HashMap<String, Integer> d = new HashMap<>();
		d.put("마우스", 10000);
		d.put("키보드", 15000);
		System.out.println(d.get("마우스"));
	}
}