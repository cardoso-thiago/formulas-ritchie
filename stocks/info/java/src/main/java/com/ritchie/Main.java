package com.ritchie;

import com.ritchie.formula.Formula;

import java.io.IOException;

public class Main {

  public static void main(String[] args) throws IOException {

    String ticker1 = System.getenv("TICKER1");
    String ticker2 = System.getenv("TICKER2");
    String ticker3 = System.getenv("TICKER3");
    String ticker4 = System.getenv("TICKER4");
    String ticker5 = System.getenv("TICKER5");

    Formula formula = new Formula(ticker1, ticker2, ticker3, ticker4, ticker5);
    formula.Run();
  }
}
