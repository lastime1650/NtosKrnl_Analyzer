# Feature_AntiStarvationThreadBoostCountVariable__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F5BFC`–`0x004F5C2E` (길이 `50` bytes)
- VA: `0x00000001404F5BFC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F5C23` → [Feature_AntiStarvationThreadBoostCountVariable__private_IsEnabledFallback](Feature_AntiStarvationThreadBoostCountVariable__private_IsEnabledFallback_function_004F5CDC.md) (function, `0x004F5CDC`)

### Direct callers
- [KiInitializeAntiStarvationPolicies](KiInitializeAntiStarvationPolicies_function_004F5B5C.md) at `0x004F5BCF`
- [KiInitializeVelocity](../../init/BE/KiInitializeVelocity_function_00BEEDB8.md) at `0x00BEEE43`

### Static image references
- `0x004F5C06` → RVA `0x00FC48D0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F5BFC  48 83 EC 28                     sub rsp, 0x28
004F5C00  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F5C06  8B 05 C4 EC AC 00               mov eax, dword ptr [rip + 0xacecc4]
004F5C0C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F5C10  A8 10                           test al, 0x10
004F5C12  74 05                           je 0x1404f5c19
004F5C14  83 E0 01                        and eax, 1
004F5C17  EB 0F                           jmp 0x1404f5c28
004F5C19  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F5C1E  BA 03 00 00 00                  mov edx, 3
004F5C23  E8 B4 00 00 00                  call 0x1404f5cdc
004F5C28  48 83 C4 28                     add rsp, 0x28
004F5C2C  C3                              ret
004F5C2D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_AntiStarvationThreadBoostCountVariable__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11332804)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11332804)))) & (16)) == 0) goto loc_004F5C19;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11332804))) & (1));
    goto loc_004F5C28;
loc_004F5C19:
    result = Feature_AntiStarvationThreadBoostCountVariable__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5C28:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_AntiStarvationThreadBoostCountVariable__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACECC4)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACECC4)))) & (16)) == 0) goto loc_004F5C19;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACECC4))) & (1));
    goto loc_004F5C28;
loc_004F5C19:
    result = Feature_AntiStarvationThreadBoostCountVariable__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5C28:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F5BFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F5BFC[BB_004F5BFC]
  bb_004F5C14[BB_004F5C14]
  bb_004F5C19[BB_004F5C19]
  bb_004F5C28[BB_004F5C28]
  bb_004F5C2D[BB_004F5C2D]
  bb_004F5BFC -->|branch| bb_004F5C19
  bb_004F5BFC -->|fallthrough| bb_004F5C14
  bb_004F5C14 -->|branch| bb_004F5C28
  bb_004F5C19 -->|flow| bb_004F5C28
```
