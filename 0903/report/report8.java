/*
 * [실행 방법]
 * 1. 자바 파일 컴파일:
 *    javac report8.java
 * 
 * 2. 바이트코드 역어셈블 (javap 명령어 사용):
 *    javap -c report8
 */

public class report8 {
    public static void main(String[] args) {
        int Y = 2;            
        int X = (Y + 4) * 3;  
        System.out.println(X); // X를 사용하므로 경고가 사라집니다. 이코드는 시스템적으로 문제를 맞기 위해 추가한코드 수식자체는 달라지지않음
    }
}