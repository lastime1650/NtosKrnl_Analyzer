# ExIsSpecialPoolAddress

- RVA: `0x0049C410`–`0x0049C427` (길이 `23` bytes)
- VA: `0x000000014049C410`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0049C414` → [ExGetHeapFromVA](../36/ExGetHeapFromVA_function_00361840.md) (function, `0x00361840`)
- `0x0049C41C` → [ExpHpIsSpecialPoolHeap](ExpHpIsSpecialPoolHeap_function_0049C430.md) (function, `0x0049C430`)

### Direct callers
- [sub_0024E650](../24/Unknown_function_0024E650.md) at `0x0024E653`
- [sub_0024ED60](../24/Unknown_function_0024ED60.md) at `0x0024ED63`
- [sub_002F06CA](../2F/Unknown_function_002F06CA.md) at `0x002F06CA`
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035E796`
- [sub_00360968](../36/Unknown_function_00360968.md) at `0x00360EED`
- [ExQueryPoolBlockSize](../65/ExQueryPoolBlockSize_function_006566F0.md) at `0x00656715`
- [sub_00B8371E](../../poolcode/B8/Unknown_function_00B8371E.md) at `0x00B83CA5`
- [DifpLwSPProcessPostPoolAlloc](../../pagevrfy/BB/DifpLwSPProcessPostPoolAlloc_function_00BB422C.md) at `0x00BB4230`
- [ExFreePoolSanityChecks](../../pagevrfy/BB/ExFreePoolSanityChecks_function_00BB44A0.md) at `0x00BB4510`
- [VfHandlePoolAlloc](../../pagevrfy/BB/VfHandlePoolAlloc_function_00BB8A90.md) at `0x00BB8E21`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049C410  48 83 EC 28                     sub rsp, 0x28
0049C414  E8 27 54 EC FF                  call 0x140361840
0049C419  48 8B C8                        mov rcx, rax
0049C41C  E8 0F 00 00 00                  call 0x14049c430
0049C421  48 83 C4 28                     add rsp, 0x28
0049C425  C3                              ret
0049C426  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExIsSpecialPoolAddress(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExGetHeapFromVA(a1, a2, a3, a4);
    result = ExpHpIsSpecialPoolHeap(result, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void ExIsSpecialPoolAddress(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExGetHeapFromVA(a1, a2, a3, a4);
    result = ExpHpIsSpecialPoolHeap(result, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049C410&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049C410[BB_0049C410]
  bb_0049C426[BB_0049C426]
```
