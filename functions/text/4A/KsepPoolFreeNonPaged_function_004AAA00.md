# KsepPoolFreeNonPaged

- RVA: `0x004AAA00`–`0x004AAA20` (길이 `32` bytes)
- VA: `0x00000001404AAA00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004AAA0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [KsepCompletionSafeWrapper](KsepCompletionSafeWrapper_function_004AA950.md) at `0x004AA9B2`
- [KseShimDriverIoCallbacks](../../page/95/KseShimDriverIoCallbacks_function_00958BFC.md) at `0x00958CF5`

### Static image references
- `0x004AAA13` → RVA `0x00F1016C` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004AAA0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AAA00  48 83 EC 28                     sub rsp, 0x28
004AAA04  48 85 C9                        test rcx, rcx
004AAA07  74 11                           je 0x1404aaa1a
004AAA09  BA 4B 53 45 62                  mov edx, 0x6245534b
004AAA0E  E8 5D 7E 6D 00                  call 0x140b82870
004AAA13  F0 FF 05 52 57 A6 00            lock inc dword ptr [rip + 0xa65752]
004AAA1A  48 83 C4 28                     add rsp, 0x28
004AAA1E  C3                              ret
004AAA1F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepPoolFreeNonPaged(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) {
        a2 = 0x6245534BULL;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepPoolFreeNonPaged(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) {
        a2 = 0x6245534BULL;
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AAA00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AAA00[BB_004AAA00]
  bb_004AAA09[BB_004AAA09]
  bb_004AAA1A[BB_004AAA1A]
  bb_004AAA1F[BB_004AAA1F]
  bb_004AAA00 -->|branch| bb_004AAA1A
  bb_004AAA00 -->|fallthrough| bb_004AAA09
  bb_004AAA09 -->|flow| bb_004AAA1A
```
