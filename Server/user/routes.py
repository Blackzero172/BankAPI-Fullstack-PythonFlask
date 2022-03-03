from __main__ import app
from .user import User
from flask import jsonify, request


@app.route("/")
def getAllUsers():
    try:
        usersList = []
        for user in User.objects:
            usersList.append(user._data)
    except Exception as e:
        return str(e), 500
    return jsonify(usersList)


@app.route("/", methods=["POST"])
def addUser():
    try:
        reqBody = request.get_json()
        name, email = reqBody["name"], reqBody["email"]
        balance = reqBody.get("balance") or 0
        credit = reqBody.get("credit") or 0
        user = User(
            name=name,
            email=email.lower(),
            balance=balance,
            credit=credit,
        )
        user.save()
    except Exception as e:
        return str(e), 500
    return jsonify(user._data)


@app.route("/deposit", methods=["POST"])
def deposit():
    try:
        reqBody = request.get_json()
        amount, email = reqBody["amount"], reqBody["email"].lower()
        user = User.objects(email=email)[0]
        if not bool(user):
            return "User not found", 404
        user["balance"] += amount
        user.save()
    except Exception as e:
        return str(e), 500
    return jsonify(user._data)


@app.route("/withdraw", methods=["POST"])
def withdraw():
    try:
        reqBody = request.get_json()
        amount, email = reqBody["amount"], reqBody["email"].lower()
        user = User.objects(email=email)[0]
        if not bool(user):
            return "User not found", 404
        if user["balance"] > amount:
            user["balance"] -= amount
        else:
            return "Not enough balance", 400
        user.save()
    except Exception as e:
        return str(e), 500
    return jsonify(user._data)


@app.route("/credit", methods=["POST"])
def setCredit():
    try:
        reqBody = request.get_json()
        amount, email = reqBody["amount"], reqBody["email"].lower()
        user = User.objects(email=email)[0]
        if not bool(user):
            return "User not found", 404
        user["credit"] = amount
        user.save()
    except Exception as e:
        return str(e), 500
    return jsonify(user._data)


@app.route("/transfer", methods=["POST"])
def transfer():
    try:
        reqBody = request.get_json()
        amount, email, targetEmail = reqBody["amount"], reqBody["email"].lower(
        ), reqBody["targetEmail"].lower()

        user = User.objects(email=email)[0]
        targetUser = User.objects(email=targetEmail)[0]
        if not bool(user):
            return "User not found", 404
        if not bool(targetUser):
            return "Target User not Found", 404
        if user["balance"] >= amount:
            user["balance"] -= amount
            targetUser["balance"] += amount
        else:
            return "Not enough balance", 400
        user.save()
        targetUser.save()
    except Exception as e:
        return str(e), 500
    return jsonify(user._data, targetUser._data)
