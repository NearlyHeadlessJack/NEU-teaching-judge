from playwright.sync_api import Playwright, sync_playwright
import sys

id =sys.argv[1]
password = sys.argv[2]
name=sys.argv[3]



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://219.216.96.4/
    page.goto("http://219.216.96.4/")

    # Go to https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2F219.216.96.4%2Feams%2FhomeExt.action%3Bjsessionid%3DD327BE796A80AFEBECAC5F31D6CFF366.std10
    page.goto("https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2F219.216.96.4%2Feams%2FhomeExt.action%3Bjsessionid%3DD327BE796A80AFEBECAC5F31D6CFF366.std10")

    # Click [placeholder="工资号/学号"]
    page.click("[placeholder=\"工资号/学号\"]")

    # Fill [placeholder="工资号/学号"]
    page.fill("[placeholder=\"工资号/学号\"]", id)

    # Click [placeholder="输入密码"]
    page.click("[placeholder=\"输入密码\"]")



    # Fill [placeholder="输入密码"]
    page.fill("[placeholder=\"输入密码\"]", password)

    # Click input[type="button"]
    page.click("input[type=\"button\"]")
    # assert page.url == "http://219.216.96.4/eams/homeExt.action;jsessionid=D327BE796A80AFEBECAC5F31D6CFF366.std10"

    # Click text=量化评教
    page.click("text=量化评教")

    # Click text=学生评教
    # with page.expect_navigation(url="http://219.216.96.4/eams/quality/stdEvaluate.action"):
    with page.expect_navigation():
        page.click("text=学生评教")

    # Click text=林明秀(进行评教)
    # with page.expect_navigation(url="http://219.216.96.4/eams/quality/stdEvaluate!answer.action?evaluationLesson.id=22493&teacher.id=8489"):
    with page.expect_navigation():
        page.click("text="+name+"(进行评教)")

    # Fill input[name="option61"]
    page.fill("input[name=\"option61\"]", "0")

    # Click input[name="option61"]
    page.click("input[name=\"option61\"]")

    # Fill input[name="option62"]
    page.fill("input[name=\"option62\"]", "0")

    # Click input[name="option62"]
    page.click("input[name=\"option62\"]")

    # Fill input[name="option63"]
    page.fill("input[name=\"option63\"]", "0")

    # Click input[name="option63"]
    page.click("input[name=\"option63\"]")

    # Fill input[name="option64"]
    page.fill("input[name=\"option64\"]", "0")

    # Click input[name="option64"]
    page.click("input[name=\"option64\"]")

    # Fill input[name="option65"]
    page.fill("input[name=\"option65\"]", "0")

    # Click input[name="option65"]
    page.click("input[name=\"option65\"]")

    # Fill input[name="option66"]
    page.fill("input[name=\"option66\"]", "0")

    # Click input[name="option66"]
    page.click("input[name=\"option66\"]")

    # Fill input[name="option67"]
    page.fill("input[name=\"option67\"]", "0")

    # Click input[name="option67"]
    page.click("input[name=\"option67\"]")

    # Fill input[name="option68"]
    page.fill("input[name=\"option68\"]", "0")

    # Click input[name="option68"]
    page.click("input[name=\"option68\"]")

    # Fill input[name="option69"]
    page.fill("input[name=\"option69\"]", "0")

    # Click input[name="option69"]
    page.click("input[name=\"option69\"]")

    # Fill input[name="option70"]
    page.fill("input[name=\"option70\"]", "0")

    # Click input[name="option70"]
    page.click("input[name=\"option70\"]")

    # Fill input[name="option71"]
    page.fill("input[name=\"option71\"]", "0")

    # Click input[name="option71"]
    page.click("input[name=\"option71\"]")

    # Click textarea
    page.click("textarea")

    # Fill textarea
    page.fill("textarea", "tebiehao")

    # Click text=提交
    page.once("dialog", lambda dialog: dialog.dismiss())
    # with page.expect_navigation(url="http://219.216.96.4/eams/quality/stdEvaluate!innerIndex.action?"):
    with page.expect_navigation():
        page.click("text=提交")
        page.press("body", "Enter")
    # assert page.url == "http://219.216.96.4/eams/quality/stdEvaluate!answer.action?evaluationLesson.id=22493&teacher.id=8489"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
