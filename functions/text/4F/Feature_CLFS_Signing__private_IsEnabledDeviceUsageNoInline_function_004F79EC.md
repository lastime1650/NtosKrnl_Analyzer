# Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F79EC`–`0x004F7A1E` (길이 `50` bytes)
- VA: `0x00000001404F79EC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F7A13` → [Feature_CLFS_Signing__private_IsEnabledFallback](Feature_CLFS_Signing__private_IsEnabledFallback_function_004F7A24.md) (function, `0x004F7A24`)

### Direct callers
- [CmpStartRMLog](../../page/7F/CmpStartRMLog_function_007F0AFC.md) at `0x007F0C1F`
- [CmpStartRMLog](../../page/7F/CmpStartRMLog_function_007F0AFC.md) at `0x007F0CA9`
- [CmpStartCLFSLog](../../page/7F/CmpStartCLFSLog_function_007F7228.md) at `0x007F731F`
- [CmpStartCLFSLog](../../page/7F/CmpStartCLFSLog_function_007F7228.md) at `0x007F73A8`
- [CmpInitCmRM](../../page/87/CmpInitCmRM_function_0087C700.md) at `0x0087CA26`
- [CmpInitCmRM](../../page/87/CmpInitCmRM_function_0087C700.md) at `0x0087CB29`
- [CmpInitCmRM](../../page/87/CmpInitCmRM_function_0087C700.md) at `0x0087CBA8`

### Static image references
- `0x004F79F6` → RVA `0x00FC4CA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F79EC  48 83 EC 28                     sub rsp, 0x28
004F79F0  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F79F6  8B 05 A4 D2 AC 00               mov eax, dword ptr [rip + 0xacd2a4]
004F79FC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F7A00  A8 10                           test al, 0x10
004F7A02  74 05                           je 0x1404f7a09
004F7A04  83 E0 01                        and eax, 1
004F7A07  EB 0F                           jmp 0x1404f7a18
004F7A09  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F7A0E  BA 03 00 00 00                  mov edx, 3
004F7A13  E8 0C 00 00 00                  call 0x1404f7a24
004F7A18  48 83 C4 28                     add rsp, 0x28
004F7A1C  C3                              ret
004F7A1D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11326116)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11326116)))) & (16)) == 0) goto loc_004F7A09;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11326116))) & (1));
    goto loc_004F7A18;
loc_004F7A09:
    result = Feature_CLFS_Signing__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7A18:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACD2A4)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACD2A4)))) & (16)) == 0) goto loc_004F7A09;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACD2A4))) & (1));
    goto loc_004F7A18;
loc_004F7A09:
    result = Feature_CLFS_Signing__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7A18:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F79EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F79EC[BB_004F79EC]
  bb_004F7A04[BB_004F7A04]
  bb_004F7A09[BB_004F7A09]
  bb_004F7A18[BB_004F7A18]
  bb_004F7A1D[BB_004F7A1D]
  bb_004F79EC -->|branch| bb_004F7A09
  bb_004F79EC -->|fallthrough| bb_004F7A04
  bb_004F7A04 -->|branch| bb_004F7A18
  bb_004F7A09 -->|flow| bb_004F7A18
```
