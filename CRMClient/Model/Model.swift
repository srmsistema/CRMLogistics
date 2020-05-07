//
//  Model.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 3/8/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.

import Foundation

struct DriverOrderStruct: Codable {
    let id: Int
    let volume: VolumeDr
    let numberOrderFromClient: Int
    let name: String
    let priceClient: Int
    let fromOrder: String
    //let dateOrderConclusion, toOrder, dateLoading, dateUnloading: JSONNull?
    let autoReleaseYear: Int
    let requirementsLoading: String
    let weight: Int
    let orderStatus: String
    let stateAwning, typeAuto, typeLoading, typeCargo: Int
    let weightMeasurementUnit, locationCargo, user: Int
    //let driver: JSONNull?
}

// MARK: - Volume
struct VolumeDr: Codable {
    let width, height, length, unit: Int
}

struct OrderStruct: Codable {
    let id: Int
    let volume: VolumeStruct
    let locationCargo, user, typeAuto, typeLoading: String
    let typeCargo, orderStatus: String
    let stateAwning: StateAwningStruct
    //let orderdriver = nullToNil(value:["driver"])
    let name: String
    let priceClient, companyProfit: Int
    //let fromOrder:NSNull
    //let fromOrder, toOrder, dateLoading, dateUnloading: NSNull?
    let autoReleaseYear: Int
    let requirementsLoading: String
    let weight, weightMeasurementUnit: Int
}

struct StateAwningStruct: Codable {
    let id: Int
    let noHoles, noGaps, dry, noPatches: Bool
}

struct VolumeStruct: Codable {
    let width, height, length, unit: Int
}


struct Profile: Codable {
    let user: ProfileInfo
    let first_name, last_name, gender, dateOfBirth: String
    let phone: String
    let photo: String
}

struct ProfileInfo: Codable {
    let id: Int
    let username, email: String
    let is_staff, is_active, is_client, is_driver: Bool
    let status, token: String
}

struct UserInfo: Codable {
    let user: User
    let first_name , last_name, gender, dateOfBirth, phone: String
}

struct TokenInfo: Codable {
    let user: Token
    let first_name,last_name, gender, dateOfBirth: String
    let phone: String
    
}

// MARK: - User
struct User: Codable {
    let username, email: String
    let password: String
}

struct Token: Codable{
    let username, email: String
    let token: String
}


struct LogInfo: Codable {
    let username, password: String
}

struct TokInfo: Codable {
    let username, token: String
}

// MARK: - CreateOrder
struct CreateOrder: Codable {
    var name: String
    var price_client: Int
    var requirements_loading: String
    var type_cargo, type_auto, auto_releaseyear, type_loading: Int
    var state_awning: StateAwning
    var weight, weight_measurementunit: Int
    var volume: Volume
    var location_cargo: LocationCargo
}

// MARK: - LocationCargo
struct LocationCargo: Codable {
    let address: String
}

// MARK: - StateAwning
struct StateAwning: Codable {
    let no_holes, no_gaps, dry, no_patches: Bool
}

// MARK: - Volume
struct Volume: Codable {
    let width, height, length, unit: Int
}

func nullToNil(value : Any?) -> Any? {
    if value is NSNull {
        return nil
    } else {
        return value
    }

}
