# PipOobeCompleteAsyncCallback

- RVA: `0x00723710`–`0x0072372F` (길이 `31` bytes)
- VA: `0x0000000140723710`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00723719` → [VhdDeferredAutoAttachVirtualDisks](../../text/6A/VhdDeferredAutoAttachVirtualDisks_function_006A84A8.md) (function, `0x006A84A8`)
- `0x00723723` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00723719` → [VhdDeferredAutoAttachVirtualDisks](../../text/6A/VhdDeferredAutoAttachVirtualDisks_function_006A84A8.md) (`PAGE` → `.text`)
  - `0x00723723` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00723710  40 53                           push rbx
00723712  48 83 EC 20                     sub rsp, 0x20
00723716  48 8B D9                        mov rbx, rcx
00723719  E8 8A 4D F8 FF                  call 0x1406a84a8
0072371E  33 D2                           xor edx, edx
00723720  48 8B CB                        mov rcx, rbx
00723723  E8 48 F1 45 00                  call 0x140b82870
00723728  48 83 C4 20                     add rsp, 0x20
0072372C  5B                              pop rbx
0072372D  C3                              ret
0072372E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipOobeCompleteAsyncCallback(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = VhdDeferredAutoAttachVirtualDisks(a1, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipOobeCompleteAsyncCallback(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = VhdDeferredAutoAttachVirtualDisks(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00723710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00723710[BB_00723710]
  bb_0072372E[BB_0072372E]
```
