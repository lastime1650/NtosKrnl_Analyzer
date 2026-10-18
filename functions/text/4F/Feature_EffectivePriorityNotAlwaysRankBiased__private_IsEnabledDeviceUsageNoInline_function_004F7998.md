# Feature_EffectivePriorityNotAlwaysRankBiased__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F7998`–`0x004F79CA` (길이 `50` bytes)
- VA: `0x00000001404F7998`
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
- `0x004F79BF` → [Feature_EffectivePriorityNotAlwaysRankBiased__private_IsEnabledFallback](Feature_EffectivePriorityNotAlwaysRankBiased__private_IsEnabledFallback_function_004F79D0.md) (function, `0x004F79D0`)

### Direct callers
- [KiInitializeVelocity](../../init/BE/KiInitializeVelocity_function_00BEEDB8.md) at `0x00BEEE16`

### Static image references
- `0x004F79A2` → RVA `0x00FC48E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F7998  48 83 EC 28                     sub rsp, 0x28
004F799C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F79A2  8B 05 40 CF AC 00               mov eax, dword ptr [rip + 0xaccf40]
004F79A8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F79AC  A8 10                           test al, 0x10
004F79AE  74 05                           je 0x1404f79b5
004F79B0  83 E0 01                        and eax, 1
004F79B3  EB 0F                           jmp 0x1404f79c4
004F79B5  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F79BA  BA 03 00 00 00                  mov edx, 3
004F79BF  E8 0C 00 00 00                  call 0x1404f79d0
004F79C4  48 83 C4 28                     add rsp, 0x28
004F79C8  C3                              ret
004F79C9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_EffectivePriorityNotAlwaysRankBiased__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11325248)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11325248)))) & (16)) == 0) goto loc_004F79B5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11325248))) & (1));
    goto loc_004F79C4;
loc_004F79B5:
    result = Feature_EffectivePriorityNotAlwaysRankBiased__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F79C4:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_EffectivePriorityNotAlwaysRankBiased__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACCF40)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACCF40)))) & (16)) == 0) goto loc_004F79B5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACCF40))) & (1));
    goto loc_004F79C4;
loc_004F79B5:
    result = Feature_EffectivePriorityNotAlwaysRankBiased__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F79C4:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F7998&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F7998[BB_004F7998]
  bb_004F79B0[BB_004F79B0]
  bb_004F79B5[BB_004F79B5]
  bb_004F79C4[BB_004F79C4]
  bb_004F79C9[BB_004F79C9]
  bb_004F7998 -->|branch| bb_004F79B5
  bb_004F7998 -->|fallthrough| bb_004F79B0
  bb_004F79B0 -->|branch| bb_004F79C4
  bb_004F79B5 -->|flow| bb_004F79C4
```
