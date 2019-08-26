import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;
import java.util.*;
import javax.swing.*;
import java.lang.Math;

public class AveragesProject2_4 extends JFrame implements ActionListener {

	private JPanel contentPane;
	private String[] labelNames = { "A", "B", "C", "D"};

	private String[] defaultValues = { "48", "23", "38", "54"};

	private Map<String, JLabel> labels = new HashMap<>();
	private Map<String, JTextField> userInput = new HashMap<>();

	// x and y coordinates of panel, width and height of panel
	private int x, y, width, height;

	private String data;
	private JLabel labelPrediction;
	private JLabel labelTries;
	private JLabel labelAverageFormula;
	private JLabel labelTrialError;
	private JLabel labelAverageError;
	private JTextField endpointURL;

	private int tries;
	private Float trialError;
	private Float averageError;

	public AveragesProject2_4(int x, int y, int width, int height) {
		this.x = x;
		this.y = y;
		this.width = width;
		this.height = height;
		this.tries = 0;
		this.trialError = 0.0f;
		this.averageError = 0.0f;

		data = "";
		labelPrediction = new JLabel("Prediction: ");
		endpointURL = new JTextField();
		labelAverageFormula = new JLabel("Average By Formula:");
		labelTrialError = new JLabel("Trial Error:");
		labelAverageError = new JLabel("Average Error:");
		labelTries = new JLabel("Tries:");
	}

	public float formula(float A, float B, float C, float D) {
		float average = A + B + C + D / 4;
		return average;
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
			pred = pred.replace("\\\"", "");

		} catch (IOException e) {
			e.printStackTrace();
		}

		return pred;
	}

	private void generatePanelContent() {

		// set panel configuration
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(this.x, this.y, this.width, this.height);
		setTitle("Sample JAVA program");
		contentPane = new JPanel();
		setContentPane(contentPane);
		contentPane.setLayout(new GridLayout(labelNames.length + 6, 2));

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
		contentPane.add(labelPrediction);
		contentPane.add(new JLabel(""));
		contentPane.add(labelAverageFormula);
		contentPane.add(new JLabel(""));
		contentPane.add(labelTries);
		contentPane.add(new JLabel(""));
		contentPane.add(labelTrialError);
		contentPane.add(new JLabel(""));
		contentPane.add(labelAverageError);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		float arr[] = new float[labelNames.length];
		// getting data from text fields and making JSON
		data = "";
		data += "{";
		for (int i = 0; i < labelNames.length; i++) {
			arr[i] = Float.valueOf(userInput.get(labelNames[i] + "Input").getText());
			data += "\"" + labelNames[i] + "\":\"" + userInput.get(labelNames[i] + "Input").getText() + "\"";
			if (i != labelNames.length - 1) {
				data += ",";
			}
		}
		data += "}";
		tries += 1;
		Float averageByFormla = formula(arr[0], arr[1], arr[2], arr[3]);
		labelAverageFormula.setText("Average by Formula: " + Float.toString(averageByFormla));
		// gives user back prediction in GUI
		Float currentPrediction = Float.valueOf(makePrediction());
		trialError = Math.abs(currentPrediction - averageByFormla);
		averageError = (averageError + trialError) / (float) tries;

		labelPrediction.setText("Prediction: " + Float.toString(currentPrediction));
		labelTrialError.setText("Trail Error: " + Float.toString(trialError));
		labelAverageError.setText("Average Error: " + Float.toString(averageError));
		labelTries.setText("Tries: " + Integer.toString(tries));
	}

	public static void main(String[] args) {
		AveragesProject2_4 Averages = new AveragesProject2_4(0, 0, 1600, 600);
		Averages.generatePanelContent();
		Averages.setVisible(true);
	}

}
