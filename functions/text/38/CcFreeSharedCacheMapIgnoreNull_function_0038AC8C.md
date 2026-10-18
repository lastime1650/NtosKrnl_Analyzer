# CcFreeSharedCacheMapIgnoreNull

- RVA: `0x0038AC8C`–`0x0038ACAC` (길이 `32` bytes)
- VA: `0x000000014038AC8C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0038ACA5` → [ExFreeToLookasideListEx](ExFreeToLookasideListEx_function_0038ACC0.md) (function, `0x0038ACC0`)

### Direct callers
- [CcDeleteSharedCacheMap](CcDeleteSharedCacheMap_function_0038A804.md) at `0x0038AAA8`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCBF2`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCCB9`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CD231`

### Static image references
- `0x0038AC9E` → RVA `0x00E11C60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0038AC8C  48 83 EC 28                     sub rsp, 0x28
0038AC90  48 85 C9                        test rcx, rcx
0038AC93  75 06                           jne 0x14038ac9b
0038AC95  48 83 C4 28                     add rsp, 0x28
0038AC99  C3                              ret
0038AC9A  CC                              int3
0038AC9B  48 8B D1                        mov rdx, rcx
0038AC9E  48 8D 0D BB 6F A8 00            lea rcx, [rip + 0xa86fbb]
0038ACA5  E8 16 00 00 00                  call 0x14038acc0
0038ACAA  EB E9                           jmp 0x14038ac95
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcFreeSharedCacheMapIgnoreNull(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_0038AC9B;
loc_0038AC95:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0038AC9B:
    result = ExFreeToLookasideListEx(v_rip + 11038651, a1, a3, a4);
    goto loc_0038AC95;
}
```

## 5. (Beta) C Style

```c
int64_t CcFreeSharedCacheMapIgnoreNull(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_0038AC9B;
loc_0038AC95:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0038AC9B:
    result = ExFreeToLookasideListEx(v_rip + 11038651, Arg1, a3, a4);
    goto loc_0038AC95;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038AC8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038AC8C[BB_0038AC8C]
  bb_0038AC95[BB_0038AC95]
  bb_0038AC9A[BB_0038AC9A]
  bb_0038AC9B[BB_0038AC9B]
  bb_0038AC8C -->|branch| bb_0038AC9B
  bb_0038AC8C -->|fallthrough| bb_0038AC95
  bb_0038AC9A -->|flow| bb_0038AC9B
  bb_0038AC9B -->|branch| bb_0038AC95
```
