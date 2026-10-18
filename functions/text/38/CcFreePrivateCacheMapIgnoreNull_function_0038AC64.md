# CcFreePrivateCacheMapIgnoreNull

- RVA: `0x0038AC64`–`0x0038AC84` (길이 `32` bytes)
- VA: `0x000000014038AC64`
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
- `0x0038AC7D` → [ExFreeToLookasideListEx](ExFreeToLookasideListEx_function_0038ACC0.md) (function, `0x0038ACC0`)

### Direct callers
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCBFA`
- [CcUninitializeCacheMap](../3C/CcUninitializeCacheMap_function_003CD520.md) at `0x003CD6C1`

### Static image references
- `0x0038AC76` → RVA `0x00E11C00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0038AC64  48 83 EC 28                     sub rsp, 0x28
0038AC68  48 85 C9                        test rcx, rcx
0038AC6B  75 06                           jne 0x14038ac73
0038AC6D  48 83 C4 28                     add rsp, 0x28
0038AC71  C3                              ret
0038AC72  CC                              int3
0038AC73  48 8B D1                        mov rdx, rcx
0038AC76  48 8D 0D 83 6F A8 00            lea rcx, [rip + 0xa86f83]
0038AC7D  E8 3E 00 00 00                  call 0x14038acc0
0038AC82  EB E9                           jmp 0x14038ac6d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcFreePrivateCacheMapIgnoreNull(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_0038AC73;
loc_0038AC6D:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0038AC73:
    result = ExFreeToLookasideListEx(v_rip + 11038595, a1, a3, a4);
    goto loc_0038AC6D;
}
```

## 5. (Beta) C Style

```c
int64_t CcFreePrivateCacheMapIgnoreNull(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_0038AC73;
loc_0038AC6D:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0038AC73:
    result = ExFreeToLookasideListEx(v_rip + 11038595, Arg1, a3, a4);
    goto loc_0038AC6D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038AC64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038AC64[BB_0038AC64]
  bb_0038AC6D[BB_0038AC6D]
  bb_0038AC72[BB_0038AC72]
  bb_0038AC73[BB_0038AC73]
  bb_0038AC64 -->|branch| bb_0038AC73
  bb_0038AC64 -->|fallthrough| bb_0038AC6D
  bb_0038AC72 -->|flow| bb_0038AC73
  bb_0038AC73 -->|branch| bb_0038AC6D
```
