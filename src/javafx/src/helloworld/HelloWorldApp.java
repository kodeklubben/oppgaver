package helloworld;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class HelloWorldApp extends Application {

	public void start(Stage primaryStage) {
		Text helloWorldText = new Text("Hello world");
		helloWorldText.setLayoutX(10);
		helloWorldText.setLayoutY(50);
		Font font = Font.font("Arial", 36);
		helloWorldText.setFont(font);
		helloWorldText.setFill(Color.BLUE);

        Pane root = new Pane(helloWorldText);
        root.setPrefWidth(300);
        root.setPrefHeight(300);

        primaryStage.setScene(new Scene(root));
        primaryStage.show();
	}

	public static void main(String[] args) {
		launch(HelloWorldApp.class, args);
	}
}
