import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;
import java.util.*;
import javax.swing.*;

public class PasswordStrengthProject1 extends JFrame implements ActionListener {

	private JPanel contentPane;
	private String[] labelNames = { "password" };
	private String[] actualLabelNames = {"length", "num_upper_case", "num_lower_case", "num_numbers",
										 "num_special_chars", "num_variations"};
	private int[] actualLabelValues = {0, 0, 0, 0, 0 , 0};

	private String[] defaultValues = { "0Yxo-eU6AjI" };

	private Map<String, JLabel> labels = new HashMap<>();
	private Map<String, JTextField> userInput = new HashMap<>();

	// x and y coordinates of panel, width and height of panel
	private int x, y, width, height;
	private int upperChars, lowerChars, numberChars, specialChars;
	private int passwordLength, numVariations;
	private String data;
	private JLabel prediction;
	private JTextField endpointURL;

	public PasswordStrengthProject1(int x, int y, int width, int height) {
		this.x = x;
		this.y = y;
		this.width = width;
		this.height = height;
		data = "";
		prediction = new JLabel("Prediction: ");
		endpointURL = new JTextField();
		this.upperChars = 0;
		this.lowerChars = 0;
		this.numberChars = 0;
		this.specialChars = 0;
		this.passwordLength = 0;
		this.numVariations = 0;
	}

	public String makePrediction() {
		URL url;
		String pred = "";
		try {
			url = new URL(endpointURL.getText());
			HttpURLConnection con = (HttpURLConnection) url.openConnection();
			con.setDoOutput(true);

			// write string for request
			OutputStream os = con.getOutputStream();
			byte[] input = data.getBytes("utf-8");
			os.write(input, 0, input.length);

			// read and output resulting prediction
			BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream(), "utf-8"));
			StringBuilder response = new StringBuilder();
			String responseLine = null;
			while ((responseLine = br.readLine()) != null) {
				response.append(responseLine.trim());
			}

			// extracting prediction from response
			int index = response.indexOf("\\\"predicted_label\\\": ") + "\\\"predicted_label\\\": ".length();
			pred = response.substring(index);
			pred = pred.substring(0, pred.indexOf(","));

		} catch (IOException e) {
			e.printStackTrace();
		}

		return pred;
	}

	private void generatePanelContent() {

		// set panel configuration
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(this.x, this.y, this.width, this.height);
		setTitle("Customer Churn Prediction Service");
		contentPane = new JPanel();
		setContentPane(contentPane);
		contentPane.setLayout(new GridLayout(labelNames.length + 2, 2));

		// added URL text field
		contentPane.add(new JLabel("URL"));
		contentPane.add(endpointURL);

		// adding attribute text fields to panel
		for (int i = 0; i < labelNames.length; i++) {
			labels.put(labelNames[i], new JLabel(labelNames[i]));
			userInput.put(labelNames[i] + "Input", new JTextField(defaultValues[i]));
			contentPane.add(labels.get(labelNames[i]));
			contentPane.add(userInput.get(labelNames[i] + "Input"));
		}

		JButton predictButton = new JButton("Predict");
		predictButton.addActionListener(this);
		contentPane.add(predictButton);
		contentPane.add(prediction);

	}

	private int isGreaterthanZero(int value) {
		if (value > 0) {
			return 1;
		} else {
			return 0;
		}
	}
	private void getPasswordCharacteristics(String password) {
		for (int index = 0; index < password.length(); index++) {
			/**
			 * The methods isUpperCase(char ch) and isLowerCase(char ch) of the Character
			 * class are static so we use the Class.method() format; the charAt(int index)
			 * method of the String class is an instance method, so the instance, which,
			 * in this case, is the variable `input`, needs to be used to call the method.
			 **/
			// Check for uppercase letters.
			if (Character.isUpperCase(password.charAt(index))) this.upperChars++;
			else if (Character.isLowerCase(password.charAt(index))) this.lowerChars++;
			else if (Character.isDigit(password.charAt(index))) this.numberChars++;
			else this.specialChars++;
		}
		this.passwordLength = this.upperChars + this.lowerChars + this.numberChars + this.specialChars;
		this.numVariations = isGreaterthanZero(this.upperChars) + isGreaterthanZero(this.lowerChars) +
							 isGreaterthanZero(this.numberChars) + isGreaterthanZero(this.specialChars);

		this.actualLabelValues[0] =	this.passwordLength;
		this.actualLabelValues[1] = this.upperChars;
		this.actualLabelValues[2] = this.lowerChars;
		this.actualLabelValues[3] = this.numberChars;
		this.actualLabelValues[4] = this.specialChars;
		this.actualLabelValues[5] = this.numVariations;
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// getting data from text fields and making JSON
		data = "";
		data += "{";
		for (int i = 0; i < actualLabelNames.length; i++) {
			data += "\"" + actualLabelNames[i] + "\":\"" + Integer.toString(actualLabelValues[i]) + "\"";
			if (i != actualLabelNames.length - 1) {
				data += ",";
			}
		}
		data += "}";

		// gives user back prediction in GUI
		prediction.setText("Prediction: " + makePrediction());
	}

	public static void main(String[] args) {
		PasswordStrengthProject1 PasswordStrength = new PasswordStrengthProject1(0, 0, 1600, 600);
		PasswordStrength.generatePanelContent();
		PasswordStrength.setVisible(true);
	}

}
