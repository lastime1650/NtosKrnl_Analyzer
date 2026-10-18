# SymCryptWipe

- RVA: `0x0051F914`–`0x0051F923` (길이 `15` bytes)
- VA: `0x000000014051F914`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **47**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0051F918` → [SymCryptWipeAsm](SymCryptWipeAsm_function_0051F250.md) (function, `0x0051F250`)

### Direct callers
- [SymCryptSha256Result](SymCryptSha256Result_function_0051E2F0.md) at `0x0051E341`
- [SymCryptSha256Result](SymCryptSha256Result_function_0051E2F0.md) at `0x0051E368`
- [SymCryptSha256Result](SymCryptSha256Result_function_0051E2F0.md) at `0x0051E3BC`
- [SymCryptParallelSha256Result1](SymCryptParallelSha256Result1_function_0051F0D0.md) at `0x0051F107`
- [SymCryptParallelSha256Result2](SymCryptParallelSha256Result2_function_0051F160.md) at `0x0051F18A`
- [SymCryptParallelSha256ResultDone](SymCryptParallelSha256ResultDone_function_0051F1E0.md) at `0x0051F21A`
- [SymCryptParallelHashProcess](../52/SymCryptParallelHashProcess_function_00521BF4.md) at `0x00521E8A`
- [SymCryptParallelHashProcess_serial](../52/SymCryptParallelHashProcess_serial_function_00521EB8.md) at `0x00521F04`
- [SymCryptRsakeyCreate](../52/SymCryptRsakeyCreate_function_00523594.md) at `0x00523603`
- [SymCryptRsakeyFree](../52/SymCryptRsakeyFree_function_00523844.md) at `0x00523850`
- [SymCryptRsakeySetValueInternal](../52/SymCryptRsakeySetValueInternal_function_005238D4.md) at `0x00523F9D`
- [SymCryptRsakeyWipe](../52/SymCryptRsakeyWipe_function_00523FCC.md) at `0x00523FD3`
- [SymCryptEcurveAllocate](../52/SymCryptEcurveAllocate_function_00524074.md) at `0x00524106`
- [SymCryptEcurveFree](../52/SymCryptEcurveFree_function_0052417C.md) at `0x00524188`
- [SymCryptEcurveInitialize](../52/SymCryptEcurveInitialize_function_005241A4.md) at `0x0052470C`
- [SymCryptEckeySetValue](../52/SymCryptEckeySetValue_function_00524C34.md) at `0x005250E0`
- [SymCryptEckeyWipe](../52/SymCryptEckeyWipe_function_005250F8.md) at `0x0052510F`
- [SymCryptRsaPkcs1CheckSignaturePadding](../52/SymCryptRsaPkcs1CheckSignaturePadding_function_005252A8.md) at `0x005252E2`
- [SymCryptIntFree](../52/SymCryptIntFree_function_005255C8.md) at `0x005255D4`
- [SymCryptIntWipe](../52/SymCryptIntWipe_function_00525850.md) at `0x00525857`
- [SymCryptEcDsaSignEx](../52/SymCryptEcDsaSignEx_function_00525D6C.md) at `0x005262D9`
- [SymCryptEcDsaSignEx](../52/SymCryptEcDsaSignEx_function_00525D6C.md) at `0x00526301`
- [SymCryptEcDsaVerify](../52/SymCryptEcDsaVerify_function_00526400.md) at `0x0052698A`
- [SymCryptRsaPkcs1Sign](../52/SymCryptRsaPkcs1Sign_function_005271A0.md) at `0x005272CC`
- [SymCryptRsaPkcs1Verify](../52/SymCryptRsaPkcs1Verify_function_005272FC.md) at `0x0052741E`
- [SymCryptSha512AppendBlocks_ull](../52/SymCryptSha512AppendBlocks_ull_function_00527624.md) at `0x00528A8C`
- [SymCryptSha512Result](../52/SymCryptSha512Result_function_00528B40.md) at `0x00528B85`
- [SymCryptSha512Result](../52/SymCryptSha512Result_function_00528B40.md) at `0x00528BAC`
- [SymCryptSha512Result](../52/SymCryptSha512Result_function_00528B40.md) at `0x00528C1B`
- [SymCryptSha1Result](../52/SymCryptSha1Result_function_00529EA0.md) at `0x00529F65`
- [SymCryptMd5Result](../52/SymCryptMd5Result_function_0052A8B0.md) at `0x0052A8DF`
- [SymCryptRsaSelftest](../52/SymCryptRsaSelftest_function_0052B638.md) at `0x0052B802`
- [SymCryptHashCommonPaddingMd4Style](../52/SymCryptHashCommonPaddingMd4Style_function_0052D2F0.md) at `0x0052D338`
- [SymCryptHashCommonPaddingMd4Style](../52/SymCryptHashCommonPaddingMd4Style_function_0052D2F0.md) at `0x0052D367`
- [SymCryptFdefIntAddMixedSize](../52/SymCryptFdefIntAddMixedSize_function_0052D41C.md) at `0x0052D4F8`
- [SymCryptFdefIntDivMod](../52/SymCryptFdefIntDivMod_function_0052D568.md) at `0x0052D5F3`
- [SymCryptFdefIntDivMod](../52/SymCryptFdefIntDivMod_function_0052D568.md) at `0x0052D61B`
- [SymCryptFdefIntDivPow2](../52/SymCryptFdefIntDivPow2_function_0052D63C.md) at `0x0052D702`
- [SymCryptFdefIntMulMixedSize](../52/SymCryptFdefIntMulMixedSize_function_0052D88C.md) at `0x0052D907`
- [SymCryptFdefRawDivMod](../52/SymCryptFdefRawDivMod_function_0052DC30.md) at `0x0052DC83`
- [SymCryptFdefRawDivMod](../52/SymCryptFdefRawDivMod_function_0052DC30.md) at `0x0052DCB7`
- [SymCryptFdefRawDivMod](../52/SymCryptFdefRawDivMod_function_0052DC30.md) at `0x0052DD32`
- [SymCryptFdefRawDivMod](../52/SymCryptFdefRawDivMod_function_0052DC30.md) at `0x0052DE60`
- [SymCryptFdefModElementSetValueNegUint32](../53/SymCryptFdefModElementSetValueNegUint32_function_005346F4.md) at `0x00534757`
- [SymCryptFdefModElementSetValueUint32Generic](../53/SymCryptFdefModElementSetValueUint32Generic_function_005347C0.md) at `0x00534820`
- [SymCryptFdefModElementToIntGeneric](../53/SymCryptFdefModElementToIntGeneric_function_00534844.md) at `0x00534886`
- [SymCryptFdefModInvMontgomery](../53/SymCryptFdefModInvMontgomery_function_00534C40.md) at `0x00534C82`
- [SymCryptFdefModInvMontgomery](../53/SymCryptFdefModInvMontgomery_function_00534C40.md) at `0x00534C9A`
- [SymCryptFdefModInvMontgomery256](../53/SymCryptFdefModInvMontgomery256_function_00534CF0.md) at `0x00534D2E`
- [SymCryptFdefModInvMontgomery256](../53/SymCryptFdefModInvMontgomery256_function_00534CF0.md) at `0x00534D4A`
- [SymCryptFdefModPreGetMontgomery](../53/SymCryptFdefModPreGetMontgomery_function_00535020.md) at `0x00535059`
- [SymCryptFdefModSetRandomGeneric](../53/SymCryptFdefModSetRandomGeneric_function_00535180.md) at `0x0053523D`
- [SymCryptFdefModSetRandomGeneric](../53/SymCryptFdefModSetRandomGeneric_function_00535180.md) at `0x0053527D`
- [SymCryptFdefModulusInitMontgomeryInternal](../53/SymCryptFdefModulusInitMontgomeryInternal_function_00535600.md) at `0x00535651`
- [SymCryptFdefIntCopyMixedSize](../53/SymCryptFdefIntCopyMixedSize_function_00535AB8.md) at `0x00535B1B`
- [SymCryptFdefIntSetValueUint32](../53/SymCryptFdefIntSetValueUint32_function_00535D38.md) at `0x00535D51`
- [SymCryptFdefIntSetValueUint64](../53/SymCryptFdefIntSetValueUint64_function_00535D6C.md) at `0x00535D8B`
- [SymCryptFdef369ModInvMontgomery](../53/SymCryptFdef369ModInvMontgomery_function_00537470.md) at `0x005374B7`
- [SymCryptFdef369ModInvMontgomery](../53/SymCryptFdef369ModInvMontgomery_function_00537470.md) at `0x005374CF`
- [SymCryptFdef369ModPreGetMontgomery](../53/SymCryptFdef369ModPreGetMontgomery_function_00537590.md) at `0x005375D9`
- [SymCryptFdef369ModPreGetMontgomery](../53/SymCryptFdef369ModPreGetMontgomery_function_00537590.md) at `0x005375F7`
- [SymCryptEcDhSecretAgreement](../53/SymCryptEcDhSecretAgreement_function_00537798.md) at `0x00537954`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0051F914  48 83 EC 28                     sub rsp, 0x28
0051F918  E8 33 F9 FF FF                  call 0x14051f250
0051F91D  48 83 C4 28                     add rsp, 0x28
0051F921  C3                              ret
0051F922  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptWipe(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = SymCryptWipeAsm(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void SymCryptWipe(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = SymCryptWipeAsm(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0051F914&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0051F914[BB_0051F914]
  bb_0051F922[BB_0051F922]
```
