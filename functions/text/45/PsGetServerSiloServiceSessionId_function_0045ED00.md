# PsGetServerSiloServiceSessionId

- RVA: `0x0045ED00`–`0x0045ED20` (길이 `32` bytes)
- VA: `0x000000014045ED00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **23**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PnpNotifyTargetDeviceChangeNotifyEntry](../../page/72/PnpNotifyTargetDeviceChangeNotifyEntry_function_00729D54.md) at `0x00729D84`
- [PspTerminateSiloSubsystemProcesses](../../page/78/PspTerminateSiloSubsystemProcesses_function_00780918.md) at `0x0078096E`
- [SepCopyClientTokenAndSetSilo](../../page/79/SepCopyClientTokenAndSetSilo_function_0079CE34.md) at `0x0079CE62`
- [CmpCheckOpenAccessOnKeyBody](../../page/87/CmpCheckOpenAccessOnKeyBody_function_00870000.md) at `0x00870783`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A020A`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A02E6`
- [IopDeviceInterfaceFilterCallback](../../page/8E/IopDeviceInterfaceFilterCallback_function_008E5410.md) at `0x008E54DD`
- [PiPnpRtlApplyMandatoryFilters](../../page/8E/PiPnpRtlApplyMandatoryFilters_function_008E5C80.md) at `0x008E5DF8`
- [PiPnpRtlApplyMandatoryDeviceFilters](../../page/8E/PiPnpRtlApplyMandatoryDeviceFilters_function_008E5E90.md) at `0x008E6100`
- [PiCMMandatoryFilterCallback](../../page/8E/PiCMMandatoryFilterCallback_function_008E6490.md) at `0x008E653E`
- [sub_008E6883](../../page/8E/Unknown_function_008E6883.md) at `0x008E6906`
- [PiCMValidateDeviceInstance](../../page/8E/PiCMValidateDeviceInstance_function_008E799C.md) at `0x008E7B2A`
- [PsIsServiceSession](../../page/91/PsIsServiceSession_function_00912FE4.md) at `0x00913016`
- [DbgkpSendErrorMessage](../../page/92/DbgkpSendErrorMessage_function_009210A8.md) at `0x0092116D`
- [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) at `0x00953897`
- [PnpNotifyDeviceClassChange](../../page/95/PnpNotifyDeviceClassChange_function_0095441C.md) at `0x009544FD`
- [PnpNotifyTargetDeviceChange](../../page/95/PnpNotifyTargetDeviceChange_function_00954790.md) at `0x00954864`
- [SeQuerySessionIdTokenEx](../../page/9E/SeQuerySessionIdTokenEx_function_009E7680.md) at `0x009E7721`
- [SepCopyAnonymousTokenAndSetSilo](../../page/A3/SepCopyAnonymousTokenAndSetSilo_function_00A3A510.md) at `0x00A3A64D`
- [SepCleanupLUIDDeviceMapDirectory](../../page/A9/SepCleanupLUIDDeviceMapDirectory_function_00A98F24.md) at `0x00A98FD4`
- [sub_00B16F66](../../page/B1/Unknown_function_00B16F66.md) at `0x00B17123`
- [sub_00B16F66](../../page/B1/Unknown_function_00B16F66.md) at `0x00B17209`
- [sub_00B26560](../../page/B2/Unknown_function_00B26560.md) at `0x00B265A4`
- [sub_00B2884E](../../page/B2/Unknown_function_00B2884E.md) at `0x00B288A8`
- [sub_00B316B4](../../page/B3/Unknown_function_00B316B4.md) at `0x00B31FC0`

### Static image references
- `0x0045ED00` → RVA `0x00FCF940` (`CACHEALI`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045ED00  48 8D 05 39 0C B7 00            lea rax, [rip + 0xb70c39]
0045ED07  48 85 C9                        test rcx, rcx
0045ED0A  75 0B                           jne 0x14045ed17
0045ED0C  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
0045ED13  8B 00                           mov eax, dword ptr [rax]
0045ED15  C3                              ret
0045ED16  CC                              int3
0045ED17  48 8B 81 E0 05 00 00            mov rax, qword ptr [rcx + 0x5e0]
0045ED1E  EB EC                           jmp 0x14045ed0c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetServerSiloServiceSessionId(__int64 a1)
{
    if (a1 != 0) goto loc_0045ED17;
loc_0045ED0C:
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11996217 + 1288)));
loc_0045ED17:
    goto loc_0045ED0C;
}
```

## 5. (Beta) C Style

```c
int64_t PsGetServerSiloServiceSessionId(int64_t Arg1)
{
    if (Arg1 != 0) goto loc_0045ED17;
loc_0045ED0C:
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB70C39 + 0x508)));
loc_0045ED17:
    goto loc_0045ED0C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045ED00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045ED00[BB_0045ED00]
  bb_0045ED0C[BB_0045ED0C]
  bb_0045ED16[BB_0045ED16]
  bb_0045ED17[BB_0045ED17]
  bb_0045ED00 -->|branch| bb_0045ED17
  bb_0045ED00 -->|fallthrough| bb_0045ED0C
  bb_0045ED16 -->|flow| bb_0045ED17
  bb_0045ED17 -->|branch| bb_0045ED0C
```
