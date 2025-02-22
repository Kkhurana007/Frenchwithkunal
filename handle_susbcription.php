<?php
// Database connection details
$host = "localhost"; // Usually 'localhost' on GoDaddy
$dbname = "french_course_subscriptions"; // Your database name
$username = "french_user"; // Your database username
$password = "your_password"; // Your database password

// Connect to the database
try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $plan = $_POST['plan'];
    $user_id = $_POST['user_id']; // You can get this from a session or form
    $payment_status = 'pending'; // Default status
    $payment_amount = $_POST['payment_amount'];
    $transaction_id = $_POST['transaction_id']; // From payment gateway

    // Insert into the appropriate table
    switch ($plan) {
        case 'monthly':
            $stmt = $conn->prepare("INSERT INTO monthly_subscriptions (user_id, subscription_date, payment_status, payment_amount, payment_gateway_transaction_id) VALUES (:user_id, NOW(), :payment_status, :payment_amount, :transaction_id)");
            break;
        case 'yearly':
            $stmt = $conn->prepare("INSERT INTO yearly_subscriptions (user_id, subscription_date, payment_status, payment_amount, payment_gateway_transaction_id) VALUES (:user_id, NOW(), :payment_status, :payment_amount, :transaction_id)");
            break;
        case 'coaching':
            $stmt = $conn->prepare("INSERT INTO coaching_subscriptions (user_id, subscription_date, payment_status, payment_amount, payment_gateway_transaction_id) VALUES (:user_id, NOW(), :payment_status, :payment_amount, :transaction_id)");
            break;
        default:
            die("Invalid plan selected.");
    }

    // Execute the query
    $stmt->execute([
        ':user_id' => $user_id,
        ':payment_status' => $payment_status,
        ':payment_amount' => $payment_amount,
        ':transaction_id' => $transaction_id
    ]);

    echo "Subscription successful!";
}
?>