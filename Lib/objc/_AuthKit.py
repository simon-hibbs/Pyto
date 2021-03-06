"""
Classes from the 'AuthKit' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


AKRemoteDevice = _Class("AKRemoteDevice")
AKPromise = _Class("AKPromise")
AKAutoBugCapture = _Class("AKAutoBugCapture")
AKAppleIDAuthenticationDaemonInterface = _Class(
    "AKAppleIDAuthenticationDaemonInterface"
)
AKAuthorizationContext = _Class("AKAuthorizationContext")
AKAppleIDAuthenticationContext = _Class("AKAppleIDAuthenticationContext")
AKAppleIDAuthenticationCommandLineContext = _Class(
    "AKAppleIDAuthenticationCommandLineContext"
)
AKTrustedPhoneNumber = _Class("AKTrustedPhoneNumber")
_AKAnisetteProviderProxy = _Class("_AKAnisetteProviderProxy")
AKAnisetteProvisioningController = _Class("AKAnisetteProvisioningController")
AKUtilities = _Class("AKUtilities")
AKDevice = _Class("AKDevice")
AKAuthorizationNotificationService = _Class("AKAuthorizationNotificationService")
AKAuthorizationValidator = _Class("AKAuthorizationValidator")
AKAuthHandlerImpl = _Class("AKAuthHandlerImpl")
AKAuthorizationAppSignInDiscovery = _Class("AKAuthorizationAppSignInDiscovery")
AKBaseFollowupManager = _Class("AKBaseFollowupManager")
AKServerRequestConfiguration = _Class("AKServerRequestConfiguration")
AKNetworkObserver = _Class("AKNetworkObserver")
AKFollowUpSynchronizer = _Class("AKFollowUpSynchronizer")
AKAnisetteProvisioningDaemonInterface = _Class("AKAnisetteProvisioningDaemonInterface")
AKUsernameFormatter = _Class("AKUsernameFormatter")
AKCircleRequestContext = _Class("AKCircleRequestContext")
AKCDPFactory = _Class("AKCDPFactory")
AKCoordinatedDataBlock = _Class("AKCoordinatedDataBlock")
AKAbsintheSigner = _Class("AKAbsintheSigner")
AKIconContext = _Class("AKIconContext")
AKFollowUpServerPayloadFormatter = _Class("AKFollowUpServerPayloadFormatter")
AKFollowUpController = _Class("AKFollowUpController")
AKApplicationMetadataInfo = _Class("AKApplicationMetadataInfo")
AKAnisetteProvisioningClientInterface = _Class("AKAnisetteProvisioningClientInterface")
AKAnisetteData = _Class("AKAnisetteData")
AKAppleIDSession = _Class("AKAppleIDSession")
AKToken = _Class("AKToken")
AKMasterToken = _Class("AKMasterToken")
AKGrandSlamResponseHandler = _Class("AKGrandSlamResponseHandler")
AKAlertHandler = _Class("AKAlertHandler")
AKAuthorizationNotificationHandlerInterface = _Class(
    "AKAuthorizationNotificationHandlerInterface"
)
AKAccountRecoveryContext = _Class("AKAccountRecoveryContext")
AKFollowUpFactoryImpl = _Class("AKFollowUpFactoryImpl")
AKURLBag = _Class("AKURLBag")
AKCircleRequestPayload = _Class("AKCircleRequestPayload")
AKDeveloperTeam = _Class("AKDeveloperTeam")
AKAppleIDServerResourceLoadDelegate = _Class("AKAppleIDServerResourceLoadDelegate")
AKAuthorizationLoginChoice = _Class("AKAuthorizationLoginChoice")
AKAppleIDSigningDaemonInterface = _Class("AKAppleIDSigningDaemonInterface")
AKAccountManager = _Class("AKAccountManager")
AKCertificatePinning = _Class("AKCertificatePinning")
AKMediaServicesController = _Class("AKMediaServicesController")
AKDeviceListRequestContext = _Class("AKDeviceListRequestContext")
AKAppleIDSigningController = _Class("AKAppleIDSigningController")
AKConfiguration = _Class("AKConfiguration")
AKAppleIDAuthenticationClientInterface = _Class(
    "AKAppleIDAuthenticationClientInterface"
)
AKFollowUpProviderFactory = _Class("AKFollowUpProviderFactory")
AKCarrierBundleUtilities = _Class("AKCarrierBundleUtilities")
AKCarrierBundlePhoneCertificate = _Class("AKCarrierBundlePhoneCertificate")
AKAuthorizationPresenterHostInterface = _Class("AKAuthorizationPresenterHostInterface")
AKFollowUpTearDownContext = _Class("AKFollowUpTearDownContext")
AKAttestationSigner = _Class("AKAttestationSigner")
AKNativeAccountRecoveryController = _Class("AKNativeAccountRecoveryController")
AKDeviceListDeltaMessagePayload = _Class("AKDeviceListDeltaMessagePayload")
AKAppleIDAuthenticationContextManager = _Class("AKAppleIDAuthenticationContextManager")
AKAttestationData = _Class("AKAttestationData")
AKAuthorizationTVServicePresenter = _Class("AKAuthorizationTVServicePresenter")
AKAuthorizationStateBroadcastHandlerInterface = _Class(
    "AKAuthorizationStateBroadcastHandlerInterface"
)
AKConsentedApplication = _Class("AKConsentedApplication")
AKURLSession = _Class("AKURLSession")
AKURLDataTask = _Class("AKURLDataTask")
AKAppleIDAuthenticationController = _Class("AKAppleIDAuthenticationController")
_AKMessageForwarder = _Class("_AKMessageForwarder")
AKAdaptiveService = _Class("AKAdaptiveService")
AKAuthorizationUpgradeContext = _Class("AKAuthorizationUpgradeContext")
AKFLFollowUpController = _Class("AKFLFollowUpController")
AKCarouselAlertClientConnection = _Class("AKCarouselAlertClientConnection")
AKAuthorizationClientInterface = _Class("AKAuthorizationClientInterface")
AKUserInformation = _Class("AKUserInformation")
AKPasswordCredential = _Class("AKPasswordCredential")
AKAuthorizationScopesUserSelection = _Class("AKAuthorizationScopesUserSelection")
AKAuthorizationCredential = _Class("AKAuthorizationCredential")
AKCredentialRequest = _Class("AKCredentialRequest")
AKAuthorizationRequest = _Class("AKAuthorizationRequest")
AKPasswordRequest = _Class("AKPasswordRequest")
AKAuthorizationRevokeUpgradeContext = _Class("AKAuthorizationRevokeUpgradeContext")
AKAuthorizationPresentationContext = _Class("AKAuthorizationPresentationContext")
AKAuthorizationUserResponse = _Class("AKAuthorizationUserResponse")
AKAuthorizationCredentialStateRequest = _Class("AKAuthorizationCredentialStateRequest")
AKAuthorization = _Class("AKAuthorization")
AKCredentialRequestContext = _Class("AKCredentialRequestContext")
AKAuthorizationDaemonInterface = _Class("AKAuthorizationDaemonInterface")
AKAuthorizationDaemonConnection = _Class("AKAuthorizationDaemonConnection")
AKAuthorizationClientImpl = _Class("AKAuthorizationClientImpl")
AKAuthorizationController = _Class("AKAuthorizationController")
