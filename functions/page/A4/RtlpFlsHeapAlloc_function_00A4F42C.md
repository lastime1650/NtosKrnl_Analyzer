# RtlpFlsHeapAlloc

- RVA: `0x00A4F42C`–`0x00A4F448` (길이 `28` bytes)
- VA: `0x0000000140A4F42C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A4F43D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [RTL_BINARY_ARRAY&lt;RTLP_FLS_SLOT,4,4&gt;::ChunkAllocate](../../text/46/RTL_BINARY_ARRAY_RTLP_FLS_SLOT_4_4_ChunkAllocate_function_0046BF64.md) at `0x0046BF8C`
- [RTL_BINARY_ARRAY&lt;RTLP_FLS_CALLBACK_ENTRY,4,4&gt;::SlotAllocate](../../text/5F/RTL_BINARY_ARRAY_RTLP_FLS_CALLBACK_ENTRY_4_4_SlotAllocate_function_005F0588.md) at `0x005F05C8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A4F43D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4F42C  48 83 EC 28                     sub rsp, 0x28
00A4F430  8B D1                           mov edx, ecx
00A4F432  41 B8 46 4C 53 6B               mov r8d, 0x6b534c46
00A4F438  B9 00 01 00 00                  mov ecx, 0x100
00A4F43D  E8 AE 2C 13 00                  call 0x140b820f0
00A4F442  48 83 C4 28                     add rsp, 0x28
00A4F446  C3                              ret
00A4F447  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpFlsHeapAlloc(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAllocatePool2(256, (unsigned int)(a1), (unsigned int)(0x6B534C46ULL), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpFlsHeapAlloc(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAllocatePool2(256, (uint32_t)(Arg1), (uint32_t)(0x6B534C46ULL), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4F42C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4F42C[BB_00A4F42C]
  bb_00A4F447[BB_00A4F447]
```
