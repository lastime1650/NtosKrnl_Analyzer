# ViDeadlockDetectionTryConvertSharedToExclusive

- RVA: `0x00615F98`–`0x00615FC2` (길이 `42` bytes)
- VA: `0x0000000140615F98`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00615FA3` → [ExTryConvertSharedSpinLockExclusive](../2E/ExTryConvertSharedSpinLockExclusive_function_002EF4C0.md) (function, `0x002EF4C0`)

### Direct callers
- [ViDeadlockRemoveMemoryRangeResources](ViDeadlockRemoveMemoryRangeResources_function_00615FE8.md) at `0x006160A6`
- [ViDeadlockRemoveMemoryRangeThreads](ViDeadlockRemoveMemoryRangeThreads_function_00616148.md) at `0x00616203`

### Static image references
- `0x00615F9C` → RVA `0x00F04060` (`.data`; read)
- `0x00615FB5` → RVA `0x00F04020` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00615F98  48 83 EC 28                     sub rsp, 0x28
00615F9C  48 8D 0D BD E0 8E 00            lea rcx, [rip + 0x8ee0bd]
00615FA3  E8 18 95 CD FF                  call 0x1402ef4c0
00615FA8  85 C0                           test eax, eax
00615FAA  74 10                           je 0x140615fbc
00615FAC  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00615FB5  48 89 0D 64 E0 8E 00            mov qword ptr [rip + 0x8ee064], rcx
00615FBC  48 83 C4 28                     add rsp, 0x28
00615FC0  C3                              ret
00615FC1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViDeadlockDetectionTryConvertSharedToExclusive(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExTryConvertSharedSpinLockExclusive(v_rip + 9363645, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        *(unsigned __int64 *)(v_rip + 9363556) = a1;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void ViDeadlockDetectionTryConvertSharedToExclusive(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExTryConvertSharedSpinLockExclusive(v_rip + 9363645, a2, a3, a4);
    if ((uint32_t)(result) != 0) {
        a1 = *(uint64_t *)(gs_base + (0 + 0x188));
        *(uint64_t *)(v_rip + 0x8EE064) = a1;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00615F98&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00615F98[BB_00615F98]
  bb_00615FAC[BB_00615FAC]
  bb_00615FBC[BB_00615FBC]
  bb_00615FC1[BB_00615FC1]
  bb_00615F98 -->|branch| bb_00615FBC
  bb_00615F98 -->|fallthrough| bb_00615FAC
  bb_00615FAC -->|flow| bb_00615FBC
```
