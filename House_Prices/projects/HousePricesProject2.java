import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;
import java.util.*;
import javax.swing.*;

public class HousePricesProject2 extends JFrame implements ActionListener {

	private JPanel contentPane;
	private String[] labelNames = { "longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms",
			"population", "households", "median_income", "<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN" };

	private String[] defaultValues = { "-122.23", "37.88", "41.0", "880.0", "129.0", "322.0", "126.0", "8.3252", "0",
			"0", "0", "1", "0" };

	private Map<String, JLabel> labels = new HashMap<>();
	private Map<String, JTextField> userInput = new HashMap<>();

	// x and y coordinates of panel, width and height of panel
	private int x, y, width, height;

	private String data;
	private JLabel prediction;
	private JTextField endpointURL;

	public HousePricesProject2(int x, int y, int width, int height) {
		this.x = x;
		this.y = y;
		this.width = width;
		this.height = height;
		data = "";
		prediction = new JLabel("Prediction: ");
		endpointURL = new JTextField();
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
		setTitle("House Prices Prediction Service (Project 2)");
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

	@Override
	public void actionPerformed(ActionEvent e) {
		// getting data from text fields and making JSON
		data = "";
		data += "{";
		for (int i = 0; i < labelNames.length; i++) {
			data += "\"" + labelNames[i] + "\":\"" + userInput.get(labelNames[i] + "Input").getText() + "\"";
			if (i != labelNames.length - 1) {
				data += ",";
			}
		}
		data += "}";

		// gives user back prediction in GUI
		prediction.setText("Prediction: " + makePrediction());
	}

	public static void main(String[] args) {
		HousePricesProject2 housePrices = new HousePricesProject2(0, 0, 400, 400);
		housePrices.generatePanelContent();
		housePrices.setVisible(true);
	}

}
