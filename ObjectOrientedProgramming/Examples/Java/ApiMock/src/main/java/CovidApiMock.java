import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.io.FileReader;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class CovidApiMock {

    public static final String path = "/home/fabian/IdeaProjects/APIMock2/src/main/resources/covid.json";

    public List<Long> getCovidCases(LocalDateTime from, LocalDateTime to) {
        return readCovidDataFromFile(path);
    }

    private List<Long> readCovidDataFromFile(String filename) {
        JSONParser parser = new JSONParser();
        List<Long> output = new ArrayList<>();

        try {
            JSONArray covidData = (JSONArray) parser.parse(new FileReader(filename));

            // A JSON object. Key value pairs are unordered. JSONObject supports java.util.Map interface.

            // A JSON array. JSONObject supports java.util.List interface.
//            JSONArray companyList = (JSONArray) jsonObject.get("Company List");

            // An iterator over a collection. Iterator takes the place of Enumeration in the Java Collections Framework.
            // Iterators differ from enumerations in two ways:
            // 1. Iterators allow the caller to remove elements from the underlying collection during the iteration with well-defined semantics.
            // 2. Method names have been improved.
            Iterator<JSONObject> iterator = covidData.iterator();
            while (iterator.hasNext()) {
                Long cases = (Long) iterator.next().get("Cases");
                output.add(cases);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return output;
    }
}
