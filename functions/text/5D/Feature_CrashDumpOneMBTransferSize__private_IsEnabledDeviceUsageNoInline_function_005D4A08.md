# Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline

- RVA: `0x005D4A08`–`0x005D4A3A` (길이 `50` bytes)
- VA: `0x00000001405D4A08`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005D4A2F` → [Feature_CrashDumpOneMBTransferSize__private_IsEnabledFallback](Feature_CrashDumpOneMBTransferSize__private_IsEnabledFallback_function_005D4A40.md) (function, `0x005D4A40`)

### Direct callers
- [PopHiberInitializeResources](../../page/75/PopHiberInitializeResources_function_0075D5FC.md) at `0x0075D6DC`
- [PopPreallocateHibernateMemory](../../page/75/PopPreallocateHibernateMemory_function_0075DB98.md) at `0x0075DC44`
- [PopAllocateHiberContext](../../page/AD/PopAllocateHiberContext_function_00ADC05C.md) at `0x00ADC6AC`
- [PopHiberCheckResume](../../pagelk/B6/PopHiberCheckResume_function_00B6D840.md) at `0x00B6DA09`
- [PopSaveHiberContext](../../pagelk/B6/PopSaveHiberContext_function_00B6F050.md) at `0x00B6F0BF`
- [PopSaveHiberContext](../../pagelk/B6/PopSaveHiberContext_function_00B6F050.md) at `0x00B6F53A`
- [PopWriteHiberPages](../../pagelk/B6/PopWriteHiberPages_function_00B6FF78.md) at `0x00B7008D`
- [PopWriteHiberPages](../../pagelk/B6/PopWriteHiberPages_function_00B6FF78.md) at `0x00B70123`
- [MmInvalidateDumpAddresses](../../pagelk/B7/MmInvalidateDumpAddresses_function_00B74970.md) at `0x00B749CB`
- [MiInitSystem](../../init/C5/MiInitSystem_function_00C5E6C0.md) at `0x00C5E743`

### Static image references
- `0x005D4A12` → RVA `0x00FC4940` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D4A08  48 83 EC 28                     sub rsp, 0x28
005D4A0C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005D4A12  8B 05 28 FF 9E 00               mov eax, dword ptr [rip + 0x9eff28]
005D4A18  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005D4A1C  A8 10                           test al, 0x10
005D4A1E  74 05                           je 0x1405d4a25
005D4A20  83 E0 01                        and eax, 1
005D4A23  EB 0F                           jmp 0x1405d4a34
005D4A25  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005D4A2A  BA 03 00 00 00                  mov edx, 3
005D4A2F  E8 0C 00 00 00                  call 0x1405d4a40
005D4A34  48 83 C4 28                     add rsp, 0x28
005D4A38  C3                              ret
005D4A39  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10420008)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10420008)))) & (16)) == 0) goto loc_005D4A25;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10420008))) & (1));
    goto loc_005D4A34;
loc_005D4A25:
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005D4A34:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9EFF28)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9EFF28)))) & (16)) == 0) goto loc_005D4A25;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9EFF28))) & (1));
    goto loc_005D4A34;
loc_005D4A25:
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005D4A34:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D4A08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D4A08[BB_005D4A08]
  bb_005D4A20[BB_005D4A20]
  bb_005D4A25[BB_005D4A25]
  bb_005D4A34[BB_005D4A34]
  bb_005D4A39[BB_005D4A39]
  bb_005D4A08 -->|branch| bb_005D4A25
  bb_005D4A08 -->|fallthrough| bb_005D4A20
  bb_005D4A20 -->|branch| bb_005D4A34
  bb_005D4A25 -->|flow| bb_005D4A34
```
