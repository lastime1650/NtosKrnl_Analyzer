# Feature_Servicing_WaitForOutstandingWritesToComplete__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F5EDC`–`0x004F5F0E` (길이 `50` bytes)
- VA: `0x00000001404F5EDC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F5F03` → [Feature_Servicing_WaitForOutstandingWritesToComplete__private_IsEnabledFallback](Feature_Servicing_WaitForOutstandingWritesToComplete__private_IsEnabledFallback_function_004F5F14.md) (function, `0x004F5F14`)

### Direct callers
- [CmpDoFileWrite](../../page/A6/CmpDoFileWrite_function_00A65880.md) at `0x00A65AD3`

### Static image references
- `0x004F5EE6` → RVA `0x00FC4C98` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F5EDC  48 83 EC 28                     sub rsp, 0x28
004F5EE0  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F5EE6  8B 05 AC ED AC 00               mov eax, dword ptr [rip + 0xacedac]
004F5EEC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F5EF0  A8 10                           test al, 0x10
004F5EF2  74 05                           je 0x1404f5ef9
004F5EF4  83 E0 01                        and eax, 1
004F5EF7  EB 0F                           jmp 0x1404f5f08
004F5EF9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F5EFE  BA 03 00 00 00                  mov edx, 3
004F5F03  E8 0C 00 00 00                  call 0x1404f5f14
004F5F08  48 83 C4 28                     add rsp, 0x28
004F5F0C  C3                              ret
004F5F0D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_WaitForOutstandingWritesToComplete__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11333036)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11333036)))) & (16)) == 0) goto loc_004F5EF9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11333036))) & (1));
    goto loc_004F5F08;
loc_004F5EF9:
    result = Feature_Servicing_WaitForOutstandingWritesToComplete__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5F08:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_WaitForOutstandingWritesToComplete__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACEDAC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACEDAC)))) & (16)) == 0) goto loc_004F5EF9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACEDAC))) & (1));
    goto loc_004F5F08;
loc_004F5EF9:
    result = Feature_Servicing_WaitForOutstandingWritesToComplete__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5F08:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F5EDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F5EDC[BB_004F5EDC]
  bb_004F5EF4[BB_004F5EF4]
  bb_004F5EF9[BB_004F5EF9]
  bb_004F5F08[BB_004F5F08]
  bb_004F5F0D[BB_004F5F0D]
  bb_004F5EDC -->|branch| bb_004F5EF9
  bb_004F5EDC -->|fallthrough| bb_004F5EF4
  bb_004F5EF4 -->|branch| bb_004F5F08
  bb_004F5EF9 -->|flow| bb_004F5F08
```
