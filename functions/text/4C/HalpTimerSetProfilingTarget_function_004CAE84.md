# HalpTimerSetProfilingTarget

- RVA: `0x004CAE84`–`0x004CAECA` (길이 `70` bytes)
- VA: `0x00000001404CAE84`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004CAE8B` → [HalpDisableInterrupts](../25/HalpDisableInterrupts_function_002521A0.md) (function, `0x002521A0`)

### Direct callers
- [EmonSetIntervalEnhanced](../55/EmonSetIntervalEnhanced_function_0055FDB0.md) at `0x0055FE66`
- [EmonSetIntervalOriginal](../55/EmonSetIntervalOriginal_function_0055FFB0.md) at `0x00560066`
- [Amd64SetInterval](../56/Amd64SetInterval_function_0056DB50.md) at `0x0056DC0D`

### Static image references
- `0x004CAE9C` → RVA `0x00FC21E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CAE84  48 83 EC 28                     sub rsp, 0x28
004CAE88  44 8B D9                        mov r11d, ecx
004CAE8B  E8 10 73 D8 FF                  call 0x1402521a0
004CAE90  65 44 8B 04 25 A4 01 00 00      mov r8d, dword ptr gs:[0x1a4]
004CAE99  45 8B C8                        mov r9d, r8d
004CAE9C  4C 8B 05 45 73 AF 00            mov r8, qword ptr [rip + 0xaf7345]
004CAEA3  4D 69 D1 28 01 00 00            imul r10, r9, 0x128
004CAEAA  43 83 64 02 14 00               and dword ptr [r10 + r8 + 0x14], 0
004CAEB0  47 89 5C 02 18                  mov dword ptr [r10 + r8 + 0x18], r11d
004CAEB5  43 89 54 02 10                  mov dword ptr [r10 + r8 + 0x10], edx
004CAEBA  43 89 54 02 1C                  mov dword ptr [r10 + r8 + 0x1c], edx
004CAEBF  84 C0                           test al, al
004CAEC1  74 01                           je 0x1404caec4
004CAEC3  FB                              sti
004CAEC4  48 83 C4 28                     add rsp, 0x28
004CAEC8  C3                              ret
004CAEC9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTimerSetProfilingTarget(int a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HalpDisableInterrupts(a1, a2, a3, a4);
    v_r10 = (v_r10) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))));
    *(unsigned int *)(v_r10 + *(unsigned __int64 *)(v_rip + 11498309) * 1 + 24) = (unsigned int)((unsigned int)(a1));
    *(unsigned int *)(v_r10 + *(unsigned __int64 *)(v_rip + 11498309) * 1 + 16) = a2;
    *(unsigned int *)(v_r10 + *(unsigned __int64 *)(v_rip + 11498309) * 1 + 28) = a2;
    if ((unsigned __int8)(result) != 0) {
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpTimerSetProfilingTarget(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HalpDisableInterrupts(Arg1, Arg2, a3, a4);
    local_r10 = (local_r10) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))));
    *(uint32_t *)(local_r10 + *(uint64_t *)(v_rip + 0xAF7345) * 1 + 0x18) = (uint32_t)((uint32_t)(Arg1));
    *(uint32_t *)(local_r10 + *(uint64_t *)(v_rip + 0xAF7345) * 1 + 0x10) = Arg2;
    *(uint32_t *)(local_r10 + *(uint64_t *)(v_rip + 0xAF7345) * 1 + 0x1C) = Arg2;
    if ((uint8_t)(result) != 0) {
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CAE84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CAE84[BB_004CAE84]
  bb_004CAEC3[BB_004CAEC3]
  bb_004CAEC4[BB_004CAEC4]
  bb_004CAEC9[BB_004CAEC9]
  bb_004CAE84 -->|branch| bb_004CAEC4
  bb_004CAE84 -->|fallthrough| bb_004CAEC3
  bb_004CAEC3 -->|flow| bb_004CAEC4
```
