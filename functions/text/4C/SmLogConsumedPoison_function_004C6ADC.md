# SmLogConsumedPoison

- RVA: `0x004C6ADC`–`0x004C6AF7` (길이 `27` bytes)
- VA: `0x00000001404C6ADC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004C6AEC` → [MmStoreLogConsumedPoison](MmStoreLogConsumedPoison_function_004C6B00.md) (function, `0x004C6B00`)

### Direct callers
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStLockVirtualRegion](../4E/SMKM_STORE_SM_TRAITS_SmStLockVirtualRegion_function_004EAF8C.md) at `0x004EB0BF`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmPageError](../60/ST_STORE_SM_TRAITS_StDmPageError_function_0060DDDC.md) at `0x0060DEDF`

### Static image references
- `0x004C6AE5` → RVA `0x00E28900` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C6ADC  48 83 EC 28                     sub rsp, 0x28
004C6AE0  4D 85 C0                        test r8, r8
004C6AE3  75 07                           jne 0x1404c6aec
004C6AE5  F0 FF 05 14 1E 96 00            lock inc dword ptr [rip + 0x961e14]
004C6AEC  E8 0F 00 00 00                  call 0x1404c6b00
004C6AF1  48 83 C4 28                     add rsp, 0x28
004C6AF5  C3                              ret
004C6AF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmLogConsumedPoison(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 == 0) {
    }
    result = MmStoreLogConsumedPoison(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SmLogConsumedPoison(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 == 0) {
    }
    result = MmStoreLogConsumedPoison(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C6ADC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C6ADC[BB_004C6ADC]
  bb_004C6AE5[BB_004C6AE5]
  bb_004C6AEC[BB_004C6AEC]
  bb_004C6AF6[BB_004C6AF6]
  bb_004C6ADC -->|branch| bb_004C6AEC
  bb_004C6ADC -->|fallthrough| bb_004C6AE5
  bb_004C6AE5 -->|flow| bb_004C6AEC
```
