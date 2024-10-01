import subprocess

if __name__ == "__main__":
    from behave.__main__ import main as behave_main
    behave_main(["--tags=@Regression", "--no-capture", "--no-capture-stderr", "-f",
                 "allure_behave.formatter:AllureFormatter", "-o", "../reports"])

    subprocess.run(["allure", "generate", "../reports", "--clean", "-o", "../reports/allure-report"])
