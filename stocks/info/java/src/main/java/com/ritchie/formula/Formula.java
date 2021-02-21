package com.ritchie.formula;

import yahoofinance.Stock;
import yahoofinance.YahooFinance;

import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;

public class Formula {

    private static final String ANSI_RED = "\u001B[31m";
    private static final String ANSI_GREEN = "\u001B[32m";
    private static final String ANSI_CYAN = "\u001B[36m";

    private final String ticker1;
    private final String ticker2;
    private final String ticker3;
    private final String ticker4;
    private final String ticker5;

    public Formula(String ticker1, String ticker2, String ticker3, String ticker4, String ticker5) {
        this.ticker1 = ticker1;
        this.ticker2 = ticker2;
        this.ticker3 = ticker3;
        this.ticker4 = ticker4;
        this.ticker5 = ticker5;
    }

    public void Run() throws IOException {
        validateTicker(ticker1);
        validateTicker(ticker2);
        validateTicker(ticker3);
        validateTicker(ticker4);
        validateTicker(ticker5);
    }

    private void validateTicker(String ticker) throws IOException {
        if(ticker != null && !ticker.isBlank()){
            printTickerInfo(ticker);
        }
    }

    private void printTickerInfo(String ticker) throws IOException {
        Stock stock = YahooFinance.get(ticker);

        BigDecimal price = stock.getQuote().getPrice();
        BigDecimal change = stock.getQuote().getChange();
        BigDecimal changeInPercent = stock.getQuote().getChangeInPercent();
        BigDecimal annualYield = stock.getDividend().getAnnualYield();
        BigDecimal annualYieldPercent = stock.getDividend().getAnnualYieldPercent();

        StringBuilder builder = new StringBuilder();
        builder.append(ANSI_CYAN);
        builder.append(ticker.split("\\.")[0]);
        builder.append(": ");
        builder.append(price);
        builder.append(" ");
        if(change.compareTo(BigDecimal.ZERO) > 0){
            builder.append(ANSI_GREEN);
            builder.append("+");
            builder.append(change);
            builder.append(" (");
            builder.append("+");
            builder.append(changeInPercent);
            builder.append("%)");
        } else {
            builder.append(ANSI_RED);
            builder.append(change);
            builder.append(" (");
            builder.append(changeInPercent);
            builder.append("%)");
        }
        builder.append(ANSI_CYAN);


        if(annualYield != null) {
            builder.append(" => Dividends (12 months): ");
            builder.append(annualYield.setScale(2, RoundingMode.HALF_EVEN));
            builder.append(" (");
            builder.append(annualYieldPercent.setScale(2, RoundingMode.HALF_EVEN));
            builder.append("%)");
        }

        System.out.println(builder.toString());
    }
}
