package in.wrapstore.automation.utils;

import org.testng.Assert;

public class AssertUtil {

    public static void verifyContains(String actual, String expected, String message) {
        Assert.assertTrue(actual.contains(expected), message);
    }

    public static void verifyEquals(String actual, String expected, String message) {
        Assert.assertEquals(actual, expected, message);
    }
}
