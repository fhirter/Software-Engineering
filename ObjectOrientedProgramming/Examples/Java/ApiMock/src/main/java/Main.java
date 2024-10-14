
import java.time.LocalDateTime;
import java.util.List;


public class Main {
    public static void main(String[] args) {
        CovidApiMock covidApiMock = new CovidApiMock();
        WeatherApiMock weatherApiMock = new WeatherApiMock();

        LocalDateTime now = LocalDateTime.now();
        LocalDateTime oneYearAgo = now.minusYears(1);
        LocalDateTime fiveDaysAgo = now.minusDays(5);

        List<Long> covidData = covidApiMock.getCovidCases(oneYearAgo, now);
        List<Integer> weatherData = weatherApiMock.getWeatherData(fiveDaysAgo, now);


    }
}

