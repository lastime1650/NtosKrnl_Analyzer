# SmWaitForSyncIo

- RVA: `0x00611478`–`0x0061149E` (길이 `38` bytes)
- VA: `0x0000000140611478`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `10`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00611493` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)

### Direct callers
- [ST_STORE&lt;SM_TRAITS&gt;::StDmEtaPerformIo](../60/ST_STORE_SM_TRAITS_StDmEtaPerformIo_function_0060D448.md) at `0x0060D4F4`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmSinglePageRetrieveSync](../60/ST_STORE_SM_TRAITS_StDmSinglePageRetrieveSync_function_0060E414.md) at `0x0060E4FE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00611478  48 83 EC 38                     sub rsp, 0x38
0061147C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00611482  45 33 C9                        xor r9d, r9d
00611485  48 81 C1 40 1B 00 00            add rcx, 0x1b40
0061148C  45 33 C0                        xor r8d, r8d
0061148F  41 8D 51 07                     lea edx, [r9 + 7]
00611493  E8 18 D2 BF FF                  call 0x14020e6b0
00611498  48 83 C4 38                     add rsp, 0x38
0061149C  C3                              ret
0061149D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmWaitForSyncIo(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a4 = 0;
    a1 = (a1) + (0x1B40ULL);
    a3 = 0;
    result = KeWaitForSingleObject(a1, a4 + 7, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SmWaitForSyncIo(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg4 = 0;
    Arg1 = (Arg1) + (0x1B40ULL);
    Arg3 = 0;
    result = KeWaitForSingleObject(Arg1, Arg4 + 7, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00611478&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00611478[BB_00611478]
  bb_0061149D[BB_0061149D]
```
