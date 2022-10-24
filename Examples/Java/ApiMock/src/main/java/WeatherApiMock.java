import java.time.Duration;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class WeatherApiMock {

    public static final int MAX_API_DAYS = 5;

    public List<Integer> getWeatherData(LocalDateTime from, LocalDateTime to) {
        return generateWeatherMockData(from, to);
    }

    private List<Integer> generateWeatherMockData(LocalDateTime from, LocalDateTime to) {
        List<Integer> output = new ArrayList<>();

        Duration duration = Duration.between(from, to);
        Duration maxDuration = Duration.ofDays(MAX_API_DAYS);
        if(duration.compareTo(maxDuration) <= 0) {
            long hoursInDuration = duration.toHours();
            for(int i = 0; i < hoursInDuration; i++) {
                Integer temperature = (int) (Math.random() * 50 -10);

                output.add(temperature);
            }
        }
        return output;
    }
}
