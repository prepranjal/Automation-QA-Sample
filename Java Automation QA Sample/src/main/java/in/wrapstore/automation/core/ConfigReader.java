package in.wrapstore.automation.core;

import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Properties;

public class ConfigReader {

    private static final Properties props = new Properties();

    static {
        // Loads from src/test/resources/config/config.properties (on test classpath)
        try (InputStream is = ConfigReader.class
                .getClassLoader()
                .getResourceAsStream("config/config.properties")) {

            if (is == null) {
                throw new IllegalStateException("config/config.properties not found on classpath.");
            }
            // Ensure correct encoding
            props.load(new java.io.InputStreamReader(is, StandardCharsets.UTF_8));
        } catch (Exception e) {
            throw new RuntimeException("Failed to load configuration: " + e.getMessage(), e);
        }
    }

    public static String getBaseUrl() {
        return getString("baseUrl");
    }

    public static String getBrowser() {
        return getString("browser", "chrome").toLowerCase();
    }

    public static int getTimeoutSeconds() {
        return getInt("timeout", 10);
    }

    public static boolean isHeadless() {
        return getBoolean("headless", false);
    }

    // ---------- helpers ----------

    public static String getString(String key) {
        String value = props.getProperty(key);
        if (value == null) {
            throw new IllegalStateException("Missing config key: " + key);
        }
        return value.trim();
    }

    public static String getString(String key, String defaultValue) {
        String value = props.getProperty(key);
        return value == null ? defaultValue : value.trim();
    }

    public static int getInt(String key, int def) {
        String value = props.getProperty(key);
        if (value == null) return def;
        try {
            return Integer.parseInt(value.trim());
        } catch (NumberFormatException e) {
            return def;
        }
    }

    public static boolean getBoolean(String key, boolean def) {
        String value = props.getProperty(key);
        return value == null ? def : Boolean.parseBoolean(value.trim());
    }
}
